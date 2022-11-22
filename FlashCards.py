from Card import Card
from listbag import ListBag
import random


class FlashCards:
    def __init__(self):
        self.card_list = ListBag()

    def read_file(self):
        try:
            file_data = open('information.txt', 'rb')
            lines = file_data.readlines()
            file_data.close()
            count = 0
            side1_value = ""
            side2_value = ""
            s1 = False
            s2 = False
            for line in lines:
                line = line.rstrip()
                if count % 2 == 0:
                    side1_value = line
                    s1 = True
                else:
                    side2_value = line
                    s2 = True
                if s1 and s2:
                    s1 = False
                    s2 = False
                    self.card_list.add(Card(side1_value.decode('utf-8'), side2_value.decode('utf-8')))
                count += 1
        except FileNotFoundError:
            self.card_list = []

    def choose_random(self):
        num = random.randrange(0, len(self.card_list))
        count = 0
        card = Card("", "")
        for i in self.card_list:
            if count == num:
                card = i
                self.card_list.remove(i)
                break
            count += 1
        return card

    def get_cards(self):
        return self.card_list



