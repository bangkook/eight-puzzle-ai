import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from eightpuzzle import EightPuzzleState, asciiBoard, breadthFirstSearch, EightPuzzleAgent

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

        submit_button = tk.Button(self.input_frame, text="Submit", command=self.solve_puzzle, font=("Arial", 18), bg="#7FB3D5")
        #submit_button = tk.Button(self.input_frame, text="Submit", command=self.display_puzzle, font=("Arial", 18), bg="#7FB3D5")
        submit_button.grid(row=7, column=1, pady=20)

        search_methods = ["DFS", "BFS", "A Star"]
        self.selected_method = tk.StringVar()
        self.selected_method.set(search_methods[0])  # Set the default method
        method_dropdown = ttk.Combobox(self.input_frame, textvariable=self.selected_method, values=search_methods)
        method_dropdown.grid(row=4, column=1, pady=20)


        #------------
        self.results_label = tk.Label(self.input_frame, text="", font=("Arial", 12))
        self.results_label.grid(row=8, column=1, pady=10)

        self.steps = []  # Store steps or moves here
        self.current_step = 0  # Track the current step

        next_button = tk.Button(self.input_frame, text="Next", command=self.show_next_step, font=("Arial", 18), bg="#7FB3D5")
        next_button.grid(row=9, column=0, pady=10)

        back_button = tk.Button(self.input_frame, text="Back", command=self.show_previous_step, font=("Arial", 18), bg="#7FB3D5")
        back_button.grid(row=9, column=2, pady=10)
        #------------

    def set_main_background(self):
        self.root.configure(bg="#FFB6C1")
 


    def solve_puzzle(self):
        selected_method = self.selected_method.get()  # Get the selected search method

        if selected_method == "BFS":
            function = breadthFirstSearch
            puzzle = [[int(self.input_puzzle[i][j].get()) for j in range(3)] for i in range(3)]
            initial_state = EightPuzzleState([puzzle[i][j] for i in range(3) for j in range(3)])
            agent = EightPuzzleAgent(initial_state, function)

            print(initial_state)
            parent, cost, expanded_nodes, depth = breadthFirstSearch(initial_state)

            # Now you have the BFS results; you can use this data to display it in the GUI
            print("BFS Results:")
            print("Cost =", cost)
            print("Expanded Nodes =", len(expanded_nodes))
            print("Search Depth =", depth)

            self.steps = agent.getPath()

            actions = agent.getPath()
            for action in actions:
                print(asciiBoard(action))

            self.show_current_step()

            self.results_label.config(text=f"Cost = {cost}, Expanded Nodes = {len(expanded_nodes)}, Search Depth = {depth}")

    def get_solution_path(self, parent, initial_state):
        path = []
        board = initial_state.board
        path.append(board)
        while board in parent.keys():
            board = parent[board]
            path.append(board)
        return path[::-1]  # Reverse the path

    def show_current_step(self):
        if self.steps:
            current_board = self.steps[self.current_step]
            self.display_board(current_board)

    def show_next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.show_current_step()

    def show_previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_current_step()

    def display_board(self, board):
        
        puzzle_display = tk.Toplevel(self.root)
        puzzle_display.title("Puzzle Display")
        puzzle_display.geometry("500x500")
        puzzle_display.configure(bg="#FFC0CB")

        canvas = tk.Canvas(puzzle_display, width=400, height=400)
        canvas.pack()

        for i in range(3):
            for j in range(3):
                num = int(board[i * 3 + j])
                x1, y1 = j * 133, i * 133
                x2, y2 = (j + 1) * 133, (i + 1) * 133
                fill_color = "#7FB3D5"
                canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
                if num != 0:
                    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(num), font=("Arial", 36), fill="white")


    # def display_puzzle(self):

    #     selected_method = self.selected_method.get()  # Get the selected search method
    #     print("Selected Method:", selected_method)

    #     puzzle_display = tk.Toplevel(self.root)
    #     puzzle_display.title("Puzzle Display")
    #     puzzle_display.geometry("500x500")
    #     puzzle_display.configure(bg="#FFC0CB")  

    #     canvas = tk.Canvas(puzzle_display, width=400, height=400)
    #     canvas.pack()

    #     for i in range(3):
    #         for j in range(3):
    #             num = int(self.input_puzzle[i][j].get())
    #             x1, y1 = j * 133, i * 133
    #             x2, y2 = (j + 1) * 133, (i + 1) * 133
    #             fill_color = "#7FB3D5" 
    #             canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
    #             if num != 0:
    #                 canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(num), font=("Arial", 36), fill="white")

    #     back_button = tk.Button(puzzle_display, text="Back", command=puzzle_display.destroy, font=("Arial", 18), bg="#7FB3D5")
    #     back_button.pack(side=tk.LEFT, padx=20, pady=20)

    #     next_button = tk.Button(puzzle_display, text="Next", font=("Arial", 18), bg="#7FB3D5")
    #     next_button.pack(side=tk.RIGHT, padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = EightPuzzleApp(root)
    root.mainloop()
