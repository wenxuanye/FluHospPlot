#mcandrew

import sys
import numpy as np
import pandas as pd

from glob import glob

class dataLatest(object):
    def __init__(self):
        self.find_datedfolders()
        self.copyfiles()

    def find_datedfolders(self):
        from glob import glob
        import re
        import os

        dates=[]
        for _ in glob("*"):
            if not os.path.isdir(_):
                continue
            if re.match("\d{4}[-]\d{2}[-]\d{2}",_):
                dates.append(_)
        dates = sorted(dates)
        latestFolder = dates[-1]

        self.latestFolder = latestFolder
        return latestFolder

    def copyfiles(self):
        from glob import glob
        import shutil
        import re
        import os
        
        for fil in glob(self.latestFolder+"/*"):
            filname = fil.split("/")[-1]
            filroot = re.sub("\d{4}[-]\d{2}[-]\d{2}[_]+","",filname)

            newpath = os.path.join( "data-latest/", filroot )

            shutil.copy2(fil,newpath)

if __name__ == "__main__":

    dl = dataLatest()
    
    

    





