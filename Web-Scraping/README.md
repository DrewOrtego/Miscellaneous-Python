# Web-Scraping

**Demonstrates**
* Use of the urllib module to make requests and examine the results
* Uses error-catching to report issues with the results
* Automatically creates unique file names to proceed with running given duplicate files

**Usage:**

    Run as a standalone script in Python 2.
    
**Purpose:**

    Collects all the images from http://www.facets.la/wallpapers/ on a folder. 
    Requires Python 2 and the Beautiful Soup module found here: 
    http://www.crummy.com/software/BeautifulSoup/#Download
     
    I created this because there wasn't a way to easily download all of the
    wonderful images on this site. Now my Windows Desktop is looking sharp!
    
**Work Flow:**

    Makes a request to the facet website and looks for the tags which
    contain the url's to the images I want to download. 
    
 **Input:**
 
    N/A
   
**Output:**

    Creates a folder to store the images in, and gives each one a unique name.
    
