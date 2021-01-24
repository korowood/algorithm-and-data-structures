"""
input:
5 3
2 -3 5

output:
7
3
1 2 4 5
"""


def grasshopper_and_coints(arr, n_, k_):
    coints = [0]
    best_step = []

    for i in range(1, len(arr)):
        prev = i - 1
        tmp = coints[prev]
        for j in range(max(0, i - k_), i):
            if coints[j] > tmp:
                prev = j
                tmp = coints[prev]
        best_step.append(prev + 1)
        coints.append(tmp + arr[i])

    best_step.append(n_)
    best_step = set(best_step)
    return best_step, coints[-1]


n, k = map(int, (input().split()))

ml = list(map(int, (input().split())))

ml.insert(0, 0)
ml.append(0)
ans, max_coints = grasshopper_and_coints(ml, n, k)
print(max_coints)
print(len(ans) - 1)
for elem in ans:
    print(elem, end=' ')
