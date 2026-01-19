class Solution:
    def getSecondLargest(self, arr):
        if len(arr) == 1:
            return -1

        l = len(arr)
        largest = arr[0]
        for i in range(l):
            if arr[i] > largest:
                largest = arr[i]

        second_largest = float('-inf')
        for i in range(l):
            if arr[i] != largest and second_largest < arr[i]:
                second_largest = arr[i]

        return second_largest if second_largest != float('-inf') else -1