import random

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

def rgb_to_hex(r, g, b):
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color

hex_color = rgb_to_hex(r, g, b)
print(f"RGB: R: {r}, G: {g}, B: {b}")
print(f"Hex: {hex_color}")
