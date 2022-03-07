#mcandrew

class preprocess(object):
    def __init__(self):
        self.collectData()
        self.subsetTo2022()
        self.data2wide()
        self.writedata()

    def collectData(self):
        import pandas as pd
        cdcepidataURL = "https://raw.githubusercontent.com/cdcepi/Flusight-forecast-data/master/data-truth/truth-Incident%20Hospitalizations.csv"
        fludata = pd.read_csv(cdcepidataURL)

        fludata["date"] = pd.to_datetime(fludata.date)
        
        self.fludata = fludata
        return fludata
        
    def subsetTo2022(self):
        fludata = self.fludata
        self.fludataSubset = fludata.loc[fludata.date>="2021-01-01"]

    def data2wide(self):
        import pandas as pd
        fludata__wide = pd.pivot_table(index=["date"], columns=["location"], values=["value"],data=self.fludataSubset)
        fludata__wide.columns  = [y for (x,y) in fludata__wide.columns ]
        
        self.fludataSubset__wide = fludata__wide
        
    def writedata(self):
        self.fludataSubset.to_csv("./fluHospData__long.csv",index=False)
        self.fludataSubset__wide.to_csv("./fluHospData__wide.csv",index=True)
        
if __name__ == "__main__":

    prep = preprocess()
