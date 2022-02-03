#mcandrew

class visualize(object):
    def __init__(self,io):
        self.io = io
        self.dataLong, self.dataWide = io.locData__long, io.locData__wide
        self.locname = io.locname
        
    def fluTrajectory(self):
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.style.use("fivethirtyeight")
        fig,ax = plt.subplots()

        plotdata = self.dataWide
        hosps = plotdata[self.locname].values
        dates = plotdata.index[::-1][::4][::-1]
        
        ax.plot( plotdata , lw=2,alpha=0.40,color="blue" )
        ax.scatter(dates,hosps[::-1][::4][::-1],s=10,color="blue",alpha=0.8)
        
        #label points 5 weeks in the past
        hospsPast5 = hosps[-5:]
        datesPast5 = plotdata.index[-5:]

        ax.scatter(datesPast5,hospsPast5,s=10,color="blue",alpha=0.8)
        for date,hosp in zip(datesPast5,hospsPast5):
            ax.text(date,hosp,s="{:d}".format(int(hosp))
                    ,ha="right",va="bottom",fontsize=6)
                    #,bbox = dict(facecolor=mpl.rcParams['axes.facecolor'], alpha=0.4)   )
        
        ax.tick_params(which="both", labelsize=6)

        ax.set_ylabel("Number of weekly\nconfirmed hospitlizations due to influenza", fontsize=6)
        ax.set_xlabel("",fontsize=6)

        ax.set_xticks(ax.get_xticks()[::-1][::10][::-1])
        ax.set_yticklabels(["{:,}".format(int(y)) for y in ax.get_yticks()])
        
        ax.text(0.01,0.95,"{:s}".format(self.locname[0]),fontsize=6,fontweight="bold",ha="left",va="top",transform=ax.transAxes)
        ax.text(0.01,0.80,"Data source = https://github.com/cdcepi/Flusight-forecast-data",fontsize=6,ha="left",va="top",transform=ax.transAxes)

        self.ax=ax
        self.fig=fig
        return fig,ax

    def mm2inch(x):
        return x/25.4
    
    def plotoutBanner(self):
        import matplotlib.pyplot as plt

        plt.subplots_adjust(bottom=0.115)
        self.fig.set_size_inches( 1600/300, 300/300 )
        plt.savefig("{:s}_UStrajectory.jpg".format(self.io.getForecastDate()),dpi=300)

    def plotoutState(self):
        import matplotlib.pyplot as plt

        plt.subplots_adjust(bottom=0.115)
        self.fig.set_size_inches( 1600/300, 800/300 )

        fd = self.io.getForecastDate()
        plt.savefig("./{:s}/{:s}_{:s}trajectory.jpg".format(fd,fd,self.io.locAbbr),dpi=300)

if __name__ == "__main__":

    pass

    

