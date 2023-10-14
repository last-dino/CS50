import requests
import sys

if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        break
    except requests.RequestException:
        pass

rate = float(response["bpi"]["USD"]["rate_float"])

result = amount * rate
print(f"${result:,.04f}", end = "")










# for results in response["bpi"]:
#     for items in results["USD"]:
#         rate = float(items["rate"])

# result = amount * rate
# print(f"${result:.04f}")
