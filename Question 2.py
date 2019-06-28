class Node(object):
      
      def __init__(self, value, n = None, p = None):
          self.value=value
          self.next= n
          self.prev= p
          
      def get_next(self):
            return self.next
      
      def get_prev(self):
            return self.prev
      
      def get_value(self):
            return self.value
      
      def set_value(self, value):
            self.value = value
            
      def set_next(self, n):
            self.next = n
            
      def set_prev(self, p):
            self.prev = p
            
 
class List(object):

      def __init__(self, h = None):
            self.size = 0
            self.head = h
            
      def print_list(self):
            cur = self.head
            while cur:
                  print(cur.value)
                  cur = cur.next
                  
      def showe(self):
            return self.end
      
      def showh(self):
            return self.head

      def size(self):
            print(self.size)
            return self.size

      def add(self, value):
            node = Node(value)
            if self.head is None:
                  node.prev = None
                  self.head = node
            else:
                  cur = self.head
                  while cur.next:
                        cur = cur.next
                  cur.next = node
                  node.prev = cur
                  node.next = None
            self.size += 1


      def prepend(self, value):
            if self.head is None:
                  node = Node(value)
                  node.prev = None
                  self.head = node
            else:
                  node = Node(value)
                  self.head.prev = node
                  node.next = self.head
                  self.head = node
                  node.prev = None

      def delete(self, value):
            node = self.head

            while node:
                  if node.get_value() == value:
                        next = node.get_next()
                        prev = node.get_prev()

                        if next:
                              next.set_prev(prev)
                        if prev:
                              prev.set_next(next)
                        else:
                              self.root = node
                        self.size -= 1
                        return True
                  else:
                        node = node.get_next()
            return False
      def find (self, d):
            node = self.head
            while node:
                  if node.get_value() == d:
                        return d
                  else:
                        node = node.get_next()
            return None
      
      
                  

            
                  

                  

l = List()
l.add(1)
l.add(6)
l.add(3)
l.add(7)
l.print_list()
l.find(6)
