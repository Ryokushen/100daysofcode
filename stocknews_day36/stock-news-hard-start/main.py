import requests
import os
from datetime import date, datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEYAPI = os.environ("STOCKAPI")
NEW_KEYAPI = os.environ("NEWSAPI")
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={STOCK_KEYAPI}"

r = requests.get(STOCK_ENDPOINT)
print(r.raise_for_status)
stock_info = r.json()

today = date.today()
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q=Tesla&from={today}&sortBy=popularity&apiKey={NEW_KEYAPI}"


dayofweek = datetime.today().weekday()

daily = stock_info["Time Series (Daily)"]

# Compare closing prices
def comparison(num1, num2):
    if num1 == num2:
        return 100.0
    try:
        return (num1 - num2) / num2 * 100.0
        
    except ZeroDivisionError:
        return 0

def send_message(listofarts, num1, num2, direction):
   
    account_sid = os.environ("TWILIO_SID")
    auth_token = os.environ("TWILIO_AUTH")
    client = Client(account_sid, auth_token)

    for article in listofarts:

        message = client.messages \
                .create(
                     body=f"Tesla:{direction}{round(comparison(num1, num2),2)}%\n\nHeadline: {article['title']}\n\nBrief: {article['description']}",
                     from_='+18147476197',
                     to='+13218908318'
                 )

        print(message.sid)

#Determine whether day of week is weekend or weekday fro search purposes
#Sunday

if dayofweek == 6:
    twodaysago = today - timedelta(days=2)
    threedays = today - timedelta(days=3)
    comp3 = float(daily[str(twodaysago)]['4. close'])
    comp4 = float(daily[str(threedays)]['4. close'])
    if comparison(comp3, comp4) > -5 or comparison(comp3, comp4) < 5:
        if comparison(comp3, comp4) > 0:
            arrow = "🔺"
        else:
            arrow = "🔻"
        g = requests.get(NEWS_ENDPOINT)
        g.raise_for_status
        new_arts = g.json()
        top_articles = new_arts['articles'][:3]
        listofarts = [article for article in top_articles]
        send_message(listofarts, comp3, comp4, arrow)
       

#Monday-Saturday
else:
    yest = today - timedelta(days=1)
    twodaysago = today - timedelta(days=2)
    comp1 = float(daily[str(yest)]['4. close'])
    comp2 = float(daily[str(twodaysago)]['4. close'])
    if comparison(comp1, comp2) > -5 or comparison(comp1, comp2) < 5:
        if comparison(comp1, comp2) > 0:
            arrow = "🔺"
        else:
            arrow = "🔻"
        g = requests.get(NEWS_ENDPOINT)
        g.raise_for_status
        new_arts = g.json()
        top_articles = new_arts['articles'][:3]
        listofarts = [article for article in top_articles]
        send_message(listofarts, comp1, comp2, arrow)




