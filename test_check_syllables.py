from poetry_functions import check_syllables
import unittest

class TestCheckSyllables(unittest.TestCase):
    
    def test_case_1(self):
        poem_lines = ['The first line leads off,', 
                      'With a gap before the next.', 'Then the poem ends.']
        pattern = ([5, 5, 4], ['*', '*', '*'])
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'], 
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}
        actual=check_syllables(poem_lines, pattern, word_to_phonemes)
        expected=['With a gap before the next.', 'Then the poem ends.']
        self.assertEqual(expected, actual)
        
    def test_case_2(self):
        poem_lines = ['The first line leads off,']
        pattern = ([0], ['*'])
        word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'GAP': ['G', 'AE1', 'P'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'LEADS':['L', 'IY1', 'D', 'Z'],
                            'WITH': ['W', 'IH1', 'DH'],
                            'LINE': ['L', 'AY1', 'N'],
                            'THEN': ['DH', 'EH1', 'N'],
                            'THE': ['DH', 'AH0'], 
                            'A': ['AH0'],
                            'FIRST': ['F', 'ER1', 'S', 'T'], 
                            'ENDS': ['EH1', 'N', 'D', 'Z'],
                            'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'OFF': ['AO1', 'F']}
        actual=check_syllables(poem_lines, pattern, word_to_phonemes)
        expected=[]
        
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
            unittest.main(exit=False)    
        
    

   