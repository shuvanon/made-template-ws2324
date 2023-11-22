import pandas as pd

class Transformer:
    def __init__(self) -> None:
        pass
    
    def transform_weather_data(self, df = pd.DataFrame):
        # Convert index into a column and reset index
        df = df.reset_index(names=['DATE', 'T2M','T2MDEW','QV2M','PRECTOTCORR','PS','WS10M','WD10M'])
        
        # Convert date column to datetime type
        df['DATE'] = pd.to_datetime(df['DATE'], format="%Y%m%d")
        
        return df
        

    def transform_traffic_data(self, df = pd.DataFrame):
        # Convert date column to datetime type
        df['TATTAG'] = pd.to_datetime(df['TATTAG'], format="%d.%m.%Y")
        
        # Count number of traffic fine occurrences for each unique date
        date_counts = df.groupby('TATTAG')['TATTAG'].count()
        
        df = pd.DataFrame({'DATE':date_counts.index, 'TRAFFIC OFFENCE FREQUENCIES':date_counts.values})
        
        return df
        
    def merge_datasets(self, weather = pd.DataFrame, traffic = pd.DataFrame):
        df = pd.merge(weather, traffic, on='DATE')
        return df.set_index(df.columns[0], drop=True)