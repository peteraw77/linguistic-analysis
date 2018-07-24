#!/usr/bin/python
import unittest
from linguistic_analysis.information_censor import InformationCensor

class TestInformationCensor(unittest.TestCase):
    
    def test_censor_proper_nouns(self):
        test_body = u'''Bob went to the store to buy a MacBook. While he was
            there, he decided to grab a burger from McDonald's. Chuck
            saw Bob buying the burger, and said, "Don't do it Bob, Stacy
            said she would leave you if you had another Big Mac." Bob told
            Chuck to stuff it as he stuffed his face with the burger.'''

        ic = InformationCensor()
        out_body = ic.censor_proper_nouns(test_body)

        print(out_body)
        self.assertEqual(len(out_body), len(test_body))

    def test_censor_named_entities(self):
        test_body = u'''Bob went to the store to buy a MacBook. While he was
            there, he decided to grab a burger from McDonald's. Chuck
            saw Bob buying the burger, and said, "Don't do it Bob, Stacy
            said she would leave you if you had another Big Mac." Bob told
            Chuck to stuff it as he stuffed his face with the burger.'''

        ic = InformationCensor()
        out_body = ic.censor_named_entities(test_body)

        print(out_body)
        self.assertEqual(len(out_body), len(test_body))

if __name__ == '__main__':
    unittest.main()
