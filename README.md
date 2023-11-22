# Market Monitor Trend Dashboard

This repository holds the code, and input files required for the interactive Market Monitor trend dashboard - hosted by streamlit.

Inside this ReadME:
1. What this dashboard is
2. When the data is refreshed
3. How to use the dashboard
4. Disclaimer
5. Contact

## What this dashboard is

In short, this dashboard shows a chart of the SPY, and highlights regions where a [Random Forest](https://en.wikipedia.org/wiki/Random_forest) machine learning model predicts that there is a uptrend/downtrend tomorrow, based on features from:
1. The [Market Montior](https://stockbee.blogspot.com/p/mm.html), by Pradeep Bonde (aka Stockbee).
2. Basic technicals from the SPY (e.g. distances from moving averages, changes in the daily range)

The dashboard, and the results contained within the data files, are intended to demonstrate one method in which machine learning can be used on financial data.

⚠️ **This dashboard should not be used to make any financial decisions from - read the disclaimer in the ReadME before using the dashboard** ⚠️

## When the data is refreshed

The TL;DR - the dashboard inputs should be updated once per day, at 8am GMT. **Please refresh the dashboard daily - and check the GitHub repository if you are not sure when the files were last updated**.

The date of the data will appear "lagged" in the dashboard, this is due to the data being refreshed from the last full trading day. Likewise, the [Market Montior](https://stockbee.blogspot.com/p/mm.html) is also refreshed on a daily cadence, and therefore, the model cannot be updated until the [Market Montior](https://stockbee.blogspot.com/p/mm.html) does. **To be clear, this data does not update during the trading day** - this is a completely free dashboard, changing it to a dynamically changing dashboard would take time and finance to develop and maintain it.

## How to use the dasboard

### Different Models
The dashboard includes the usage of 3 different models.
1. Input features from the [Market Montior](https://stockbee.blogspot.com/p/mm.html) only.
2. Input features from the SPY technicals only.
3. Input features from both.

The above can be controlled via the selectbox on the sidebar of the dashboard.

In all cases, the target variable (e.g., what the model is aiming to predict) remains fixed, the only changes are the feature inputs.

### Trend Probability
Models such as a [Random Forest](https://en.wikipedia.org/wiki/Random_forest) have the ability to spit out *probabilities* - this term should be used loosely since the model is not measuring any probabilistic outputs, but the term can be used for convenience in description. It is found by using the `model.predict_proba` function on any sklearn model.

In essence, the model output is a continuous number, between 0 and 1, which indicates how "sure" the model is of the target variable. For instance, 0.9 means the model is quite sure tomorrow will be an uptrend - 0.1 means it's quite sure tomorrow will be a downtrend.

This can be adjusted via the slider bar to make the model more stringent of the results - the dashboard will update in accordance to this.

### Date Ranges
The potting date ranges can also be controlled from the date select boxees in the sidebar.

**Please note that the models were all trained on data up until 2021 - so it is unfair to judge the model performance on data before this time**. Therefore, the date select will only go back to 2021.

The [Market Montior](https://stockbee.blogspot.com/p/mm.html) data has all columns that are non-empty from 2016 onwards - so it is impossible to see anything further back from then. Even if this is requested, the training requires at least 5+ years to uncover generic rules to predict the target variable.

At request, I can make a separate model based on the SPY only, which has a cut-off training date further back in time (e.g. 2015).

### Plotting Controls

There have been two simple controls introduced - highlight colour, and the trend opacity. Please adjust to suit your best viewing.

## Disclaimer

Please note that the author of the dashboard is not a professional investor or trader, all content produced by the author is based solely on the authors’ own opinions and experiences.

None of the content produced by the author is intended to be financial advice. Any content made and/or published by the author is purely intended for information and/or education purposes only. You should not base any of your investment/trading/financial decisions on the information or content provided the author. The author cannot confirm the accuracy of any of the information or content produced.

The content written by the author are based on their own opinions, formed through their own personal research and testing – therefore, any information, code or otherwise, should be used at the discretion and risk of the content consumer.

Accordingly, the author makes no representation or warranty, either express or implied, in relation to the accuracy or reliability or completeness of the information or content or code published by the author. The author shall not have any liability whatsoever in respect of any direct, indirect or consequential loss or damage arising from your use of the content. 

All content produced by author is intended as generic information about the financial markets and no content should be construed as an endorsement or recommendation about a particular investment.

## Contact

If you have any further questions - please contact the author on [X](https://twitter.com/DrDanobi).




