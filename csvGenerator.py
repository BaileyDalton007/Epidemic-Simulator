import csv
import pandas as pd

def writeCSV(df):
    df.to_csv('out.csv', index=False)
