#Native Solution

def lastOccur(l,x):

    for i in reversed(range(len(l))):

        if l[i] == x:
            return i
    return -1

l = [10,15,20,20,40,40]

print(20,lastOccur(l, 20))
print(40,lastOccur(l, 40))


#Effective solution

def lastOccur(l, x):
    low = 0
    high = len(l) - 1

    while low <= high:

        mid = (low + high) // 2

        if l[mid] < x:
            low = mid + 1

        elif l[mid] > x:
            high = mid - 1

        else:

            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


l = [5, 10, 10, 10, 10, 20, 20]

print(10,lastOccur(l, 10))
print(20,lastOccur(l, 20))
print(25,lastOccur(l, 25))
