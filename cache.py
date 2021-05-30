class Cache:
    def __init__(self):
        self.data = dict()
        self.file = open('cache.txt')
        for hash, value in [map(int, line.strip().split()) for line in open('cache.txt').readlines()]:
            self.data[hash] = value
        self.file.close()

    def __getitem__(self, item):
        return self.data[item]

    def __del__(self):
        file = open('cache.txt', 'w')
        for hash, value in self.data.items():
            file.write(hash + ' ' + value)
