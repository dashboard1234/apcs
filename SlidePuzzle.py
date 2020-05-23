#from tkinter import *
from tkinter import constants
from tkinter import Canvas
from tkinter import Tk
#from tkinter import messagebox
import random
import os

class Tile:
    def __init__(self, tileSize, number): 
        self.number = number
        if number != 0:
            self.image = Canvas(width=tileSize, height=tileSize, bg = 'cyan') 
            text = self.image.create_text(0,0,fill="red",font="Times 40 italic bold", \
                            text=str(number), anchor=constants.NW)
            coords = self.image.bbox(text)
            xOffset = (tileSize / 2) - ((coords[2] - coords[0]) /2 )
            yOffset = (tileSize / 2) - ((coords[3] - coords[1]) /2)
            self.image.move(text, xOffset, yOffset)
        else:
            self.image = Canvas(width=tileSize, height=tileSize, bg = 'white')
            #pass
       

class Board:
    def __init__(self, gridSize, tileSize):
        self.window = Tk()
        #self.window = window
        self.window.title("Use arrow keys or mouse to move, spacebar to restart")
        self.tiles = [None]*gridSize*gridSize
        self.tileLocations = {}
        self.gridSize = gridSize
        self.tileSize = tileSize
        self.window.bind("<space>", lambda event:self.scramble())
        self.window.bind("<KeyPress>", lambda event: self.emptyTileMove(event))
        self.window.bind("<Button-1>", lambda event: self.clickMove(event))
               
        for i in range(gridSize):
            for j in range(gridSize):
                if i == gridSize-1 and j == gridSize-1:
                    #self.tiles.append(Tile(tileSize, 0))
                    self.tiles[0] = Tile(tileSize, 0)
                    self.tileLocations[0] = (i,j)
                else:
                    #self.tiles.append(Tile(tileSize, i*gridSize + j + 1))
                    self.tiles[i*gridSize + j + 1] = Tile(tileSize, i*gridSize + j + 1)
                    self.tileLocations[i*gridSize + j + 1] = (i,j)
        print(self.tileLocations)
        self.scramble()

    def emptyTileNeighbors(self):
        return [(self.tileLocations[0][0]-1, self.tileLocations[0][1]),
                (self.tileLocations[0][0], self.tileLocations[0][1]-1),
                (self.tileLocations[0][0]+1, self.tileLocations[0][1]),
                (self.tileLocations[0][0], self.tileLocations[0][1]+1)]
    def canMove(self, tileNumber: int):
        return (self.tileLocations[tileNumber] in self.emptyTileNeighbors())

    def getTileNumberByPos(self, tilePos): 
        for key, value in self.tileLocations.items(): 
            if tilePos == value: 
                return key 
    
    def scramble(self): # start from solvable initial position, move iterations moves
        iterations = 250
        for i in range(iterations):
            emptyNeighbors = self.emptyTileNeighbors()
            picked = random.choice(emptyNeighbors)
            if picked in self.tileLocations.values():
                pickedTileNumber = self.getTileNumberByPos(picked)
                # swap empty tile position and picked tile
                self.tileLocations[0], self.tileLocations[pickedTileNumber] \
                    = self.tileLocations[pickedTileNumber], self.tileLocations[0]
            else:
                continue
        self.redraw()
       
    def redraw(self):
        gridSize = self.gridSize
        for i in range(gridSize):
            for j in range(gridSize):
                posX, posY = self.tileLocations[i*gridSize+j][0], self.tileLocations[i*gridSize+j][1]
                self.tiles[i*gridSize+j].image.grid(row=posX, column=posY)
    
    def emptyTileMove(self, event):
        emptyPos = self.tileLocations[0]
        if event.keysym == "Up":
            emptyUpPos = (emptyPos[0]-1, emptyPos[1])
        elif event.keysym == "Down":
            emptyUpPos = (emptyPos[0]+1, emptyPos[1])
        elif event.keysym == "Right":
            emptyUpPos = (emptyPos[0], emptyPos[1]+1)
        elif event.keysym == "Left":
            emptyUpPos = (emptyPos[0], emptyPos[1]-1)
        if emptyUpPos in self.tileLocations.values():
            numberToSwap = self.getTileNumberByPos(emptyUpPos)
            self.tiles[0].image.grid(row=emptyUpPos[0], column=emptyUpPos[1]) 
            self.tiles[numberToSwap].image.grid(row=emptyPos[0], column=emptyPos[1])
            self.tileLocations[0], self.tileLocations[numberToSwap] \
                    = self.tileLocations[numberToSwap], self.tileLocations[0]
        else:
            self.illegalMove()
        self.checkWin()

    def clickMove(self, event):
        #print(event.x_root,event.y_root)
        posX, posY = (event.y_root - 50) // (self.tileSize+10), event.x_root // (self.tileSize+10)
        if (posX, posY) in self.emptyTileNeighbors():
            emptyPos = self.tileLocations[0]
            numberToSwap = self.getTileNumberByPos((posX,posY))
            self.tiles[0].image.grid(row=posX, column=posY)
            self.tiles[numberToSwap].image.grid(row=emptyPos[0], column=emptyPos[1])
            self.tileLocations[0], self.tileLocations[numberToSwap] \
                    = self.tileLocations[numberToSwap], self.tileLocations[0]
        self.checkWin()

    def checkWin(self):
        print(self.tileLocations)
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if i == self.gridSize -1 and j == self.gridSize -1:
                    if self.tileLocations[0] != (self.gridSize-1, self.gridSize-1):
                        #print((self.gridSize -1,self.gridSize -1),0, self.tileLocations[0])
                        return
                elif self.tileLocations[i*self.gridSize + j + 1] != (i, j):
                    #print((i,j),i*self.gridSize + j + 1,self.tileLocations[i*self.gridSize + j + 1])
                    return
        print("winner")
        winner = lambda x: os.system("say you win")
        winner(1)
    
    def illegalMove(self):
        beep = lambda x: os.system("say oops")
        beep(1)
        
if __name__ == "__main__":
    bd = Board(3, 120)
    bd.window.mainloop()

    
    