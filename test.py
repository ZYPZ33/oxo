from guizero import App, Text, PushButton, Picture, TextBox

size = 200
titlename = "Hello Qt!"
app = App(title=titlename, width=size, height=size)
board = [["_" for row in range(3)] for column in range(3)]

message = Text(app, text="\nHello,\n Openbox!")

openBoximage = Picture(app)
openBoximage.image = "/home/user/image.jpg"

inputBox = TextBox(app)

buttonBox = PushButton(app, text="Hello!", command=exit)


app.display()
