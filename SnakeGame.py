'''SnakeGame.py
By Tenzin Dophen, Adapted from Jed Yang 2017-03-15
This class contains objects which draws a body like a snake with a tail, which
can be moved around by a user, using the arrows on the keyboards for direction. The snake
can eat any objects(circles, supposed to be apples)  also drawn in the class snake on the way which will increase 
the user's score but also grows the snake's tail by 1 each time it eats. The user loses(the game ends and the window closes) if 
the snake goes touches the boundaries of the window or the head of the snake touches any of its tails.
Happy Gaming'''



from graphics import *
import sys
from random import randint

class Snake(GraphWin):
    def __init__(self,color, bgcolor):
        """Assign these numbers to instance variables."""
        GraphWin.__init__(self, 'Snake Module snake', 1000, 900)
        self.setBackground(color_rgb(0,0,225))
        self.x = 10
        self.y = 10
        self.dx = 5   # the number by which the snake should move
        self.dy = 0
        self.a = 0  # position of the apple 
        self.b = 0  # position of the apple 
        self.score = 0
        self.color = color
        self.bgcolor = bgcolor


        self.total = 0    
        self.bodyParts = [] #list to store the body of the snake(i.e head and the tails)
        self.makeHead()# class the function to make the head of the snake
        self.make_Tail()# class the function to make the tail of the snake
        self.apple()# class the function to make the apple
        self.draw()
        
        
        
        # binds all the keys, i.e. arrow keys on the keyboard
        self.bind_all('<Up>',  self.upHandler)
        self.bind_all('<Down>', self.downHandler)
        self.bind_all('<Left>', self.leftHandler)
        self.bind_all('<Right>', self.rightHandler)
        
     
        
  
      
    def stepsnake(self):
      """Step one time unit.  Use move()  based on dx, dy"""
      

      self.move_snake(self.dx, self.dy)  # calls the move_snake fucntion to move the snake
      
      if self.x < 0 or self.x > self.width or self.y < 0 or self.y > self.height:
        #the game ends if the snake's head touches the boundaries of the window
        sys.exit()
      for i in range(1, len(self.bodyParts)-1):
        if self.bodyParts[0].getP1().getX() - self.bodyParts[i+1].getP1().getX() == 0 and self.bodyParts[0].getP1().getY() - self.bodyParts[i+1].getP1().getY() == 0:
            sys.exit()
      # the game ends and the window closes if the head of the tail touches any of its tails that is created after it eats the apple
    '''This fucntion is called everytime the snake takes a step ad is used eat the apples 
    on the way as well as call the relvant function to add the tail'''    
    def eat(self):
        d = abs(self.x - self.a)   # checks the distance between the apple and the snake's x coordinate of head
        e = abs(self.y - self.b)#checks the distance between the apple and the snake's head y coordinate of head
        if d < 20 and e < 20:  # checks if the distance between the snake and the head is within 20 
            self.apple.undraw()  # remove the apple 
            self.a = randint(0,self.width -100) # generates random number within the window, but not too close to the boundary
            self.b = randint(0,self.height-100)# generates random number within the window, but not too close to the boundary
            self.apple = Circle(Point (self.a , self.b ), 10) # set up an apple 
            self.apple.setFill("white")
            self.apple.draw(self) # draw a new apple in a random place 
            self.total = self.total + 1 # keeps track of the apples the snake eats
            self.make_Tail() # class the function to add a new tail 
            
    
            
    
    def move_snake(self, dx, dy):
      """Move the snake upwards/downwards by dy and right and left by dx."""
  
      self.eat() # calls the eat function to check if the snake eats any apple
     
    
      self.bodyParts[0].move(dx,dy) # move the head of the snake

      ''' The for loop runs through the list of the snake bodyparts, starting from the item on the end of the list 
      to the second item on the list, basically all the tails and just not the head.
      In the for loop, starting from the last tail in the list, it moves and switches its place to the one above it, 
      using the x and y coordinate to help cover the distance. The getP1() returns the points of the tail while the getX() and get Y returns the x and y corrdinates of the tail''' 
      for i in range(len(self.bodyParts)-1, 0, -1):
        self.bodyParts[i].move(self.bodyParts[i-1].getP1().getX() - self.bodyParts[i].getP1().getX(),self.bodyParts[i-1].getP1().getY() - self.bodyParts[i].getP1().getY() )
   
      self.x = self.x + dx # updates the location fo the snake
      self.y = self.y + dy # updates the location of the snake

      
    
    def upHandler(self, event):
        
        self.dy= -10 - self.total*2   #moves the snake upwards and increases the step it should take everytime it eats an apple, updated by the value of self.total 
        self.dx = 0
        
    def downHandler(self, event):
        
        self.dy = 10 + self.total*2 #moves the snake downwards and increases the step it should take everytime it eats an apple, updated by the value of self.total
        self.dx = 0
  
    def rightHandler(self, event):#moves the snake to the right  and increases the step it should take everytime it eats an apple, updated by the value of self.total
       
        self.dx = 10 + self.total*2
        self.dy = 0
        
    def leftHandler(self, event):
      
        self.dx = -10 - self.total*2 #moves the snake to the left  and increases the step it should take everytime it eats an apple, updated by the value of self.total
        self.dy = 0
        

    def draw(self):
        #Draw the head and the apple in the window.
        self.head.draw(self)
        self.apple.draw(self)
    
    def makeHead(self):
        #Set up head.
      
        self.head = Rectangle(Point(self.x, self.y ), Point(self.x -20, self.y + 20 ))
        self.headColor = color_rgb(200, 200, 20)
        self.head.setFill(self.headColor)
 
        self.bodyParts.append(self.head) # add the head to the list bodyParts
    
        
    def apple(self):
        a = randint(0,self.width - 100) # generate random number within the window
        b = randint(0,self.height - 100)# generate random number within the window
        self.a = a
        self.b = b
        self.apple = Circle(Point (self.a , self.b ), 10) # make the apple
        self.apple.setFill("white")
    
    def make_Tail(self):
        self.score = 5 * self.total  #updates the score the user earns 
        print("SCORE = ", self.score) #prints the score
        #draws the tail so that its right behind the head with different colour
        self.tail = Rectangle(Point(self.x + (self.total *(-20)), self.y ), Point(self.x +(self.total +1) *(-20), self.y + 20))
        self.tailColor = color_rgb(100, 200, 20)
        self.tail.setFill(self.tailColor)
        self.tail.draw(self)
        self.bodyParts.append(self.tail) # adds the tail to the list 

      

   
def snakeModule():
    
    
    snake = Snake(color_rgb(255,255,0), color_rgb(0,0,0)) # class the Snake Class
    while snake.winfo_exists():
        snake.stepsnake() # class the stepsnake function everytime
        update(24)
     

      # pause for roughly 1/24 of a second
   
if __name__ == '__main__':
    snakeModule()   #Only runs snakeModule() if the program is not being called by another
