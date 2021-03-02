import tkinter as tk
from typing import List

class Calculator:
    """Teste"""

    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
        ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    
    def start(self):
        self.root.mainloop()