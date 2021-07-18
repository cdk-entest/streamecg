import matplotlib.pyplot as plt

class Draw(object):
    def __init__(self,figsize=(10,5),sharex=False,sharey=False,nrows=4,ncols=1,ymin=None,ymax=None):
        self.nrows = nrows
        self.ncols = ncols
        self.ymin = ymin
        self.ymax = ymax
        self.fig,self.axes = plt.subplots(nrows,ncols,figsize=(10,5),sharex=sharex,sharey=sharey)
        plt.ion()
        self.fig.show()
        self.fig.canvas.draw()
        self.fig.tight_layout()
    
    def graph(self, y, color='blue', linewidth=0.5, marker=None, markersize=None):
        if self.nrows>1:
                for k in range(self.nrows):
                    self.axes[k].clear()
                    if self.ymin  is not None:
                        self.axes[k].set_ylim(self.ymin,self.ymax)
                    if marker is None:
                        self.axes[k].plot(y, color=color, linewidth=linewidth, markersize=markersize)
                    else:
                        self.axes[k].plot(y, marker, linewidth=linewidth, markersize=markersize)


        if self.nrows==1:
            self.axes.clear()
            if marker is None:
                self.axes.plot(y, color=color, linewidth=linewidth, markersize=markersize)
            else:
                self.axes.plot(y, marker, linewidth=linewidth, markersize=markersize)
            self.axes.set_ylim(self.ymin, self.ymax)

        self.fig.canvas.draw()
