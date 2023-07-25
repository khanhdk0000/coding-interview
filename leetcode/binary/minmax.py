def check(A, K, max_block_sum):
    block_sum = 0
    count = 0

    for elem in A:
        if block_sum + elem > max_block_sum:
            block_sum = elem
            count += 1
        else:
            block_sum += elem
        
        if count >= K:
            return False

    return True


def solution(K, M, A):

    lower_bound = max(A)
    # upper_bound = sum(A)
    print(lower_bound, upper_bound)

    if K == 1:
        return upper_bound

    if K >= len(A):
        return lower_bound

    while lower_bound <= upper_bound:
        possible_candidate = (lower_bound + upper_bound) // 2
        # print("before", possible_candidate, upper_bound, lower_bound)

        if check(A, K, possible_candidate):
            upper_bound = possible_candidate - 1
        else:
            lower_bound = possible_candidate + 1
        # print("after", possible_candidate, upper_bound, lower_bound)

    return lower_bound

# testcase 1
K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]
print(solution(K, M, A))

# # testcase 2
# K = 2
# M = 5
# A = [5, 3]
# print(solution(K, M, A))

# # testcase 3
# K = 3
# M = 5
# A = [5, 3]
# print(solution(K, M, A))

# # testcase 4
# K = 2
# M = 7
# A = [4, 1, 2, 7]
# print(solution(K, M, A))