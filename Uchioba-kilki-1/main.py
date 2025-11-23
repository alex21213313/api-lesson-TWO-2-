import requests
import argparse


def get_conversion_rates(token, currency):
    url = f"https://v6.exchangerate-api.com/v6/{token}/latest/{currency}"
    response = requests.get(url)
    response.raise_for_status()
    conversion_rates = response.json()
    return conversion_rates

def main():
    parser = argparse.ArgumentParser(description="Получение курсов обмена для заданной валюты.")
    parser.add_argument("-cur", "--currency", help="Укажите валюту, например, USD, EUR", required=True)
    args = parser.parse_args()

    
    currency = args.currency.upper()

    
   
    try:
        rates = get_conversion_rates(token, currency)
        print(f"Курсы обмена для валюты: {currency}")
        for currency, rate in rates["conversion_rates"].items():
         print(f"1 {currency} = {rate} {rates[currency]}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении курсов обмена: {e}")

if __name__ == "__main__":
    main()


















































