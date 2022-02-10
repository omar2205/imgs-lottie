def center(window, size):
    w = int(size.split('x')[0])
    h = int(size.split('x')[1])

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))

    window.geometry(f'{w}x{h}+{x}+{y}')
