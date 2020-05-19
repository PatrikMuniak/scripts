import time
import pandas as pd

sp500 = pd.read_csv('constituents_csv.csv')

for row in sp500['Name']:
    print('\n'*40)
    print(row)
    time.sleep(0.5)
