# AI-Powered Stock Market Analytics Platform

An interactive financial analytics platform built using Python, Streamlit, Scikit-learn, and Plotly that provides real-time stock market analysis, technical indicators, portfolio analytics, machine learning-based price prediction, sentiment analysis, and trading strategy backtesting.

## Live Demo

https://stock-market-analytics-platform-pgdzimo2unvz4v8v6dvrzs.streamlit.app


---

# Features

## Stock Market Dashboard

* Real-time stock data visualization
* Candlestick charts
* Moving averages (50-Day & 200-Day)
* Daily returns analysis
* Trading volume analysis
* Volatility metrics

## Technical Indicators

* RSI (Relative Strength Index)
* MACD (Moving Average Convergence Divergence)
* Bollinger Bands

## AI Stock Prediction

* Machine Learning-based stock price prediction
* Linear Regression forecasting
* Mean Absolute Error (MAE) evaluation
* Actual vs Predicted price visualization

## Portfolio Analytics

* Multi-stock portfolio comparison
* Correlation heatmaps
* Cumulative returns analysis
* Sharpe Ratio calculation
* Portfolio volatility analysis

## News Sentiment Analysis

* Financial news aggregation
* NLP-based sentiment analysis using TextBlob
* Positive/Negative/Neutral sentiment classification
* Market sentiment visualization

## Strategy Backtesting

* Moving Average Crossover Strategy
* Buy/Sell signal generation
* Strategy vs Buy-and-Hold performance comparison

---

# Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Scikit-learn

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Financial Data & Analytics

* yFinance
* Technical Analysis (TA)

### NLP & Sentiment Analysis

* TextBlob
* Feedparser

### Deployment & Tools

* Streamlit
* Git
* GitHub
* Streamlit Community Cloud

---

# Project Structure

```bash
stock-market-analysis/
│
├── app/
│   ├── dashboard.py
│   └── main.py
│
├── data/
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/your-username/stock-market-analytics-platform.git
```

## Navigate to Project Folder

```bash
cd stock-market-analytics-platform
```

## Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app/dashboard.py
```

---

# Future Improvements

* XGBoost & LSTM-based forecasting
* FinBERT sentiment analysis
* User authentication & watchlists
* Real-time alerts
* Database integration
* Portfolio optimization algorithms

---

# Author

Mananya Trivedi

Built as a portfolio project for Data Science, Analytics, and FinTech internship opportunities.
