#!/usr/bin/env python3
# Author: Angelo Garcia
# Date: December 1, 2025
# Description: Converts Celsius to Fahrenheit and handles invalid input


def fahrenheit():
    while True:  # Keep asking until valid input is given
        try:
            # Ask the user for a Celsius temperature
            tc = float(input("Enter temperature in degrees Celsius: "))

            # Convert Celsius to Fahrenheit
            tf = (9 / 5) * tc + 32

            # Print the result
            print(f"{tc}°C is equal to {tf}°F")
            break  # Exit loop if input is valid
        except ValueError:
            # Handle the case when input is not a number
            print("Please enter a valid number.")  # Friendly error message


def main():
    # Call the conversion function
    fahrenheit()


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
