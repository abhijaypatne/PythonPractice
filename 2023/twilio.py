import requests


def main():
    try:
        url = "https://jsonmock.hackerrank.com/api/transactions/search"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            transactions = data["data"]

            max_user_name = ""
            max_amount = float("-inf")

            for transaction in transactions:
                user_name = transaction["userName"]
                amount = float(transaction["amount"].replace("$", "").replace(",", ""))

                if amount > max_amount:
                    max_amount = amount
                    max_user_name = user_name

            print("UserName with Max Amount:", max_user_name)
        else:
            print("Failed to retrieve data. Response Code:", response.status_code)

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
