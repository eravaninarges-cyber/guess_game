import random

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    won = False

    print("\n به بازی حدس اعداد خوش آمدید!")
    print("من یک عدد بین 1 تا 100 انتخاب کرده‌")
    print("شما 5 فرصت برای حدس زدن دارید.\n")

    while attempts < max_attempts:

        print("تلاش فعلی:", attempts + 1, max_attempts)
        print("جان باقی مانده:", max_attempts - attempts)

        try:
            guess = int(input("حدس خود را وارد کنید: "))

            if guess < 1 or guess > 100:
                print(" لطفاً عددی بین 1 تا 100 وارد کنید.\n")
                continue

        except ValueError:
            print(" ورودی نامعتبر است! لطفاً فقط عدد وارد کنید.\n")
            continue

        attempts += 1

        difference = abs(secret_number - guess)

        if guess == secret_number:
            won = True
            print("\n آفرین! شما عدد را درست حدس زدید!")

            if attempts == 1:
                print(" رتبه شما: نمونه ای")
            elif attempts == 2:
                print(" رتبه شما: بسیار خوب")
            elif attempts == 3:
                print(" رتبه شما: خوب")
            elif attempts == 4:
                print(" رتبه شما: قبول")
            elif attempts == 5:
                print(" رتبه شما: با شانس بردی!")

            break

        elif guess < secret_number:
            direction = "بزرگ‌تر وارد کن!"
        else:
            direction = "کوچک‌تر وارد کن!"

        if difference <= 5:
            hint = "خیلی نزدیکی!"
        elif difference <= 15:
            hint = "نزدیکی، ولی هنوز فاصله داری!"
        else:
            hint = "خیلی دوری!"

        print(direction)
        print(hint)
        print()

    if not won:
        print("\n متأسفانه فرصت‌های شما تمام شد!")
        print("عدد مخفی برابر بود با:", secret_number)

    print("\nبازی تمام شد!")


# اجرای بازی و امکان شروع مجدد

while True:
    play_game()

    answer = input("\nآیا می‌خواهید دوباره بازی کنید؟ (بله/خیر): ")

    if answer.strip().lower() not in ["بله", "ب", "yes", "y"]:
        print("\امیدوارم دوباره بازی کنید.")
        break
