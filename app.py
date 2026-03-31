import streamlit as st
from prompts import *
from utils import get_response

st.set_page_config(page_title="AI Stock Research", layout="wide")

st.title("📈 AI Stock Research Assistant")

if st.button("Run Analysis"):

    with st.spinner("Fetching Global News..."):
        global_news = get_response(GLOBAL_NEWS_PROMPT)

    st.subheader("🌍 Global News")
    st.write(global_news)

    with st.spinner("Fetching India News..."):
        india_news = get_response(INDIA_NEWS_PROMPT)

    st.subheader("🇮🇳 India News")
    st.write(india_news)

    with st.spinner("Analyzing Sectors..."):
        sector_prompt = SECTOR_PROMPT.format(
            global_news=global_news,
            india_news=india_news
        )
        sectors = get_response(sector_prompt)

    st.subheader("🏭 Sector Impact")
    st.write(sectors)

    with st.spinner("Finding Stocks..."):
        stock_prompt = STOCK_PROMPT.format(sectors=sectors)
        stocks = get_response(stock_prompt)

    st.subheader("📊 Stocks in Discussion")
    st.write(stocks)

    with st.spinner("Detecting Momentum..."):
        momentum_prompt = MOMENTUM_PROMPT.format(stocks=stocks)
        momentum = get_response(momentum_prompt)

    st.subheader("🚀 Momentum Stocks")
    st.write(momentum)

    with st.spinner("Building Portfolio..."):
        portfolio_prompt = PORTFOLIO_PROMPT.format(momentum=momentum)
        portfolio = get_response(portfolio_prompt)

    st.subheader("💼 Suggested Portfolio")
    st.write(portfolio)
