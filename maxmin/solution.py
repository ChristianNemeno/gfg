class Solution:
    def getMinMax(self, arr):
        # code here
        max = arr[0]
        min = arr[0]

        l = len(arr)
        for i in range(l):
            if arr[i] < min:
                min = arr[i]


        for i in range(l):
            if arr[i] > max:
                max = arr[i]


        return [min, max]