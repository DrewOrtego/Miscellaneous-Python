''' tokenizer.py

    Used to process in/valid commands. The basic elements of this game are 
    powered by the tokenizer. A token is a word-type and its associated word, 
    such as a "noun" called "chair". The game will always look for a valid 
    pattern of tokens when deciding whether a user's input is valid or not.
'''

from commandProcessing import commands as c

valid_patterns = (
    # TO BE REMOVED
    ['adjective'], # REMOVE
    ['verb', 'adjective'], # REMOVE
    ['verb', 'noun', 'adjective'], # REMOVE
    #--------------------------------------

    ['direction'], # ex. north
    ['interface'], # ex. help
    ['noun'], # ex. fish
    ['npc'], # ex. aquaman
    ['verb'], # ex. eat

    ['noun', 'verb'], # ex. fish eat
    ['verb', 'direction'], # ex. move north
    ['verb', 'noun'], # ex. eat fish
    ['verb', 'npc'], # ex. hug aquaman

    ['verb', 'noun', 'npc'], # ex. give aquaman fish
    ['verb', 'npc', 'noun'], # ex. give fish aquaman
    ['verb', 'preposition', 'noun'], # ex. give a fish

    ['verb', 'noun', 'combine', 'noun'], # ex. give fish to aquaman
    ['verb', 'preposition', 'preposition', 'noun'], # ex. look at a fish 

    ['verb', 'preposition', 'noun', 'combine', 'noun'], # ex. give a fish to aquaman
    ['verb', 'noun', 'combine', 'preposition', 'noun'], # ex. give fish to the ocean

    ['verb', 'preposition', 'noun', 'combine', 'preposition', 'noun'], # ex. give the fish to the ocean

    # Any noun-pattern is also executable when an adjective preceeds the noun
    ['adjective', 'noun'], # ex. slippery fish
    ['adjective', 'noun', 'verb'], # TODO
    ['verb', 'adjective', 'noun'],
    ['verb', 'adjective', 'noun', 'npc'],  # TODO
    ['verb', 'npc', 'adjective', 'noun'],  # TODO
    ['verb', 'preposition', 'adjective', 'noun'],
    ['verb', 'adjective', 'noun', 'combine', 'adjective', 'noun'], # TODO
    ['verb', 'preposition', 'preposition', 'adjective', 'noun'], # TODO
    ['verb', 'preposition', 'adjective', 'noun', 'combine', 'adjective', 'noun'], # TODO
    ['verb', 'adjective', 'noun', 'combine', 'preposition', 'adjective', 'noun'], # TODO
    ['verb', 'preposition', 'adjective', 'noun', 'combine', 'preposition', 'adjective', 'noun'] # TODO
)

def get_token(user_input):
    ''' Tokenizes the given input and returns a list element. Skips over the
        "ignore" commands and doesn't include them in the returned list.
        Any unrecognized words will be returned as an error.'''
    tokenized_words = []
    for word in user_input:
        word = word.lower()
        if   word in c.adjectives:  tokenized_words.append({'adjective':word})
        elif word in c.combine:     tokenized_words.append({'combine':word})
        elif word in c.directions:  tokenized_words.append({'direction':word})
        elif word in c.interface:   tokenized_words.append({'interface':word})
        elif word in c.nouns:       tokenized_words.append({'noun':word})
        elif word in c.npcs:        tokenized_words.append({'npc':word})
        elif word in c.preposition: tokenized_words.append({'preposition':word})
        elif word in c.verbs:       tokenized_words.append({'verb':word})
        else: return [{'unknown_word':word}]
    return tokenized_words


def pattern_match(tokenized_input):
    ''' Compares the word-type pattern of the user's input to the list of all 
        valid patterns. Returns True if the pattern of the input is matched to 
        a listed pattern.'''
    global valid_patterns
    user_pattern = [list(token_key.keys())[0] for token_key in tokenized_input]
    if user_pattern in valid_patterns:
        return user_pattern
    else:
        return False

