def get_verified_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age >= 18:
                print("Age verified.")
                return age
            else:
                print("You must be 18 years or older to proceed.")
        except ValueError:
            print("Invalid input. Please enter a valid age as a whole number.")

if __name__ == "__main__":
    user_age = get_verified_age()
    print(f"User's age: {user_age}")
