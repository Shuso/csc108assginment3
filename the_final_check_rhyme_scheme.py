






# helper function no.1
def get_phonemes(poem_lines, word_to_phonemes):
    """ (list of str, pronunciation dictionary) -> list of list of str
    >>> >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}

     >>> poem_lines = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.']
     >>> get_phonemes(poem_lines, word_to_phonemes)
     [['AO1', 'F'], ['N', 'EH1', 'K', 'S', 'T'], ['EH1', 'N', 'D', 'Z']]
    
     """
     
    phoneme_list=[]
    for line in poem_lines:
        word=clean_up(line.split()[-1:][0]) # conver type list to type string and also clean it up
        phoneme=word_to_phonemes.get(word)
        phoneme_list.append(phoneme)# a list of list of string
    return phoneme_list

#helper function no.2
def find_rhyme_list(phoneme_list):
    """ (list of list of str) -> list of list of str
    >>> phoneme_list= [['AO1', 'F'], ['N', 'EH1', 'K', 'S', 'T'], ['EH1', 'N', 'D', 'Z']]
    >>> find_rhyme_list(phoneme_list)
    [['F', 'AO1'], ['T', 'S', 'K', 'EH1'], ['Z', 'D', 'N', 'EH1']]
    
    """
    rhyme_list=[]
    for phoneme in phoneme_list:
        rhyme=locate_syllable(phoneme)
        rhyme_list.append(rhyme)
    return rhyme_list

#helper function no.3
def locate_syllable(phoneme): 
    """ (list of str) - > list of str 
    >>> locate_syllable(['N', 'EH1', 'K', 'S', 'T'])
    ['T', 'S', 'K', 'EH1']
   
    """
    rev=phoneme[::-1] # locate the last syllable by  locating the frist syllable of its reverse
    for i in range(len(rev)):
        if rev[i][-1].isdigit():
            return rev[:i+1]     


#helper function no.4
s=['A','B','A','B','C']
def find_match_indice(s):
    """   (list of str) ->list of str
    
    >>> s=['A','B','A','B','C']
    >>> find_match_indice(s)
    ['02', '13', '02', '13', '4']
    
    """
    
    index_list=[]
    same_symbol=''
    i=0
    
    for ch in s:
        for i in range(len(s)):
            if s[i]==ch:
                same_symbol+=str(i)
        index_list.append(same_symbol)
        same_symbol=''
    
    return index_list


#helper function no.5
def find_rhyme_scheme(rhyme_list):
    """ (list of list of str) - > list of str
    >>> rhyme_list=[['AO1', 'F'], ['AO1', 'F'],['N', 'EH1', 'K', 'S', 'T'], ['AO1', 'F'],['EH1', 'N', 'D', 'Z']]
    >>> find_rhyme_scheme(rhyme_list)
    ['013','013','2','013','4']"""  
    rhyme_scheme=[]
    same_rhyme=''
    i=0
    
    for item in rhyme_list:
        for i in range(len(rhyme_list)):
            if rhyme_list[i]==item:
                same_rhyme+=str(i)
        rhyme_scheme.append(same_rhyme)
        same_rhyme=''
    
    return rhyme_scheme

# THE MAIN COURSE
def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) 
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    """
    phoneme_list=get_phonemes(poem_lines, word_to_phonemes)
    rhyme_list= find_rhyme_list(phoneme_list)
    actual_scheme=find_rhyme_scheme(rhyme_list)
    given_scheme=find_match_indice(pattern[1])
    
    
    not_match=[]
    total_not_match=[]
    #number_list=[]
    
    for i in range(len(given_scheme)):
        
        if len(given_scheme[i])>1 and actual_scheme[i] != given_scheme[i]: #compare the two schemes, the two schemes are parallel list.
            # add a list of all the lines for that supposed-to-rhyme group to total_not_match
            number_list = []            
            for ch in given_scheme[i]:    # get the index inside of the given_scheme                                                                    
                number_list.append(ch)   # number_list is the index list that I gonna append to the not_match
            for item in number_list:
                not_match.append(poem_lines[int(item)] )   # and then return poem_lines correspond to the index
            if not_match not in total_not_match:   
                total_not_match.append(not_match)
        not_match=[]
    return total_not_match
                                     
                                     
if __name__ == '__main__':
    import doctest
    doctest.testmod()
                                              
                    
                    
       