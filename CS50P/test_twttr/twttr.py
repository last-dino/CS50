def main():
    print("Output", shorten(input("Input: ")))


def shorten(word):

    for c in word:
        if c == "A" or c == "a" or c == "E" or c == "e" or c == "I" or c == "i" or c == "O" or c == "o" or c == "U" or c == "u":
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()