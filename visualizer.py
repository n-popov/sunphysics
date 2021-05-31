import matplotlib
from matplotlib import pyplot
import numpy


def visualize(x, y, name):
#    print("Plotting", *y, sep='\n')
    fig = pyplot.gcf()
    matplotlib.rcParams.update({'font.size': 24})
    fig.set_size_inches(14, 10)
    pyplot.scatter(x, y, color = 'red', linewidths = 2, edgecolors = 'black', s = 80) #color = 'red'
#    pyplot.plot(x, y)
    z = numpy.polyfit(x, y, 5)
    p = numpy.poly1d(z)
    pyplot.plot(x, p(x),"r--", color = 'red', linewidth = 3)
    pyplot.title('Зависимость интенсивности от угла поворота полароида', fontsize=20, fontweight='bold')
    pyplot.xlabel('угол поворота полароида, градусы')
    pyplot.ylabel('интенсивность')
    pyplot.grid(True)
    pyplot.tight_layout()
    pyplot.savefig(name)
    pyplot.clf()