DEFAULT_CAPACITY = 10

def __init__ (self, sourceCollection = None):
    self._items = Array(ArrayBag.DEFAULT_CAPACITY)
    self._size = 0
    if sourceCollection:
        for item in sourceCollection:
            self.add(item)
