from colorama import Fore, Back
import numpy


colors = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.MAGENTA,
    Fore.RED,
    Fore.YELLOW,
    Fore.WHITE,
    Fore.BLACK
]
bg = [
    Back.BLUE,
    Back.CYAN,
    Back.GREEN,
    Back.MAGENTA,
    Back.RED,
    Back.YELLOW,
    Back.WHITE,
    Back.BLACK
]

rows = int(input("Rows: "))
setback = int(input("Setback: "))
interval = input("Interval: ")
body_char = "  "
frequency = float(input("Frequency: "))
trunk_h = int(input("Trunk height: "))
trunk_w = int(input("Trunk width: "))
trunk_char = "  "
empty = "  "

colorchars = list("bcgmrywk")

x = colorchars.index(input(f"Body color ({' '.join(colorchars)}): "))
body_color = colors.pop(x) + bg.pop(x)
colorchars.pop(x)

x = colorchars.index(input(f"Background color ({' '.join(colorchars)}): "))
default_color = colors.pop(x) + bg.pop(x)
colorchars.pop(x)

x = colorchars.index(input(f"Trunk color ({' '.join(colorchars)}): "))
trunk_color = colors.pop(x) + bg.pop(x)
colorchars.pop(x)

if not interval:
    interval = float("inf")
else:
    interval = int(interval)

width = lambda x: 2*(x - setback*int(x/interval)) + 1

max_width = width(rows-1)

tree = []

for i in range(rows):
    tree.append([0.]*((max_width-width(i))//2) + [1.]*width(i) + [0.]*((max_width-width(i))//2))

tree += [[0.]*((max_width-2*trunk_w-1)//2) + [-1.]*(2*trunk_w+1) + [0.]*((max_width-2*trunk_w-1)//2)]*trunk_h

tree = numpy.array(tree)
out = ""

mask = numpy.random.rand(*tree.shape)
tree *= mask

for row in tree:
    for n in row:
        if n == 0:
            out += default_color+empty
            continue
        if n < 0:
            out += trunk_color+trunk_char
            continue
        n = (n-1+frequency)/frequency
        if n < 0:
            out += body_color
        else:
            out += colors[int(n*len(colors))]+bg[int(n*len(bg))]
        out += body_char
    out += Back.RESET+Fore.RESET+"\n"

print(out)
