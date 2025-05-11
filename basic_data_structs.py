# STACK > last in, last out
# stack code:
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
    
# stack example:
s = Stack()
s.push("A")
s.push("B")
print(s.pop()) # B
print(s.pop()) # A

# QUEUE > first in, first out
# queue code:
class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self._data.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

# queue example:
q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q.dequeue()) # A
print(q.dequeue()) # B

# SYMBOL TABLE
# symbol table code:
class SymbolTable:
    def __init__(self):
        self._st = {}

    def put(self, key, val):
        self._st[key] = val

    def get(self, key):
        return self._st[key]

    def contains(self, key):
        return key in self._st

    def is_empty(self):
        return len(self._st) == 0

    def keys(self):
        return self._st.keys()

    def values(self):
        return self._st.values()

# symbol table example:
st = SymbolTable()
st.put("cat", "meow")
st.put("dog", "bark")
print(st.get("dog"))         # bark
print("cat" in st.keys())    # True
