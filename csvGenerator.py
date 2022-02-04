import csv
import pandas as pd

def writeCSV(df):
    df.to_csv('SimOutput.csv', index=False)
