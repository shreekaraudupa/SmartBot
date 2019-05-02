
'''
import spacy.en
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher
m_tool = Matcher(nlp.vocab)

p1 = [{'LOWER': 'quickbrownfox'}]
p2 = [{'LOWER': 'quick'}, {'IS_PUNCT': True}, {'LOWER': 'brown'}, {'IS_PUNCT': True}, {'LOWER': 'fox'}]
p3 = [{'LOWER': 'quick'}, {'LOWER': 'brown'}, {'LOWER': 'fox'}]
p4 =  [{'LOWER': 'quick'}, {'LOWER': 'brownfox'}]

m_tool.add('QBF', None, p1, p2, p3, p4)

sentence = nlp(u'The quick-brown-fox jumps over the lazy dog. The quick brown fox eats well. \
               the quickbrownfox is dead. the dog misses the quick brownfox')

phrase_matches = m_tool(sentence)
print(phrase_matches )

for match_id, start, end in phrase_matches:
    string_id = nlp.vocab.strings[match_id]
    span = sentence[start:end]
    print(match_id, string_id, start, end, span.text)


'''