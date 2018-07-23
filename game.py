#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 Morten Jakobsen. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

class TicTacToe:
    pos = ["", 1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = "x"
    move = ""
    winner = ""

    def printGameField(self):
        print "┌───┬───┬───┐"
        print "│ " + str(self.pos[7]) + " │ " + str(self.pos[8]) + " │ " + str(self.pos[9]) + " │"
        print "├───┼───┼───┤"
        print "│ " + str(self.pos[4]) + " │ " + str(self.pos[5]) + " │ " + str(self.pos[6]) + " │"
        print "├───┼───┼───┤"
        print "│ " + str(self.pos[1]) + " │ " + str(self.pos[2]) + " │ " + str(self.pos[3]) + " │"
        print "└───┴───┴───┘"
        return

    def tryPerformPlayerMove(self):
        if(self.pos[self.move] == self.move):
            self.pos[self.move] = self.player
            self.switchPlayer()
        else:
            print("Bad move, try again.")
        return

    def askPlayerForMove(self):
        self.move = input("Player " + self.player + ", make a move: ")

    def switchPlayer(self):
        if(self.player == "x"):
            self.player = "o"
        else: 
            self.player = "x"

    def checkForWinner(self):
        if(self.pos[1] == self.pos[2] and self.pos[2] == self.pos[3]):
            self.winner = self.pos[1]
        elif(self.pos[4] == self.pos[5] and self.pos[5] == self.pos[6]):
            self.winner = self.pos[4]
        elif(self.pos[7] == self.pos[8] and self.pos[8] == self.pos[9]):
            self.winner = self.pos[7]
        elif(self.pos[7] == self.pos[4] and self.pos[4] == self.pos[1]):
            self.winner = self.pos[7]
        elif(self.pos[8] == self.pos[5] and self.pos[5] == self.pos[2]):
            self.winner = self.pos[8]
        elif(self.pos[9] == self.pos[6] and self.pos[6] == self.pos[3]):
            self.winner = self.pos[9]
        elif(self.pos[7] == self.pos[5] and self.pos[5] == self.pos[3]):
            self.winner = self.pos[7]
        elif(self.pos[9] == self.pos[5] and self.pos[5] == self.pos[1]):
            self.winner = self.pos[9]
        else:
            self.winner = ""

    def resetGame(self):
        self.pos = ["", 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player = "x"
        self.move = ""
        self.winner = ""

    def playGame(self):
        self.printGameField()
        while(1):
            self.askPlayerForMove()
            self.tryPerformPlayerMove()
            self.printGameField()
            self.checkForWinner()
            if(self.winner != ""):
                print("Winner is " + self.winner + "!")
                break
# End of class

# Begin game execution
game = TicTacToe()
game.playGame()