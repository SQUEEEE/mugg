import random

PLAYERS = 4
playerList = []


class Node:
	def __init__(self,val):
		self.value = val
		self.next = None


class Deck:
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
		if self.isEmpty():
			return None
		else:
			return(self.top.value)


class Player:
	def __init__(self):
		self.openDeck = Deck()
		self.closedDeck = Deck()
		self.accuracy = 1

	def __str__(self):
		s = "Open Deck: " + str(self.openDeck.peek()) + "\n" + "Closed Deck: " + str(self.closedDeck.peek()) + "\n" + "Accuracy: " + str(self.accuracy) + "\n"
		return s


#for checking status of player cards
def printPlayerList():
	for player in playerList:
		print(player)


def initGame():

	#make deck

	deck = []
	partDeck = list(range(1,16))
	counter = 0

	while(counter<6):
		deck.extend(partDeck)
		counter+=1

	random.shuffle(deck)

	print(len(deck))
	print(deck)



	for i in range(0,PLAYERS):
		playerList.append(Player())


	printPlayerList()

	#hand out cards to players
	while deck:
		for player in playerList:
			if deck:
				player.closedDeck.push(deck.pop())


	printPlayerList()


initGame()

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