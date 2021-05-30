import os
from PIL import Image

class ExperimentsHolder:
    def __init__(self, directories):
        self.data = [self.extract(directory) for directory in directories]

    def extract(self, directory):
        extracted_images_names = \
            [os.path.join(directory, file) for file in os.listdir(directory)]
        return extracted_images_names

    def __getitem__(self, item):
        return self.data[item]
