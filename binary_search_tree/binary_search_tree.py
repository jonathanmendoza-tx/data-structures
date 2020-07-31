"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import *
from stack import *

class BSTNode:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, value):

		if value < self.value:

			if self.left is None:

				self.left = BSTNode(value)

			else:
				self.left.insert(value)

		elif value >= self.value:

			if self.right is None:

				self.right = BSTNode(value)

			else:
				self.right.insert(value)

	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):

		if self.value == target:
			return True

		if target < self.value:

			if not self.left:

				return False

			else:
				return self.left.contains(target)

		else:
			if not self.right:

				return False

			else:
				return self.right.contains(target)

	# Return the maximum value found in the tree
	def get_max(self):

		if not self:

			return None

		max_value = self.value

		current = self

		while current:

			if current.value > max_value:
				max_value = current.value

			current = current.right

		return max_value

	# Call the function `fn` on the value of each node
	def for_each(self, fn):

		fn(self.value)

		if self.left is not None:
			self.left.for_each(fn)

		if self.right is not None:
			self.right.for_each(fn)

		# cur_node = self
		# f(cur_node.value)

		# while cur_node.left:
		# 	cur_node = cur_node.left
		# 	fn(cur_node)

	# stretch
	def delete(self, value):
		# search like in contains()

		# different cases
		# if node at bottom level
			# update parent left/right = None

		# if node has only one child
			# parent.left/right = node.left/right

		# if node has two children
			# larger valued child becomes parent of sibling

		# Part 2 -----------------------

		# Print all the values in order from low to high
		# Hint:  Use a recursive, depth first traversal
		pass

	def in_order_print(self):

		if self:
			if self.left:
				# go left with recurssion

				self.left.in_order_print()

			print(self.value)

			if self.right:
				# go right with recurssion
				self.right.in_order_print()

	# Print the value of every node, starting with the given node,
	# in an iterative breadth first traversal
	def bft_print(self):
		# use a queue
		# print current node
		# add children to queue (left to right if not None)
		
		q = Queue()

		q.enqueue(self)

		while len(q) > 0:

			self = q.dequeue()

			print(self.value)

			if self.left:
				q.enqueue(self.left)

			if self.right:
				q.enqueue(self.right)

			


	# Print the value of every node, starting with the given node,
	# in an iterative depth first traversal
	def dft_print(self):
		#create a stack
		stack = Stack()

		#push some initial value(s) onto stack
		stack.push(self)

		#while stack is not empty
		while len(stack) > 0:
			#pop ???
			current = stack.pop()
			#print ???
			print(current.value)
			#push ???
			if current.left:
				stack.push(current.left)

			if current.right:
				stack.push(current.right)

		#done when stack is empty

	# Stretch Goals -------------------------
	# Note: Research may be required

	# Print Pre-order recursive DFT
	def pre_order_dft(self):
		pass

	# Print Post-order recursive DFT
	def post_order_dft(self):
		pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
