import spacy
from spacy import symbols

class SentenceAnalyzer:
    '''
    Class for analyzing sentence structure and extracting key information
    '''

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
    
    #TODO method for checking the form of a sentence
    #TODO return all strings in lower case

    def subject_object_analysis(self, clause):
        '''
        Processes a clause and locates the subject, object, and verb
        '''
        # check to make sure we have only one clause
        if self.is_compound(clause):
            raise Exception('''Sentence has multiple clauses;
                compound sentences must be split before processing''')

        #TODO use chunking or make into arrays
        subj = None
        obj = None
        verb = None

        out = self.nlp(clause)

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
        out = self.nlp(sentence)
        entities = [(ent.text, ent.label_) for ent in out.ents]

        return entities

    def is_imperative(self, sentence):
        '''
        Check if a given sentence is imperative
        '''
        out = self.nlp(sentence)

        # check if the sentence begins with a present tense verb
        if out[0].tag_ != 'VB':
            return False

        # check if there is a subject
        for word in out:
            if word.dep == symbols.nsubj:
                return False

        return True

    def is_compound(self, sentence):
        '''
        Determine if sentence is compound or not
        '''
        out = self.nlp(sentence)

        # generators have no inherent method to find length
        num_sentences = sum(1 for sent in out.sents)
        
        return num_sentences > 1

    def split_compound_sentence(self, sentence):
        '''
        Separate a compound sentence into its clauses
        '''
        #TODO: make this work
        out = self.nlp(sentence)

        return [str(sent) for sent in out.sents]
