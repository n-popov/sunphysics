import matplotlib
from matplotlib import pyplot
import numpy

x = [5, 10, 15, 20]
y1 = [3, 9, 13, 16]

y2 = [5, 7, 13, 15]

y3 = [5, 8, 10, 14]

y4 = [4, 9, 14, 14]

fig = pyplot.gcf()
matplotlib.rcParams.update({'font.size': 24})
fig.set_size_inches(14, 10)

pyplot.scatter(x, y1, color='red', linewidths=2, edgecolors='black', s=80)
z1 = numpy.polyfit(x, y1, 1)
p1 = numpy.poly1d(z1)
pyplot.plot(x, p1(x), "r--", color='red', linewidth=3)

pyplot.scatter(x, y2, color='blue', linewidths=2, edgecolors='black', s=80)
z2 = numpy.polyfit(x, y2, 1)
p2 = numpy.poly1d(z2)
pyplot.plot(x, p2(x), "r--", color='blue', linewidth=3)

pyplot.scatter(x, y3, color='green', linewidths=2, edgecolors='black', s=80)
z3 = numpy.polyfit(x, y3, 1)
p3 = numpy.poly1d(z3)
pyplot.plot(x, p3(x), "r--", color='green', linewidth=3)

pyplot.scatter(x, y4, color='grey', linewidths=2, edgecolors='black', s=80)
z4 = numpy.polyfit(x, y4, 1)
p4 = numpy.poly1d(z4)
pyplot.plot(x, p4(x), "r--", color='grey', linewidth=3)

pyplot.title('Зависимость угла поворота плоскости поляризации от концентрации сахара', fontsize=20, fontweight='bold')

pyplot.annotate("T = 22⁰С: y = " + str(p1), xy=(7, 15), color='red')
pyplot.annotate("T = 35⁰С: y = " + str(p2), xy=(7, 13), color='blue')
pyplot.annotate("T = 50⁰С: y = " + str(p3), xy=(15, 6), color='green')
pyplot.annotate("T = 75⁰С: y = " + str(p4), xy=(15, 4), color='grey')

pyplot.xlabel('концентрация, г/100мл')
pyplot.ylabel('угол, градусы')
pyplot.grid(True)
pyplot.tight_layout()
pyplot.savefig('temp')
pyplot.clf()


xx = [22, 35, 50, 70]
yy = [53, 44, 35, 43]

pyplot.scatter(xx, yy, color='grey', linewidths=2, edgecolors='black', s=80)
pyplot.plot(xx, yy, "r--", color='grey', linewidth=3)

pyplot.axis([0, 80, 0, 60])
pyplot.title('Зависимость удельного вращения от температуры', fontsize=20, fontweight='bold')
pyplot.xlabel('температура, ⁰С')
pyplot.ylabel('αD')
pyplot.grid(True)
pyplot.tight_layout()
pyplot.savefig('a_ot_t')
pyplot.clf()