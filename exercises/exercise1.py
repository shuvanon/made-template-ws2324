import pandas as pd
from sqlalchemy import String, TEXT, BIGINT, Float, DECIMAL

data_path = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'

#loading data
data_table = pd.read_csv(data_path, sep=";", on_bad_lines='skip')

#changing column types
# column_types = {'column_1': BIGINT, 'column_2': TEXT, 'column_3': TEXT, 'column_4': TEXT, 'column_5': TEXT,
#                'column_6': TEXT, 'column_7': Float,'column_8': Float, 'column_9': BIGINT, 'column_10': Float,
#                'column_11': TEXT,'column_12': TEXT, 'geo_punkt': DECIMAL}

#saving table to sqlite file
data_table.to_sql('airports','sqlite:///airports.sqlite', if_exists='replace', index=False)