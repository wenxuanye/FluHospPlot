#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class interface(object):
    def __init__(self):
        self.loadFluData()
       
    def loadFluData(self):
        import pandas as pd
        self.fludata__long = pd.read_csv("fluHospData__long.csv")
        self.fludata__wide = pd.read_csv("fluHospData__wide.csv",index_col="date")

    def locdata(self,loc):
        import pandas as pd
        fluDataLong = self.fludata__long
        fluDataWide = self.fludata__wide
        
        self.locData__long = fluDataLong.loc[fluDataLong.location.isin(loc)]
        self.locData__wide = fluDataWide[loc]
        self.locname = loc

        self.locAbbr  = str(self.locData__long.iloc[0]["location_name"])
        
        return self.locData__long, self.locData__wide

    def getForecastDate(self):
        import datetime
        from epiweeks import Week

        from datetime import datetime as dt

        today = dt.today()
        dayofweek = today.weekday()

        thisWeek = Week.thisweek()
        if dayofweek in {6,0}: # a SUNDAY or MONDAY
            thisWeek = thisWeek
        else:
            pass
        self.thisWeek = thisWeek
        
        forecastDate = ((thisWeek).startdate() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        self.forecast_date = forecastDate
        return forecastDate

    def writeDataOut(self):
        self.fludata__long.to_csv("./{:s}/{:s}__fluhospdata_long.csv".format(self.forecast_date,self.forecast_date),index=False)
        self.fludata__wide.to_csv("./{:s}/{:s}__fluhospdata_wide.csv".format(self.forecast_date,self.forecast_date),index=False)
        
if __name__ == "__main__":
    pass
