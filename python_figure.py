import matplotlib.pyplot as plt
from matplotlib import rc, gridspec
# import matplotlib.rc as rc
# import matplotlib.gridspec as gridspec
import numpy as np

rc("font", **{"size":24}) # set default font size
rc("text", usetex=True) # to use latex labels
plt.figure(figsize=(8.6, 7)) # figure size (width, height) in inches

gs = gridspec.GridSpec(1, 1)

# to modify margins of plot and the height space and width space between
# adjacent subplots
gs.update(left=0.2,
          right=0.95,
          top=0.98,
          bottom=0.12,
          hspace=0.0,
          wspace=0.0)

xdata = np.linspace(-2*np.pi, 2*np.pi, 200)
ydata = np.sin(xdata)

ax = plt.subplot(gs[0,0])

ax.plot(xdata, ydata, linewidth=3, color="#C70039") # line plot
ax.axhline(y=0, color="lightgrey", linewidth=2, zorder=-1) # add horizontal line

# abscissae
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$"])
ax.set_xlabel(r"$x$")

# ordinates
ax.set_yticks([-1, 0, 1])
ax.set_ylabel(r"$\sin(x)$")

# place label outside plot
plt.text(0.02, 0.95, r"$\mathrm{(a)}$", transform=plt.gcf().transFigure)

# save figure
plt.savefig("python_figure.pdf")
