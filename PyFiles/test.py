import pandas

tideDataFrame = pandas.read_csv("IrishNationalTideGaugeNetwork.csv", chunksize= 10000, usecols= [1,7])
tideDataFrame