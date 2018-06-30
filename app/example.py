import argparse
from tasks import fetch_bitcoin_price_index, calculate_moving_average
from celery import chain


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_date')
    parser.add_argument('--end_date')
    parser.add_argument('--window', default=3)
    args = parser.parse_args()
    task = chain(
        fetch_bitcoin_price_index.s(start_date=args.start_date, end_date=args.end_date),
        calculate_moving_average.s(window=args.window)
    ).delay()
    print(task.id)
