"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new = Node(value)
    if self.head == None:
        self.head = new
        self.tail = new
    else:
        self.tail.set_next(new)
        self.tail = new

  def remove_head(self):
    if self.head != None:
        currentHead = self.head
        self.head = self.head.get_next()
        if self.head == None:
            self.tail = None
        return currentHead.value
    else:
        return None

  def contains(self, value):
    first = self.head
    while first != None:
      if first.value == value:
        return True
      else:
        first = first.next_node
    return False

  def get_max(self):
    first = self.head
    values = []
    if first == None:
      return None
    while first:
      values.append(first.value)
      first = first.next_node
    return max(values)
