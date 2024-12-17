import tkinter as tk
from tkinter import ttk
import random

class DiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("Rzut kostką")
        self.root.geometry("200x150")
        
        self.result_label = ttk.Label(
            root, 
            text="?", 
            font=("Arial", 48, "bold")
        )
        self.result_label.pack(pady=20)
        
        roll_button = ttk.Button(
            root, 
            text="Rzuć kostką",
            command=self.roll_dice
        )
        roll_button.pack()
        
    def roll_dice(self):
        result = random.randint(1, 6)
        self.result_label.configure(text=str(result))

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRoller(root)
    root.mainloop()

