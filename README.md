# Product Price Tracker

This application is a web-based tool that allows users to track prices of products from specified e-commerce sites. The app uses a Flask backend and React frontend, with a web scraping mechanism powered by Python and Selenium. The application also provides CORS-enabled API endpoints, allowing smooth communication between the frontend and backend.

## Features

- **Price Tracking**: Track price changes of products by inputting product URLs.
- **Real-time Price Check**: Check the latest price of a product on-demand.
- **Alerts**: Set up alerts to notify users when a product price drops below a specified threshold.
- **API Support**: Exposes an API endpoint to get current prices and product details.
- **Cross-Origin Resource Sharing (CORS)**: Allows secure interaction between frontend and backend.

## Tech Stack

- **Frontend**: React, Axios
- **Backend**: Flask, Flask-CORS
- **Web Scraping**: Python, Selenium

## Setup


### Backend

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd productpricetracker/backend
   
 2.Setup the virtual environment:
    
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

 3.Run the backend:

      python main.py

### Frontend 

1.Navigate to the frontend directory:
      
      cd productpricetracker/frontend
2.Install frontend dependencies:
      
      npm install
3.Run the frontend development server:
      
      npm start
