import pandas as pd
import streamlit as st

from plotly import graph_objects as go
from datetime import datetime, timedelta

MAPPING = {
    'Market Monitor Only': 'mm_only.csv',
    'SPY Only': 'spy_only.csv',
    'Market Monitor & SPY': 'mm_and_spy.csv'
}

st.set_page_config(layout="wide")

model = st.sidebar.selectbox(
    label='Model Features From',
    options=[
        'Market Monitor Only',
        'SPY Only',
        'Market Monitor & SPY',
    ]
)

# Load in the data for the dash
df = pd.read_csv('data/' + MAPPING[model])
df['Date'] = pd.to_datetime(df['Date'])

upper_date = st.sidebar.date_input(
    label='Upper Date',
    value=df['Date'].max(),
    max_value=df['Date'].max(),
    min_value=df['Date'].min(),
)

lower_date = st.sidebar.date_input(
    label='Lower Date',
    value=datetime.now() - timedelta(days=2*365),
    min_value=df['Date'].min(),
    max_value=df['Date'].max()
)

trend_thresh = st.sidebar.slider(
    label='Trend Probability',
    value=0.5,
    min_value=0.0,
    max_value=0.99,    
)

highlight_color = st.sidebar.selectbox(
    label='Trend Highlight Color',
    options=['yellow', 'red', 'blue', 'green', 'orange'],    
)

highlight_opacity = st.sidebar.slider(
    label='Highlight Opacity',
    value=0.1,
    min_value=0.0,
    max_value=0.99,    
)

df = df[
    (df['Date'] <= pd.to_datetime(upper_date))
    & (df['Date'] >= pd.to_datetime(lower_date))      
]

df = df.reset_index(drop=True)

st.title('SPY Trend Prediction')
st.write('Data last refreshed: ' + df['Date'].max().strftime('%Y-%m-%d'))
st.write('Uptrend probability for tomorrow: ' + str(df['trend_pred'].round(2).values[-1]))

fig = go.Figure()

fig.add_trace(
    go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        showlegend=False,
    )   
)

# Create the threshold column, so that we can see the effect of changing
# the model "surety" - this is needed to generate the highlighted regions
df['threshold'] = df['trend_pred'] >= float(trend_thresh)

# Find the intervals where the model has detected the pattern
df_pattern = (
    df[df['threshold']]
    .groupby((~df['threshold']).cumsum())
    ['Date']
    .agg(['first', 'last'])
)

# For each interval, plot as a highlighted section
for idx, row in df_pattern.iterrows():
    fig.add_vrect(
        x0=row['first'], 
        x1=row['last'],
        line_width=0,
        fillcolor=highlight_color,
        opacity=highlight_opacity,
    )

# # Add the box overlays for the treding threshold
# ranges = []
# start_date = None

# for idx, row in df.iterrows():
#     if row['trend_pred'] >= trend_thresh:
#         if start_date is None:
#             start_date = row['Date']
#     elif start_date is not None:
#         end_date = row['Date']
#         ranges.append((start_date, end_date))
#         start_date = None

# for start_date, end_date in ranges:
#     fig.add_vrect(
#         x0=start_date,  
#         x1=end_date,    
#         fillcolor=highlight_color,
#         line_width=0,
#         opacity=highlight_opacity,
#     )

fig.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title="Date",
    yaxis_title="SPY Price ($)",
    width=1200,
    height=700,
)

st.plotly_chart(fig)

expander = st.expander('About this dash')
expander.write('''
    This dash is cool AF
''')