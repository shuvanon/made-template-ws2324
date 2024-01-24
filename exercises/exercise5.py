import pandas as pd
import urllib.request
import zipfile
from sqlalchemy.types import Integer, String, Float

useCols = ["stop_id","stop_name", "stop_lat", "stop_lon", "zone_id"]
dType = {"stop_id" : int, "stop_name" : str, "stop_lat" : float, "stop_lon" : float, "zone_id" : int}
dTypeOut = {"stop_id" : Integer, "stop_name" : String, "stop_lat" : Float, "stop_lon" : Float, "zone_id" : Integer}

#Download and extract zip file
urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "./exercises/exercise5.zip")
zip = zipfile.ZipFile("./exercises/exercise5.zip")
zip.extractall('./exercises')

#Create df
df = pd.read_csv("./exercises/stops.txt",sep=',', decimal='.', index_col=False, usecols=useCols, dtype=dType, encoding='utf-8')

#Filter
df = df[(df["zone_id"] == 2001)]

#Validate
df = df[(df["stop_lat"] >= -90) & (df["stop_lat"] <= 90) & (df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)]

print(df)

df.to_sql('stops', 'sqlite:///./gtfs.sqlite', if_exists='replace', index=False, dtype=dTypeOut)