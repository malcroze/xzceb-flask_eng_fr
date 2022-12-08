import unittest 

from machinetranslation import translator

class TestTranslate(unittest.TestCase): 
    def test_frenchNull(self): 
        self.assertEqual(translator.french_to_english(None), '') 
        
    def test_englishNull(self): 
        self.assertEqual(translator.english_to_french(None), '') 
        
    def test_frenchBonjour(self): 
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello") 
        
    def test_englishHello(self): 
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour") 
        
unittest.main()