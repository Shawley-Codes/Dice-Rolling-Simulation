#ai for the game
#Scott Hawley 7/31
#This code runs the rules for the game and starts the game
#it imports the method to roll dice

import dice
import turtle
import random
import time

class ai():
    #instantiate a calss of dice to be used by the rest of the class
    def __init__(self):
        print("Ai created")
        self.game = dice.dice(turtleOBJ = None, sort=0)
        self.game.initialize()
        self.text = turtle.Turtle()
        self.text.penup()
        self.text.hideturtle()
        self.text.color("Blue")
        self.text.right(90)
        self.text.forward(150)
        self.text.right(90)
        self.text.forward(175)
        self.text.left(180)
        self.text.pendown()
        self.text.write("Game Start", font=("Arial",14,"normal"))
        
#conditions NameError: name 'conditionals' is not defined means that
#it is not being recognized as part of the class

    #is called after every roll to check if any rules have been met
    #returns a true or false statement
    def conditionals(self, d1, d2, x, d3):
        print("checking conditions\n")
        #check condition one, if sum of items is 2
        if d1 + d2 == 2:
            print("Lose\n")
            self.text.clear()
            self.text.write("You Lose, Rolled 1 & 1!", font=("Arial",14,"normal"))
            return True
        #check condition two, if first roll adds to 7
        elif x == 0 and d1 + d2 == 7:
            print("Win\n")
            self.text.clear()
            self.text.write("You Win, Rolled sum of 7 on First Roll!", font=("Arial",14,"normal"))
            return True
        #check condition three, if first roll is a 5 and 6
        elif x == 0 and d1 == 5:
            if d2 == 6:
                print("Win\n")
                self.text.clear()
                self.text.write("You Win, Rolled 6 & 5 on First Roll!", font=("Arial",14,"normal"))
                return True
        elif x == 0 and d1 == 6:
            if d2 == 5:
                print("Win\n")
                self.text.clear()
                self.text.write("You Win, Rolled 5 & 6 on First Roll!", font=("Arial",14,"normal"))
                return True
        #check condition four, if the roll after the first is 7
        elif x != 0 and d1 + d2 == 7:
            print("Lose\n")
            self.text.clear()
            self.text.write("You Lose, Rolled sum of 7 after First Roll!", font=("Arial",14,"normal"))
            return True
        #check condition five, if the sum of the first roll is repeated
        elif x != 0 and d1 + d2 == d3:
            print("Win\n")
            self.text.clear()
            self.text.write(("You Win, Rolled same sum as First Roll: ", d3), font=("Arial",12,"normal"))
            return True
        #no condiditions met, keep rolling
        else:
            print("No W/L\n")
            self.text.clear()
            self.text.write(('Roll number: ', x+1) ,font=("Arial",14,"normal"))
            return False
        return False

    #is called to start the game
    #takes in constant delay
    def play(self, DELAY):
        print("Enter AI\n")
        x = 0
        #runs until a conditional returns true
        while True:
            print("Roll number ", x+1)
            #calls rolle twice, the checks the roll for attribute key, assigns it
            self.game.roll()
            #pull key attribute (number) and assign it to a variable
            d1 = self.game.key
            print("d1 = ", d1)
            self.game.roll()
            d2 = self.game.key
            print("d2 = ", d2)
            #checks if this is the first roll and the 
            if x == 0:
                d3 = d1 + d2
                print("d3 = ", d3)
            #calls conditions and leaves loop if returns true
            rule = self.conditionals(d1, d2, x, d3)
            if(rule == True):
                break
            x += 1
            time.sleep(DELAY)
        return

#main is used to call function and extranious tasks
def main():
    print("Enter Main")
    random.seed(time.time())
    DELAY = 1.25
    rules = ai()
    rules.play(DELAY)
    print("Game is finished")
    
    return

#call main
main()
