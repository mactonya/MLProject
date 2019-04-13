import player
import init
import dialog
'''
All four players are initialized and ready to play

	Loop the following:
	- (Shuffle players so we get a new sequence)
	- Player X choose an action
		- Check if that action is possible
	- Then choose a color combination
	- Choose the card to give, if needed
	- Call the function to do action
		- If it is a guessing, do the judge:
			- An successful attempt will end the round
			- An unsuccessful attemp will stop the player from any action afterwards
	- Return the results
	- Goto next player

End the game after one earns 9 points
'''

# dialog.start_game()
init.new_round()
dialog.print_deck(init.players['A'].hand)
(X, FORMAT) = init.option_choser(init.players['A'], dialog.enter_options(), dialog.enter_color())
if X != -1:
	dialog.return_result(X, FORMAT)