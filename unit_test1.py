from func import maths , locate_number
import unittest
class Test_case(unittest.TestCase):
    def test_add(self):
        result = maths.add(2,3)
        self.assertEqual(result,5)
    def test_sub(self):
        result = maths.sub(3,2)
        self.assertEqual(result,1)
    def test_locate_number(self):
        list1 = [10, 9, 7, 6, 5, 4, 3, 2, 1]
        test1 = {'input': {'list1': list1, 'querry': 7}, 'output': 2}
        output = locate_number(test1['input']['list1'],test1['input']['querry'])
        self.assertEqual(output,test1['output'])

