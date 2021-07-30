class array:
    def __init__(self, nums=None):
        if nums == None:
            try:
                self.arr = list(input().split(" "))
                self.arr = [int(i) for i in self.arr]
            except:
                print("Input a valid array of integers")
                quit()
        else:
            self.arr = nums
        
    def swap(self, i1, i2):
        self.arr[i1], self.arr[i2] = self.arr[i2], self.arr[i1]

    def bubbleSortRecurse(self, n):
        for i in range(n-1):
            if self.arr[i] > self.arr[i+1]:
                self.swap(i, i+1)
            
        if n-1 > 1:
            self.bubbleSortRecurse(n-1)

    def bubbleSortIterative(self):
        isSorted = False
        lastUnsorted = len(self.arr)-1
        while not isSorted:
            isSorted = True
            for i in range(lastUnsorted):
                if self.arr[i] > self.arr[i+1]:
                    self.swap(i, i+1)
                    isSorted = False
            lastUnsorted -= 1

    def bubbleSort(self, method="i"):
        if method=="r":
            self.bubbleSortRecurse(len(self.arr))
        else:
            self.bubbleSortIterative()

    
if __name__ == "__main__":
    import random as r
    sample_size = 1000
    nums = r.sample(range(-100000, 100000), sample_size)

    x = array(nums)
    x.bubbleSort()
    for i in range(len(x.arr)-1):
        print(x.arr[i], end=" < ")
    print(x.arr[-1])
