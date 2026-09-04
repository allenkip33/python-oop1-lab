#!/usr/bin/env python3

class Coffee:
    def __init__(self):
        self.price =  float(input("Enter the price"))

        while True:
            size_input = input("Enter the size :").capitalize()
            if size_input not in ("Small", "Medium", "Large"):
                print("size must be Small, Medium, or Large")
            else:
                self.input = size_input
                break

    def tip(self):
            print("This coffee is great, here’s a tip!")
            self.price += 1


