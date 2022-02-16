from PIL import Image
import time,sys,mouse,keyboard,math
a = Image.open(sys.argv[1]).convert('RGB').resize((170,150))
print("press q to stop")
def distance(co1, co2):
    return math.sqrt(pow(abs(co1[0] - co2[0]), 2) + pow(abs(co1[1] - co2[2]), 2))

def closest_col(list, col):
    closest = list[0]
    for c in list:
        if distance(c, col) < distance(closest, col):
            closest = c
    return closest

time.sleep(1)
#colors = [(0,0,0),(127,127,127),(195,195,195),(255,255,255),(136,0,21),(237,28,36),(255,174,201),(185,122,87),(255,137,39),(255,242,0),(239,228,176),(255,201,14),(34,177,76),(0,162,232),(153,217,234),(181,230,29),(63,72,204),(163,73,164),(200,191,231),(112,146,190)]
#xcol = [380,410,410,390]
#ycol = [780,810,790,790]
#xb = 400
#yb = 300
colors = [(0,0,0),(127,127,127),(195,195,195),(255,255,255),(136,0,21),(237,28,36),(255,174,201),(185,122,87),(255,137,39),(255,242,0),(239,228,176),(255,201,14),(34,177,76),(0,162,232),(153,217,234),(181,230,29),(63,72,204),(163,73,164),(200,191,231),(112,146,190)]
xcol = [760,782,782,760,804,826,826,804,848,870,870,848,892,914,914,892,936,958,958,936]
ycol = [60,60,80,80,60,60,80,80,60,60,80,80,60,60,80,80,60,60,80,80]
xb = 200
yb = 200
p = 2.005

def drawcolor(num):
    mouse.move(x=xcol[num],y=ycol[num])
    mouse.click()
    for y in range(a.height):
        for x in range(a.width):
            g = closest_col(colors,a.getpixel((x,y)))
            if g == colors[num]:
                mouse.move(x=xb+x*p,y=yb+y*p)
                mouse.click()
                if keyboard.is_pressed("q"):
                   exit("q pressed")

drawcolor(2)
drawcolor(1)
drawcolor(0)
drawcolor(4)
drawcolor(5)
drawcolor(6)
drawcolor(7)
drawcolor(8)
drawcolor(9)
drawcolor(10)
drawcolor(11)
drawcolor(12)
drawcolor(13)
drawcolor(14)
drawcolor(15)
drawcolor(16)
drawcolor(17)
drawcolor(18)
drawcolor(19)
