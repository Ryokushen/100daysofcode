import requests
import os
from datetime import date, datetime, timedelta
from twilio.rest import Client

STOCK = "AMZN"
COMPANY_NAME = "Amazon.com, Inc"
STOCK_KEYAPI = "stock_keyapi"
NEW_KEYAPI = "News_KeyAPI"
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey={STOCK_KEYAPI}"

r = requests.get(STOCK_ENDPOINT)
print(r.raise_for_status)
stock_info = r.json()

today = date.today()
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q=Amazon&from={today}&sortBy=popularity&apiKey={NEW_KEYAPI}"


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
   
    account_sid = 'twilio account sid'
    auth_token = "auth token"
    client = Client(account_sid, auth_token)

    for article in listofarts:

        message = client.messages \
                .create(
                     body=f"Amazon:{direction}{round(comparison(num1, num2),2)}%\n\nHeadline: {article['title']}\n\nBrief: {article['description']}",
                     from_='twilio_number',
                     to='personal_cellphone'
                 )

        print(message.sid)

#Determine whether day of week is weekend or weekday for search purposes

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

#Monday       
elif dayofweek == 0:
    threedaysago = today - timedelta(days=3)
    fourdays = today - timedelta(days=4)
    comp3 = float(daily[str(threedaysago)]['4. close'])
    comp4 = float(daily[str(fourdays)]['4. close'])
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

#Tuesday
elif dayofweek == 1:
    yest = today - timedelta(days=1)
    fourdays = today - timedelta(days=4)
    comp3 = float(daily[str(yest)]['4. close'])
    comp4 = float(daily[str(fourdays)]['4. close'])
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

#Wednesday-Saturday
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




