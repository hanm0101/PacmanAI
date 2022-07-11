# sampleAgents.py
# parsons/07-oct-2017
#
# Version 1.1
#
# Some simple agents to work with the PacMan AI projects from:
#
# http://ai.berkeley.edu/
#
# These use a simple API that allow us to control Pacman's interaction with
# the environment adding a layer on top of the AI Berkeley code.
#
# As required by the licensing agreement for the PacMan AI we have:
#
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# The agents here are extensions written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game
import util

# RandomAgent
#
# A very simple agent. Just makes a random pick every time that it is
# asked for an action.
class RandomAgent(Agent):

    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # Random choice between the legal options.
        return api.makeMove(random.choice(legal), legal)

# RandomishAgent
#
# A tiny bit more sophisticated. Having picked a direction, keep going
# until that direction is no longer possible. Then make a random
# choice.
class RandomishAgent(Agent):

    # Constructor
    #
    # Create a variable to hold the last action
    def __init__(self):
         self.last = Directions.STOP
    
    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # If we can repeat the last action, do it. Otherwise make a
        # random choice.
        if self.last in legal:
            return api.makeMove(self.last, legal)
        else:
            pick = random.choice(legal)
            # Since we changed action, record what we did
            self.last = pick
            return api.makeMove(pick, legal)

# SensingAgent
#
# Doesn't move, but reports sensory data available to Pacman
class SensingAgent(Agent):

    def getAction(self, state):

        # Demonstrates the information that Pacman can access about the state
        # of the game.

        # What are the current moves available
        legal = api.legalActions(state)
        print ("Legal moves: ", legal)

        # Where is Pacman?
        pacman = api.whereAmI(state)
        print ("Pacman position: ", pacman)

        # Where are the ghosts?
        print ("Ghost positions:")
        theGhosts = api.ghosts(state)
        for i in range(len(theGhosts)):
            print (theGhosts[i])

        # How far away are the ghosts?
        print ("Distance to ghosts:")
        for i in range(len(theGhosts)):
            print (util.manhattanDistance(pacman,theGhosts[i]))

        # Where are the capsules?
        print ("Capsule locations:")
        print (api.capsules(state))
        
        # Where is the food?
        print ("Food locations: ")
        print (api.food(state))

        # Where are the walls?
        print ("Wall locations: ")
        print (api.walls(state))
        
        # getAction has to return a move. Here we pass "STOP" to the
        # API to ask Pacman to stay where they are.
        return api.makeMove(Directions.STOP, legal)

# GoWestAgent
#
# You should write a GoWestAgent
#which always tries to have Pacman go west on the grid when it is possible. What happens when WEST is
#not a legal move is up to you.
# 
# 
class GoWestAgent(Agent):
    
    def getAction(self, state):
        # Get the actions we can try, and remove "WEST" if that is one of them.
        legal = api.legalActions(state)
        if Directions.WEST in legal:
            legal.remove(Directions.STOP)
        # If there is west as an option
        # go West direction
        if Directions.WEST in legal:
            return api.makeMove(Directions.WEST, legal)
        else:
            # Otherwise stop
            pick = Directions.STOP
            # Since we changed action, record what we did
            self.last = pick
            return api.makeMove(pick, legal)

#C:\Users\User\Desktop\AIN\pacman\pacman>python pacman.py --pacman GoWestAgent
#Traceback (most recent call last):
 # File "pacman.py", line 680, in <module>
  #  runGames( **args )
  #File "pacman.py", line 646, in runGames
    #game.run()
  #File "C:\Users\User\Desktop\AIN\pacman\pacman\game.py", line 700, in run
   # self.state = self.state.generateSuccessor( agentIndex, action )
  #File "pacman.py", line 107, in generateSuccessor
   # PacmanRules.applyAction( state, action )
  #File "pacman.py", line 343, in applyAction
   # raise Exception("Illegal action " + str(action))
#Exception: Illegal action West

# HungryAgent
#
# 
class HungryAgent(Agent):

    '''
    def getAction(self, state):

        # Where is Pacman?
        pacman = api.whereAmI(state)
        print ("Pacman position: ", pacman)

        # Where is the food?
        print ("Food locations: ")
        foods = api.food(state)
        for i in range(len(foods)):
            print (foods[i])

        # How far away are the food?
        print ("Distance to food:")
        for i in range(len(foods)):
            distance = util.manhattanDistance(pacman,foods[i])
            print (util.manhattanDistance(pacman,foods[i]))
            
        # What are the current moves available
        legal = api.legalActions(state)
        print ("Legal moves: ", legal)

        if Directions.STOP in legal:
            legal.remove(Directions.STOP)

        # Move towards the shortest distance food first to the West, then to the North.
        if self.topLeft == False:
            if pacman[0] > minX + 1:
                if Directions.WEST in legal:
                    return api.makeMove(Directions.WEST, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)
            else:
                if Directions.NORTH in legal:
                    return api.makeMove(Directions.NORTH, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)

        #pacman to location
        #index = 
        #your own state
        #if then 

    #def shortestDist(distance):
            #shortest = distance[0]
        #for i in range(1, len(distance)):
            #if distance[i] < shortest:
                #shortest = distance[i]
       # return shortest
       '''

    def sortFoodByDistance(self, foodList, distList):
        gap = len(distList) / 2
        while gap > 0:
            for i in range(gap, len(distList)):
                tempFood = foodList[i]
                tempDist = distList[i]
                j = i
                while j >= gap and distList[j - gap] > tempDist:
                    foodList[j] = foodList[j - gap]
                    distList[j] = distList[j - gap]
                    j = j - gap
                    foodList[j] = tempFood
                distList[j] = tempDist
            gap = gap / 2

    def getAction(self, state):
        legal = api.legalActions(state)
        pacmanPosition = api.whereAmI(state)
        foodLocations = api.distanceLimited(api.food(state), state)
        foodDistances = []

        for location in foodLocations:
            foodDistances.append(util.manhattanDistance(location, pacmanPosition))

        self.sortFoodByDistance(foodLocations, foodDistances)

        if len(foodLocations) > 0:
            closestFood = foodLocations[0]
            if len(foodLocations) > 2 and (util.manhattanDistance(pacmanPosition, closestFood) == util.manhattanDistance(pacmanPosition, foodLocations[1])):
                closestFood = foodLocations[random.randint(0, 1)]
            validMoves = []
            if closestFood[0] < pacmanPosition[0] and Directions.WEST in legal:
                validMoves.append(Directions.WEST)
            if closestFood[0] > pacmanPosition[0] and Directions.EAST in legal:
                validMoves.append(Directions.EAST)
            if closestFood[1] < pacmanPosition[1] and Directions.SOUTH in legal:
                validMoves.append(Directions.SOUTH)
            if closestFood[1] > pacmanPosition[1] and Directions.NORTH in legal:
                validMoves.append(Directions.NORTH)
            return api.makeMove(random.choice(validMoves), legal)
        return api.makeMove(random.choice(legal), legal)
    

# Corner Seeking Agent
#Find out where the corners are.
# Remember where Pacman is going and where it has gone.
class CornerSeekingAgent(Agent):

    # Constructor
    #
    # Create a variable to hold the last action as lastAction
    def __init__(self):
         self.topRight = False
         self.topLeft = False
         self.bottomRight = False
         self.bottomLeft = False

    def getAction(self, state):
        # Where are the corners?
        #print ("Corner locations: ")
        corners = api.corners(state)
        #for i in range(len(corners)):
            #print (corners[i])

        # Variables for max and min
        minX = 100 #set up minimum value for the horizontal move
        minY = 100 #set up minimum value for the vertical move
        maxX = 0 #set up max for horizontal
        maxY = 0 #set up max for vertical

        # Find the maximum and minimum values for the corners 
        for i in range(len(corners)): #going through all the lengths of corners
            corner_X = corners[i][0] #horizontal values
            corner_Y = corners[i][1] #vertical values
            
            if corner_X < minX:  #if the horizontal value is smaller than the minimum for X then the minimum is the value 
                minX = corner_X
            if corner_Y < minY: #if the vertical value is smaller than the minimum for Y then minimum is the value 
                minY = corner_Y
            if corner_X > maxX: #if the horizontal value is greater than the max then the value is the max
                maxX = corner_X
            if corner_Y > maxY: #if the vertical value is greater than the max then the value is the max
                maxY = corner_Y

        # What are the current moves available
        legal = api.legalActions(state)

        if Directions.STOP in legal:
            legal.remove(Directions.STOP)

        # Where is Pacman?
        pacman = api.whereAmI(state)

        # Check if pacman has been in Top Left corner, then move to Top Left
        #
        # Check we aren't there:
        if pacman[0] == minX + 1:
           if pacman[1] == maxY - 1:
                print ("Got to Top Left Corner!")
                self.topLeft = True

        # If not, move towards it, first to the West, then to the North.
        if self.topLeft == False:
            if pacman[0] > minX + 1:
                if Directions.WEST in legal:
                    return api.makeMove(Directions.WEST, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)
            else:
                if Directions.NORTH in legal:
                    return api.makeMove(Directions.NORTH, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)

        # Check if pacman has been in Bottom Left corner, then move to Bottom Left
        #
        # Check we aren't there:
        if pacman[0] == minX + 1:
            if pacman[1] == minY + 1:
                print ("Got to Bottom Left Corner!")
                self.bottomLeft = True

        # If not, move towards it, first to the West, then to the North.
        if self.bottomLeft == False:
            if pacman[0] > minX + 1:
                if Directions.WEST in legal:
                    return api.makeMove(Directions.WEST, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)
            else:
                if Directions.SOUTH in legal:
                    return api.makeMove(Directions.SOUTH, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)

        # Check if pacman has been in Top Right corner, then move to Top Right
        #
        # Check we aren't there:
        if pacman[0] == maxX - 1:
           if pacman[1] == maxY - 1:
                print ("Got to Top Right Corner!")
                self.topRight = True

        # If not, move towards it, first to the East, then to the North.
        if self.topRight == False:
            if pacman[0] < maxX - 1:
                if Directions.EAST in legal:
                    return api.makeMove(Directions.EAST, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)
            else:
                if Directions.NORTH in legal:
                    return api.makeMove(Directions.NORTH, legal)
                else:
                    pick = random.choice(legal)
                    return api.makeMove(pick, legal)
        
        # Check if pacman has been in Bottom Right corner, then move to Bottom Right
        #
        # Check we aren't there:
        if pacman[0] == maxX - 1:
           if pacman[1] == minY + 1:
                print ("Got to bottomRight!")
                self.bottomRight = True
                return api.makeMove(Directions.STOP, legal)
           else:
               return api.makeMove(Directions.SOUTH, legal)

        return api.makeMove(Directions.STOP, legal)

# SurvivalAgent
#
# uses the location of Pacman and the ghosts to stay alive as long as possible
class SurvivalAgent(Agent):

    # Constructor
    #
    #
    def __init__(self):
        self.last = Directions.STOP

    def getAction(self, state):

        legal = api.legalActions(state)
        pacman = api.whereAmI(state)
        ghostLocations = api.distanceLimited(api.ghosts(state), state)
        ghostDistances =[]
        for i in ghostLocations:
            ghostDistances.append(util.manhattanDistance(i, pacman))

        self.sortGhostByDistance(ghostLocations, ghostDistances)
        #nearest = 
        #for i in ghostLocations:
            #if util.manhattanDistance(pacman, ghostLocations[i]) <= util.manhattanDistance(pacman, ghostDistances[0]):
        nearest = ghostLocations[0]
        for i in range(len(ghostLocations)):
            if util.manhattanDistance(pacman, ghostLocations[i]) <= util.manhattanDistance(pacman, nearest):
                nearest = ghostLocations[i]

        # Calculate coords of pacman and ghosts to determine Direction
        xDiff = pacman[0] - nearest[0]
        yDiff = pacman[1] - nearest[1]
        temp = (xDiff, yDiff)

        pick = random.choice(legal)
        
        if util.manhattanDistance(pacman, nearest) < 4:
            # Uses difference in coords to determine Direction to travel
            if abs(temp[0]) > abs(temp[1]):
                if temp[0] < 0 and Directions.WEST in legal:
                    return api.makeMove(Directions.WEST, legal)
                elif temp[0] >= 0 and Directions.EAST in legal:
                    return api.makeMove(Directions.EAST, legal)
                else:
                    return api.makeMove(pick, legal)
            else:
                if temp[1] < 0 and Directions.SOUTH in legal:
                    return api.makeMove(Directions.SOUTH, legal)
                elif temp[1] >= 0 and Directions.NORTH in legal:
                    return api.makeMove(Directions.NORTH, legal)
                else:
                    return api.makeMove(pick, legal)
        else:
            return api.makeMove(pick, legal)

    def sortGhostByDistance(self, ghostList, distGhostList):
        gap = len(distGhostList) / 2
        while gap > 0:
            for i in range(gap, len(distGhostList)):
                tempFood = ghostList[i]
                tempDist = distGhostList[i]
                j = i
                while j >= gap and distGhostList[j - gap] > tempDist:
                    ghostList[j] = ghostList[j - gap]
                    distGhostList[j] = distGhostList[j - gap]
                    j = j - gap
                    ghostList[j] = tempFood
                distGhostList[j] = tempDist
            gap = gap / 2  

# FoodGhostAgent
#
# Combines both HungryAgent and SurvivalAgent
class FoodGhostAgent(Agent):

    # Constructor
    #
    #
    def __init__(self):
        self.last = Directions.STOP

    def getAction(self, state):

        # Get the actions we can try
        legal = api.legalActions(state)
        pacman = api.whereAmI(state)
        theFood = api.food(state)
        theGhosts = api.ghosts(state)
        nearestFood = theFood[0]
        print (nearestFood)
        if len(theGhosts) == 0:
            nearestGhost = (0, 0)
        else:
            nearestGhost = theGhosts[0]
        # remove "STOP" action from legal actions
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # If we can repeat the last action, do it
        if self.last in legal:
            return api.makeMove(self.last, legal)
        for i in range(len(theFood)):
            if util.manhattanDistance(pacman, theFood[i]) <= util.manhattanDistance(pacman, nearestFood):
                nearestFood = theFood[i]
        for i in range(len(theGhosts)):
            if util.manhattanDistance(pacman, theGhosts[i]) <= util.manhattanDistance(pacman, nearestGhost):
                nearestGhost = theGhosts[i]

        # Calculate coords of pacman and food to determine Direction
        xFoodDiff = pacman[0] - nearestFood[0]
        yFoodDiff = pacman[1] - nearestFood[1]
        tempFood = (xFoodDiff, yFoodDiff)

        # Calculate coords of pacman and ghosts to determine Direction
        xGhostDiff = pacman[0] - nearestGhost[0]
        yGhostDiff = pacman[1] - nearestGhost[1]
        tempGhost = (xGhostDiff, yGhostDiff)

        pick = random.choice(legal)

        detectionDist = 5
        
        # DETECT CLOSE GHOSTS
        if util.manhattanDistance(pacman, nearestGhost) < detectionDist:
            # Uses difference in coords to determine Direction to travel
            if abs(tempGhost[0]) > abs(tempGhost[1]):
                if tempGhost[0] < 0 and Directions.WEST in legal:
                    return api.makeMove(Directions.WEST, legal)
                elif tempGhost[0] >= 0 and Directions.EAST in legal:
                    return api.makeMove(Directions.EAST, legal)
                else:
                    return api.makeMove(pick, legal)
            else:
                if tempGhost[1] < 0 and Directions.SOUTH in legal:
                    return api.makeMove(Directions.SOUTH, legal)
                elif tempGhost[1] >= 0 and Directions.NORTH in legal:
                    return api.makeMove(Directions.NORTH, legal)
                else:
                    return api.makeMove(pick, legal)
        else:
            # FIND FOOD: Uses difference in coords of food to determine Direction to travel
            if abs(tempFood[0]) > abs(tempFood[1]):
                if tempFood[0] < 0 and Directions.EAST in legal:
                    #print "EAST: ", legal, " ", pacman, " ", nearestFood, " ", util.manhattanDistance(pacman, nearestFood)
                    return api.makeMove(Directions.EAST, legal)
                elif tempFood[0] >= 0 and Directions.WEST in legal:
                    #print "WEST: ", legal, " ", pacman, " ", nearestFood, " ", util.manhattanDistance(pacman, nearestFood)
                    return api.makeMove(Directions.WEST, legal)
                else:
                    #print "### RAND: ", legal, " ", pacman, " ", nearestFood, " ", util.manhattanDistance(pacman, nearestFood)
                    return api.makeMove(pick, legal)

            else:
                if tempFood[1] < 0 and Directions.NORTH in legal:
                    #print "NORTH: ", legal, " ", pacman, " ", nearestFood, " ", util.manhattanDistance(pacman, nearestFood)
                    return api.makeMove(Directions.NORTH, legal)
                elif tempFood[1] >= 0 and Directions.SOUTH in legal:
                    #print "SOUTH: ", legal, " ", pacman, " ", nearestFood, " ", util.manhattanDistance(pacman, nearestFood)
                    return api.makeMove(Directions.SOUTH, legal)
                else:
                    #print "### RAND: ", legal, " ", pacman, " ", nearestFood, " ", util.manhattanDistance(pacman, nearestFood)
                    return api.makeMove(pick, legal)      