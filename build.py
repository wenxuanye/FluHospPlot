#mcandrew

import sys
import os

from interface import interface
from visualize import visualize as viz

if __name__ == "__main__":

    io = interface()
    io.getForecastDate()
    
    if os.path.isdir(io.forecast_date):
        pass
    else:
        os.mkdir(io.forecast_date)
    
    io.locdata(["US"])
    vis = viz(io)

    vis.fluTrajectory()
    vis.plotoutState()

    for loc in io.fludata__wide:
        io.locdata([loc])
        vis = viz(io)
        vis.fluTrajectory()
        
        vis.plotoutState()
    io.writeDataOut()
