from emoji import emojize

def main():
    print("Output:", get_emoji(input("Input: ")))

def get_emoji(prompt):
    return emojize(prompt, language='alias')

main()