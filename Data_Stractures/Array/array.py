class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __repr__(self):
        return f"length: {self.length}, data: {self.data}"

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


newArray = MyArray()
newArray.push('hi')
newArray.push('you')
newArray.push('!')
newArray.delete(0)
newArray.push('are')
newArray.push('nice')
newArray.delete(1)
print(newArray)

