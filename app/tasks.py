import requests
import pandas as pd
import numpy as np

from worker import app



@app.task(bind=True, name='fetch_bitcoin_price_index')
def fetch_bitcoin_price_index(self, start_date, end_date):
    url = f'https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}'
    response = requests.get(url)
    if not response.ok:
        raise ValueError(f'Unexpected status code: {response.status_code}')
    return [{'date': key, 'value': value} for key, value in response.json()['bpi'].items()]


@app.task(bind=True, name='calculate_moving_average')
def calculate_moving_average(self, args, window):
    df = pd.DataFrame(args)
    df['ma'] = df['value'].rolling(window=window, center=False).mean()
    return list(df.replace(np.nan, '', regex=True).T.to_dict().values())