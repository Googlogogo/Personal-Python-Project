import calendar
import datetime

today = datetime.date.today()
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
now = datetime.datetime.now()

while True:
    while True:
        year = int(input("Which year were you born in? "))
        if current_year - 150 <= year < current_year:
            while True:
                month = int(input("Which month were you born in? "))
                if not 1 <= month <= 12:
                    print("The month must be between 1 and 12!")
                    continue
                else:
                    break

            if month in {1, 3, 5, 7, 8, 10, 12}:
                d_max = 31
            if month in {4, 6, 9, 11}:
                d_max = 30
            if month == 2:
                if calendar.isleap(year):
                    d_max = 29
                else:
                    d_max = 28

            while True:
                day = int(input("Which day were you born on? "))
                if not 1 <= day <= d_max:
                    print("The day must be between 1 and " + str(d_max) + "!")
                    continue
                else:
                    break

            break

        elif year == current_year:
            while True:
                month = int(input("Which month were you born in? "))
                if month > current_month or not 1 <= month <= 12:
                    print("The month must be smaller than the current month " + str(current_month) + "!")
                    continue
                else:
                    break

            if month in {1, 3, 5, 7, 8, 10, 12}:
                d_max = 31
            if month in {4, 6, 9, 11}:
                d_max = 30
            if month == 2:
                if calendar.isleap(year):
                    d_max = 29
                else:
                    d_max = 28

            while True:
                day = int(input("Which day were you born on? "))
                if not 1 <= day <= d_max:
                    print("The day must be between 1 and " + str(d_max) + "!")
                    continue
                else:
                    if month == current_month and day > current_day:
                        print("The day must be smaller than the current day " + str(current_day) + "!")
                        continue
                    else:
                        break
            break

        else:
            print("The year must be between " + str(current_year - 150) + " and " + str(current_year) + "!")
            continue

    if month == 2 and day == 29:
        x = year + 4 * ((current_year - year) / 4 + 1) - current_year
        next_birthday = datetime.date(int(current_year + x), month, day)
        diff = next_birthday - today
        if current_month > month:
            print("🎉You are very special! You are " + str(current_year - year) + " years old, but " +
                  "you only had " + str((current_year - year) / 4) + " birthdays!")
            print("💪Only " + str(diff.days) + " days until your next REAL birthday!")
        elif current_month == month and current_day == day:
            print("🎂Happy birthday! But you are very special! You are " + str(current_year - year) +
                  " years old, but you only had " + str((current_year - year) / 4) + " birthdays!")
            print(str(diff.days) + " days until your next REAL birthday!")
        elif current_month < month or current_month == month and current_day < day:
            print(
                "🎉You are very special! You are " + str(current_year - year) + " years old, but "
                + "you only had " + str((current_year - year - 1) / 4) + " birthdays!")
            print("💪Only " + str(diff.days) + " days until your next REAL birthday!")

    else:
        if datetime.date(year, month, day) < datetime.date(year, current_month, current_day):
            next_birthday = datetime.date(current_year + 1, month, day)
            diff = next_birthday - today
            print("You are " + str(current_year - year) + " years old.")
            print("💪Only " + str(diff.days) + " days until your next birthday!")

        elif datetime.date(year, month, day) > datetime.date(year, current_month, current_day):
            next_birthday = datetime.date(current_year, month, day)
            diff = next_birthday - today
            print("You are " + str(current_year - year - 1) + " years old.")
            print("💪Only " + str(diff.days) + " days until your next birthday!")

        else:
            if str(current_year - year).endswith("11") or str(current_year - year).endswith("12") \
                    or str(current_year - year).endswith("13"):
                end = "th birthday!"
            elif str(current_year - year).endswith("1"):
                end = "st birthday!"
            elif str(current_year - year).endswith("2"):
                end = "nd birthday!"
            elif str(current_year - year).endswith("3"):
                end = "rd birthday!"
            else:
                end = "th birthday!"
            print("🎂Happy " + str(current_year - year) + end)

    delta_days = (now - datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")).days
    print("👏Congratulations! You have lived on this beautiful planet Earth for " + str(delta_days) + " days!")

    once_more = input('\nOne more time? (Type "Y" or "N") ')
    if once_more == "Y":
        continue
    else:
        break
