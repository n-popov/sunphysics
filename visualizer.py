from matplotlib import pyplot


def visualize(y, name):
    pyplot.plot(y)
    pyplot.title(name)
    pyplot.savefig(name)