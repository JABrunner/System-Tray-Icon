import pystray
import PIL.Image

#load image
image = PIL.Image.open("circuit_96px.png")

#define events for items clicked
def on_clicked(icon, item):
    if str(item) == "Say Hello to My Little Friend":
        print("Hello World")
    elif str(item) == "Exit":
        #close app on this selection
            icon.stop()
    elif str(item) == "This doesn't actually do anything, Don't Click":
        print("THIS DOESN'T DO ANYTHING!!!!")
    else:
        print("Not Implemented yet")

#set menu list items
icon = pystray.Icon("System Tray Mockup", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello to My Little Friend", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    pystray.Menu("Theres More?!?!?", pystray.Menu(
        pystray.Menu("This doesn't actually do anything, Don't Click")
    ))
))


icon.run()