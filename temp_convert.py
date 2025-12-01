#!/usr/bin/env python3
# Author: Angelo Garcia
# Date: December 1, 2025
# Description:
#     Converts a temperature from Celsius to Fahrenheit.


def fahrenheit():
    # Ask the user for a Celsius temperature
    tc = float(input("Enter temperature in degrees Celsius: "))

    # Convert Celsius to Fahrenheit using the formula
    tf = (9 / 5) * tc + 32

    # Print the final result
    print(f"{tc}°C is equal to {tf}°F")


def main():
    # Call the conversion function
    fahrenheit()


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
