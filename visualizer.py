from matplotlib import pyplot


def visualize(y, name):
    print("Plotting", *y, sep='\n')
    pyplot.plot(y)
    pyplot.title(name)
    pyplot.savefig(name)