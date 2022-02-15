from PIL import Image
import time,sys,mouse,keyboard
a = Image.open(sys.argv[1]).convert('L').resize((170,150))
time.sleep(1)
colors = [0,127,195,255]
xcol = [390,410,410,390]
ycol = [810,810,790,790]
xb = 400
yb = 300
#xcol = [760,780,780,760]
#ycol = [60,60,60,60]
#xb = 200
#yb = 200
p = 2.1
def drawcolor(num):
    mouse.move(x=xcol[num],y=ycol[num])
    mouse.click()
    for y in range(a.height):
        for x in range(a.width): 
            g = min(colors, key=lambda b:abs(b-a.getpixel((x,y))))
            if g == colors[num]:
                mouse.move(x=xb+x*p,y=yb+y*p)
                mouse.click()
                if keyboard.is_pressed("q"):
                   exit("q pressed")
drawcolor(2)
drawcolor(1)
drawcolor(0)
