import bisect


# https://leetcode.com/discuss/interview-question/3138744/Cohesity-OA-or-Graph-with-DP-or-2023/1788095
def get_minimum_groups(length: list, breadth: list):
    stack = []
    for i in [j for _, j in sorted(zip(length, breadth))]:
        j = bisect.bisect_right(stack, i)
        stack[j:j + 1] = [i]

    return len(stack)


# https://stackoverflow.com/questions/75829157/partition-rectangles-into-groups
def get_minimum_groups2(length: list, breadth: list):
    n = len(length) - 1
    rectangles = [(length[i], breadth[i]) for i in range(n)]
    rectangles.sort(key=lambda x: x[0])
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if rectangles[i][1] >= rectangles[j][1]:
                lis[i] = max(lis[i], lis[j] + 1)

    return n - max(lis)


def main():
    print("Hello world.")
    length = [1, 2, 5, 4, 3]
    breadth = [3, 5, 2, 1, 3]
    print(get_minimum_groups(length=length, breadth=breadth))
    print(get_minimum_groups2(length=length, breadth=breadth))

    length = [1, 1, 1, 1, 1]
    breadth = [1, 1, 1, 1, 1]
    print(get_minimum_groups(length=length, breadth=breadth))
    print(get_minimum_groups2(length=length, breadth=breadth))


if __name__ == "__main__":
    main()
