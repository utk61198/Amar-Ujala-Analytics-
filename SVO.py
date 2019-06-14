import os
import settings
import copy

os.environ['CLASSPATH'] = settings.CLASSPATH
os.environ['STANFORD_PARSER'] = settings.STANFORD_PARSOR
os.environ['STANFORD_MODELS'] = settings.STANFORD_MODELS
from nltk.parse.stanford import StanfordParser
from nltk.tree import ParentedTree, Tree
parser = StanfordParser()
def initialRun(text):
    t = list(parser.raw_parse(text))[0]
    t = ParentedTree.convert(t)
    subject_list=copy.deepcopy(findSubject(t))
    object_list=copy.deepcopy(findObject(t))
    verb_list=copy.deepcopy(findVerb(t))

    return subject_list,verb_list,object_list

def findSubject(t):
    for s in t.subtrees(lambda t: t.label() == 'NP'):
        for n in s.subtrees(lambda n: n.label().startswith('NN')):
            return list((n[0], displayList(n)))

def findVerb(t):
    v = None
    for s in t.subtrees(lambda t: t.label() == 'VP'):
        for n in s.subtrees(lambda n: n.label().startswith('VB')):
          return list((n[0], displayList(n)))

def findObject(t):
    for s in t.subtrees(lambda t: t.label() == 'VP'):
        for n in s.subtrees(lambda n: n.label() in ['NP', 'PP', 'ADJP']):
            if n.label() in ['NP', 'PP']:
                for c in n.subtrees(lambda c: c.label().startswith('NN')):
                    return list((c[0], displayList(c)))
            else:
                for c in n.subtrees(lambda c: c.label().startswith('JJ')):
                    return list((c[0], displayList(c)))

def displayList(node):
    list = []
    parent = node.parent()

    if node.label().startswith('JJ'):

        for s in parent:
            if s.label() == 'RB':
                list.append(s[0])

    elif node.label().startswith('NN'):
        for s in parent:
            if s.label() in ['DT', 'PRP$', 'POS', 'JJ', 'CD', 'ADJP', 'QP', 'NP']:
                list.append(s[0])

    elif node.label().startswith('VB'):
        for s in parent:
            if s.label() == 'ADVP':
                list.append(' '.join(s.flatten()))


    if node.label().startswith('JJ') or node.label().startswith('NN'):
        for s in parent.parent():
            if s != parent and s.label() == 'PP':
                list.append(' '.join(s.flatten()))

    elif node.label().startswith('VB'):
        for s in parent.parent():
            if s != parent and s.label().startswith('VB'):
                list.append(' '.join(s.flatten()))
        return list


