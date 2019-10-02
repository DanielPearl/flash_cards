import random
import json

# Read JSON File
with open('flash_cards.json', 'r') as myfile:
    data=myfile.read()
d = json.loads(data)

#Create Border
def border(val):
    line = ""
    for i in range(0, len(val)):
        line += "-"
    return line

#Print Border
def print_val(val):
    print("")
    print(border(val))
    print(val)
    print(border(val))
    print("")

# Run Program
while True:
    key = random.choice(list(d.keys()))
    value = d[key]

    print_val(key)
    input("Press Enter to show answer...")

    print_val(value)
    input("Press Enter for next flash card...")
