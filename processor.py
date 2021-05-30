from PIL import Image
import cache
import hashlib



def red_level(image_name, images_cache):
    image_hash = hash(image_name)
    if image_hash in images_cache.data.keys():
        return images_cache[image_hash]
    retval = 0
    image = Image.open(image_name)
    for x_idx in range(image.width):
        for y_idx in range(image.height):
           retval += image.getpixel((x_idx, y_idx))[0]
    images_cache.data[image_hash] = retval
    return retval
