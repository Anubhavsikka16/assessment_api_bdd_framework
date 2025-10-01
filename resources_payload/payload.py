def eod_data(symbols):
    end_of_day_data= {
     "symbols": symbols
    }
    return end_of_day_data

def historical_data(symbol, start, end):
    historical_data={
        "symbols": symbol,
        "date_from": start,
        "date_to": end
        
    }
    return historical_data

def tickers_list(limit):
    tickers_list={
        "limit": limit
    }
    return tickers_list