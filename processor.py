from PIL import Image


def red_level(image_name):
#    print(f"processing {image_name}")
    reds = []
    image = Image.open(image_name)
    for x_idx in range(1700, 2100):
        for y_idx in range(1230, 1450):
            R, _, _ = image.getpixel((x_idx, y_idx))
            if R > 100:
                reds.append(R)
    if len(reds) == 0:
        return 0
    return sum(reds) # / len(reds)
