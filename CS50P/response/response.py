import validators

def main():
    response = input("What's your email address? ")
    print(validate(response))

def validate(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()