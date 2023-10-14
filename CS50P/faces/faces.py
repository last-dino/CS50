def main():
    sentence = input("What's your input? ")
    sentence = convert(sentence)
    print(sentence)

def convert(sentence):
    sentence = sentence.replace(":)", "🙂").replace(":(", "🙁")
    return sentence

main()