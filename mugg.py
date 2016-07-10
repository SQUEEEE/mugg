class Node:
	def __init__(self,val):
		self.value = val
		self.next = None


class Stack:
	def __init__(self):
		self.top = None
		


	def push(self, val):
		node = Node(val)
		node.next = self.top
		self.top = node

	def pop(self):
		x = self.top.value
		self.top = self.top.next
		return x

	def isEmpty(self):
		if not self.top:
			return True
		else:
			return False

	def peek(self):
		return(self.top.value)



partDeck = list(range(1,16))



'''


myStack = Stack()
print("Stack is empty:", myStack.isEmpty())

myStack.push(5)
print("Stack is empty:", myStack.isEmpty())

val = myStack.pop()

print("Popped value is", val)

myStack.push(3)
myStack.push(4)

print("Top value is", myStack.peek())

'''