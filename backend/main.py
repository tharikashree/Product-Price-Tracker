from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_ADDRESS= os.getenv('SMTP_ADDRESS')

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

app = Flask(__name__)

CORS(app, resources={r"/check-price": {"origins": "http://localhost:3000"}})

@app.route('/check-price',methods=['POST'])
def check_price():
        if request.method == 'OPTIONS':
          return jsonify({'message': 'CORS preflight request successful'}), 200

        data=request.get_json()
        url=data['url']
        expected_price=float(data['expected_price'])
        email = data['email']
        res=requests.get(url,headers=header)

        soup = BeautifulSoup(res.content,"html.parser")
        # print(soup.prettify())
        title = soup.find(id="productTitle").get_text().strip()
        price=soup.find(class_="a-price-whole").get_text().replace(".","")
        current_price=float(price)
        
        if current_price<=expected_price:
            message=f"{title} is selling in the price : ₹{price}"
            print("email")
            with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
                connection.starttls()
                result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL_ADDRESS,
                    to_addrs=email,
                    msg=f"Subject:Amazon Price Alert!\n\n{message}\nLink: {url}".encode("utf-8")
                )
            return jsonify({"status": "success", "message": "Email sent!"})
        else:
            return jsonify({"status": "success", "message": "No price drop detected"})

if __name__ == '__main__':
    app.run(port=5000)