import player
import medium
import dialog
import os

'''
All four players are mediumialized and ready to play

	Loop the following:
	- (Shuffle players so we get a new sequence)
	- Player X choose an action
		- Check if that action is possible
	v Then choose a color combination
	v Choose the card to give, if needed
	- Call the function to do action
		- If it is a guessing, do the judge:
			- An successful attempt will end the round
			- An unsuccessful attemp will stop the player from any action afterwards
	- Return the results
	- Goto next player

End the game after one earns 9 points
'''

# medium.player_name[0] = dialog.start_game()
current_player = medium.player_name[0]
while True:
	medium.new_round()
	while True:
		if medium.players[current_player].is_banned:
			print(current_player + '\'s turn has been banned.')
			input("Press Enter to continue... ")
			os.system('cls' if os.name == 'nt' else 'clear')
		else:
			print(current_player + '\'s turn: ')
			# Debug: print everyone's hand
			dialog.print_deck(medium.players[current_player].hand)
			(X, FORMAT) = medium.option_choser(medium.players[current_player], dialog.enter_options(), dialog.enter_color())
			result = dialog.return_result(X, FORMAT)
			if result != -1:
				if result == 100:
					break
				current_player = medium.next_player(current_player)
	if medium.game_end():
		break
	medium.unban_all()
	dialog.current_score(medium.player_name)
print("The game has ended; the winner is: " + medium.winner() + "!")
input("Press Enter to continue... ")
os.system('cls' if os.name == 'nt' else 'clear')
