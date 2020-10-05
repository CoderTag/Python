import itertools as it


def demo():
    weight = [5, 7]
    measured = set()
    for factor in it.product([1, 0, -1], repeat=2):
        mysum = 5 * factor[0] + 7 * factor[1]
        if mysum > 0:
            measured.add(mysum)
    print(measured)


def solve():
    weight = (x for x in range(1, 38))
    all_seq = [x for x in it.combinations(weight, 4) if sum(x) is 40]
    # print(all_seq)

    for seq in all_seq:
        measured = set()
        for factor in it.product([-1, 0, 1], repeat=4):
            mysum = sum((seq[i] * factor[i] for i in range(4)))
            if mysum > 0:
                measured.add(mysum)
        if len(measured) is 40:
            print("Winner Seq is : ", seq)
            print(measured)
            break


solve()
