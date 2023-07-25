# /****************************************************************
#  *             CODERBYTE PERMUTATION STEP CHALLENGE             *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function PermutationStep(num) take the num parameter*
#  * being passed & return the next number greater than num using *
#  * the same digits.                                             *
#  *                                                              *
#  * For example: if num is 123 return 132, if it's 12453 return  *
#  * 12534. If a number has no greater permutations,              *
#  * return -1 (ie. 999).                                         *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: 11121		                                *
#  * Output 1: 11211                                              *
#  *                                                              *
#  * Input 2: 41352                                               *
#  * Output 2: 41523                                              *
#  *                                                              *
#  * Input 3: 897654321                                           *
#  * Output 3: 912345678                                          *
#  *                                                              *
#  * Input 4: 76666666                                            *
#  * Output 4: -1                                                 *
#  *                                                              *
#  ***************************************************************/

def heaps_algorithm_iterative(A):
    n = len(A)
    c = [0] * n
    print(A)
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                A[0], A[i] = A[i], A[0]
            else:
                A[c[i]], A[i] = A[i], A[c[i]]
            print(A)
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

def PermutationStep(num):
    pass

input = 123
# print(PermutationStep(input))
heaps_algorithm_iterative([1,2,3])