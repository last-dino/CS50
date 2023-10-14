def main():
    time = input("What time is it? ").strip()
    timeNumber = convert(time)
    if 7 <= timeNumber <= 8:
        print("breakfast time")
    elif 12 <= timeNumber <= 13:
        print("lunch time")
    elif 18 <= timeNumber <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    return int(hour) + int(minute)/60

if __name__ == "__main__":
    main()