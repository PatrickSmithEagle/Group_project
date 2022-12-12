# Team Hematite
# 12-5-22
# Card class

# Card class
class Card:
    def __init__(self, s1, s2):
        self.side1 = process_text(s1)
        self.side2 = process_text(s2)

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2


# processes the text so that it is formatted to fit in the space provided
def process_text(t):
    parts = t.split()
    letters = 0
    for p in parts:
        letters += len(p)+1
    count = 0
    while True:
        count += 1
        if (8*count)*(3*count) > letters:
            num_lines = count
            break

    lines = []
    line = ""
    line_length = 0
    added = False
    for p in parts:
        line_length += len(p)+1
        line += p
        line += " "
        added = True
        # todo change line length check to before word is added to the line
        if line_length >= 11+num_lines*num_lines:
            lines.append(line)
            line_length = 0
            line = ""
            added = False
    if added:
        lines.append(line)
    return lines
