import random
import tkinter as tk
choices = {"r": "Rock", "p": "Paper", "s": "Scissor"}
def check_winner(user_input_choice):
    system_input_choice = random.choice(list(choices.keys()))
    result = f"You chose {choices[user_input_choice]}.\nSystem chose {choices[system_input_choice]}.\n"
    if(system_input_choice == user_input_choice):
        result += "Match is Draw 😒"
    elif(user_input_choice == "r" and system_input_choice == "p" or
         user_input_choice == "p" and system_input_choice == "s" or
         user_input_choice == "s" and system_input_choice == "r"
        ):
        result += "You Win 🎉"
    else:
        result += "You Lost the match 👎"

    result_label.config(text=result)   

window = tk.Tk() #window app setup
window.title("Rock Paper Scissors Game") # Window ka title

# Window size
window_width = 400
window_height = 400

# Get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the center position
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}") # window ka size
title = tk.Label(window, text="Rock Paper Scissors", font=("Karla", 20, "italic")) # window ke andar ka label
title.pack(pady=10) #alignments

# button frame and alignments
button_frame = tk.Frame(window)
button_frame.pack(pady=10) 
# buttons
rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    width=10,
    activebackground="black", # background color when button is clicked
    activeforeground="white", # text color when button is clicked
    command=lambda: check_winner("r"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame, 
    text="📄 Paper", 
    width=10, 
    activebackground="black", # background color when button is clicked
    activeforeground="white", # text color when button is clicked
    command=lambda: check_winner("p")
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    button_frame, 
    text="✂️ Scissors", 
    width=10, 
    activebackground="black", # background color when button is clicked
    activeforeground="white", # text color when button is clicked
    command=lambda: check_winner("s"))
scissors_btn.grid(row=0, column=2, padx=10)

# This is the result place
result_label = tk.Label(window, text="", font=("Arial", 14), wraplength=350, justify="center")
result_label.pack(pady=20)

window.mainloop() #window ko open krega and rakhega and ye last me hi rahega

    












