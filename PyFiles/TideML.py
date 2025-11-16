import pandas as pd
import sklearn.linear_model

class tideML:
    def __init__(self):
        self.tideDataFrame = pd.read_csv("IrishNationalTideGaugeNetwork.csv")

        self.tideDataFrame.drop(["latitude","longitude","altitude","Water_Level_OD_Malin","station_id","QC_Flag","datasourceid"], axis=1, inplace = True)

        self.tideModel = sklearn.linear_model.LinearRegression()
        self.tideModel.fit(self.tideDataFrame[2:,["time"]],self.tideDataFrame[2:,["Water_Level_LAT"]], sample_weight=0.05)

    def predictTide(self, time):
        return self.tideModel.predict(time)

