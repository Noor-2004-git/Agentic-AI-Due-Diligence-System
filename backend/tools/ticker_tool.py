import yfinance as yf


def get_ticker(company: str) -> str:
    """
    Resolve a company name or ticker to a valid Yahoo Finance ticker.
    """

    # If the user already entered a ticker like MSFT or TSLA
    if len(company) <= 5 and company.isupper():
        return company

    try:
        search = yf.Search(company, max_results=1)

        if search.quotes:
            return search.quotes[0]["symbol"]

    except Exception:
        pass

    return company.upper()