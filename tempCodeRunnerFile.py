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
                    
        puzzle_display.mainloop()