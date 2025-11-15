
import sklearn
import numpy
import pandas
import matplotlib
from TideData import IrishNationalTideGaugeNetwork

class TideML():
    tideData = IrishNationalTideGaugeNetwork

    def __init__ (self, tideData):
        self.tideData = tideData