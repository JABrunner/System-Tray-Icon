import pystray
import PIL.Image

image = PIL.Image.open("System-Tray-Icon-main/System Tray Icon/circuit_96px.png")

def on_clicked(icon, item):
    if str(item) == "Say Hello":
        print("Greetings")
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == "Hey Look a Submenu":
        print("Nothing implemented yet")

icon = pystray.Icon("Test", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Hey Look a Submenu", on_clicked),
    pystray.MenuItem("Exit", on_clicked)

    
))

icon.run()
