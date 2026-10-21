class DoublyNode:
    def __init__(self, val=-1,nextt=None, prev=None, key=-1):
        self.val = val
        self.next = nextt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.fake_head = DoublyNode()
        self.fake_tail = DoublyNode()
        self.fake_head.next = self.fake_tail
        self.fake_tail.prev = self.fake_head

        self.map = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            node = self.map[key]
            if self.fake_head.next is not node:
                left = node.prev
                right = node.next
                old_head = self.fake_head.next

                self.fake_head.next = node
                node.prev = self.fake_head.next

                node.next = old_head
                old_head.prev = node

                left.next = right
                right.prev = left

            return self.map[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            newnode = DoublyNode(val=value, key=key)
            old_head = self.fake_head.next
            self.fake_head.next = newnode
            newnode.prev = self.fake_head
            newnode.next = old_head
            old_head.prev = newnode

            self.map[key] = newnode

            if len(self.map) == self.capacity + 1:
                old_tail = self.fake_tail.prev
                self.fake_tail.prev = old_tail.prev
                old_tail.prev.next = self.fake_tail

                del self.map[old_tail.key]
        
        else:
            node = self.map[key]
            node.val = value

            if self.fake_head.next is node:
                return
            
            left = node.prev
            right = node.next
            old_head = self.fake_head.next
            self.fake_head.next = node
            node.prev = self.fake_head
            node.next = old_head
            old_head.prev = node
            left.next = right
            right.prev = left
        
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) 