import requests


def get_last_traded_price(stock):
    print(stock)
    try:
        # NSE
        url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}.NS?modules=summaryDetail".format(stock)
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        return response.json()["quoteSummary"]["result"][0]["summaryDetail"]["previousClose"]["raw"]
    except:
        # BSE
        url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{}.BO?modules=summaryDetail".format(stock)
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        return response.json()["quoteSummary"]["result"][0]["summaryDetail"]["previousClose"]["raw"]

