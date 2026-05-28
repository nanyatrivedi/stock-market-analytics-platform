# AI-Powered Stock Market Analytics Platform

An interactive financial analytics platform built using Python, Streamlit, Scikit-learn, and Plotly that provides real-time stock market analysis, technical indicators, portfolio analytics, machine learning-based price prediction, sentiment analysis, and trading strategy backtesting.

## Live Demo

[Launch Live App](https://stock-market-analytics-platform-pgdzimo2unvz4v8v6dvrzs.streamlit.app)
 
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
git clone https://github.com/nanyatrivedi/stock-market-analytics-platform.git
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

---

# Screenshots

## Dashboard Overview

<img src="assets/Screenshot 2026-05-28 at 10.15.26 PM.png" width="100%">

---

## Candlestick Chart

<img src="assets/Screenshot 2026-05-28 at 10.15.35 PM.png" width="100%">

---

## Moving Averages

<img src="assets/Screenshot 2026-05-28 at 10.15.39 PM.png" width="100%">

---

## Technical Indicators

<img src="assets/Screenshot 2026-05-28 at 10.15.45 PM.png" width="100%">

---

## AI Prediction

<img src="assets/Screenshot 2026-05-28 at 10.16.04 PM.png" width="100%">

---

## Portfolio Analytics

<img src="assets/Screenshot 2026-05-28 at 10.16.58 PM.png" width="100%">

---

## Strategy Backtesting

<img src="assets/Screenshot 2026-05-28 at 10.17.08 PM.png" width="100%">

---

## News Sentiment Analysis

<img src="assets/Screenshot 2026-05-28 at 10.17.27 PM.png" width="100%">


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
