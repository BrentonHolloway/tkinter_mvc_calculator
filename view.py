'''
    Created Dec 9, 2019

    @author: Brenton Holloway
    @version: 1.0.0
'''
import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    PAD = 10
    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculator v1.0.0")

        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(self.main_frame, justify='right', textvariable=self.value_var, state='disabled')
        ent.pack(fill='x')

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frame)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack(fill='x', expand=True)

        buttons_in_row = 0

        for caption in self.button_captions:
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x', expand=True)
                buttons_in_row = 0

            btn = ttk.Button(frm, text=caption, command=(lambda button=caption: self.controller.on_button_click(button)))
            if caption == '=':
                btn.pack(side='left', fill='x', expand=True)
            else:
                btn.pack(side='left')
            buttons_in_row += 1