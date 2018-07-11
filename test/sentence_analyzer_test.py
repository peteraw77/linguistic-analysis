#!/usr/bin/python
import unittest
from linguistic_analysis.sentence_analyzer import SentenceAnalyzer

class TestSentenceAnalyzer(unittest.TestCase):

    def test_subject_object_analysis(self):
        sa = SentenceAnalyzer()
        
        question = u"Can we carry this sofa?"
        self.assertEqual(sa.subject_object_analysis(question), ('we', 'sofa', 'carry'))

        question = u"Is Bob going to the zoo?"
        self.assertEqual(sa.subject_object_analysis(question), ('Bob', 'zoo', 'going'))

        #TODO(Peter) add more test cases

    def test_get_named_entities(self):
        sa = SentenceAnalyzer()

        question = u"What is wrong with this MacBook?"
        self.assertEqual(sa.parse_named_entities(question), [('MacBook', 'GPE')])

        question = u"How are you Dave, did you enjoy your McDonald's?"
        self.assertEqual(sa.parse_named_entities(question), [('Dave', 'PERSON'), ("McDonald's", 'ORG')])

if __name__ == '__main__':
    unittest.main()
