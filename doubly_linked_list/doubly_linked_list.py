class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
          self.next = ListNode(value, self, self.next)


  def insert_before(self, value):
          self.prev = ListNode(value, self.prev, self)


  def delete(self):
      if self.prev != None:
          self.prev.next = self.next
      if self.next != None:
          self.next.prev = self.prev


class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head == None:
        self.head = ListNode(value)
    else:
        self.head.insert_before(value)
        self.head = self.head.prev


  def remove_from_head(self):
      value = self.head.value
      self.head = self.head.next
      if self.head == None:
          self.tail = None
      return value


  def add_to_tail(self, value):
    if self.tail == None:
        self.tail = ListNode(value)
    else:
        self.tail.insert_after(value)
        self.tail = self.tail.next

  def remove_from_tail(self):
    value = self.tail.value
    self.tail = self.tail.prev
    if self.tail == None:
        self.head = None
    return value

  def move_to_front(self, node):
      if self.tail == node:
          value = self.tail.value
          self.tail.delete()
          self.add_to_head(value)


  def move_to_end(self, node):
      if self.head == node:
          value = self.head.value
          self.head.delete()
          self.add_to_tail(value)

  def delete(self, node):
      pass
