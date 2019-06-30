import unittest

#Make a class for the nodes of the linked list

class Node(object):
      #Every time we need a new node, a new one is made here
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
            
#Make the actual list class
class List(object):
      #We make the list with a beginning and a size so we can locate specific nodes
      def __init__(self, h = None):
            self.size = 0
            self.head = h
      #Allows us to print the current list
      def print_list(self):
            ellist = []
            cur = self.head
            while cur:
                  ellist.append(cur.value)
                  cur = cur.next
            return ellist
      

      #Allows us to print the current size of the list
      def size(self):
            cur = self.head
            count = 0
            while cur.next != None:
                  count += 1
                  cur = cur.next
            if cur.next == None:
                  return 0
            
      #The function we use to add a new node
      def add(self, value):
            #We make a node with the desired value using Node class which is initialised above
            node = Node(value)
            #First we check there is nothing in the beginning node
            if self.head is None:
            #If it is empty we place our new desired node at the beginning node
                  node.prev = None
                  self.head = node
                  self.size += 1
            
            else:
            #use a 'Current' value to keep checking next node until one is empty
                  cur = self.head
                  while cur.next:
                        cur = cur.next
            #Once we find a spot without a node, we input our desired node there
                  cur.next = node
                  node.prev = cur
                  node.next = None
                  self.size += 1


      #Function to add at the beginning of the linked list
      def prepend(self, value):
            #If first node doesn't exist then first and last nodes are the same node
            #Therefore we still add at beginning if there is nothing in beginning
            if self.head is None:
                  node = Node(value)
                  node.prev = None
                  self.head = node
                  self.size += 1
            else:
                  node = Node(value)
            #We input the node before the beginning node
                  self.head.prev = node
            #We set the node before the beginning node
            #to be the new beginning node
                  node.next = self.head
                  self.head = node
                  node.prev = None
                  self.size += 1
      #Function to delete a node, check against value and position of node before deleting
      def delete(self, value, pos):
            
            #Make a 'current' node to iterate through
            node = self.head
            
            #Check if this index exists
            if pos < 0 or pos > self.size:
                  print("Position Out of Range")
            
            elif pos != 0:
                  #while we are not at position we iterate
                  #until we arrive at our desired position
                  while pos > 0:
                        node = node.next
                        pos -= 1
                        
                  #if it is not the last node
                  #we can link next to prev and vice versa
                  if node.next is not None and node.value == value:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                        self.size -= 1
                        
                  #if it is last we don't link anything, just clear the pointer
                  elif node.value == value:
                        node.prev.next = None
                        self.size -= 1
                        
                  #if value doesn't match, return false
                  elif node.value != value:
                        return False
                  
            #if it is at the beginning position and our list isn't empty
            #we delete the first node
            elif pos == 0 and node.value == value:
                  self.head = self.head.next
                  self.head.prev = None
                  self.size -= 1

            #if value doesn't match, return false
            elif node.value != value:
                  return False
      def find (self, d):
          node = self.head
          while node:
              if node.get_value() == d:
                  return d
              else:
                  node = node.get_next()
          return None
        
    #function to find middle node
      def find_middle(self):
          m = self.size
          cur = self.head
            #Check where middle is
          if (m/2) == (float(m)/2):
              m = (m/2)-1
                #iterate till we find middle
              while m > 0:
                  cur = cur.next
                  m -= 1
          elif (m/2) != (float(m)/2):
              m = (m/2)
              while m > 0:
                  cur = cur.next
                  m -= 1
          return cur.value

class ListTest(unittest.TestCase):

    def testAdding(self):
            l.add(5)
            self.assertEqual(l.find(5), 5)
            l.add(3)
            self.assertEqual(l.print_list(), [5, 3])
            l.add(4)
            self.assertEqual(l.print_list(), [5, 3, 4])
            l.prepend(6)
            self.assertEqual(l.print_list(), [6, 5, 3, 4])
            l.prepend(9)
            self.assertEqual(l.print_list(), [9, 6, 5, 3, 4])
            l.prepend(2)
            self.assertEqual(l.print_list(), [2, 9, 6, 5, 3, 4])
            l.add(2)
            self.assertEqual(l.print_list(), [2, 9, 6, 5, 3, 4, 2])

    def testFinding(self):
        self.assertEqual(l.find_middle(), 5)
        l.add(3)
        l.add(1)
        self.assertEqual(l.find_middle(), 3)
    


l = List()

                
