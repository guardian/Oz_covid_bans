import pandas as pd
import os
from modules.yachtCharter import yachtCharter

data_path = os.path.dirname(__file__) + "/data/"

ceevee = f"{data_path}inter/countries.csv"

df = pd.read_csv(ceevee, parse_dates=['When'])

df = df.dropna()

df = df.loc[df['Country of acquisition of COVID-19'] != "Total"]

df['Number (%) of cases in the last four'] = df['Number (%) of cases in the last four'].astype(str)
df['Percent'] = df['Number (%) of cases in the last four'].str.extract(r"\((.*?)\)")

df['Percent'] = df['Percent'].str.replace("%", "").str.strip()
# df['Percent'] = df['Percent'].str.strip()

df['Percent'] = pd.to_numeric(df['Percent'])

df['Percent'] = df['Percent']/100

sorted = df.sort_values(by="When", ascending=False)

sorted = sorted[['When', 'Country of acquisition of COVID-19', 'Percent']]
sorted['When'] = sorted['When'].dt.strftime('%Y-%m-%d')

print(sorted['Country of acquisition of COVID-19'].unique())
countries = ['India', 'United Kingdom, Channel Islands and Isle of Man', 'United States of America', 'United Kingdom','USA','United States']

sorted.loc[sorted['Country of acquisition of COVID-19'] == 'United Kingdom, Channel Islands and Isle of Man', 'Country of acquisition of COVID-19'] ='United Kingdom'
sorted.loc[sorted['Country of acquisition of COVID-19'] == 'United States', 'Country of acquisition of COVID-19'] ='United States of America'
sorted.loc[sorted['Country of acquisition of COVID-19'] == 'USA', 'Country of acquisition of COVID-19'] ='United States of America'

sorted = sorted.loc[sorted['Country of acquisition of COVID-19'].isin(countries)]

weeks_preceding = ['2020-11-28', '2020-12-26', '2021-01-30', '2021-02-27', '2021-04-17']
sorted = sorted.loc[sorted['When'].isin(weeks_preceding)]



pivoted = sorted.pivot(index='When', columns='Country of acquisition of COVID-19')['Percent']
# pivoted = df.pivot(index='date',columns='location')
# pivoted.columns.droplevel().rename(None)
pivoted.columns.name = None




# print(pivoted)


def makeSince100Chart(df):

    template = [
            {
                "title": "New South Wales' overseas acquired cases by country of origin",
                "subtitle": f"Percentage of overseas acquired cases in the preceding four weeks",
                "footnote": "",
                "source": "New South Wales Health COVID-19 weekly surveillance reports",
                "dateFormat": "%Y-%m-%d",
                "yScaleType":"",
                "xAxisLabel": "Month",
                "yAxisLabel": "Percentage of overseas acquired cases",
                "minY": "",
                "maxY": "",
                "periodDateFormat":"",
                "margin-left": "100",
                "margin-top": "15",
                "margin-bottom": "20",
                "margin-right": "20",
                "breaks":"no"
            }
        ]
    key = [{"key": "India", "colour":	"#c70000"},
        {"key": "United States of America", "colour":	"#ed6300"},
        {"key": "United Kingdom","colour": "#0084c6"}]
    periods = []
    labels = []
    chartId = [{"type":"linechart"}]
    df.fillna('', inplace=True)
    df = df.reset_index()
    chartData = df.to_dict('records')
    # print(since100.head())
    # print(chartData)
    yachtCharter(template=template, key=key, data=chartData, chartId=[{"type":"groupedbar"}], options=[{"enableShowMore":"1"}], chartName="covid_country_of_acqui")
    # yachtCharter(template=template, data=chartData, chartId=[{"type":"linechart"}], options=[{"colorScheme":colours, "lineLabelling":"FALSE"}], chartName="total_cases_per_m_over_time")


makeSince100Chart(pivoted)

# pivoted = pivoted.reset_index()
# with open(f"{data_path}overseas_source_grouped_bar.csv", "w") as f:
#     pivoted.to_csv(f, index=False, header=True)
