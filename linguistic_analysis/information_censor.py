import spacy

class InformationCensor:
    '''
    Class to parse documents for sensitive information and censor it
    without losing context.
    '''

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def censor_proper_nouns(self, text):
        '''
        Find all proper nouns in a body of text and replace them with
        asterisks. This is the preferred method as of now.
        '''
        out = self.nlp(text)
        censored_text = str(text) # deep copy

        for token in out:
            if token.tag_ == 'NNP':
                word = '*'*len(token.text)
                # maybe only one occurrence should be replaced...?
                censored_text = censored_text.replace(token.text, word)

        return censored_text
    
    def censor_named_entities(self, text):
        '''
        Censor only what spacy considers named entities. This works
        sometimes but it's far too inconsistent to be useful.
        '''
        out = self.nlp(text)
        censored_text = str(text) # deep copy

        for entity in out.ents:
            word = '*'*len(entity.text)
            # maybe only one occurrence should be replaced...?
            censored_text = censored_text.replace(entity.text, word)

        return censored_text
