from tkinter import *


def single_button_click(event):
    '''
    Prints Single CLick
    '''
    print("Single Click")


def double_button_click(event):
    '''
    Prints Double Click then exits
    '''
    print("Double Click")
    import sys
    sys.exit()


widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('< Button - 1 >', single_button_click)
widget.bind('< Double - 1 >', double_button_click)
widget.mainloop()
