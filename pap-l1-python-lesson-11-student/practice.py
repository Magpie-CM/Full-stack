# Practice Session
# Make it possible to play multiple rounds of rps, based on player response.
# When the player quits, print out the match results including:
# Number of games played
# Number of games player won
# Number of games computer won
# Number of ties
# Winner of match


# Exercise 1
# 1. Make sure you've finished all the code from the in-class assignment, 
# you've tested it, and it's working
# 2. Copy/paste the code into this file
# Test it again

# Exercise 2
# Create 4 global variables with 0 values:
# player_wins, computer_wins, num_ties, num_games 

# Exercise 3
# 1. Assign a variable: keep_playing to the play_rps_game() function call
# 2. Inside play_rps_game(), inside the else, create a variable keep_playing
# get its value input from the user, ask if they want to play again: 
# "Would you like to keep playing? (y/n) "
# return keep_playing
# 2. Outside all functions, create a while - else loop
# while keep_playing is equal to "y", call play_rps_game(), like this:
# keep_playing = play_rps_game()
# else, pass for now

# Exercise 4
# Create a function to calculate the match final results
# Work out the decision making logic
# Return the results

# Exercise 5
# 1. Inside get_rps_game_results(), increment player_wins, computer_wins, num_ties
# make sure to follow the decision logic
# Don't forget to use the global keyword so you can increment the variables
# like this: 
# global player_wins, num_ties, computer_wins
# 2. Inside play_rps_game(), increment num_games
# Don't forget the glabal keyword

# Exercise 6
# 1. In the while keep_playing loop, inside the else, print a match summary like this:
# Rounds played: 
# You won:      
# Computer won:    
# Ties:
# 2. Call the match final results function and print its output

# Woohoo, congrats! You've written a Python program!

