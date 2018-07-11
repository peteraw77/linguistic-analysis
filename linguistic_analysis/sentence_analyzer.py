import spacy
from spacy import symbols

class SentenceAnalyzer:
    '''
    Class for analyzing sentence structure and extracting key information
    '''

    def subject_object_analysis(self, sentence):
        '''
        Processes the sentence and locates the subject, object, and verb
        '''

        #TODO make into arrays
        subj = None
        obj = None
        verb = None

        nlp = spacy.load('en_core_web_sm')
        out = nlp(sentence)

        # check to make sure we have only one clause
        if len(out.sents) > 1:
            raise Exception('''Sentence has multiple clauses;
                compound sentences must be split before processing''')

        for word in out:
            if word.dep == symbols.nsubj:
                subj = word
            elif word.dep == symbols.dobj or word.dep == symbols.pobj:
                obj = word

        parent_1 = subj
        parent_2 = obj
 
        while not verb:
            try:
                parent_1 = parent_1.head
                parent_2 = parent_2.head
            except AttributeError:
                print("Incorrect sentence structure...")
                break

            if parent_1 == parent_2:
                verb = parent_1

        return (str(subj), str(obj), str(verb))

    def parse_named_entities(self, sentence):
        '''
        Searches the sentence for proper nouns
        '''

        nlp = spacy.load('en_core_web_sm')
        out = nlp(sentence)
        entities = [(ent.text, ent.label_) for ent in out.ents]

        return entities

    def split_compound_sentence(self, sentence):
        '''
        Separate a compound sentence into its clauses
        '''
        nlp = spacy.load('en_core_web_sm')
        out = nlp(sentence)

        return doc.sents
