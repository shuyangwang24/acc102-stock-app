import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📈 Stock Data Visualization Dashboard")

@st.cache_data
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df['日期'] = pd.to_datetime(df['日期'])
    df['Daily Return (%)'] = df['收盘'].pct_change() * 100
    df['MA5'] = df['收盘'].rolling(5).mean()
    df['MA20'] = df['收盘'].rolling(20).mean()
    return df

stock_files = {
    "Kweichow Moutai (600519)": "600519.csv",
    "Wuliangye (000858)": "000858.csv",
    "CATL (300750)": "300750.csv",
}

stock_data = {name: load_data(path) for name, path in stock_files.items()}

st.sidebar.header("Select Stock")
selected_stock = st.sidebar.selectbox("Choose a stock", list(stock_data.keys()))
df = stock_data[selected_stock]

min_date = df['日期'].min().date()
max_date = df['日期'].max().date()
date_range = st.sidebar.date_input(
    "Date Range",
    (min_date, max_date),
    min_value=min_date,
    max_value=max_date
)
if len(date_range) == 2:
    mask = (df['日期'].dt.date >= date_range[0]) & (df['日期'].dt.date <= date_range[1])
    df_filtered = df.loc[mask].copy()
else:
    df_filtered = df.copy()

col1, col2, col3, col4 = st.columns(4)
with col1:
    latest_price = df_filtered['收盘'].iloc[-1]
    st.metric("Latest Close Price", f"{latest_price:.2f}")
with col2:
    period_return = (df_filtered['收盘'].iloc[-1] / df_filtered['收盘'].iloc[0] - 1) * 100
    st.metric("Period Return (%)", f"{period_return:.2f}")
with col3:
    avg_daily_return = df_filtered['Daily Return (%)'].mean()
    st.metric("Avg Daily Return (%)", f"{avg_daily_return:.2f}")
with col4:
    max_daily_loss = df_filtered['Daily Return (%)'].min()
    st.metric("Max Daily Loss (%)", f"{max_daily_loss:.2f}")

st.subheader("Price Trend with Moving Averages")
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_filtered['日期'], y=df_filtered['收盘'], name='Close Price'))
fig.add_trace(go.Scatter(x=df_filtered['日期'], y=df_filtered['MA5'], name='MA5', line=dict(dash='dash')))
fig.add_trace(go.Scatter(x=df_filtered['日期'], y=df_filtered['MA20'], name='MA20', line=dict(dash='dash')))
fig.update_layout(xaxis_title="Date", yaxis_title="Price (CNY)")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Daily Return Distribution")
fig2 = px.histogram(df_filtered, x='Daily Return (%)', nbins=50, title="Histogram of Daily Returns")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Raw Data"):
    st.dataframe(df_filtered.tail(20))