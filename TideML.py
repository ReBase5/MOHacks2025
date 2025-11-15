
import os
import numpy
import pandas
import sklearn.linear_model

class TideML():
    def __init__(self):
        tideDataFrame = pandas.read_csv("IrishNationalTideGaugeNetwork.csv", columns=['Time','Water_Level_LAT'])

        self.tideModel = sklearn.linear_model.LinearRegression()
        self.tideModel.fit(tideDataFrame.columns[1],tideDataFrame.columns[2], sample_weight=0.5)

    def predictTide(self, time):
        return self.tideModel.predict(time)

