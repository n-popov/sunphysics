import os


def extract(directory):
    extracted_images_names = \
        [os.path.join(directory, file) for file in os.listdir(directory)]
    return extracted_images_names


class ExperimentsHolder:
    def __init__(self, directories, angles, deltas):
        self.data = list(zip([extract(directory) for directory in directories],
                             angles, deltas))

    def __getitem__(self, item):
        return self.data[item]
