from tkinter import *


screen = Tk()
screen.geometry("500x500")
screen.title("Car info")

Vehichle = []
x_axis = 15
y_axis = 35  # 25 for space in related categories,
######################################################################## Make and model
make = ""
model = ""

Label(screen, text="Vehichle Make:").place(x=x_axis, y=y_axis)
y_axis += 35
make_entry = Entry(textvariable=make, width="30").place(x=x_axis, y=y_axis)
y_axis += 35
Label(screen, text="Vehichle Model:").place(x=x_axis, y=y_axis)
y_axis += 35
model_entry = Entry(textvariable=model, width="30").place(
    x=x_axis, y=y_axis)
y_axis += 50

Vehichle.append(make)
Vehichle.append(model)
# gfh##########ghx################dgfh############ Transmission
MT = IntVar()
AT = IntVar()
NA = IntVar()


def var_states():
    print("MT: %d,\nAT: %d" % (MT.get(), AT.get()))

Label(screen, text="Choose a transmission").place(x=x_axis, y=y_axis)
y_axis += 25
Checkbutton(screen, text="Manual", variable=MT).place(x=x_axis, y=y_axis)
y_axis += 25
Checkbutton(screen, text="Automatic",
            variable=AT).place(x=x_axis, y=y_axis)
y_axis += 25
Checkbutton(screen, text="Both", variable=NA).place(x=x_axis, y=y_axis)
y_axis += 50
Button(screen, text='Show', command=var_states).place(x=x_axis, y=y_axis)
y_axis += 50

# dgh######dgfh###########dgfh#########dgfh#############dgfh############ Colors


# todo clean up y axis, make colors int variables
# for color in colors if color == 1 use it

Black = IntVar()
White = IntVar()
Red = IntVar()
Green = IntVar()


Label(screen, text="Choose colors").place(x=x_axis, y=y_axis)
y_axis += 25
Checkbutton(screen, text="Black", variable=Colors[
            "Black"]).place(x=x_axis, y=y_axis)
y_axis += 25
Checkbutton(screen, text="Purple", variable=Colors[
    "Purple"]).place(x=x_axis, y=y_axis)
y_axis += 25
Checkbutton(screen, text="Orange", variable=Colors[
            "Orange"]).place(x=x_axis, y=y_axis)
x_axis += 50
Checkbutton(screen, text="White", variable=Colors[
            "White"]).place(x=x_axis, y=y_axis)
y_axis -= 25
Checkbutton(screen, text="Red", variable=Colors[
            "Red"]).place(x=x_axis, y=y_axis)
y_axis -= 25
Checkbutton(screen, text="Green", variable=Colors[
            "Green"]).place(x=x_axis, y=y_axis)
print(Colors["Black"])
print(MT.get)
print(AT)

mainloop()
