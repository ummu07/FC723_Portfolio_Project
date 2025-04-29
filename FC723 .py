#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FC723 Portfolio Project 1
This script implements the Euclidean Algorithm to compute the Greatest Common Divisor (GCD)
of two positive integers. It also checks if the numbers are relatively prime. 

@author: ummusalmahumarrani
"""

class EuclideanAlgorithm:
    def __init__(self):
        # Constructor method, currently no initialization needed
        pass

    def compute_gcd(self, a, b):
        """
        Computes the Greatest Common Divisor (GCD) of two positive integers
        using the Euclidean Algorithm.
        """
        while b != 0:  # Continue looping until b becomes zero
            temp = b  # Store the value of b in temp
            b = a % b  # Update b to be the remainder of a divided by b
            a = temp  # Update a to be the old value of b
        return a  # When b becomes zero, a contains the GCD

def main():
    calculator = EuclideanAlgorithm()  # Create an instance of EuclideanAlgorithm class

    try:
        # Get user input and validate it
        a = int(input("Enter the first positive integer: "))  # Prompt user for the first integer
        b = int(input("Enter the second positive integer: "))  # Prompt user for the second integer

        if a <= 0 or b <= 0:  # Check if either number is not positive
            print("Error: Only positive integers are allowed.")  # Print error message
            return  # Exit the program

        gcd = calculator.compute_gcd(a, b)  # Call the compute_gcd method and store the result
        print(f"The GCD of {a} and {b} is {gcd}.")  # Print the result

        # Extension: Check if numbers are relatively prime
        if gcd == 1:
            print("The numbers are relatively prime.")  # If GCD is 1, numbers are relatively prime
        else:
            print("The numbers are not relatively prime.")  # Otherwise, they are not

    except ValueError:
        print("Error: Invalid input. Please enter positive integers only.")  # Catch and handle non-integer inputs

if __name__ == "__main__":
    main()  # Run the main function