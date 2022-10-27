import requests
from bs4 import BeautifulSoup as bs4 




def flipkart(product):
    status = 0
    url = product.replace(" ","%20")
    URL = f"https://www.flipkart.com/search?q={url}&sort=recency_desc"
    while True:
        page = requests.get(URL)
        status = page.status_code
        if status ==200:
            break
    soup = bs4(page.content, "html.parser")
    
    name = soup.find('div',attrs={"class":"_4rR01T"})
    if product not in name.text.lower():
        return "Not availabe on Flipkart!"
    item = soup.find_all('div',attrs={ "class":"_30jeq3 _1_WHN1"})
    prices = []
    for i in item:
      prices.append(int(i.text.replace(",","")[1:]))
    return sorted(prices)[0]


def amazon(product):
    url = product.replace("%20","+")
    status = 0
    URL = f"https://www.amazon.in/s?k={url}&rh=p_85%3A10440599031&s=relevanceblender&dc&qid=1666776711&rnid=10440598031&ref=sr_st_relevanceblender&ds=v1%3AeLI3K1M3%2F9ueN78VR6CGtEvIx1vNZA%2F4GaJTMKK9MUg"
    while True:
        page = requests.get(URL)
        status = page.status_code
        if status ==200:
            break
    soup = bs4(page.content, "html.parser")
    name = soup.find('span',attrs={"class":"a-size-medium a-color-base a-text-normal"})
    if product not in name.text.lower():
        return "Not availabe on Amazon!"
    re = soup.find_all('span',attrs={ "class":"a-price-whole"})
    prices = []
    for i in re:
      prices.append(int(i.text.replace(",","")))
    return sorted(prices)[0]

product = input("Enter the name of the smartphone: ") 
print("Price of your product is:\nFlipkart: ",flipkart(product),"\nAmazon: ",amazon(product))
