from pyfiglet import Figlet
import sys
import random

# def main():
#     printFiglet(input("Input: "))

# def printFiglet(prompt):
#     if len(sys.argv) != 1 and len(sys.argv) != 3:
#         sys.exit("Invalid usage")
#     figlet = Figlet()
#     if len(sys.argv) == 1:
#         figlet.setFont(font = random.choice(figlet.getFonts()))

#     elif len(sys.argv) == 3:
#         try:
#             figlet.setFont(font = sys.argv[2])
#             if sys.argv[1] != "-f" and sys.argv[1] != "-font":
#                 raise ValueError
#             if sys.argv[2] not in figlet.getFonts():
#                 raise ValueError
#         except ValueError:
#             sys.exit()
#     else:
#         sys.exit()
#     print("Output:\n", figlet.renderText(prompt), sep = "")

# if __name__ == "__main__":
#     main()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

figlet = Figlet()
if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(figlet.getFonts()))

elif len(sys.argv) == 3:
    try:
        figlet.setFont(font = sys.argv[2])
        if sys.argv[2] not in figlet.getFonts():
            raise ValueError
        if sys.argv[1] != "-f" and sys.argv[1] != "-font":
            raise ValueError
        # if sys.argv[2] not in figlet.getFonts():
        #     raise FontNotFound(sys.argv[2])
    except ValueError:
        sys.exit("Invalid usage")
else:
    sys.exit()

prompt = input("Input: ")
print("Output:\n", figlet.renderText(prompt), sep = "")