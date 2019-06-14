#mongoColection
mongoCollection is the python script to fetch the latest 500 stories rom the mongoDB
settings.py contains all the variables that are used in mongoCollection

#keywordExtraction
Here rake-nltk is used to extract keywords from a text, it is built upon rake and features of natural
language toolkit added to it
Install rake-nltk from the command line of using the pycharm interpreter

#SV0

first implemented Textacy api,but the results were not good as it was not able to break down sentences into clear subjects
 verbs and objects.
Finally implemented STANFORD PARSER falling into the different categories like:
CC - Coordinating conjunction
CD - Cardinal number
DT - Determiner
EX - Existential there
FW - Foreign word
IN - Preposition or subordinating conjunction
JJ - Adjective
JJR - Adjective, comparative
JJS - Adjective, superlative
LS - List item marker
MD - Modal
NN - Noun, singular or mass
NNS - Noun, plural
NNP - Proper noun, singular
NNPS - Proper noun, plural
PDT - Predeterminer
POS - Possessive ending
PRP - Personal pronoun
PRP$ - Possessive pronoun (prolog version PRP-S)
RB - Adverb
RBR - Adverb, comparative
RBS - Adverb, superlative
RP - Particle
SYM - Symbol
TO - to
UH - Interjection
VB - Verb, base form
VBD - Verb, past tense
VBG - Verb, gerund or present participle
VBN - Verb, past participle
VBP - Verb, non-3rd person singular present
VBZ - Verb, 3rd person singular present
WDT - Wh-determiner
WP - Wh-pronoun
WP$ - Possessive wh-pronoun (prolog version WP-S)
WRB - Wh-adverb
After that, wrote a code to find the desired tokens by traversing in the tree given by the stanford parser

#testCases

This python scripts extracts the news headlines from mongo and perform Subject,verb,Object extraction from the headlines
and puts them into a csv file

# sentiment analysis

for performing sentiment analysis SKLEARN(naive_bayes) was used along with KERAS and PANDAS


