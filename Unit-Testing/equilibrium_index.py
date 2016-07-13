''' equilibrium_index.py
    Andrew Ortego
    7/6/2016

    Determines if a given array has an equilibrium indices in it. Returns a list
    of each index which is an equilibrium index for a given array. If no 
    equilibrium index is found, -1 is returned.
'''

import unittest


def solution(array):
    ''' Collect all index values which are equilibrium indices and store them
        in a list. Return the list if it is not empty, otherwise return -1.'''
    positions = [cur_index for cur_index in range(len(array)-1) 
        if is_equilibrium_index(array, cur_index)]
    if positions != []:
        return positions
    return -1


def is_equilibrium_index(array, index):
    ''' Calculate the sum of all left-most and right-most indices based on the
        current position of the equilibrium index.'''
    # sum of all integers to the right of the first index:
    if index == 0:
        sum_left  = array[0]
        sum_right = sum(array[i] for i in range(index+1, len(array)))

    # sum of all integers to the left of the last index:
    elif index == len(array)-1:
        sum_left  = sum(array[i] for i in range(index))
        sum_right = array[index]

    # sum of all integers to the left and right of current index:
    else:
        sum_left  = sum(array[i] for i in range(index))
        sum_right = sum(array[i] for i in range(index+1, len(array)))

    return sum_left == sum_right


class TestEquilibriumIndex(unittest.TestCase):
    ''' The equilibrium index of a sequence is an index such that the sum of 
    elements at lower indexes is equal to the sum of elements at higher indexes.

    In the array [-7, 1, 5, 2, -4, 3, 0], 3 is an equilibrium index, because:
    A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

    6 is also an equilibrium index, because:
    A[0] + A[1] + A[2] + A[3] + A[4] + A[5] = A[6]'''


    def test_no_equilibrium(self):
        ''' Base case. No indices to iterate over.'''
        array0 = [1]
        self.assertEqual(solution(array0), -1)


    def test_first_index(self):
        ''' Case where the first index is the equilibrium index.'''
        array = [6, 10, -4]
        self.assertEqual(solution(array), [0])


    def test_middle_index(self):
        ''' Case where the middle index is the equilibrium index.'''
        array1 = [-3, -1, 0, -1, -3]
        self.assertEqual(solution(array1), [2])


    def test_last_index(self):
        ''' Case where the last index is the equilibrium index.'''
        array3 = [10, -4, 6]
        self.assertEqual(solution(array3), [2])


    def test_all_indices(self):
        ''' Case where all indices are symmetrical.'''
        array2 = [99, 0, 99]
        self.assertEqual(solution(array2), [0, 1, 2])


    def test_known_1(self):
        ''' Random data.'''
        array4 = [-7, 1, 5, 2, -4, 3, 0]
        self.assertEqual(solution(array4), [3, 6])


    def test_known_2(self):
        ''' More random data.'''
        array5 = [-1, 3, -4, 5, 1, -6, 2, 1]
        self.assertEqual(solution(array5), [1, 3])


if __name__ == '__main__':
    unittest.main()

