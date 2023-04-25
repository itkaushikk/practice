class SmallestInfiniteSet:

    def __init__(self):
        self.allset = []
        for i in range(1, 1001):
            self.allset.append(i)
        
    def popSmallest(self) -> int:
        min_num = min(self.allset)
        self.allset.remove(min_num)
        return min_num

    def addBack(self, num: int) -> None:
        if num not in self.allset:
            self.allset.append(num)
        
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)