import pandas

tideDataFrame = pandas.read_csv("IrishNationalTideGaugeNetwork.csv", chunksize= 10000)
