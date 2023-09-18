from guizero import App, Picture, Text, PushButton, TextBox, ButtonGroup, Combo

windowName = "Python thingy"
app = App(title=windowName)
image = Picture(app, "/home/user/image.jpg")
text = Text(app, text="Hello")
push = PushButton(app, text="Self-destruct button!", command=exit)
inputBox = TextBox(app, text="type here")
choice = ButtonGroup(app, list(range(3)))
change = Combo(app, list(range(3)))

app.display()
