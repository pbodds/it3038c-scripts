import requests, re
from bs4 import BeautifulSoup

url = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
webpage = requests.get(url, headers=agent)

soup = BeautifulSoup(webpage.content, "lxml")


try: 
	title = soup.find("h1", attrs={"class": 'heading-5 v-fw-regular'})
	titleValue = title.string

	
	costDiv = soup.find("div" , attrs={"class": 'priceView-hero-price priceView-customer-price'})
	for cost in costDiv.find_all('span', attrs={"aria-hidden": 'true'}):
		print("Name: %s with a price of %s " % (titleValue, cost.string))
	
	ratingDiv = soup.find("div", attrs={"class": 'c-ratings-reviews flex c-ratings-reviews-small align-items-center gap-50 ugc-ratings-reviews flex-wrap small-gaps text-center'})
	for rating in ratingDiv.find_all("p", attrs={"class": 'visually-hidden'}):
		print(rating.string)
	
		
except AttributeError: 	
	print("Error.")