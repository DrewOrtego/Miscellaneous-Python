''' processInput.py

    Module used to run validated commands. Imported from main.py.
'''

from operator import methodcaller
from commandProcessing import interface
from userInterface.formatOutput import formatOutput as print

def executeCommand(tokenized_input, token_pattern, objects):
    ''' Processes a valid input-pattern and executes command(s).'''
    global valid_patterns

    if token_pattern == ['adjective']:
        token_adjective(tokenized_input, objects)

    elif token_pattern == ['direction']:
        token_dir(tokenized_input, objects)

    elif token_pattern == ['interface']:
        token_interface(tokenized_input, objects)

    elif token_pattern == ['noun']:
        token_noun(tokenized_input, objects)

    elif token_pattern == ['npc']:
        token_npc(tokenized_input, objects)

    elif token_pattern == ['verb']:
        token_verb(tokenized_input, objects)

    elif token_pattern == ['adjective', 'noun']:
        token_adjective_noun(tokenized_input, objects)

    elif token_pattern == ['noun', 'verb']:
        token_noun_verb(tokenized_input, objects)

    elif token_pattern == ['verb', 'adjective']:
        token_verb_noun(tokenized_input, objects)

    elif token_pattern == ['verb', 'direction']:
        token_verb_direction(tokenized_input, objects)

    elif token_pattern == ['verb', 'noun']:
        token_verb_noun(tokenized_input, objects)

    elif token_pattern == ['verb', 'npc']:
        token_verb_npc(tokenized_input, objects)

    elif token_pattern == ['verb', 'adjective', 'noun']:
        token_verb_adjective_noun(tokenized_input, objects)

    elif token_pattern == ['verb', 'noun', 'adjective']:
        token_verb_noun_adjective(tokenized_input, objects)

    elif token_pattern == ['verb', 'npc', 'noun']:
        token_verb_npc_noun(tokenized_input, objects)

    elif token_pattern == ['verb', 'npc', 'preposition', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_verb_npc_noun(stripped_list, objects)

    elif token_pattern == ['verb', 'noun', 'npc']:
        token_verb_noun_npc(tokenized_input, objects)

    elif token_pattern == ['verb', 'preposition', 'noun',  'npc']:
        stripped_list = strip_preposition(tokenized_input)
        token_verb_noun_npc(stripped_list, objects)

    elif token_pattern == ['verb', 'preposition', 'noun'] or \
        token_pattern == ['verb', 'preposition', 'preposition', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_verb_noun(stripped_list, objects)

    elif token_pattern == ['verb', 'preposition', 'adjective', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_verb_adjective_noun(stripped_list, objects)

    elif token_pattern == ['verb', 'noun', 'combine', 'noun']:
        token_combined_nouns(tokenized_input, objects)

    elif token_pattern == ['verb', 'noun', 'combine', 'preposition', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_combined_nouns(stripped_list, objects)

    elif token_pattern == ['verb', 'preposition', 'noun', 'combine', 'noun']:
        stripped_list = strip_preposition(tokenized_input)
        token_combined_nouns(stripped_list, objects)

    elif token_pattern == ['verb', 'preposition', 'noun', 'combine', 
        'preposition', 'noun']:
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


def increment_moves(objects):
    ''' Add 1 to the sum of completed moves.'''
    objects['Game'].completed_moves += 1


def is_available(noun, objects):
    ''' Returns an item-object if the given noun is currently available to the
        actor. The item needs to be checked for its presence in the room, or
        presence inside of another object, or in the actor's inventory.
        Also parses for adjectives associated with nouns.'''
    room_name = objects['CurrentRoom'].__class__.__name__
    for i in objects['Inventory'][room_name]:
        if noun in i.name or noun in i.adjective:
            return i
        elif i.contains_item or i.has_item:
            stored_item = objects['Inventory'].get(i.__class__.__name__)[0]
            if noun in stored_item.name and stored_item.visible:
                return stored_item
    for i in objects['Inventory']['Actor']:
        if noun in i.name or noun in i.adjective:
            return i
    else:
        return None


def is_present(npc, objects):
    ''' Returns a npc-object if the given npc is currently available to the
        actor i.e. in the current room.'''
    room_name = objects['CurrentRoom'].__class__.__name__
    for n in objects['Npc_Location'][room_name]:
        if npc in n.name[0].lower():
            return n
    else:
        return None

# ------------------------------------------------------------------------------
# Input-processing functions (called from executeCommand)
# ------------------------------------------------------------------------------
def token_adjective(tokenized_input, objects):
    ''' Process a single adjective-command. Similar to the token_noun 
        function.'''
    adjective = get_value(tokenized_input[0])
    increment_moves(objects)
    if is_available(adjective, objects):
        print('''What would you like to do with the {}?'''.format(adjective))
    else:
        print('''There is no {} here.'''.format(adjective))


def token_dir(tokenized_input, objects):
    ''' Process a single direction command.'''
    get_direction = methodcaller(get_value(tokenized_input[0]), objects)
    direction = get_direction(objects['CurrentRoom'])

    if get_key(direction) is 'message':
        print(get_value(direction))

    elif get_key(direction) is 'movement':
        increment_moves(objects)
        objects['CurrentRoom'] = get_value(direction)
        current_game = objects['Game']
        if current_game.verbose_msg:
            objects['CurrentRoom'].look(objects)


def token_noun(tokenized_input, objects):
    ''' Process a single noun-command.'''
    noun = get_value(tokenized_input[0])
    increment_moves(objects)
    if is_available(noun, objects):
        print('''What would you like to do with the {}?'''.format(noun))
    else:
        print('''There is no {} here.'''.format(noun))
        

def token_npc(tokenized_input, objects):
    ''' Process a command referring to a non-playable character.'''
    npc = get_value(tokenized_input[0])
    increment_moves(objects)
    if is_present(npc, objects):
        print('''{} is here.'''.format(npc[0].upper() + npc[1:].lower()))
    else:
        print('''There's no one here by that name.''')


def token_verb(tokenized_input, objects):
    ''' Process a single verb-command. "look" is unique as it can be used with
        or without an item.'''
    verb = get_value(tokenized_input[0])
    increment_moves(objects)
    if verb == 'look' or verb == 'l':
        objects['CurrentRoom'].look(objects)
    else:
        print('''What do you want to {}?'''.format(verb))


def token_adjective_noun(tokenized_input, objects):
    ''' Process a noun preceeded by an adjective.'''
    increment_moves(objects)
    adjective = get_value(tokenized_input[0])
    noun = get_value(tokenized_input[1])
    noun_obj = is_available(noun, objects)
    if noun_obj and adjective in noun_obj.adjective:
        print("What would you like to do with the {}?".format(\
            adjective + " " + noun))
    else:
        print('''There is no {} here.'''.format(adjective + " " + noun))
    

def token_interface(tokenized_input, objects):
    ''' Process an interface-command.'''
    command = str(get_value(tokenized_input[0]))
    method = methodcaller(command, objects)
    method(interface)


def token_verb_noun(tokenized_input, objects):
    ''' Process an action upon a noun. First, determine if the item is present,
        then-- if so-- execute it's corresponding verb command.'''
    increment_moves(objects)
    noun = get_value(tokenized_input[1])
    noun_obj = is_available(noun, objects)
    if noun_obj:
        verb = get_value(tokenized_input[0])
        command = methodcaller(verb, objects)
        command(noun_obj)
    else:
        print('''There is no {} here.'''.format(noun))


def token_verb_npc(tokenized_input, objects):
    ''' Process a single verb command when applied to a present NPC.'''
    increment_moves(objects)
    verb_cmd = get_value(tokenized_input[0])
    npc_cmd = get_value(tokenized_input[1])
    npc_obj = is_present(npc_cmd, objects)
    if npc_obj:
        if verb_cmd == 'give':
            print('''What would you like to give to {0}?'''.format(
                npc_obj.name[0]))
        else:
            command = methodcaller(verb_cmd, objects)
            command(npc_obj)
    else:
        print('''There's no one here by that name.''')

        
def token_verb_adjective_noun(tokenized_input, objects):
    ''' Same as token_verb_noun, but includes an adjective before the noun.'''
    increment_moves(objects)
    verb = get_value(tokenized_input[0])
    adjective = get_value(tokenized_input[1])
    noun = get_value(tokenized_input[2])
    noun_obj = is_available(noun, objects)
    if noun_obj and adjective in noun_obj.adjective:
        command = methodcaller(verb, objects)
        command(noun_obj)
    else:
        print('''There is no {0} {1} here.'''.format(adjective, noun))


def token_verb_noun_adjective(tokenized_input, objects):
    ''' Same as token_verb_noun, but includes an adjective before the noun.'''
    increment_moves(objects)
    verb = get_value(tokenized_input[0])
    noun = get_value(tokenized_input[1])
    adjective = get_value(tokenized_input[2])
    noun_obj = is_available(noun, objects)
    if noun_obj and adjective in noun_obj.adjective:
        command = methodcaller(verb, objects)
        command(noun_obj)
    else:
        print('''There is no {0} {1} here.'''.format(adjective, noun))


def token_verb_noun_npc(tokenized_input, objects):
    ''' Another way to have an item interact with a user.'''
    increment_moves(objects)
    verb_cmd = get_value(tokenized_input[0])
    noun_cmd = get_value(tokenized_input[1])
    npc_cmd  = get_value(tokenized_input[2])
    noun_obj = is_available(noun_cmd, objects)
    npc_obj  = is_present(npc_cmd, objects)
    if noun_obj:
        if npc_obj:
            command = methodcaller(verb_cmd, noun_obj, objects)
            command(npc_obj)
        else:
            print('''There's no one here by that name.''')
    else:
        print('''There is no {0} here.'''.format(noun_obj))


def token_verb_npc_noun(tokenized_input, objects):
    increment_moves(objects)
    verb_cmd = get_value(tokenized_input[0])
    npc_cmd  = get_value(tokenized_input[1])
    noun_cmd = get_value(tokenized_input[2])
    noun_obj = is_available(noun_cmd, objects)
    npc_obj  = is_present(npc_cmd, objects)
    if noun_obj:
        if npc_obj:
            command = methodcaller(verb_cmd, noun_obj, objects)
            command(npc_obj)
        else:
            print('''There's no one here by that name.''')
    else:
        print('''There is no {0} here.'''.format(noun_obj))


def token_noun_verb(tokenized_input, objects):
    ''' Reverse the contents of tokenized_input and process as a verb-noun.'''
    tokenized_input = tokenized_input[::-1]
    current_game = objects['Game']
    token_verb_noun(tokenized_input, current_game)


def token_verb_direction(tokenized_input, objects):
    ''' Processes verbs associated with movement, but ultimately just executes
        a lone direction command.'''
    increment_moves(objects)
    verb = get_value(tokenized_input[0])
    if verb in ['move']:
        direction = []
        direction.append(list(tokenized_input)[1])
        current_game = objects['Game']
        token_dir(direction, current_game)
    else:
        print('''You used the word {} in a way I don't 
            understand.'''.format(verb))


def token_combined_nouns(tokenized_input, objects):
    ''' Uses a 'combine' command to allow two items to interact.'''
    increment_moves(objects)
    verb   = get_value(tokenized_input[0])
    noun1  = get_value(tokenized_input[1])
    action = get_value(tokenized_input[2])
    noun2  = get_value(tokenized_input[3])

    noun_obj1 = is_available(noun1, objects)
    noun_obj2 = is_available(noun2, objects)

    if noun1 == noun2:
        print('''There is no... wait, what?''')
    elif noun_obj1 == None:
        print('''There is no {} here.'''.format(noun1))
    elif noun_obj2 == None:
        print('''There is no {} here.'''.format(noun2))
    else:
        function_name = '_'.join([verb, action])
        m = [mtd for mtd in dir(noun_obj1) if callable(getattr(noun_obj1, mtd))]
        if function_name in m:
            command = methodcaller(function_name, noun_obj2, objects)
            command(noun_obj1)
        else:
            print('''You combined the words '{0}' and '{1}' in way I didn't 
                understand'''.format(verb, action))


def strip_preposition(tokenized_input):
    ''' Strip out the preposition(s) and call the token_combined_nouns func.'''
    preposition_removed = []
    for t in tokenized_input:
        if get_key(t) != 'preposition':
            preposition_removed.append(t)
    return preposition_removed

