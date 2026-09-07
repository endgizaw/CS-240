from PIL import Image


# 1. Build an ASCII-to-decimal converter.

s = "Endo"
for c in s:
    print(ord(c))


# 2. Build a number-base converter supporting binary, decimal, octal, and hexadecimal.

# def to_binary(n):
#     if n >= 0:
#         result = bin(n)
#         result = result[2:]
    # else:  # handle neg values but not needed
    #     magnitude = -n
    #     result = bin(magnitude)
    #     result = result[2:]
    #     result = "-" + result
    # return result


# def to_octal(n):
#     if n >= 0:
#         result = oct(n)
#         result = result[2:]
#     # else: # handle neg values but not needed
#     #     magnitude = -n
#     #     result = oct(magnitude)
#     #     result = result[2:]
#     #     result = "-" + result
#     return result


# def to_hex(n):
#     if n >= 0:
#         result = hex(n)
#         result = result[2:]
#     # else:  # handle neg values but not needed
#     #     magnitude = -n
#     #     result = hex(magnitude)
#     #     result = result[2:]
#     #     result = "-" + result
#     return result


# def two_comp(bits, bit_width):
#     value = int(bits, 2)
#     if (value >= 2 ** (bit_width - 1)):
#         value -= 2 ** bit_width
#     return value


# def int_to_binary(n, bit_width):
#     if n < 0:
#         n = (1 << bit_width) + n
#     return format(n, f'0{bit_width}b')


# bit_width = 8
# test_vals = [0, 255, -1]

# for num in test_vals:
#     if num >= 0:
#         print(f"{to_binary(num)}")
#         print(f"{to_hex(num)}")
#         print(f"{to_octal(num)}")
#     else:
#         tc = int_to_binary(num, bit_width)
#         print(f"{tc}")
#         print(f"{two_comp(tc, bit_width)}")


# 3. Write a program that reads an image and prints its pixel values.

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

# 4. Write a program that consumes pixel values and creates an image.


# def convert(pixel):
#     if pixel == "R":
#         return (237, 28, 36)
#     elif pixel == "B":
#         return (0, 0, 0)
#     elif pixel == "Y":
#         return (255, 242, 0)
#     else:
#         return pixel


# input_text_file = open("awesome_picture.txt", "r")
# lines = input_text_file.readlines()
# h, w = len(lines), lines[0].count(" ")
# img = Image.new(mode="RGB", size=(w, h), color=(0, 0, 0))

# for y in range(h):
#     pixels = lines[y].split()
#     for x in range(w):
#         pixel = pixels[x]
#         img.putpixel((x, y), convert(pixel))

# 5. Test boundary cases, including zero, the largest supported unsigned value, and at least one negative two's-complement value.
