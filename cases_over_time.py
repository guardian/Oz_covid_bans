import pandas as pd 
from modules.yachtCharter import yachtCharter
import os 
data_path = os.path.dirname(__file__) + "/data/"

cases = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

df = pd.read_csv(cases)

# print(df)

countries = ["India", "United States", "United Kingdom", "Italy"]

df = df.loc[df['location'].isin(countries)]

df = df[['location', 'date','new_cases_smoothed_per_million', 'total_cases_per_million', 'positive_rate', 'weekly_hosp_admissions_per_million', 'total_deaths_per_million']]

# df = df[['date', 'location','total_cases_per_million' ]]
# pivoted = df.pivot(index='date', columns='location')['total_cases_per_million'].reset_index()

df = df[['date', 'location','new_cases_smoothed_per_million' ]]
pivoted = df.pivot(index='date', columns='location')['new_cases_smoothed_per_million']
# pivoted = df.pivot(index='date',columns='location')
# pivoted.columns.droplevel().rename(None)
pivoted.columns.name = None
# pivoted.index = pivoted['date']

print(pivoted)


def makeSince100Chart(df):
   
    template = [
            {
                "title": "New cases per million",
                "subtitle": f"Seven day rolling average of new cases per million population",
                "footnote": "",
                "source": "Our World in Data",
                "dateFormat": "%Y-%m-%d",
                "yScaleType":"",
                "xAxisLabel": "Date",
                "yAxisLabel": "Cases per million people",
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
    yachtCharter(template=template, data=chartData, chartId=[{"type":"linechart"}], options=[{"colorScheme":"guardian", "lineLabelling":"FALSE"}], chartName="total_cases_per_m_over_time")
    # yachtCharter(template=template, data=chartData, chartId=[{"type":"linechart"}], options=[{"colorScheme":colours, "lineLabelling":"FALSE"}], chartName="total_cases_per_m_over_time")


# makeSince100Chart(pivoted)

pivoted = pivoted.reset_index()
with open(f"{data_path}new_cases_per_m_line.csv", "w") as f:
    pivoted.to_csv(f, index=False, header=True)