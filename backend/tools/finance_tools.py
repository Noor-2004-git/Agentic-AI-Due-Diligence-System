import yfinance as yf


def get_financial_data(company: str) -> str:
    """
    Fetch basic financial information about a company.
    """

    ticker = yf.Ticker(company)

    info = ticker.info

    return f"""
Company: {info.get('longName', 'N/A')}

Current Price: {info.get('currentPrice', 'N/A')}

Market Cap: {info.get('marketCap', 'N/A')}

PE Ratio: {info.get('trailingPE', 'N/A')}

Revenue: {info.get('totalRevenue', 'N/A')}

Net Income: {info.get('netIncomeToCommon', 'N/A')}

Industry: {info.get('industry', 'N/A')}
"""