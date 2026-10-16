import sys

class Link(object):
    def __init__(self, data, next_link=None):
        self.data = data
        self.next = next_link
class CircularList(object):
  # Constructor
  def __init__ ( self ):
      self.head = None
  # Insert an element (value) in the list
  def insert ( self, data ):
      new_link = Link(data)
      if not self.head:
          self.head = new_link
          new_link.next = self.head
	
  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, data ):

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code

if __name__ == "__main__":
  main()
