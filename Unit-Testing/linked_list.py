''' Create a new list, B, using list A. Each value of B (K)
    is determined by the value at A[K]. A[0] is always B[0],
    and B[len(B)-1] is always -1.'''

import unittest

def solution(A):
    N = len(A)
    K = 0
    B = []
    for x in range(0,N):
        B.append(A[K])
        if A[K] == -1: break
        else: K = A[K]
    return B

class TestEquilibriumIndex(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution([1, 4, -1, 3, 2]), [1, 4, 2, -1])

    def test2(self):
        self.assertEqual(solution([4, 1, 3, 2, -1]), [4, -1])

    def test3(self):
        self.assertEqual(solution([3, 4, -1, 1, 2]), [3, 1, 4, 2, -1])

if __name__=="__main__":
    unittest.main()
