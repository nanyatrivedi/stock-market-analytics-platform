import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

import numpy as np
import plotly.express as px

from textblob import TextBlob
import feedparser

def show_overview():
    current_price = data['Close'].iloc[-1]
    highest_price = data['High'].max()
    lowest_price = data['Low'].min()
    average_volume = data['Volume'].mean()

    data['Daily Return'] = data['Close'].pct_change()

    volatility = data['Daily Return'].std() * 100

    st.subheader(f"{ticker} Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
    "Current Price",
    f"${current_price:.2f}"
    )

    col2.metric(
    "Highest Price",
    f"${highest_price:.2f}"
    )

    col3.metric(
    "Lowest Price",
    f"${lowest_price:.2f}"
    )

    col4.metric(
    "Volatility",
    f"{volatility:.2f}%"
    )

    st.subheader("Latest Stock Data")

    st.dataframe(data.tail())

    st.subheader("Candlestick Chart")

    fig = go.Figure(data=[go.Candlestick(
    x=data[date_column],
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
    )])

    fig.update_layout(
    height=600,
    xaxis_title="Date",
    yaxis_title="Price"
    )

    st.plotly_chart(
    fig,
    use_container_width=True
    )

    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()

    st.subheader("Moving Averages")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
    x=data['Date'],
    y=data['Close'],
    mode='lines',
    name='Closing Price'
    ))

    fig2.add_trace(go.Scatter(
    x=data['Date'],
    y=data['MA50'],
    mode='lines',
    name='50-Day MA'
    ))

    fig2.add_trace(go.Scatter(
    x=data['Date'],
    y=data['MA200'],
    mode='lines',
    name='200-Day MA'
    ))

    fig2.update_layout(
    height=600,
    xaxis_title="Date",
    yaxis_title="Price"
    )

    st.plotly_chart(
    fig2,
    use_container_width=True
    )

def show_technical_indicators():
    rsi_indicator = RSIIndicator(close=data['Close'])

    data['RSI'] = rsi_indicator.rsi()

    st.subheader("RSI Indicator")

    fig_rsi = go.Figure()

    fig_rsi.add_trace(go.Scatter(
        x=data['Date'],
        y=data['RSI'],
        mode='lines',
        name='RSI'
    ))

    fig_rsi.add_hline(
        y=70,
        line_dash="dash",
        annotation_text="Overbought"
    )

    fig_rsi.add_hline(
        y=30,
        line_dash="dash",
        annotation_text="Oversold"
    )

    fig_rsi.update_layout(
        height=400,
        yaxis_title="RSI"
    )

    st.plotly_chart(
        fig_rsi,
        use_container_width=True
    )

    macd = MACD(close=data['Close'])

    data['MACD'] = macd.macd()
    data['MACD_SIGNAL'] = macd.macd_signal()

    st.subheader("MACD")

    fig_macd = go.Figure()

    fig_macd.add_trace(go.Scatter(
        x=data['Date'],
        y=data['MACD'],
        mode='lines',
        name='MACD'
    ))

    fig_macd.add_trace(go.Scatter(
        x=data['Date'],
        y=data['MACD_SIGNAL'],
        mode='lines',
        name='Signal Line'
    ))

    fig_macd.update_layout(
        height=400
    )

    st.plotly_chart(
        fig_macd,
        use_container_width=True
    )

    bollinger = BollingerBands(close=data['Close'])

    data['BB_HIGH'] = bollinger.bollinger_hband()
    data['BB_LOW'] = bollinger.bollinger_lband()

    st.subheader("Bollinger Bands")

    fig_bb = go.Figure()

    fig_bb.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        mode='lines',
        name='Closing Price'
    ))

    fig_bb.add_trace(go.Scatter(
        x=data['Date'],
        y=data['BB_HIGH'],
        mode='lines',
        name='Upper Band'
    ))

    fig_bb.add_trace(go.Scatter(
        x=data['Date'],
        y=data['BB_LOW'],
        mode='lines',
        name='Lower Band'
    ))

    fig_bb.update_layout(
        height=500
    )

    st.plotly_chart(
        fig_bb,
        use_container_width=True
    )

    st.subheader("Daily Returns")

    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Daily Return'],
        mode='lines',
        name='Daily Return'
    ))

    fig3.update_layout(
        height=500,
        xaxis_title="Date",
        yaxis_title="Return"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.subheader("Trading Volume")

    fig4 = go.Figure()

    fig4.add_trace(go.Bar(
        x=data[date_column],
        y=data['Volume'],
        name='Volume'
    ))

    fig4.update_layout(
        height=500,
        xaxis_title="Date",
        yaxis_title="Volume"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

def show_ai_prediction():
    st.subheader("AI Stock Price Prediction")

    data['Prediction'] = data['Close'].shift(-1)

    X = data[['Close']]
    y = data['Prediction']

    X = X[:-1]
    y = y[:-1]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    st.write(f"Mean Absolute Error: {mae:.2f}")


    latest_close = data[['Close']].iloc[[-1]]

    next_day_prediction = model.predict(latest_close)

    st.metric(
        "Predicted Next Day Closing Price",
        f"${next_day_prediction[0]:.2f}"
    )

    prediction_df = pd.DataFrame({
        'Actual': y_test.values,
        'Predicted': predictions
    })

    fig_pred = go.Figure()

    fig_pred.add_trace(go.Scatter(
        y=prediction_df['Actual'],
        mode='lines',
        name='Actual Price'
    ))

    fig_pred.add_trace(go.Scatter(
        y=prediction_df['Predicted'],
        mode='lines',
        name='Predicted Price'
    ))

    fig_pred.update_layout(
        height=500,
        title="Actual vs Predicted Prices"
    )

    st.plotly_chart(
        fig_pred,
        use_container_width=True
    )

def show_portfolio():
    st.header("Portfolio Analytics")

    portfolio_stocks = st.multiselect(
        "Select Stocks for Portfolio",
        ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'NVDA', 'AMZN'],
        default=['AAPL', 'MSFT']
    )

    if len(portfolio_stocks) > 0:

        portfolio_data = yf.download(
            portfolio_stocks,
            start=start_date,
            end=end_date
        )['Close']

        portfolio_returns = portfolio_data.pct_change()

        cumulative_returns = (
            1 + portfolio_returns
        ).cumprod()

        st.subheader("Portfolio Performance")

        fig_portfolio = go.Figure()

        for stock in cumulative_returns.columns:

            fig_portfolio.add_trace(go.Scatter(
                x=cumulative_returns.index,
                y=cumulative_returns[stock],
                mode='lines',
                name=stock
            ))

        fig_portfolio.update_layout(
            height=500,
            xaxis_title="Date",
            yaxis_title="Cumulative Return"
        )

        st.plotly_chart(
            fig_portfolio,
            use_container_width=True
        )

        st.subheader("Stock Correlation Heatmap")

        correlation = portfolio_returns.corr()

        fig_corr = px.imshow(
            correlation,
            text_auto=True,
            aspect="auto",
            title="Correlation Matrix"
        )

        st.plotly_chart(
            fig_corr,
            use_container_width=True
        )

        st.subheader("Portfolio Risk Metrics")

        portfolio_volatility = (
            portfolio_returns.std().mean() * 100
        )

        average_return = (
            portfolio_returns.mean().mean() * 100
        )

        sharpe_ratio = (
            average_return / portfolio_volatility
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Return",
            f"{average_return:.2f}%"
        )

        col2.metric(
            "Portfolio Volatility",
            f"{portfolio_volatility:.2f}%"
        )

        col3.metric(
            "Sharpe Ratio",
            f"{sharpe_ratio:.2f}"
        )

    st.header("Strategy Backtesting")

    st.subheader("Moving Average Crossover Strategy")

    data['Signal'] = 0

    data.loc[
        data['MA50'] > data['MA200'],
        'Signal'
    ] = 1

    data.loc[
        data['MA50'] < data['MA200'],
        'Signal'
    ] = -1

    data['Market Return'] = data['Close'].pct_change()

    data['Strategy Return'] = (
        data['Signal'].shift(1) *
        data['Market Return']
    )

    data['Cumulative Market Return'] = (
        1 + data['Market Return']
    ).cumprod()

    data['Cumulative Strategy Return'] = (
        1 + data['Strategy Return']
    ).cumprod()

    fig_strategy = go.Figure()

    fig_strategy.add_trace(go.Scatter(
        x=data[date_column],
        y=data['Cumulative Market Return'],
        mode='lines',
        name='Buy & Hold'
    ))

    fig_strategy.add_trace(go.Scatter(
        x=data[date_column],
        y=data['Cumulative Strategy Return'],
        mode='lines',
        name='Strategy Return'
    ))

    fig_strategy.update_layout(
        height=500,
        xaxis_title="Date",
        yaxis_title="Cumulative Return"
    )

    st.plotly_chart(
        fig_strategy,
        use_container_width=True
    )

    strategy_return = (
        data['Cumulative Strategy Return'].iloc[-1] - 1
    ) * 100

    market_return = (
        data['Cumulative Market Return'].iloc[-1] - 1
    ) * 100

    col1, col2 = st.columns(2)

    col1.metric(
        "Strategy Return",
        f"{strategy_return:.2f}%"
    )

    col2.metric(
        "Buy & Hold Return",
        f"{market_return:.2f}%"
    )

    st.subheader("Buy & Sell Signals")

    buy_signals = data[data['Signal'] == 1]

    sell_signals = data[data['Signal'] == -1]

    fig_signals = go.Figure()

    fig_signals.add_trace(go.Scatter(
        x=data[date_column],
        y=data['Close'],
        mode='lines',
        name='Closing Price'
    ))

    fig_signals.add_trace(go.Scatter(
        x=buy_signals['Date'],
        y=buy_signals['Close'],
        mode='markers',
        name='Buy Signal',
        marker=dict(size=10)
    ))

    fig_signals.add_trace(go.Scatter(
        x=sell_signals['Date'],
        y=sell_signals['Close'],
        mode='markers',
        name='Sell Signal',
        marker=dict(size=10)
    ))

    fig_signals.update_layout(
        height=600
    )

    st.plotly_chart(
        fig_signals,
        use_container_width=True
    )

def show_news_sentiment():
    st.header("News Sentiment Analysis")

    rss_url = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"

    feed = feedparser.parse(rss_url)

    news_items = feed.entries[:10]

    sentiments = []

    for item in news_items:

        title = item.title

        sentiment_score = TextBlob(title).sentiment.polarity

        sentiments.append(sentiment_score)

        if sentiment_score > 0:
            label = "Positive"

        elif sentiment_score < 0:
            label = "Negative"

        else:
            label = "Neutral"

        st.write(f"### {title}")
        st.write(f"Sentiment: {label}")
        st.write("---")

    average_sentiment = np.mean(sentiments)

    if average_sentiment > 0:
        overall_sentiment = "Overall Positive"

    elif average_sentiment < 0:
        overall_sentiment = "Overall Negative"

    else:
        overall_sentiment = "Overall Neutral"

    st.subheader(overall_sentiment)

    fig_sentiment = go.Figure()

    fig_sentiment.add_trace(go.Bar(
        x=[f"News {i+1}" for i in range(len(sentiments))],
        y=sentiments,
        name='Sentiment Score'
    ))

    fig_sentiment.update_layout(
        height=400,
        yaxis_title="Sentiment Score"
    )

    st.plotly_chart(
        fig_sentiment,
        use_container_width=True
    )

st.set_page_config(
    page_title="Stock Market Dashboard",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}
            
section[data-testid="stSidebar"] {
    background-color: #161A23;
}

div[data-testid="metric-container"] {
    background-color: #1E2530;
    border: 1px solid #2E3748;
    padding: 15px;
    border-radius: 12px;
}

button[data-baseweb="tab"] {
    font-size: 16px;
    margin-right: 10px;
}

h1, h2, h3 {
    color: white;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; 
color: white;
font-size: 48px;'>
AI-Powered Stock Market Analytics Platform
</h1>
""", unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Technical Indicators",
    "AI Prediction",
    "Portfolio",
    "News Sentiment"
])

st.sidebar.markdown("""
# Dashboard Controls
Customize your analytics dashboard
""")

ticker = st.sidebar.text_input(
    "Enter Stock Ticker",
    "AAPL"
)

start_date = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2023-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("today")
)

with st.spinner("Loading market data..."):

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

if data.empty:
    st.error("No stock data found. Please try another ticker.")
    st.stop()

data.reset_index(inplace=True)
date_column = data.columns[0]

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

with tab1:
    show_overview()

with tab2: 
    show_technical_indicators()
with tab3:
    show_ai_prediction()

with tab4:
    show_portfolio()

with tab5:
    show_news_sentiment()