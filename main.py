import yfinance as yf

data = yf.download(tickers = "YM=F", period = "max", interval = "1m",
        group_by = 'ticker', auto_adjust = True, prepost = True,
        threads = True, proxy = None)

