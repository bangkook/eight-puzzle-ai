import tkinter as tk
from tkinter import messagebox

class EightPuzzleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eight Puzzle Game")
        self.root.geometry("600x600")

        self.set_main_background()

        self.input_frame = tk.Frame(root)
        self.input_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.input_puzzle = [[tk.StringVar() for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.input_puzzle[i][j] = tk.StringVar()
                entry = tk.Entry(self.input_frame, textvariable=self.input_puzzle[i][j], width=5, font=("Arial", 24))
                entry.grid(row=i, column=j, padx=5, pady=5)

        submit_button = tk.Button(self.input_frame, text="Submit", command=self.display_puzzle, font=("Arial", 18), bg="#7FB3D5")
        submit_button.grid(row=3, column=1, pady=20)

    def set_main_background(self):
        self.root.configure(bg="#FFB6C1")

    def display_puzzle(self):
        puzzle_display = tk.Toplevel(self.root)
        puzzle_display.title("Puzzle Display")
        puzzle_display.geometry("500x500")
        puzzle_display.configure(bg="#FFC0CB")  

        canvas = tk.Canvas(puzzle_display, width=400, height=400)
        canvas.pack()

        for i in range(3):
            for j in range(3):
                num = int(self.input_puzzle[i][j].get())
                x1, y1 = j * 133, i * 133
                x2, y2 = (j + 1) * 133, (i + 1) * 133
                fill_color = "#7FB3D5" 
                canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
                if num != 0:
                    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(num), font=("Arial", 36), fill="white")

        back_button = tk.Button(puzzle_display, text="Back", command=puzzle_display.destroy, font=("Arial", 18), bg="#7FB3D5")
        back_button.pack(side=tk.LEFT, padx=20, pady=20)

        next_button = tk.Button(puzzle_display, text="Next", font=("Arial", 18), bg="#7FB3D5")
        next_button.pack(side=tk.RIGHT, padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = EightPuzzleApp(root)
    root.mainloop()
