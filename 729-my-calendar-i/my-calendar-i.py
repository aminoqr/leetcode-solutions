class Tree:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
    
    def insert(self, startTime, endTime):
        curr = self
        while True:
            if startTime >= curr.end:
                if not curr.right:
                    curr.right = Tree(startTime, endTime)
                    return True
                curr = curr.right
            elif endTime <= curr.start:
                if not curr.left:
                    curr.left = Tree(startTime, endTime)
                    return True
                curr = curr.left
            else:
                return False



class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = Tree(startTime, endTime)
            return True
        
        return self.root.insert(startTime, endTime)

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)