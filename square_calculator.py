def calculate_square(number):
    """Calculates the square of a given number."""
    return number ** 2

def main():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        squared_value = calculate_square(number)
        print(f"The square of {number} is {squared_value}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
