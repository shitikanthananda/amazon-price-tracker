import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

MY_EMAIL = "udemyshitikanthapython@gmail.com"
PASSWORD = "ijdkawaabzslthyw"
PRODUCT_URL = "https://www.amazon.in/gp/product/B0BDJKL7KY/ref=s9_acss_bw_cg_Babel_1d1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=KH9M2A07070Y50KWHZND&pf_rd_t=101&pf_rd_p=cf29e933-540a-4495-a34f-591e76201f0f&pf_rd_i=78382736031&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,or;q=0.6"
}

response = requests.get(PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

item = soup.find(name="span", class_="a-price-whole").get_text()
item_name = soup.find(name="span", class_="a-size-large product-title-word-break").get_text().strip()
item_price = (item.split(".")[0].split(","))
current_price = "".join(item_price)
# print(current_price)
# print(item_name)

BUY_PRICE = 100000

if int(current_price) < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="nshitikantha@gmail.com",
                            msg=f"Subject:Price Drop Alert!!\n\n{item_name} is now  ₹{current_price}.\n{PRODUCT_URL}".encode("utf-8"))
