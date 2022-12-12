# Team Hematite
# 12-5-22
# flashcard listbag program

from FlashCards import FlashCards
from Card import Card
import tkinter as tk
import tkinter.font as tf

# constant height of input text box to offset the canvas
INPUT_HEIGHT = 60
CANVAS_WIDTH = 800
CORNER_RADIUS = 20
TEXT_SIZE = 34
TEXT_SPACING = 24
CARD_WIDTH = CANVAS_WIDTH-CORNER_RADIUS
CARD_HEIGHT = (CANVAS_WIDTH / 16 * 9)-CORNER_RADIUS-INPUT_HEIGHT
# background
COLOR1 = '#588c7e'
# button bg
COLOR2 = '#f2ae72'
# text
COLOR3 = '#d96459'
# card bg, button highlight, and button text
COLOR4 = '#f2e394'


# user interface
class FlashCardUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Flash Cards')
        self.main_window.geometry(f'{CANVAS_WIDTH}x{int(CANVAS_WIDTH / 16 * 9)}')
        self.main_window.resizable(False, False)
        self.main_window.configure(bg=COLOR1)
        self.f = FlashCards()
        self.f.read_file()
        self.canvas = tk.Canvas(self.main_window, width=CANVAS_WIDTH, height=int(CANVAS_WIDTH / 16 * 9)-INPUT_HEIGHT, bg=COLOR1, highlightthickness=0)
        self.canvas.grid(row=1, column=1, columnspan=8)
        self.side = 1
        self.card = Card("", "")
        self.text = tk.StringVar()
        self.text.set("Shuffle")
        button_font = tf.Font(family='Helvetica', size=16, weight='bold')
        self.flip_button = tk.Button(self.main_window, text="Flip", command=self.flip, width=20, height=1, bg=COLOR2, font=button_font, fg=COLOR3, activeforeground=COLOR2, activebackground=COLOR4, highlightbackground=COLOR4)
        self.flip_button.grid(row=2, column=4, pady=2)
        self.next_button = tk.Button(self.main_window, textvariable=self.text, command=self.next_card, width=20, height=1, bg=COLOR2, font=button_font, fg=COLOR3, activeforeground=COLOR2, activebackground=COLOR4, highlightbackground=COLOR4)
        self.next_button.grid(row=2, column=5, pady=2)
        self.draw_card(0, 0, CORNER_RADIUS, "")
        tk.mainloop()

    # checks if there are available cards in the bag and if so chooses one
    def next_card(self):
        self.text.set("Next")
        if self.f.get_cards().is_empty():
            self.f.read_file()
        elif len(self.f.get_cards()) == 1:
            self.text.set("Shuffle")
        self.card = self.f.choose_random()
        self.draw_card(0, 0, CORNER_RADIUS, self.card.get_side1())
        self.side = 1

    # shows the other side of a card
    def flip(self):
        if self.side == 1:
            self.draw_card(0, 0, CORNER_RADIUS, self.card.get_side2())
            self.side = 2
        else:
            self.draw_card(0, 0, CORNER_RADIUS, self.card.get_side1())
            self.side = 1

    # draws the card and determines the best text size and spacing to fit the text on the card
    def draw_card(self, x, y, r, t):
        self.canvas.delete("all")
        size_inc_amt = (len(t)-2)//2*4
        text_size = TEXT_SIZE - size_inc_amt
        spacing = TEXT_SPACING - size_inc_amt
        text_font = tf.Font(family='Georgia', size=text_size, weight='bold')
        self.canvas.create_rectangle(x + r, y + r, x+CARD_WIDTH, y+CARD_HEIGHT, fill=COLOR4)
        count = 0
        for text in t:
            self.canvas.create_text(CANVAS_WIDTH/2, CARD_HEIGHT/2 - (len(t)*spacing+size_inc_amt) + count * (spacing*2+len(t)), text=text, font=text_font, fill=COLOR3)
            count += 1


flash_cards = FlashCardUI()
