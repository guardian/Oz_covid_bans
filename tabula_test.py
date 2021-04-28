import tabula
import pandas as pd 
import os 

data_path = os.path.dirname(__file__) + "/data/"

df = tabula.read_pdf('/Users/josh_nicholas/github/tests/210428_nsw_epi/data/countries_of.pdf', pages="all")

cut_down = [x for x in df if "Country of acquisition" in x.columns[0]]



# when = ['20 February 2021', '27 February 2021', 
# '12 December 2020', '9 January 2021', 
# '5 December 2020', '30 January 2021', 
# '26 December 2020', '16 January 2021', '28 November 2020', '6 March 2021', '13 February 2021']

when = ['20 February 2021', '27 February 2021', 
'12 December 2020', '9 January 2021', 
'5 December 2020', '30 January 2021', 
'26 December 2020', '16 January 2021', '28 November 2020', '6 March 2021', '13 February 2021', "17 April 2021"]


# latest = tabula.read_pdf('/Users/josh_nicholas/github/tests/210428_nsw_epi/data/210428_nsw_epidemiology_reports/covid-19-surveillance-report-20210415.pdf', pages="11")
# latest[0]['When'] = "10 April 2021"

new_latest = tabula.read_pdf('/Users/josh_nicholas/github/Oz_covid_bans/data/210428_nsw_epidemiology_reports/covid-surveillance-report-20210422.pdf', pages="11")

print(new_latest[0])
cut_down.append(new_latest[0])

for i in range(0, len(when)):
    cut_down[i].columns = ['Country of acquisition of COVID-19', 'Number (%) of cases in the last four']
    cut_down[i]['When'] = when[i]

final_df = pd.concat(cut_down)
print(final_df)

with open(f"{data_path}countries.csv", "w") as f:
    final_df.to_csv(f, index=False, header=True)

