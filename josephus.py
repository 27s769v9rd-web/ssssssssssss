import sys

class Link(object):
    def __init__(self, data, next_link=None):
        self.data = data
        self.next = next_link

class CircularList(object):
    # Constructor
    def __init__(self):
        self.head = None
    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        if not self.head:
            self.head = new_link
            new_link.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_link
            new_link.next = self.head
    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        if not self.head:
            return None
        current = self.head
        prev = None
        while True:
            if current.data == data:
                # If it's the only element
                if current == self.head and current.next == self.head:
                    self.head = None
                    return current
                # If we are deleting the head
                if current == self.head:
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = current.next
                    last.next = self.head
                    return current
                # Deleting from middle or end
                prev.next = current.next
                return current
            prev = current
            current = current.next
            if current == self.head:
                break
        return None
    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        current = self.find(start)
        if not current:
            return None, None
        for _ in range(n - 1):
            current = current.next
        deleted_data = current.data
        next_link = current.next
        self.delete(deleted_data)
        return deleted_data, next_link
    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if not self.head:
            return "[]"
        res = "["
        current = self.head
        while True:
            res += str(current.data)
            current = current.next
            if current == self.head:
                break
            res += ", "
        res += "]"
        return res

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    if not line:
        return
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    clist = CircularList()
    for i in range(1, num_soldiers + 1):
        clist.insert(i)

    current_start = start_count
    for _ in range(num_soldiers):
        deleted_data, next_link = clist.delete_after(current_start, elim_num)
        print(deleted_data)
        if next_link:
            current_start = next_link.data

if __name__ == "__main__":
    main()
