from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


def permutations(lst):
    if len(lst) == 0:
        return [[]]

    stack = ArrayStack()
    queue = ArrayQueue()
    results = []


    queue.enqueue([])

    while not queue.is_empty():
        part = queue.dequeue()

        if len(part) == len(lst):
            results.append(part)
        else:
            for elem in lst:
                if elem not in part:
                    new_partial = part + [elem]
                    queue.enqueue(new_partial)
    return results



print(permutations([1, 2, 3]))