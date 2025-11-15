import pandas
import sklearn.linear_model

class tideML:
    def __init__(self):
        self.tideDataFrame = pandas.read_csv("IrishNationalTideGaugeNetwork.csv", chunksize= 10000)
        self.tideDataFrame.drop(columns=["latitude","longitude","altitude","Water_Level_OD_Malin","station_id","QC_Flag","datasourceid"])

        self.tideModel = sklearn.linear_model.LinearRegression()
        self.tideModel.fit(self.tideDataFrame[:,["time"]],self.tideDataFrame[:,["Water_Level_LAT"]], sample_weight=0.5)

    def predictTide(self, time):
        return self.tideModel.predict(time)

