# Duplicate Zeros
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.
# Учитывая массив целых чисел фиксированной длины arr, продублируйте каждое вхождение нуля,
# сдвинув оставшиеся элементы вправо. Обратите внимание, что элементы,
# превышающие длину исходного массива, не записываются.
# Внесите указанные выше изменения во входной массив на месте, не возвращайте ничего из вашей функции.


class Solution(object):
    def duplicateZeros(self, arr):
        if 0 in arr:
            lenarr = len(arr)
            temparr =[]
            for i in range(len(arr)):
                if arr[i] == 0:
                    temparr.append(i)
            for i in reversed(temparr):
                arr.insert(i, 0)
            if len(arr) > lenarr:
                for i in range(len(arr) - lenarr):
                    del arr[-1]


newTest1, nT1 = Solution(), [1, 0, 2, 3, 0, 4, 5, 0]
newTest1.duplicateZeros(nT1)
print(nT1)      # [1,0,0,2,3,0,0,4]

newTest2, nT2 = Solution(), [1, 2, 3]
newTest2.duplicateZeros(nT2)
print(nT2)

