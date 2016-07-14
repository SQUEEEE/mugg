import random

PLAYERS = 4
DECKS = 6
playerList = []
finishedDecks = [0]*DECKS


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

def checkFinishedDecks(value):
#checks the finished decks for a value and returns the place of the deck in the list

	for deck in finishedDecks:
		if deck == value:
			return finishedDecks.index(value)

	return False



def printPlayerList():
#for checking status of player cards
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


	print("First instance of 0 in finishedDecks:", checkFinishedDecks(0))

	print("First instance of 5 in finishedDecks:", checkFinishedDecks(5))

	print("Changing finishedDecks[3] to 5")

	finishedDecks[3] = 5


	print("First instance of 5 in finishedDecks:", checkFinishedDecks(5))

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