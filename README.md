# Stock Data Visualization Dashboard

## 1. Problem & User
This dashboard helps individual investors quickly visualize historical stock performance, including price trends, moving averages, and daily return distributions.

## 2. Data
- **Source**: AKShare (open-source financial data interface)
- **Stocks**: Kweichow Moutai (600519), Wuliangye (000858), CATL (300750)
- **Time range**: 2020-01-01 to 2026-04-18
- **Fields**: date, open, close, high, low, volume

## 3. Methods
- **Data cleaning**: date parsing, handling missing values
- **Feature engineering**: daily returns, 5-day/20-day moving averages
- **Visualization**: Plotly interactive charts
- **Web app**: Streamlit for interactive filtering and display

## 4. Key Findings
- CATL shows the highest volatility and highest growth potential.
- Kweichow Moutai has the most stable daily returns.
- All three stocks experienced a significant drawdown in late 2022.

## 5. How to Run
```bash
```
pip install -r requirements.txt
streamlit run app.py

## 6. Links
- **GitHub Repository**: https://github.com/shuyangwang24/acc102-stock-app
- **Demo Video**: [Replace with your video link]

## 7. Limitations & Next Steps
- Only three stocks included. Could expand to more sectors.
- No fundamental analysis. Could add P/E ratio, dividend yield.
