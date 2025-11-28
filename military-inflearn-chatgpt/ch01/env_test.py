import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig("plot.png")