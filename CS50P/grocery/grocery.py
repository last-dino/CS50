def main():
    make_list()

def make_list():
    grocery = {}
    while True:
        try:
            item = input().upper()
            if item not in grocery:
                grocery[item] = 1
            else:
                grocery[item] += 1
        except EOFError:
            print()
            break
    items = sorted(grocery.keys())
    for key in items:
        print(grocery[key], key)

main()