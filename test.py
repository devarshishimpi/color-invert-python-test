from PIL import Image

# Define color mapping for inversion
color_mapping = {
    (0, 0, 0): (255, 255, 255),   # Black to White
    (255, 255, 255): (0, 0, 0),   # White to Black
    (0, 0, 255): (0, 255, 255),   # Dark Blue to Light Blue
    (0, 255, 255): (0, 0, 255),   # Light Blue to Dark Blue
    # Add more color mappings as needed
}

# Open the image
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'

image = Image.open(input_image_path)

# Convert the image to RGB mode (if not already)
if image.mode != 'RGB':
    image = image.convert('RGB')

# Invert the colors
inverted_pixels = []
for pixel in image.getdata():
    if pixel in color_mapping:
        inverted_pixel = color_mapping[pixel]
    else:
        inverted_pixel = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
    inverted_pixels.append(inverted_pixel)

inverted_image = Image.new('RGB', image.size)
inverted_image.putdata(inverted_pixels)

# Save the inverted image
inverted_image.save(output_image_path)

print("Image colors inverted and saved as", output_image_path)
