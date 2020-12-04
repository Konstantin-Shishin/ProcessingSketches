 # Системная переменная pmouseY всегда содержит
 # вертикальное положение мыши в кадре до текущего кадра.
 def draw():
    background(204)
    line(20, mouseY, 80, pmouseY)
    print("%d : %d" % (mouseY, pmouseY))
