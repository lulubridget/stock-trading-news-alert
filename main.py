import requests
import os

STOCK = "TKO"
COMPANY_NAME = "Tesla Inc"
alphavantage_api_key=os.environ.get("alphavantage_api_key")
newsapi_key=os.environ.get("newsapi_key")
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
paraments = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api_key
}
response = requests.get("https://www.alphavantage.co/query?", params=paraments, verify=False)
response.raise_for_status()
data = response.json()
print(data)
# daily = data["Time Series (Daily)"]
# daily_list = [value for (key,value) in daily.items()]
# yesterday_price = daily_list[0]
# the_day_before_yesterday_price = daily_list[1]
# yesterday_closing_price = yesterday_price['4. close']
# the_day_before_yesterday_closing_price = the_day_before_yesterday_price['4. close']
# result = round(float(yesterday_closing_price) - float(the_day_before_yesterday_closing_price)/float(yesterday_closing_price)*100)
# up_down = None
# if result >0 :
#     up_down = "📈"
# else:
#     up_down = "📉"
# ## STEP 2: Use https://newsapi.org
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# news_paraments = {
#     "q": "TKO Group Holdings",
#     "apiKey": newsapi_key
# }
# if abs(result) > 1:
#     news_response = requests.get("https://newsapi.org/v2/everything?", params=news_paraments, verify=False)
#     news_response.raise_for_status()
#     news_data = news_response.json()
#     three_articles = news_data["articles"][:3]
    
#     formatted_three_articles = [f"{STOCK}: {up_down}{result}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#     print(formatted_three_articles)
## STEP 3: send email
    