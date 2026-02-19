import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
current_player = "X"
board = [" " for _ in range(9)]

# Function to check winner
def check_winner():
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

# Button click function
def button_click(index):
    global current_player
    
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            root.quit()

        elif " " not in board:
            messagebox.showinfo("Draw", "It's a Draw!")
            root.quit()

        current_player = "O" if current_player == "X" else "X"

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 30), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
