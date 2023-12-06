import pandas as pd
import string
from sqlalchemy.types import Integer, String, Float
import numpy as np

def excelToInt(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num - 1

useColumsNames = [
    'date',
    'CIN',
    'name',
    'petrol',
    'diesel',
    'gas',
    'electro',
    'hybrid',
    'plugInHybrid',
    'others'
]

columnTypes = {
    'date': str, 
    'CIN': str,
    'name': str
    }

columnTypesOut = {'date': String, 
    'CIN': String,
    'name': String,
    'petrol': Integer,
    'diesel': Integer,
    'gas': Integer,
    'electro': Integer,
    'hybrid': Integer,
    'plugInHybrid': Integer,
    'others': Integer, 
    }

def main():
    #read and drop first 6 rows
    df = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv", 
                     sep=";", 
                     encoding='latin1', 
                     skiprows=6, skipfooter=4,
                     engine="python", 
                     usecols=[excelToInt('A'),
                              excelToInt('B'),
                              excelToInt('C'),
                              excelToInt('M'),
                              excelToInt('W'),
                              excelToInt('AG'),
                              excelToInt('AQ'),
                              excelToInt('BA'),
                              excelToInt('BK'),
                              excelToInt('BU')], 
                     names=useColumsNames, 
                     dtype=columnTypesOut)
    

    #filter CIN
    df = df[df['CIN'].str.len() == 5]
    
    #filter for positive integer
    numeric_columns = ["petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    
    df.dropna()
    
    df.to_sql('cars', 'sqlite:///./cars.sqlite', if_exists='replace', index=False, dtype=columnTypesOut)
    
if __name__ == "__main__":
    main()