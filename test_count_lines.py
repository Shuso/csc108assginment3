from poetry_functions import count_lines
import unittest

class TestCountLines(unittest.TestCase):
    
    def test_case_1(self):
        actual=count_lines(['The first line leads off,\n', '\n', '  \n',
        'With a gap before the next.\n', 'Then the poem ends.\n'])
        expected= 3
        
    def test_case_2(self):
        actual=count_lines([ '\n'])
        expected=0
        self.assertEqual(actual, expected)

if __name__ == '__main__':
            unittest.main(exit=False)    
        
    
    
    