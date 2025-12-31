import yfinance as yf    
import pandas as pd    
import matplotlib.pyplot as plt    

stock = "TSLA"    
period = "30d"    

data = yf.download(stock, period=period)    

print("Stock data preview:")    
print(data.head())    

data["MA_10"] = data["Close"].rolling(10).mean()    
data["MA_20"] = data["Close"].rolling(20).mean()    
data = data.dropna()    

if data.empty:    
    print("Not enough data to calculate moving averages.")    
else:    
    highest = data["Close"].max()    
    lowest = data["Close"].min()    
    average = data["Close"].mean()    

    print("\nPrice Summary:")    
    print("Highest:", round(highest, 2))    
    print("Lowest:", round(lowest, 2))    
    print("Average:", round(average, 2))    

    next_day = data["MA_10"].iloc[-1]    
    print("\nApproximate next day price:", round(next_day, 2))    

    if data["MA_10"].iloc[-1] > data["MA_20"].iloc[-1]:    
        print("Trend: Stock going upward")    
    else:    
        print("Trend: Stock going downward")    

    data.to_csv("tesla_stock_data.csv")    
    print("\nStock data saved as tesla_stock_data.csv")    

    plt.figure(figsize=(12, 6))    
    plt.plot(data["Close"], label="Closing Price", color="blue")    
    plt.plot(data["MA_10"], label="10 Day Moving Average", color="red")    
    plt.plot(data["MA_20"], label="20 Day Moving Average", color="green")    
    plt.title("Tesla Stock Price Analysis (Last 30 Days)")    
    plt.xlabel("Date")    
    plt.ylabel("Price (USD)")    
    plt.legend()    
    plt.grid(True)    
    plt.show()