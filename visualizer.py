import matplotlib
from matplotlib import pyplot
import numpy


def visualize(xx, y, name):
#    print("Plotting", *y, sep='\n')
    fig = pyplot.gcf()
    matplotlib.rcParams.update({'font.size': 24})
    fig.set_size_inches(14, 10)
    x = [(n / 57.3 - 1.57) for n in xx]
    pyplot.scatter(x, y, color = 'red', linewidths = 2, edgecolors = 'black', s = 80) #color = 'red'
    z = numpy.polyfit(x, y, 6)
    p = numpy.poly1d(z)
    xp = [(n / 57.3 - 1.57) for n in list(range(1, 180))]
    xpp = [(n / 57.3 - 1.57) for n in list(range(1, 180))]
    pyplot.plot(xp, p(xp),"r--", color = 'red', linewidth = 3)
    pyplot.plot(xp, max(y) * numpy.cos(xpp) * numpy.cos(xpp),"r--", color = 'grey', linewidth = 3)
    pyplot.title('Зависимость интенсивности от угла поворота полароида', fontsize=20, fontweight='bold')
    pyplot.xlabel('нормированный угол поворота полароида')
    pyplot.ylabel('интенсивность')
    pyplot.grid(True)
    pyplot.tight_layout()
    pyplot.savefig(name + '_norm')
    pyplot.clf()