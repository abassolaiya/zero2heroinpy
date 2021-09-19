# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:56:35 2021

@author: -
"""

import unittest
import cap

class TestCp(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
if __name__=='__main__':
    unittest.main()