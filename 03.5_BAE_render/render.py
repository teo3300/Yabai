from tkinter import Tk, Canvas, PhotoImage, mainloop

mx = 240*160
white = "#fff"
black = "#000"

path = "../03.0_out_BAE/BAE_file/"

def decode(path,name,ext):
    data = []
    with open(path+name+"."+ext, "rb") as val:
        byte = val.read(1)
        while byte:
                data.append(int.from_bytes(byte, "big"))
                byte = val.read(1)
    return data

def render(img, data, prev=black):                          # better explained in the ROM program
    fill = prev
    pos = 0
    for i in data:
        prevPos = pos
        if i < 248:
            print
            nxt = i
            while pos < (prevPos + nxt):
                img.put(fill, (pos%240, int(pos/240)))
                pos += 1
            if fill == white:
                fill = black
            else:
                fill = white
        elif i < 254:
            nxt = 240<<(i-247)
            while pos < (prevPos + nxt):
                img.put(fill, (pos%240, int(pos/240)))
                pos += 1
            if fill == white:
                fill = black
            else:
                fill = white
        elif i != 255:
            while pos != mx:
                img.put(fill, (pos%240, int(pos/240)))
                pos += 1
    return img



width = 240
height = 160
window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")

name = input("Frame:")

pad = 0
data = decode(path, name, "BAE")
render(img, data)

mainloop()