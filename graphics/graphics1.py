from graphics import *
from graphics.graphics import *

def main():
    win = GraphWin("window",300,300)
    
    
    win.getKey()
    win.close()
#main()
def point():
    win = GraphWin("point",500,500)
    p = Point(30,40) # try changing the value of the point

    print(p.getX())
    print(p.getY())

    
    p.draw(win)


    win.getKey()
    win.close()
#point()
def pointCol():
    # can set the color of a point using POINTNAME . setOutline("COLOR")

    # use the code above to draw a point in the top left thats blue

    # and a point in the bottom right thats red
    pass
#pointCol()

def circles():
    # to draw circles we need the centre of the circle (point) and a radius
    win  = GraphWin("circles",500,500)

    centre = Point(100,100)
    circle1 = Circle(centre,50)
    circle1.draw(win)
    win.update()
    

    circle2 = Circle(Point(300,300),80)
  
    circle2.draw(win)

    win.getMouse()
    win.close()


    # we can set the color using .setOutline() and the fill using .setFill()



    # we can also move the circles using .move() , try circle2.move(10,20)
#circles()

def lines():
    # we draw lines by providing the starting point and the ending point
    win = GraphWin("lines",500,500)

    line1 = Line(Point(20,25),Point(30,60))
    line1.draw(win)

    win.getMouse()

    line1.move(0,50)
    line1.setOutline("red")
    win.update()

    win.getMouse()
    win.close()



lines()

