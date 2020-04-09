def composeLists(lst, indexes):
    """
    :param lst: list of integers
    :param indexes: list of integers
    :return: lists of integers, one containing the elements of lst on positions given by the indexes list,
        the other list containing the remaining elements of lst
    """
    b = []
    for i in range(len(lst)):
        if i in indexes:
            b.append(lst[i])

    c = []
    for i in range(len(lst)):
        if i not in indexes:
            c.append(lst[i])

    return b, c


def avg(lst):
    """
    :param lst: a list of integers
    :return: an integer representing the average of the elements from the input list
    """
    if len(lst) == 0:
        return 0
    sum = 0
    for i in lst:
        sum += i

    return sum / len(lst)


def findLists(lst, start, indexes, result):
    """
    :param lst: the main list A which we want to divide in two separate lists B, C with the same average
    - we go through list A starting from the 'start' index, using it's indexes we create two separate lists
    - calculate and compare the average of B, C
    - if the average of both lists is equal then we found a solution and stop the searching
    - otherwise we continue traversing the list A beginning from another 'start'
      and changing the indexes until we found a valid solution
    """
    if not result:
        for i in range(start, len(lst)):
            indexes.append(i)
            b, c = composeLists(lst, indexes)
            if avg(b) == avg(c):
                result.append([b, c])
            findLists(lst, i + 1, indexes, result)
            indexes.remove(i)
    return result


def main():
    """
    - we read the input list from the file 'input.in'
    :return: True - it is possible to divide the input list in two separate lists with equal averages,
             False - otherwise
    """
    f = open("input.in", "r")

    a = [int(x) for x in f.readline().split()]

    result = findLists(a, 0, [], [])
    if not result:
        return False
    return True
