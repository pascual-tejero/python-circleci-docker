import random

supportedCurrencies = ["EUR", "GBP", "NGN", "USD", "YEN"]

def getAllExchangeRates():
	"""
	Returns exchange rates for all supported currencies
	"""

	rates = {}
	for rate in supportedCurrencies:
		rates[rate] = getExchangeRatesForCurrency(rate)
	return rates

def getExchangeRatesForCurrency(currency):
	"""
	Returns exchange rates for a given currency
	"""

	availableCurrencies = supportedCurrencies.copy()
	availableCurrencies.remove(currency)
	rates = {}
	for rate in availableCurrencies:
		rates[rate] = str(round(random.random(), 2))
	return rates

def getSupportedCurrencies():
	"""
	Returns a list of supported currencies
	"""

	return supportedCurrencies