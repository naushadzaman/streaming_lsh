'''
Created on Jun 13, 2011

@author: kykamath
'''

#from classes import Document, Permutation
#from library.vector import Vector, VectorGenerator
#
#numberOfDocuments = 5
#dimension=2
#lengthOfSignature = 13
#numberOfPermutations = 5
#
##documents = [Document(Vector({1:1,2:2})), Document(Vector({1:5,2:1})), Document(Vector({1:-2,2:1})),
##             Document(Vector({1:10,2:2})), Document(Vector({1:-5,2:-10}))]
#documents = dict((i, Document(i, VectorGenerator.getRandomGaussianUnitVector(dimension, 0, 1))) for i in xrange(numberOfDocuments))
#unitRandomVectors = [VectorGenerator.getRandomGaussianUnitVector(dimension, 0, 1) for i in range(lengthOfSignature)]
#permutations = [Permutation(lengthOfSignature) for i in range(numberOfPermutations)]
#for doc in documents: documents[doc].setDocumentSignatureUsingUnitRandomVectors(unitRandomVectors)
#
##    print doc, doc.setDocumentSignatureUsingUnitRandomVectors(unitRandomVectors), doc.signature
#
#for permutation in permutations: 
#    for docId in documents: permutation.documentSignatures[docId] = documents[doc].signature.permutate(permutation)
#    print permutation.documentSignatures


import random
numberOfDocuments = 100
dimensions = 52
topics = {
          'elections':{'prob': 0.3, 'tags': {'#gop': 0.4, '#bachmann': 0.2, '#perry': 0.2, '#romney': 0.2}},
          'soccer': {'prob': 0.2, 'tags': {'#rooney': 0.15, '#chica': 0.1, '#manutd': 0.6, '#fergie': 0.15}},
          'arab': {'prob': 0.3, 'tags': {'#libya': 0.4, '#arab': 0.3, '#eqypt': 0.15, '#syria': 0.15}},
          'page3': {'prob': 0.2, 'tags': {'#paris': 0.2, '#kim': 0.4, '#britney': 0.2, '#khloe': 0.2}},
          }

stopwords = 'abcdefghijklmnopqrstuvwxyz1234567890'

def pickOneByProbability(objects, probabilities):
    initialValue, objectToRange = 0.0, {}
    for i in range(len(objects)):
        objectToRange[objects[i]]=(initialValue, initialValue+probabilities[i])
        initialValue+=probabilities[i]
    randomNumber = random.random()
    for object, rangeVal in objectToRange.iteritems():
        if rangeVal[0]<=randomNumber<=rangeVal[1]: return object

for i in range(numberOfDocuments):
    topic = pickOneByProbability(topics.keys(), [topics[k]['prob'] for k in topics.keys()])
    print ' '.join([topic] + [pickOneByProbability(topics[topic]['tags'].keys(), [topics[topic]['tags'][k] for k in topics[topic]['tags'].keys()]) for i in range(2)] + [random.choice(stopwords) for i in range(5)])
