def main():
    text = input("Text: ")
    letter, sentence, word = 0, 0, 1
    for c in text:
        if c.isalpha():
            letter += 1

        if c.isspace():
            word += 1

        if c == '.' or c == '!' or c == '?':
            sentence += 1

    L = letter / word * 100
    S = sentence / word * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index >= 1 and index <= 16:
        print(f"Grade {index}\n")

    elif index < 1:
        print("Before Grade 1\n")

    else:
        print("Grade 16+\n")

    return 0

if __name__ == "__main__":
    main()