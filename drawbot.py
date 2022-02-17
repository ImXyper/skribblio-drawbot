from PIL import Image
import time,sys,mouse,keyboard
a = Image.open(sys.argv[1])
a = a.convert('RGB').resize((200,140))
instx = []
insty = []
def distance(co1, co2):
    return pow(abs(co1[0] - co2[0]), 2) + pow(abs(co1[1] - co2[2]), 2)
def closest_col(list, col):
    closest = list[0]
    for c in list:
        if distance(c, col) < distance(closest, col):
            closest = c
    return closest
time.sleep(1)
colors = [(255,255,255),(193,193,193),(239,19,11),(255,113,0),(255,228,0),(0,204,0),(0,178,255),(35,31,211),(163,0,186),(211,124,170),(160,82,45),(0,0,0),(76,76,76),(116,11,7),(194,56,0),(232,162,0),(0,85,16),(0,85,158),(14,8,101),(85,0,105),(167,85,116),(99,48,13)]
xcol = [380,401,422,443,464,485,506,527,548,570,591,380,401,422,443,464,485,506,527,548,570,591]
ycol = [780,780,780,780,780,780,780,780,780,780,780,801,801,801,801,801,801,801,801,801,801,801]
xb = 400
yb = 300
#colors = [(0,0,0),(127,127,127),(136,0,21),(237,28,36),(255,127,39),(255,242,0),(34,177,76),(0,162,232),(63,72,204),(163,73,164),(255,255,255),(195,195,195),(185,122,87),(255,174,201),(255,201,14),(239,228,176),(187,230,29),(153,217,234),(112,146,190),(200,191,231)]
#xcol = [760,782,804,826,848,870,892,914,936,958,760,782,804,826,848,870,892,914,936,958,]
#ycol = [60,60,60,60,60,60,60,60,60,60,80,80,80,80,80,80,80,80,80,80]
#xb = 200
#yb = 200
p = 2.004
def drawcolor(num):
    instx.append(xcol[num])
    insty.append(ycol[num])
    for y in range(a.height):
        for x in range(a.width):
            if a.getpixel((x,y)) != (255,255,255):
                g = closest_col(colors,a.getpixel((x,y)))
                if g == colors[num]:
                    instx.append(xb+x*p)
                    insty.append(yb+y*p)
print("Rendering..")
drawcolor(1)
drawcolor(2)
drawcolor(3)
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
drawcolor(20)
drawcolor(21)
input("Image done rendering.\nPress enter when ready.\nPress q to stop drawing at anytime.")
for i in range(len(instx)):
    mouse.move(instx[i],insty[i])
    mouse.click()
    if keyboard.is_pressed("q"):
        exit("q pressed")
