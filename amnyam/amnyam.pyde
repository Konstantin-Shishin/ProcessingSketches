x1=500
y1=200
x2=700
y2=100 # координаты квадратов
f2=255 # заливка статического квадрата по умолчанию
def setup():
    background(0)
    size(1000,400)
def draw():
    global x1,y1, x2, y2, f2    
    fill(f2)
    rect(x2,y2,10,10) # статический квадрат
    fill(255)
    rect(x1,y1,10,10) # движущийся квадрат
    if keyPressed and key == "w" :
        y1-=1
    if keyPressed and key == "s" :
        y1+=1
    if keyPressed and key == "a" :
        x1-=1
    if keyPressed and key == "d" :
        x1+=1
    if keyPressed and key == "e" :
        x1+=1
        y1-=1
    if keyPressed and key == "q" :
        x1-=1
        y1-=1
    if keyPressed and key == "z" :
        x1-=1
        y1+=1
    if keyPressed and key == "c" :
        x1+=1
        y1+=1
    if x1+10 > x2 and x2+10 > x1 and y1+10 > y2 and y2+10 > y1 : # условие столкновения
        f2=0 # квадрат зальется черным
        
#Встроенная переменная key содержит значение последней нажатой клавиши.          
#Поэтому не может быть условия типа key == "a" and key == "d" 
#Так как, так или иначе, какая-то из клавиш нажимается в первую очередь      
