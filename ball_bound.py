from tkinter import *
#物体設定
ball={
      "x":350,
      "y":300,
      "w":30,
      "vx":15,
      "vy":-15,
      }
#GUI
root=Tk()
root.title(u"like Windows")
cv = Canvas(root, width = 1200,height =900)
cv.pack()

def d_o():
    cv.delete('all')
    cv.create_oval(
        ball["x"]-ball["w"],ball["y"]-ball["w"],
        ball["x"]+ball["w"],ball["y"]+ball["w"],
        fill="red"
        )
#運動設定    
def move_ball():
    bx=ball["x"]+ball["vx"]
    by=ball["y"]+ball["vy"]
    if bx<0 or bx>1200: ball["vx"]*=-1
    if by<0 or by>900: ball["vy"]*=-1
    if 0<=bx<=1200: ball["x"]=bx
    if 0<=by<=900: ball["y"]=by
    
def game_loop():
    d_o()
    move_ball()
    root.after(50, game_loop)

game_loop()
root.mainloop()