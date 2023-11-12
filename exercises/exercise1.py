import pandas as pd
from sqlalchemy import INTEGER, String, Float, CHAR

data_path = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'

#loading data
data_table = pd.read_csv(data_path, sep=";", on_bad_lines='skip')

#changing column types
column_types = {'column_1': INTEGER, 'column_2': String, 'column_3': String, 'column_4': String, 'column_5': String,
               'column_6': String, 'column_7': Float,'column_8': Float, 'column_9': INTEGER, 'column_10': Float,
               'column_11': CHAR,'column_12': String, 'geo_punkt': String}

#saving table to sqlite file
data_table.to_sql('airports','sqlite:///airports.sqlite', if_exists='replace', index=False, dtype=column_types)