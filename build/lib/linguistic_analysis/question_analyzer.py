import spacy
from spacy.symbols import nsubj, dobj

class QuestionAnalyzer:

    def get_key_elements(self, question):
        subj = None
        obj = None
        rel = None

        nlp = spacy.load('en_core_web_sm')
        out = nlp(question)

        for word in out:
            if word.dep == nsubj:
                subj = word
            elif word.dep == dobj:
                obj = word

        parent_1 = None
        parent_2 = None
 
        while not rel:
            try:
                parent_1 = subj.head
                parent_2 = obj.head
            except:
                print("Incorrect sentence structure...")
                break

            if parent_1 == parent_2:
                rel = parent_1

        return (str(subj), str(obj), str(rel))

    def get_named_entities(self, question):
        nlp = spacy.load('en_core_web_sm')
        out = nlp(question)
        entities = [(ent.text, ent.label_) for ent in out.ents]

        return entities
