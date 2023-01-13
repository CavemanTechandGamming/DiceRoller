import tkinter as tk
import random

# The DiceRoller class is a tkinter GUI application for rolling virtual dice.


class DiceRoller:
    def __init__(self, master):
        # The master parameter is the root Tk() instance that the GUI is built on.
        self.master = master
        # Set the title of the window to "Dice Roller".
        self.master.title("Dice Roller")
        # Create the widgets (buttons and labels) for the application.
        self.create_widgets()

    def create_widgets(self):
        # A list of tuples representing the different types of dice that can be rolled
        dice_types = [("D2", 2), ("D4", 4), ("D6", 6), ("D8", 8), ("D10", 10), ("D12", 12), ("D20", 20), ("D100", 100)]
        # Sort the list of dice by the number of sides
        dice_types.sort(key=lambda x: x[1])

        # Create a label to display the results of the dice roll
        self.result_label = tk.Label(self.master)
        # wrap the result_label content so it not go out of the screen
        wraplength = self.master.winfo_width()+350
        self.result_label.config(font=("Arial", 16), wraplength=wraplength)
        self.result_label.grid(row=0, column=0, columnspan=2)

        # A dictionary to store the state of the spinboxes
        self.spinner_var = {}
        # A dictionary to store the state of the buttons
        self.button_var = {}
        for i, (dice_type, sides) in enumerate(dice_types):
            # Create a StringVar variable for the spinbox and set the default value to 1
            self.spinner_var[dice_type] = tk.StringVar(value="1")
            # Create the spinbox for the number of dice to roll
            spinner = tk.Spinbox(self.master, from_=1, to=1000, textvariable=self.spinner_var[dice_type], width=4)
            spinner.grid(row=i+1, column=1)
            # Create a button for the dice type and set its command to roll_dice
            self.button_var[dice_type] = tk.Button(self.master, text=dice_type, width=6, height=2, command=lambda dice_type=dice_type, sides=sides: self.roll_dice(dice_type, sides))
            self.button_var[dice_type].grid(row=i+1, column=0, sticky='w', padx=5)
        # configure column for resizing
        self.master.columnconfigure(0, weight=1)

    def roll_dice(self, dice_type, sides):
        # Get the number of dice to roll from the corresponding spinbox
        num_dice = int(self.spinner_var[dice_type].get())
        # Perform the roll using random.randint and store the results in a list
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        # Convert the list of rolls to a string
        roll_str = ", ".join(str(roll) for roll in rolls)
        # If more than one die was rolled, add the total to the string
        if num_dice > 1:
            roll_str += f"\nTotal: {sum(rolls)}"
        # Update the label with the roll result
        self.result_label.config(text=roll_str)


if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Set the size and disable resizing of the window
    root.geometry("400x500")
    root.resizable(False, False)
    # Create an instance of DiceRoller class and pass the main window as the master
    app = DiceRoller(root)
    # Run the main event loop to handle events
    root.mainloop()
