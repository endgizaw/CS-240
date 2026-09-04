from PIL import Image

# Build an ASCII-to-decimal converter.

# s = "Endalk"
# for c in s:
#    print(ord(c))


# Build a number-base converter supporting binary, decimal, octal, and hexadecimal.

# Write a program that reads an image and prints its pixel values.

# def convert(pixel):
#     if pixel == "(237, 28, 36)":
#         return "R"
#     elif pixel == "(0, 0, 0)":
#         return "B"
#     elif pixel == "(255, 242, 0)":
#         return "Y"
#     else:
#         return pixel


# image = Image.open("smiley2.png").convert("RGBA")
# output_text_file = open("awesome_picture.txt", "w")

# for y in range(image.height):
#     for x in range(image.width):
#         r, g, b, _ = image.getpixel((x, y))
#         pixel = f"({r}, {g}, {b})"
#         pixel = convert(pixel)
#         output_text_file.write(pixel)
#         output_text_file.write(" ")
#     output_text_file.write("\n")

# output_text_file.close()

# Write a program that consumes pixel values and creates an image.


def convert(pixel):
    if pixel == (237, 28, 36):
        return "R"
    elif pixel == (0, 0, 0):
        return "B"
    elif pixel == (255, 242, 0):
        return "Y"
    else:
        return pixel


input_text_file = open("awesome_picture.txt", "r")
lines = input_text_file.readlines()
h, w = len(lines), lines[0].count(" ")
img = Image.new(mode="RGB", size=(h, w), color=(0, 0, 0))

for y in range(h):
    pixels = lines[y].split()
    print(pixels)
    for x in range(w):
        pixel = pixels[x]
        img.putpixel((x, y), convert(pixels))
    print()

# Test boundary cases, including zero, the largest supported unsigned value, and at least one negative two's-complement value.
