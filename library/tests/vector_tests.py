'''
Created on Jun 14, 2011

@author: kykamath
'''
import unittest
from vector import Vector, VectorGenerator

class VectorTests(unittest.TestCase):
    
    def test_initialization(self):
        vector = Vector()
        self.assertEqual(vector, {})
        vector = Vector({1:1})
        self.assertEqual(vector, {1:1})
        self.assertEqual(vector.mod(), 1)
    
    def test__dimension(self):
        vector = Vector()
        self.assertEqual(vector.dimension,0)
        vector[10]=10;vector[11]=11
        self.assertEqual(vector.dimension,2)
    
    def test_addition_and_subtraction(self):
        v1, v2 = Vector(), Vector()
        v1[1]=5;v1[2]=10; v2[1]=5;v2[2]=10
        self.assertEqual(v1+v2,{1: 10, 2: 20})
        self.assertEqual(v1-v2,{1: 0, 2: 0})
    
    def test_dot(self):
        v1 = Vector()
        v1[1]=5;v1[2]=10;
        self.assertEqual(v1.dot({1:5}),25)
        self.assertEqual(v1.dot({1:2,2:1}), 20)
        
    def test_mod(self):
        v1 = Vector()
        v1[1]=4;v1[2]=3
        self.assertEqual(v1.mod(), 5)
        
    def test_getNormalizedVector(self):
        v1 = Vector()
        v1[1]=4;v1[2]=3
        self.assertEqual(v1.getNormalizedVector(), {1:0.8, 2:0.6})
        
class VectorGeneratorDemo:
    @staticmethod
    def getGaussianUnitVector(): VectorGenerator.getRandomGaussianUnitVector(10, 0, 1)
        
if __name__ == '__main__':
    unittest.main()