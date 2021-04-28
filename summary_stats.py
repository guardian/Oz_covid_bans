import pandas as pd 
import os 

data_path = os.path.dirname(__file__) + "/data/"


# Work out max new covid cases

cases = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'

df = pd.read_csv(cases)

df = df[['location', 'date','new_cases_per_million', 'total_cases_per_million', 'positive_rate', 'weekly_hosp_admissions_per_million', 'total_deaths_per_million']]

# df = df.drop_duplicates(subset=['location'], keep='last')

listo = []

for country in df['location'].unique().tolist():
    inter = df.loc[df['location'] == country]
    maxer = inter.loc[inter['new_cases_per_million'] == inter['new_cases_per_million'].max()]
    maxer = maxer.drop_duplicates(subset=['location'], keep='last')
    listo.append(maxer)


df = pd.concat(listo)


df = df[['location', 'date','new_cases_per_million']]
df['Rank'] = df['new_cases_per_million'].rank(ascending=False)

sorted = df.sort_values(by='Rank', ascending=True)
print(sorted.head(100))

# print(df.loc[df['location'].isin(countries)])



# print(df)

# print(df)

# countries = ["India", "United States", "United Kingdom", "Italy", 'China']

# df = df.loc[df['location'].isin(countries)]

# df = df[['location', 'date','new_cases_smoothed_per_million', 'total_cases_per_million', 'positive_rate', 'weekly_hosp_admissions_per_million', 'total_deaths_per_million']]

# # df = df[['date', 'location','total_cases_per_million' ]]
# # pivoted = df.pivot(index='date', columns='location')['total_cases_per_million'].reset_index()

# df = df[['date', 'location','new_cases_smoothed_per_million' ]]
# pivoted = df.pivot(index='date', columns='location')['new_cases_smoothed_per_million']
# # pivoted = df.pivot(index='date',columns='location')
# # pivoted.columns.droplevel().rename(None)
# pivoted.columns.name = None
# # pivoted.index = pivoted['date']

# print(pivoted)





## Work out returning residents

new_df = pd.read_excel(f"{data_path}340109.xls", sheet_name="Data1")

new_df.columns = [x.replace("Number of movements ; ", '') for x in new_df.columns]
new_df.columns = [x.replace(";  Short-term Residents returning ;", '') for x in new_df.columns]
new_df.columns = [x.strip() for x in new_df.columns]

# cut = [x for x in new_df.columns if "Total" not in x]
new_df = new_df[[x for x in new_df.columns if "Total" not in x]]
new_df = new_df[[x for x in new_df.columns if "Other" not in x]]
new_df.rename(columns={'Unnamed: 0':"Date"}, inplace=True)

totals = new_df
totals = totals[11:]


totals['Date'] = pd.to_datetime(totals['Date'])
totals = totals.loc[totals['Date']>"2020-03-01"]

totals['Date'] = totals['Date'].dt.strftime('%Y-%m-%d')

totals.index = totals['Date']
totals = totals.drop(columns='Date')

totals = totals.sum().reset_index()
totals.columns = ['Country', 'Returned residents']

totals = totals.sort_values(by="Returned residents", ascending=False)

# print(totals)