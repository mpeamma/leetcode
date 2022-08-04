class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.right = None
        self.left = None

def traverse(start, end, node):
    if start >= node.end:
        if node.right:
            return traverse(start, end, node.right)
        else:
            node.right = Node(start, end)
            return True
    elif end <= node.start:
        if node.left:
            return traverse(start, end, node.left)
        else:
            node.left = Node(start, end)
            return True
    else:
        return False

class MyCalendar:

    def __init__(self):
        self.data = []
        self.root = None      

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return traverse(start, end, self.root)

    def book2(self, start: int, end: int) -> bool:
        for item in self.data:
            if ((start >= item["start"] and start < item["end"]) or 
                (end > item["start"] and end <= item["end"]) or
                (start <= item["start"] and end > item["start"])):
                return False
        
        self.data.append({"start": start, "end": end})
        return True
        


myCalendar = MyCalendar()
print(myCalendar.book(10, 20)) # return True
print(myCalendar.book(15, 25)) # return False, It can not be booked because time 15 is already booked by another event.
print(myCalendar.book(20, 30)) # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.