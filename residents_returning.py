import pandas as pd 
import os 
from modules.yachtCharter import yachtCharter

data_path = os.path.dirname(__file__) + "/data/"

excel = f"{data_path}inter/340109.xls"

old_df = pd.read_excel(excel, sheet_name="Data1")
# df = pd.read_excel(r'/Users/josh_nicholas/github/Oz_covid_bans/data/340109.xls')

old_df = old_df[['Unnamed: 0','Number of movements ; UK, CIs & IOM ;  Short-term Residents returning ;','Number of movements ; India ;  Short-term Residents returning ;','Number of movements ; China ;  Short-term Residents returning ;','Number of movements ; United States of America ;  Short-term Residents returning ;',]]

old_df.columns = ["Date", "United Kingdom", "India", "China", "United States"]



old_df = old_df[11:]

old_df['Date'] = pd.to_datetime(old_df['Date'])

## Work out for line chart

df = old_df.loc[old_df['Date']>"2020-03-01"]

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

df.index = df['Date']
df = df.drop(columns='Date')

def makeSince100Chart(df):
   
    template = [
            {
                "title": "Residents returning by country",
                "subtitle": f"",
                "footnote": "",
                "source": "Australian Bureau of Statistics",
                "dateFormat": "%Y-%m-%d",
                "yScaleType":"",
                "xAxisLabel": "Date",
                "yAxisLabel": "Number of residents",
                "minY": "",
                "maxY": "",
                "periodDateFormat":"",
                "margin-left": "50",
                "margin-top": "15",
                "margin-bottom": "20",
                "margin-right": "20",
                "breaks":"no"
            }
        ]
    key = []
    periods = []
    labels = []
    chartId = [{"type":"linechart"}]
    df.fillna('', inplace=True)
    df = df.reset_index()
    chartData = df.to_dict('records')
    # print(since100.head())
    # print(chartData)
    yachtCharter(template=template, data=chartData, chartId=[{"type":"linechart"}], options=[{"colorScheme":"guardian", "lineLabelling":"FALSE"}], chartName="oz_residents_returning")
    # yachtCharter(template=template, data=chartData, chartId=[{"type":"linechart"}], options=[{"colorScheme":colours, "lineLabelling":"FALSE"}], chartName="total_cases_per_m_over_time")


# makeSince100Chart(df)

print(df)

df = df.reset_index()
with open(f"{data_path}residents_returning.csv", "w") as f:
    df.to_csv(f, index=False, header=True)