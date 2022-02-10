
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# x = int((screen_width / 2) - (window.width / 2))
# y = int((screen_height / 2) - (window.height / 2))

# window.geometry(f"320x350+{x}+{y}")
window.configure(bg = "#0F0F0F")


canvas = Canvas(
    window,
    bg = "#0F0F0F",
    height = 350,
    width = 320,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    320.0,
    64.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    64.0,
    320.0,
    350.0,
    fill="#E4E4E4",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    160.0,
    28.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    49.0,
    87.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    199.0,
    87.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    73.0,
    158.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Label(
    image=button_image_1,
    # borderwidth=0,
    # highlightthickness=0,
    # command=lambda: print("button_1 clicked"),
    # relief="flat"
)
button_1.place(
    x=24.000000000000004,
    y=240.0,
    width=273.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Label(
    image=button_image_2,
    # borderwidth=0,
    # highlightthickness=0,
    # command=lambda: print("button_2 clicked"),
    # relief="flat"
)
button_2.place(
    x=24.000000000000004,
    y=293.0,
    width=273.0,
    height=35.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    80.0,
    118.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=28.000000000000004,
    y=103.0,
    width=104.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    240.0,
    118.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=188.0,
    y=103.0,
    width=104.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    161.0,
    189.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=29.000000000000004,
    y=174.0,
    width=264.0,
    height=28.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Label(
    image=button_image_3,
    # borderwidth=0,
    # highlightthickness=0,
    # command=lambda: print("button_3 clicked"),
    # relief="flat"
)
button_3.place(
    x=268.0,
    y=177.0,
    width=24.0,
    height=24.0
)
window.resizable(False, False)
# window.mainloop()

