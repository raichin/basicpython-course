import turtle
tao = turtle.Pen()
def Pentagon():
    tao.left(180)
    for i in range(5):
        tao.left(144)
        tao.forward(100)

def Project():  
    for b in range(8):
        tao.left(45)
        tao.penup()
        tao.forward(200)
        tao.pendown()
        Pentagon()
        tao.penup()
        tao.back(-200)
        

Project()
    
