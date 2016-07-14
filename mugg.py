import random

PLAYERS = 4
DECKS = 6
playerList = []
finishedDecks = [0]*DECKS
deck = []


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
		if self.isEmpty():
			return None
		else:
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
	def __init__(self, id):
		self.playerId = id
		self.openDeck = Deck()
		self.closedDeck = Deck()
		self.accuracy = 1
		self.nextPlayers = []

	def __str__(self):
		s = "Open Deck: " + str(self.openDeck.peek()) + "\n" + "Closed Deck: " + str(self.closedDeck.peek()) + "\n" + "Accuracy: " + str(self.accuracy) + "\n"
		return s

	def turn(self):

		success = False
		print("My turn!", self.playerId)

		#loop: check if openDeck-card can be put somewhere, then if closedDeck can be put somewehere. if neither, turn is over 
		#somewhere is: firsthand the finishedDecks, then other players


		nextOpen = self.openDeck.peek()

		#check if the finishedDecks have the number before the nextOpen
		finDeck = checkFinishedDecks(nextOpen-1)

		#if this exists,then replace that position with the nextOpen
		if finDeck:
			finishedDeck[finDeck] = self.openDeck.pop()





def checkFinishedDecks(value):
#checks the finished decks for a value and returns the place of the deck in the list

	for deck in finishedDecks:
		if deck == value:
			return finishedDecks.index(value)

	return False

def checkFinishedGame():
	if min(finishedDecks) == 15:
		return True
	else:
		return False


def printPlayerList(pList=playerList):
#for checking status of player cards
	for player in pList:
		print("Player #", player.playerId)
		print(player)

def printDivide():
	print("----------------------------")





def makeDeck():

	partDeck = list(range(1,16))
	counter = 0

	while(counter<6):
		deck.extend(partDeck)
		counter+=1

	random.shuffle(deck)


def initPlayers():

	for i in range(0,PLAYERS):
		playerList.append(Player(i))


	#make the nextPlayers-list
	for player in playerList:
		pIndex = playerList.index(player)
		player.nextPlayers = playerList[pIndex+1:]+playerList[:pIndex]


def handOutCards():

	#hand out cards to players
	while deck:
		for player in playerList:
			if deck:
				player.closedDeck.push(deck.pop())


	#all players put up their first card

	firstCards = []
	for player in playerList:
		firstCard = player.closedDeck.pop()

		player.openDeck.push(firstCard)
		firstCards.append(firstCard)


	#check which player begins

	firstPlayer = firstCards.index(min(firstCards))

	print("First player is", firstPlayer)

	
	#reorder so that the first player is first in the list
	players = playerList[firstPlayer:] + playerList[:firstPlayer]




def initGame():
	makeDeck()
	initPlayers()
	handOutCards()


def gameLoop():

	#the turns in the game take place here
	while not checkFinishedGame():
		for player in playerList:
			player.turn()
			printPlayerList()
			printDivide()


		for i in range(len(finishedDecks)):
			finishedDecks[i]=15




initGame()
gameLoop()

