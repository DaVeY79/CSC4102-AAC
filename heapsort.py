class Heap:
    def __init__(self,items = [],order = "D"):
        self.heap = [None,*items]
        self.order = order
        self.__buildMaxHeap()

    def push(self,data):
        self.heap.append(data)
        self.__buildMaxHeap()

    def pop(self):
        if len(self.heap) == 2:
            val = self.heap.pop()
            return val
        elif len(self.heap) > 2:
            self.__swap(1,len(self.heap)-1)
            val = self.heap.pop()
            if self.order == "A":
                self.__minHeapify(1)
            else:
                self.__maxHeapify(1)
            return val
        else:
            return False

    def __swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def __buildMaxHeap(self):
        if self.order == "A":
            for i in range(len(self.heap)//2,0,-1):
                self.__minHeapify(i)
        else:
            for i in range(len(self.heap)//2,0,-1):
                self.__maxHeapify(i)

    def __maxHeapify(self,index):
        left = index*2
        right = (index*2)+1
        if (len(self.heap) > left) and (self.heap[left] > self.heap[index]):
            largest = left
        else:
            largest = index
        if (len(self.heap) > right) and (self.heap[right] > self.heap[largest]):
            largest = right
        if largest != index:
            self.__swap(index,largest)
            self.__maxHeapify(largest)

    def __minHeapify(self,index):
        left = index*2
        right = (index*2)+1
        if (len(self.heap) > left) and (self.heap[left] < self.heap[index]):
            smallest = left
        else:
            smallest = index
        if (len(self.heap) > right) and (self.heap[right] < self.heap[smallest]):
            smallest = right
        if smallest != index:
            self.__swap(index,smallest)
            self.__minHeapify(smallest)

if __name__ == "__main__":
    m = Heap([27,3,17,16,15,10,1,5,7,12,4,8,9])
    m.push(6)
    while True:
        a = m.pop()
        if a is False:
            break
        else:
            print(a)
