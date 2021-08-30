from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=gpu'

# opening up the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grapping items in the page
containers = page_soup.findAll("div", {"class":"item-container"})
filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name\n"
f.write(headers)

for container in containers:
  title = container.a.img["title"]
  price = container.findAll("li", {"class":"price-current"})[0].text.strip()
  f.write(title.replace(",", "|") + "," + price.replace(",", "") + "\n")

f.close()