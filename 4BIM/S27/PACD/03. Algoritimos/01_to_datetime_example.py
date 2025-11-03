import pandas as pd

def exemplo_to_datetime():
    dates = pd.to_datetime(['2024-06-02', '2024-06-03'])
    print(dates)

if __name__ == '__main__':
    exemplo_to_datetime()