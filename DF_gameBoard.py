import DF_player
class gameBoard:

	def __init__(self):
		ubication={
			"home":0,
			"moonPortal": [
				{"portal":1, "moonPrice":[1,1]},
				{"portal":2, "moonPrice":[2,3]}, 
				{"portal":3, "moonPrice":[4,5]}
			],
			"sunPortal": [
				{"portal":1, "sunPrice":[1,1]},
				{"portal":2, "sunPrice":[2,3]}, 
				{"portal":3, "sunPrice":[4,5]}
			],
			"mixPortal": {"portal":1, "price":{"moonPrice":6, "sunPrice":6, "mixedPrice":[5,5]}}    
		}
	def playerMovement(nextUbi, playerMoving,players):
		for idx,x in enumerate(players):
			if players[idx].ubi == nextUbi:
				playerMoving.ubi=nextUbi
				players[idx].ubi="home"
