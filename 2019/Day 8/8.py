with open("8.in", "r") as f:
    pixels = f.read()

h, w = 6, 25  # height, width of image
ppl = h*w  # pixels per layer

# Separate the list of pixels into individual layers of length w.
layers = [pixels[i:i+ppl] for i in range(0, len(pixels), ppl)]

# Enumerate these pixel layers.
# Sort them (ascending) by the number of zeroes they contain (with a cool lambda expression).
zeroes = sorted(list(enumerate(layers)), key=lambda x: x[1].count("0"))

# Return the number of the layer with the fewest zeroes.
z = zeroes[0][0]
print(z)

# == PART 1 ==
# Calculate the product of the number of "1" and "2" digits in the layer with the fewest zeroes.
part_1 = int(layers[z].count("1")) * int(layers[z].count("2"))
print(part_1)

# Zip together each pixel layer so pixels are now in tuples of other pixels at the same coordinate.
zipped = list(zip(*layers))

# Probably an unnecessarily complicated list comprehension but I wanted to feel smart.
# Removes all transparent pixels (2) from each layer and returns the top-most coloured pixel.
# These pixels are then joined together to represent the pixels of the image.
image = "".join([[p for p in layer if p != "2"][0] for layer in zipped])

# Replace zeroes with blank space to improve readability of final image.
image = image.replace("0", " ")

# == PART 2 ==
# Print the image in rows of length w so the message can be read.
for i in range(h):
    print("".join(image[i*w: i*w + w]))
