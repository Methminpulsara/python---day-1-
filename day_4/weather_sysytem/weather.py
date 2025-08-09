
temps_for_a_week_per_day = [[0.0 for _ in range(3)] for _ in range(7)]
while True:
    print("\n Add Details              [1]")
    print(" Show Maximum Weather Value [2]")
    print(" Show Maximum Weather Value [3]")
    print(" Exit                       [0]")

    choose = int(input("\nPlease press numbers to continue: "))

    if choose == 0:
        break

    elif choose == 1:
        while True:
            day = int(input("Enter Day (1-7): "))
            hour = int(input("Enter hour (1-3): "))
            weather_value = int(input("Enter weather value: "))

            if 1 <= day <= 7 and 1 <= hour <= 3 and weather_value >= 0:
                temps_for_a_week_per_day[day - 1][hour - 1] = weather_value
            else:
                print("Invalid input, please try again.")
                continue

            print("\nCurrent Weather Data:")
            for r in temps_for_a_week_per_day:
                print(r)

            yes_or_no = input("\nDo you want to add another details (y/n): ").lower()
            if yes_or_no != "y":
                break

    elif choose == 2:

        while True:

            print(f"\nMaximum weather")
            day = int(input("Enter Your day :  "))
            if day in range(1, 8):
                maximum = max(temps_for_a_week_per_day[day - 1])
                print(f"Max Value is your selected day {day} is {maximum} ")
            else:
                print("invalid input ! ")
            yes_or_no = input("\nDo you want to add another details (y/n): ").lower()
            if yes_or_no != "y":
                break

    elif choose == 3:
        print("View Averages ")
        # day = int(input("Enter Your day :  "))
        # if day in range(1,8):
        #     print("Average " , temps_for_a_week_per_day[day -1 / 3 ]  )

    elif choose == 4 :
        total = 0
        for day in temps_for_a_week_per_day:
            for hour in day:
               total += hour
        print("\nAverage for the weeek  ", total//21)

    else:
        print("Invalid choice, please try again.")
