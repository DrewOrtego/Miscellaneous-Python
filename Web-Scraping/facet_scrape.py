#-------------------------------------------------------------------------------
# facet_scrape.py
#
# Scrape facets.la and download all it's wallpaper images!
#
# Notes:
# scrape_images() had a rough time trying to save the <title> content using BS4
# & pass it to urlretrieve() as a string. BS4 has generally been a poor way to
# save information, but great for navigating html tags. Also, no Regex! Yay!
#-------------------------------------------------------------------------------

from sys     import exit
from random  import randint
from os      import chdir, getcwd, mkdir
from urllib2 import urlopen
from urllib  import urlretrieve
try:
    from bs4 import BeautifulSoup as bs
except ImportError as error:
    msg = """                     ** IMPORT ERROR **
    BeautifulSoup module not detected! Get the module here:
    http://www.crummy.com/software/BeautifulSoup/#Download"""
    exit(msg)


def get_sites(facet_la):
    """ Returns a list of sites that are derived from the 'a href' tags."""

    web_page = urlopen(facet_la)
    soup = bs(web_page)
    list_sites = []
    for tag in soup.find_all('a', href=True):
        list_sites.append(tag['href'])
    del list_sites[0:6] # facet.la's first 6 sites don't contain any wallpapers.
    return list_sites


def set_directory():
    """ Create the directory for storing the scraped images, and set the current
    working directory to it. By default, this program will create the new
    directory in the location of this file."""

    try:
        mkdir('facet_images')
        chdir('facet_images')
    except WindowsError:
        # This occcurs if the folder 'facet_images' already exists.
        alt_dir = ('facet_images' + str(randint(0, 999)))
        mkdir(alt_dir)
        chdir(alt_dir)
    finally:
        print "Images will be saved to", getcwd(), "\n-------------------------"


def scrape_images(web_sites):
    """Scan through the list of websites. Find the image url located in each
    website and save that image in the given directory."""

    for site in web_sites:
        print "Accessing", site + "... ",
        current_page = urlopen(site)
        soup = bs(current_page)
        for div in soup.find_all('div', id='facet-image'):
            for img in div.find_all('img', alt=''):
                image_url = img['src']
                file_name = image_url.split('/')[-1]
                try:
                    urlretrieve(image_url, file_name) # Download, save an image.
                except IOError as error:
                    print "urlretrieve() IOError when saving:", error
                else:
                    full_file_path = getcwd() + "\\" + file_name
                    print "saved", full_file_path


if __name__ == '__main__':
    image_sites = get_sites('http://www.facets.la/wallpapers/')
    set_directory()
    scrape_images(image_sites)
