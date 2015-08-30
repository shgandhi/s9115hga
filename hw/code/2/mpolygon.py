import _tkinter
import Tkinter
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot
# force non-interactive mode, or set 'interactive' to False
# in your ~/.matplotlib/matplotlibrc
matplotlib.pyplot.ioff()

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

wait_for_user()