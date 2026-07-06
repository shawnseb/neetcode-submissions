class MedianFinder:
    

    def __init__(self):
        self.arrmax = []
        self.arrmin = []
        

    def addNum(self, num: int) -> None:
        widthmax = len(self.arrmax)
        widthmin = len(self.arrmin)
        if widthmax == widthmin:
            if len(self.arrmax) == 0 or num <= -1*self.arrmax[0]:
                heapq.heappush(self.arrmax, -1*num)
            else:
                heapq.heappush(self.arrmin, num)

        elif widthmax > widthmin and num < -1*self.arrmax[0]:
            heapq.heappush(self.arrmin,-1*heapq.heappop(self.arrmax))
            heapq.heappush(self.arrmax, -1*num)


        elif widthmin > widthmax and num > self.arrmin[0]:
            heapq.heappush(self.arrmax, -1*heapq.heappop(self.arrmin))
            heapq.heappush(self.arrmin, num)
        elif widthmin == 0 or num >= self.arrmin[0]:
            heapq.heappush(self.arrmin, num)
        else:
            heapq.heappush(self.arrmax, -1*num)
        
        

    def findMedian(self) -> float:
        print(self.arrmin)
        print(self.arrmax)
        if len(self.arrmin) == len(self.arrmax):
            return  (-1*self.arrmax[0] + (self.arrmin[0]))/2
        elif len(self.arrmin) > len(self.arrmax):
            return self.arrmin[0]
        else:
            return -1*self.arrmax[0]
        
        