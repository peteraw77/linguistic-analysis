import spacy
from spacy import symbols

class SentenceAnalyzer:

    def subject_object_analysis(self, question):
        subj = None
        obj = None
        rel = None

        nlp = spacy.load('en_core_web_sm')
        out = nlp(question)

        for word in out:
            if word.dep == symbols.nsubj:
                subj = word
            elif word.dep == symbols.dobj or word.dep == symbols.pobj:
                obj = word

        parent_1 = subj
        parent_2 = obj
 
        while not rel:
            try:
                parent_1 = parent_1.head
                parent_2 = parent_2.head
            except AttributeError:
                print("Incorrect sentence structure...")
                break

            if parent_1 == parent_2:
                rel = parent_1

        return (str(subj), str(obj), str(rel))

    def parse_named_entities(self, question):
        nlp = spacy.load('en_core_web_sm')
        out = nlp(question)
        entities = [(ent.text, ent.label_) for ent in out.ents]

        return entities
