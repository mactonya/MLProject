import player

# Start Initializing
#	- Players: Add players, choose colors
#	- Init all objects
#	- (Choose characters)
#Loop for x rounds:
#	Stage 1: Information
#		- Dices: (Roll new dices)
#		- Shuffle_piles->Player: Distribute Company / Forecast cards
#	Stage 2: Supply
#		- Main_pile->Player: Deal 2 cards for each player
#		- Board<-Player: Place stock cards
#		- Board/Player/Commercial: (Deal commercials and place them)
#	Stage 3: Demand
#		- Board<-Player: Loop the bid process
#		- Board->Player: After bid, collect cards and take fees
#	Stage 4: Action
#		- Board<-Player: Do +2/-2s
#		- Board->player: Doubling and bankrupting
#		- (Character actions)
#	Stage 5: Sell
#		- Player: Sell
#	Stage 6: Movement
#		- Player/Shuffle_piles: Show all cards
#		- Board<-Player/Shuffle_piles: Move
#		- Board->player: Doubling and bankrupting
#		- Shuffle_piles->player: $$ing
#		- Board: Advance to next round
#	End of game: convert everyting into money