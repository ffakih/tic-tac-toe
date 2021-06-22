# tic-tac-toe AI: CMPT310: Artifical Intelligence

User vs Machine tic tac toe implemented using Monte Carlo Algorithm

## Description

The AI always wins if the AI starts first
When the user starts first, the user can set up a “fork”, a “fork” is a triangular trap technique used in tic-tac-toe that is similar to a checkmate
We don’t have a way to teach the AI to catch the trap unless we implement a heuristic, which goes against the assignment requirements

	e.g   	  X | 1 | X
		  3 | 4 | 5
		  X | 7 | 8

The User has THREE ways to win here, it is unstoppable.
This happens because the Monte Carlo Algorithm maximizes the amount of wins the AI will get, the algorithm does not account for being set up for traps. Even after adjusting the weight of win / draw / lose, to maximize draws rather than wins, although it decreases the AI’s loss rate, but there are still ways for the AI to lose (ONLY IF THE USER GOES FIRST)


### Executing program

Run using python

## Authors

Firas Fakih

