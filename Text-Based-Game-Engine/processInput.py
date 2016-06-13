''' processInput.py

    Module used to run validated commands. Imported from main.py.
'''
import interface
from formatOutput import formatOutput as print
from operator import methodcaller

def executeCommand(tokenized_input, token_pattern, objects):
    ''' Processes a valid input-pattern and executes command(s).'''
    global valid_patterns

    if token_pattern == ['direction']:
        token_dir(tokenized_input, objects)

    elif token_pattern == ['verb']:
        token_verb(tokenized_input, objects)

    elif token_pattern == ['noun']:
        token_noun(tokenized_input, objects)

    elif token_pattern == ['adjective', 'noun']:
        token_adjective_noun(tokenized_input, objects)

    elif token_pattern == ['interface']:
        token_interface(tokenized_input, objects)

    elif token_pattern == ['verb', 'noun']:
        token_verb_noun(tokenized_input, objects)

    elif token_pattern == ['verb', 'adjective', 'noun']:
        token_verb_adjective_noun(tokenized_input, objects)

    elif token_pattern == ['verb', 'preposition', 'noun'] or \
        token_pattern == ['verb', 'preposition', 'preposition', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_verb_noun(stripped_list, objects)

    elif token_pattern == ['verb', 'preposition', 'adjective', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_verb_adjective_noun(stripped_list, objects)

    elif token_pattern == ['noun', 'verb']:
        token_noun_verb(tokenized_input, objects)

    elif token_pattern == ['verb', 'direction']:
        token_verb_direction(tokenized_input, objects)

    elif token_pattern == ['verb', 'noun', 'combine', 'noun']:
        token_combined_nouns(tokenized_input, objects)

    elif token_pattern == ['verb', 'preposition', 'noun', 'combine', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_combined_nouns(stripped_list, objects)

    elif token_pattern == ['verb', 'noun', 'combine', 'preposition', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_combined_nouns(stripped_list, objects)

    elif token_pattern == ['verb', 'preposition', 'noun',
        'combine', 'preposition', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_combined_nouns(stripped_list, objects)


def get_key(token):
    ''' In Python 3, dict.values() (along with dict.keys() and dict.items()) 
        returns a view, rather than a list. See the documentation here. You 
        therefore need to wrap your call to dict.values() in a call to list.'''
    return list(token.keys())[0]


def get_value(token):
    ''' Same as get_key, but for dict value's.'''
    return list(token.values())[0]


def is_available(noun, current_game, objects):
    ''' Returns an item-object if the given noun is currently available to the
        actor. The item needs to be checked for its presence in the room, or
        presence inside of another object, or in the actor's inventory.'''
    room_name = objects['CurrentRoom'].__class__.__name__

    for i in objects['Inventory'][room_name]:
        if noun in i.name:
            return i

        elif i.contains_item or i.has_item:
            stored_item = objects['Inventory'].get(i.__class__.__name__)[0]
            if noun in stored_item.name and stored_item.visible:
                return stored_item

    for i in objects['Inventory']['Actor']:
        if noun in i.name:
            return i

    else:
        return None        

# ------------------------------------------------------------------------------
# Input-processing functions (called from executeCommand)
# ------------------------------------------------------------------------------

def token_dir(tokenized_input, objects):
    ''' Process a single direction command.'''
    current_game = objects['Game']
    get_direction = methodcaller(get_value(tokenized_input[0]), objects)
    direction = get_direction(objects['CurrentRoom'])

    if get_key(direction) is 'message':
        print(get_value(direction))

    elif get_key(direction) is 'movement':
        current_game.completed_moves += 1
        objects['CurrentRoom'] = get_value(direction)
        if current_game.verbose_msg:
            interface.look(objects)


def token_verb(tokenized_input, objects):
    ''' Process a single verb-command. "look" is unique as it can be used with
        or without an item.'''
    verb = get_value(tokenized_input[0])
    objects['Game'].completed_moves += 1
    if verb == 'look' or verb == 'l':
        interface.look(objects)
    else:
        print("What do you want to {}?".format(verb))


def token_noun(tokenized_input, objects):
    ''' Process a single noun-command.'''
    current_game = objects['Game']
    noun = get_value(tokenized_input[0])
    current_game.completed_moves += 1
    if is_available(noun, current_game, objects):
        print("What would you like to do with the {}?".format(noun))
    else:
        print("There is no {} here.".format(noun))


def token_adjective_noun(tokenized_input, objects):
    ''' Process a noun preceeded by an adjective.'''
    current_game = objects['Game']
    current_game.completed_moves += 1
    adjective = get_value(tokenized_input[0])
    noun = get_value(tokenized_input[1])
    noun_obj = is_available(noun, current_game, objects)
    if noun_obj and adjective in noun_obj.adjective:
        print("What would you like to do with the {}?".format(\
            adjective + " " + noun))
    else:
        print("There is no {} here.".format(adjective + " " + noun))
    

def token_interface(tokenized_input, objects):
    ''' Process an interface-command.'''
    command = str(get_value(tokenized_input[0]))
    method = methodcaller(command, objects)
    method(interface)


def token_verb_noun(tokenized_input, objects):
    ''' Process an action upon a noun. First, determine if the item is present,
        then-- if so-- execute it's corresponding verb command.'''
    current_game = objects['Game']
    current_game.completed_moves += 1
    noun = get_value(tokenized_input[1])
    noun_obj = is_available(noun, current_game, objects)
    if noun_obj:
        verb = get_value(tokenized_input[0])
        command = methodcaller(verb, objects)
        command(noun_obj)
    else:
        print("There is no {} here.".format(noun))


def token_verb_adjective_noun(tokenized_input, objects):
    ''' Same as token_verb_noun, but includes an adjective before the noun.'''
    adjective = get_value(tokenized_input[1])
    noun = get_value(tokenized_input[2])
    noun_obj = is_available(noun, current_game, objects)
    if noun_obj and adjective in noun_obj.adjective:
        verb = get_value(tokenized_input[0])
        command = methodcaller(verb, objects)
        command(noun_obj)
    else:
        print("There is no {} here.".format(adjective + noun))
    objects['Game'].completed_moves += 1


def token_noun_verb(tokenized_input, objects):
    ''' Reverse the contents of tokenized_input and process as a verb-noun.'''
    tokenized_input = tokenized_input[::-1]
    token_verb_noun(tokenized_input, current_game)


def token_verb_direction(tokenized_input, objects):
    ''' Processes verbs associated with movement, but ultimately just executes
        a lone direction command.'''
    current_game = objects['Game']
    current_game.completed_moves += 1
    verb = get_value(tokenized_input[0])
    if verb in ['move']:
        direction = []
        direction.append(list(tokenized_input)[1])
        token_dir(direction, current_game)
    else:
        print("You used the word {} in a way I don't understand.".\
            format(verb))


def token_combined_nouns(tokenized_input, objects):
    ''' Uses a 'combine' command to allow two items to interact. Agnostic to
        the noun's location.'''
    current_game = objects['Game']
    current_game.completed_moves += 1
    verb   = get_value(tokenized_input[0])
    noun1  = get_value(tokenized_input[1])
    action = get_value(tokenized_input[2])
    noun2  = get_value(tokenized_input[3])

    noun_obj1 = is_available(noun1, current_game, objects)
    noun_obj2 = is_available(noun2, current_game, objects)

    if noun1 == noun2:
        print("There is no... wait, what?")
    elif noun_obj1 == None:
        print("There is no {} here.".format(noun1))
    elif noun_obj2 == None:
        print("There is no {} here.".format(noun2))
    else:
        function_name = '_'.join([verb, action])
        m = [method for method in dir(noun_obj1) if callable(getattr(noun_obj1,\
            method))]
        if function_name in m:
            command = methodcaller(function_name, noun_obj2, objects)
            command(noun_obj1)
        else:
            print("You combined the words '{0}' and '{1}' in way I \
                didn't understand".format(verb, action))


def strip_preposition(tokenized_input):
    ''' Strip out the preposition(s) and call the token_combined_nouns func.'''
    preposition_removed = []
    for t in tokenized_input:
        if get_key(t) != 'preposition':
            preposition_removed.append(t)
    return preposition_removed
    
