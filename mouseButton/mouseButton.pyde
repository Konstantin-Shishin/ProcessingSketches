# Щелкните внутри окна и нажмите кнопку
# левая и правая кнопки мыши
# измените заливку прямоугольника
def draw():
    if mousePressed and (mouseButton == LEFT):
        fill(0)
    elif mousePressed and (mouseButton == CENTER):
        fill(255)
    else:
        fill(126)
    rect(25, 25, 50, 50)
