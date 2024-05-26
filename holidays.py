import requests

def get_holidays(year, month):
    holidays = []

    if month in [1, 2, 3, 4, 5, 6]:
        days_in_month = 31
    else:
        days_in_month = 30

    for day in range(1, days_in_month + 2):
        url = f'https://holidayapi.ir/jalali/{year}/{month}/{day}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data["is_holiday"]:
                holidays.append((year, month, day, data["events"][0]["description"]))
    return holidays

def main():
    year = 1403
    month = input("Enter the month (1-12): ")

    holidays = get_holidays(year, month)

    if holidays:
        print("Holidays in the specified month:")
        for holiday in holidays:
            print(f"{holiday[0]}/{holiday[1]}/{holiday[2]}: {holiday[3]}")
    else:
        print("No holidays found for the specified month.")

if __name__ == "__main__":
    main()
