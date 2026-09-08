#!/usr/bin/env python3

class Coffee:
    def __init__(self, size: str, price: float):
        formatted_size = size.capitalize()
        if formatted_size not in ("Small", "Medium", "Large"):
            raise ValueError("size must be Small, Medium, or Large")
            
        self.size = formatted_size
        self.price = float(price)

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1.0
