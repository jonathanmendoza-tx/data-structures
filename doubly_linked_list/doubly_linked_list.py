"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:

	def __init__(self, value, prev=None, next=None):
		self.prev = prev
		self.value = value
		self.next = next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:

	def __init__(self, node=None):
		self.head = node
		self.tail = node
		self.length = 1 if node is not None else 0

	def __len__(self):
		return self.length

	"""
	Wraps the given value in a ListNode and inserts it 
	as the new head of the list. Don't forget to handle 
	the old head node's previous pointer accordingly.
	"""

	def add_to_head(self, value):

		new_node = ListNode(value)

		if self.length == 0:

			self.head = new_node
			self.tail = new_node

		elif self.length == 1:

			self.head = new_node

			self.head.next = self.tail

			self.tail.prev = self.head

		elif self.length > 1:

			old_head = self.head

			self.head = new_node
			self.head.next = old_head

			self.head.next.prev = self.head

		self.length += 1

	"""
	Removes the List's current head node, making the
	current head's next node the new head of the List.
	Returns the value of the removed Node.
	"""

	def remove_from_head(self):

		if self.length == 1:

			value = self.head.value

			self.head = None
			self.tail = None

		elif self.length > 1:
			value = self.head.value

			self.head.next.prev = None
			self.head = self.head.next

		self.length -= 1

		return value

	"""
	Wraps the given value in a ListNode and inserts it 
	as the new tail of the list. Don't forget to handle 
	the old tail node's next pointer accordingly.
	"""

	def add_to_tail(self, value):
		new_node = ListNode(value)

		if self.length == 0:

			self.head = new_node
			self.tail = new_node

		elif self.length == 1:

			self.tail = new_node
			self.tail.prev = self.head

			self.head.next = self.tail

		elif self.length > 1:

			self.tail = new_node

			cur_node = self.head

			while cur_node.next is not None:
				cur_node = cur_node.next

			cur_node.next = self.tail
			self.tail.prev = cur_node

		self.length += 1

	"""
	Removes the List's current tail node, making the 
	current tail's previous node the new tail of the List.
	Returns the value of the removed Node.
	"""

	def remove_from_tail(self):

		if self.length == 0:

			return None

		elif self.length == 1:

			value = self.tail.value

			self.tail = None
			self.head = None

		elif self.length > 1:

			value = self.tail.value

			self.tail.prev.next = None
			self.tail = self.tail.prev

		self.length -= 1

		return value

	"""
	Removes the input node from its current spot in the 
	List and inserts it as the new head node of the List.
	"""

	def move_to_front(self, node):
		# save value, delete(node)
		# add_to_head(value)
		value = node.value

		self.delete(node)
		self.add_to_head(value)

	"""
	Removes the input node from its current spot in the 
	List and inserts it as the new tail node of the List.
	"""

	def move_to_end(self, node):

		if node.next is not None:

			if node.prev is None:

				self.head = node.next
				self.head.prev = None

			else:

				node.prev.next = node.next
				node.next.prev = node.prev

			old_tail = self.tail

			self.tail = node

			self.tail.next = None
			self.tail.prev = old_tail
			self.tail.prev.next = self.tail

	"""
	Deletes the input node from the List, preserving the 
	order of the other elements of the List.
	"""

	def delete(self, node):

		if node is not None:

			if node.next is None and node.prev is None:

				self.head = None
				self.tail = None

			elif node.next is None:

				node.prev.next = None
				self.tail = node.prev

			elif node.prev is None:

				node.next.prev = None
				self.head = node.next

			else:

				node.prev.next = node.next
				node.next.prev = node.prev

			self.length -= 1

		else:
			return None

	"""
	Finds and returns the maximum value of all the nodes 
	in the List.
	"""

	def get_max(self):
		
		cur_node = self.head
		value = self.head.value

		while cur_node.next is not None:
			
			cur_node = cur_node.next

			if value < cur_node.value:
				value = cur_node.value



		return value
