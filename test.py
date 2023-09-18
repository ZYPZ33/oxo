from guizero import App, Text, PushButton

titlename = "Hello Qt!"
app = App(title=titlename, width=200, height=200)
board = [["_" for row in range(3)] for column in range(3)]

o1 = Text(app, text="\nHello,\n Openbox!")
i1 = PushButton(app, text="Hello!", command=exit)
app.display()
