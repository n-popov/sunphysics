from PIL import Image

def edit(name):
    image = Image.open(name)
    xs = []
    ys = []
    for x_idx in range(1700, 2100):
        for y_idx in range(1250, 1450):
            R, _, _ = image.getpixel((x_idx, y_idx))
            if R < 50:
                image.putpixel((x_idx, y_idx), (0, 0, 255))
            else:
                xs.append(x_idx)
                ys.append(y_idx)
    image.save('processed.JPG')
    return xs, ys

X, Y = edit("unprocessed.JPG")
print(min(X), max(X))
print(min(Y), max(Y))