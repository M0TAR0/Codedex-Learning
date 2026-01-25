import tkinter as tk
from tkinter import font
from tkinter import ttk
import random
from rock_paper_scissors import get_computer_choice, determine_winner


class RPSApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock • Paper • Scissors")
        master.configure(bg='#f7f7fb')

        self.user_score = 0
        self.computer_score = 0

        self.header_font = font.Font(family='Segoe UI', size=14, weight='bold')
        self.big_font = font.Font(family='Segoe UI', size=12)

        header = tk.Label(master, text="Rock Paper Scissors", font=self.header_font, bg='#f7f7fb')
        header.pack(pady=(10, 4))

        self.score_label = tk.Label(master, text=self._score_text(), font=self.big_font, bg='#f7f7fb')
        self.score_label.pack()

        controls = tk.Frame(master, bg='#f7f7fb')
        controls.pack(pady=8)

        # Use PNG images on ttk buttons for smoother look
        self.rock_img = tk.PhotoImage(file='rock.png')
        self.paper_img = tk.PhotoImage(file='paper.png')
        self.scissors_img = tk.PhotoImage(file='scissors.png')

        rock_btn = ttk.Button(controls, image=self.rock_img, text='Rock (R)', compound='top', command=lambda: self.play('rock'))
        rock_btn.grid(row=0, column=0, padx=6)
        paper_btn = ttk.Button(controls, image=self.paper_img, text='Paper (P)', compound='top', command=lambda: self.play('paper'))
        paper_btn.grid(row=0, column=1, padx=6)
        scissors_btn = ttk.Button(controls, image=self.scissors_img, text='Scissors (S)', compound='top', command=lambda: self.play('scissors'))
        scissors_btn.grid(row=0, column=2, padx=6)

        actions = tk.Frame(master, bg='#f7f7fb')
        actions.pack(pady=(6, 2))

        self.result_label = tk.Label(actions, text='', font=self.big_font, bg='#f7f7fb', fg='#2b2b2b')
        self.result_label.pack()

        self.computer_label = tk.Label(actions, text='', bg='#f7f7fb', fg='#5a5a5a')
        self.computer_label.pack()

        bottom = tk.Frame(master, bg='#f7f7fb')
        bottom.pack(pady=8)

        reset_btn = ttk.Button(bottom, text='Reset Score', command=self.reset_score)
        reset_btn.pack(side=tk.LEFT, padx=6)
        quit_btn = ttk.Button(bottom, text='Quit', command=master.quit)
        quit_btn.pack(side=tk.LEFT, padx=6)

        # Menu with Reset and Quit
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Reset Score', command=self.reset_score)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=master.quit)
        menubar.add_cascade(label='File', menu=filemenu)
        master.config(menu=menubar)

        # Playful computer messages
        self.win_messages = [
            "NOOO I LOST 😱",
            "Argh! You got me...",
            "How did you do that?!",
            "Not again!"
        ]
        self.lose_messages = [
            "Yes! I win 😈",
            "Hah, easy!",
            "Computer triumphs!",
            "Try again human."
        ]
        self.tie_messages = [
            "A tie — so tense!",
            "We think alike.",
            "Stalemate."
        ]

        # Keyboard shortcuts
        master.bind('<r>', lambda _: self.play('rock'))
        master.bind('<R>', lambda _: self.play('rock'))
        master.bind('<p>', lambda _: self.play('paper'))
        master.bind('<P>', lambda _: self.play('paper'))
        master.bind('<s>', lambda _: self.play('scissors'))
        master.bind('<S>', lambda _: self.play('scissors'))
        master.bind('<q>', lambda _: master.quit())
        master.bind('<Control-r>', lambda _: self.reset_score())

    def _score_text(self):
        return f"You: {self.user_score}   Computer: {self.computer_score}"

    def play(self, user_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            self.user_score += 1
            result = random.choice(self.win_messages)
            fg = '#0a7d0a'
        elif winner == 'computer':
            self.computer_score += 1
            result = random.choice(self.lose_messages)
            fg = '#b30000'
        else:
            result = random.choice(self.tie_messages)
            fg = '#444444'

        self.score_label.config(text=self._score_text())
        self.result_label.config(text=result, fg=fg)
        self.computer_label.config(text=f"Computer chose: {computer_choice}")

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=self._score_text())
        self.result_label.config(text='Score reset — ready!')
        self.computer_label.config(text='')


if __name__ == '__main__':
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
