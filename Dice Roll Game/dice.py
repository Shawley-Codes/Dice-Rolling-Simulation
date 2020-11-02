#Scott Hawley
#7/17
#Hw9

#libraries
import turtle
import random

class dice(object):
    def __init__(self, turtleOBJ=None, sort = 0):
        print("defining dice")
        #define each item to self
        self.__turtleOBJ = turtle.Turtle()
        self.__turtleOBJ2 = turtle.Turtle()
        self.__sort = sort
        self.key = 0

    def __getitem__(self, key):
        print("getting the faces")
        #append .gif to a number then return the values
        keySHAPE = str(key)+".gif"
        if(self.__sort == 0):
            self.__sort = 1
            return self.__turtleOBJ.shape(keySHAPE)
        elif(self.__sort == 1):
            self.__sort = 0
            return self.__turtleOBJ2.shape(keySHAPE)
            
    def roll(self):
        print("rolling")
        #adds 1 values to key then overloads to call getitem
        self.key = random.randint(1,6) 
        return self[self.key]

    def initialize(self):
        print("initialize")
        #upload all used images
        turtle.setup(400,400)
        self.__turtleOBJ.penup()
        self.__turtleOBJ2.penup()
        #initialize spacing for each dice
        self.__turtleOBJ.forward(100)
        self.__turtleOBJ2.backward(100)
        turtle.addshape("0.gif")
        turtle.addshape("1.gif")
        turtle.addshape("2.gif")
        turtle.addshape("3.gif")
        turtle.addshape("4.gif")
        turtle.addshape("5.gif")
        turtle.addshape("6.gif")
        #initialize shape for each dice
        self.__turtleOBJ.shape("0.gif")
        self.__turtleOBJ2.shape("0.gif")
    
    #this call runs the game as a static method
    #def game():
    #    print("The game has started")
        #instanciate dice then call the functions
    #    play = dice(turtleOBJ = None, sort=0)
    #    play.initialize()
        #seed the random number generator
    #    import time
    #    random.seed(time.time())
    #    DELAY = .75
    #    #roll the dices 10 times
    #    for x in range(10):
    #        print("this is roll number ", x+1)
            #call the roll function and pass the return into key
       #     play.roll()
      #      play.roll()
            #delay the program before it loops
     #       time.sleep(DELAY)
    #    return

    #turn game static
    #game = staticmethod(game)

#run this porgram if no main is detected
#if __name__ == '__main__':
    #play = dice(turtleOBJ = None, sort=0)
    #dice.game()





