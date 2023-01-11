import tkinter as tk
import random


class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller")
        self.create_widgets()

    def create_widgets(self):
        dice_types = [("D2", 2), ("D4", 4), ("D6", 6), ("D8", 8),
                      ("D10", 10), ("D12", 12), ("D20", 20), ("D100", 100)]
        dice_types.sort(key=lambda x: x[1])

        self.result_label = tk.Label(self.master)
        wraplength = self.master.winfo_width()+350
        self.result_label.config(font=("Arial", 16), wraplength=wraplength)
        self.result_label.grid(row=0, column=0, columnspan=2)

        self.spinner_var = {}
        self.button_var = {}
        for i, (dice_type, sides) in enumerate(dice_types):
            self.spinner_var[dice_type] = tk.StringVar(value="1")
            spinner = tk.Spinbox(self.master, from_=1, to=9999999999,
                                 textvariable=self.spinner_var[dice_type], width=4)
            spinner.grid(row=i+1, column=1)

            self.button_var[dice_type] = tk.Button(self.master, text=dice_type, width=6, height=2,
                                                   command=lambda dice_type=dice_type, sides=sides: self.roll_dice(dice_type, sides))
            self.button_var[dice_type].grid(
                row=i+1, column=0, sticky='w', padx=5)
        self.master.columnconfigure(0, weight=1)

    def roll_dice(self, dice_type, sides):
        num_dice = int(self.spinner_var[dice_type].get())
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        roll_str = ", ".join(str(roll) for roll in rolls)
        if num_dice > 1:
            roll_str += f"\nTotal: {sum(rolls)}"
        self.result_label.config(text=roll_str)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    root.resizable(False, False)
    app = DiceRoller(root)
    root.mainloop()