#!/usr/bin/python
import unittest
from linguistic_analysis.sentence_analyzer import SentenceAnalyzer

class TestSentenceAnalyzer(unittest.TestCase):

    def test_subject_object_analysis(self):
        sa = SentenceAnalyzer()
        
        sentence = u"We can carry this sofa."
        self.assertEqual(sa.subject_object_analysis(sentence), ('We', 'sofa', 'carry'))

        question = u"Is Bob going to the zoo?"
        self.assertEqual(sa.subject_object_analysis(question), ('Bob', 'zoo', 'going'))

        #TODO add more test cases

    def test_get_named_entities(self):
        sa = SentenceAnalyzer()

        sentence = u"Something is wrong with this MacBook."
        self.assertEqual(sa.parse_named_entities(sentence), [('MacBook', 'GPE')])

        question = u"How are you Dave, did you enjoy your McDonald's?"
        self.assertEqual(sa.parse_named_entities(question), [('Dave', 'PERSON'), ("McDonald's", 'ORG')])

    def test_is_imperative(self):
        sa = SentenceAnalyzer()

        statement = u"Get me the sandwich."
        self.assertTrue(sa.is_imperative(statement))

        sentence = u"Using this, you can get home"
        self.assertFalse(sa.is_imperative(sentence))

    def test_is_compound(self):
        sa = SentenceAnalyzer()

        sentence = u"I like chicken, you like beef."
        self.assertTrue(sa.is_compound(sentence))

        sentence = u"I fed the cat after I brushed my teeth"
        self.assertTrue(sa.is_compound(sentence))

if __name__ == '__main__':
    unittest.main()
