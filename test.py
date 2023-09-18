from guizero import App, Text, PushButton, Picture, TextBox

titlename = "Hello Qt!"
app = App(title=titlename, width=200, height=200)
board = [["_" for row in range(3)] for column in range(3)]

o1 = Text(app, text="\nHello,\n Openbox!")

o2 = Picture(app)
o2.image = "/home/user/image.jpg"

i1 = TextBox(app)

i2 = PushButton(app, text="Hello!", command=exit)


app.display()
