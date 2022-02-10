#!/usr/bin/python3
from tkinter import filedialog as fd, PhotoImage, messagebox
from tkinter.constants import END
from gui import window, button_1 as gen, button_2 as ex
from gui import button_3 as select_save
from gui import entry_1 as frames_entry, entry_2 as size_entry, entry_3 as output_loc

from center import center
center(window, size='320x350')
icon = PhotoImage(file='./icon.png')
window.iconphoto(False, icon)
window.title('Generate JSON')

def save_json_file():
    s = fd.askdirectory(parent=window)
    output_loc.delete(0, END)
    output_loc.insert(0, s) # type: ignore

def generate():
    images = fd.askopenfilenames(parent=window, title='Select all the images')
    if not images:
        return
    frames = frames_entry.get()
    size = size_entry.get()
    output = output_loc.get()
    if (len(frames) == 0 or len(size) == 0 or len(output) == 0 or
    len(images) == 0):
        messagebox.showerror(title='Error', message='Check inputs')
        return
    from generate import Anim
    from lottie.utils import script
    try:
        anim = Anim(frames=frames, size=size,
                             images_location=images)
        anim = anim.get()
    except ValueError as err:
        messagebox.showerror(title='Error', message=f'Error\n\n{err}')
        return

    script.script_main(anim, path=output, basename="my_anim", formats=['json'])
    messagebox.showinfo(
                'Done!', f'JSON file successfully generated\n{output}.')
    

gen.bind('<Button-1>', lambda _: generate())
ex.bind('<Button-1>', lambda _: window.quit())
select_save.bind('<Button-1>', lambda _: save_json_file())

if __name__ == "__main__":
    window.mainloop()
