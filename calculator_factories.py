import tkinter as tk #importando toda a lib
from typing import List

def make_root():
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root


def make_label(root):
    label = tk.Label(
        root, text='Sem conta ainda',
        anchor='e', justify='right', background='#fff'
    )
    label.grid(column=0, row=0, columnspan=5, sticky="news")
    return label


def make_display(root):
    display = tk.Entry(root)
    display.grid(column=0, row=1, columnspan=5, sticky="news", pady=(0, 10))
    display.config(
        font=('Helvetica', 20, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'beak'


def make_buttons(root):
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=20, width=1, background='#f1f2f3', bd=0,
                cursor='hand2', highlightthickness=0,
                highlightcolor='#ccc', highlightbackground='#ccc',
                activebackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons