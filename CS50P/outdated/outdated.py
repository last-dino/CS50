def main():
    convert_date()

def convert_date():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ").strip()
            if "," in date:
                date = date.replace(", ", " ")
                month, day, year = date.split(" ")
                for i in range(len(months)):
                    if months[i] == month.capitalize():
                        month = str(i + 1)
            else:
                month, day, year = date.split("/")
            if int(month) < 1 or int(month) > 12:
                continue
            if int(day) < 1 or int(day) > 31:
                continue
            break
        except ValueError:
            pass

    print(f"{year}-{int(month):02}-{int(day):02}")

main()