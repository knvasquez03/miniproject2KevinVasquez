### INF601 - Advanced Programming in Python
### Kevin Vasquez
### Mini Project 2

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()


df = pd.read_csv("./data/niaaa_apparent_per_capita_consumption_1977_2023.csv")

df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["ethanol_all_drinks_gallons_per_capita"] = pd.to_numeric(
    df["ethanol_all_drinks_gallons_per_capita"], errors="coerce"
)

df = df.dropna(subset=["year", "ethanol_all_drinks_gallons_per_capita"])


latest_year = df["year"].max()

df_latest = df[df["year"] == latest_year]

top10 = df_latest.sort_values(
    by="ethanol_all_drinks_gallons_per_capita",
    ascending=False
).head(10)

states = top10["state_name"]
values = top10["ethanol_all_drinks_gallons_per_capita"]

plt.figure(figsize=(10,6))
plt.barh(states, values)
plt.xlabel("Ethanol (All Drinks) Gallons Per Capita")
plt.ylabel("State")
plt.title(f"Top 10 States by Alcohol Consumption ({int(latest_year)})")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(str(charts / "top10_states.png"))
plt.show()

# ---------------------------------
# Kansas vs US Average Over Time
# ---------------------------------

# National average (mean of all states per year)
us_avg = df.groupby("year")[
    "ethanol_all_drinks_gallons_per_capita"
].mean()

# Kansas data
kansas = df[df["state"] == "kansas"]
kansas = kansas.set_index("year")[
    "ethanol_all_drinks_gallons_per_capita"
]

plt.figure(figsize=(10,6))
plt.plot(us_avg.index, us_avg.values, label="US Average")
plt.plot(kansas.index, kansas.values, label="Kansas")
plt.xlabel("Year")
plt.ylabel("Ethanol (All Drinks) Gallons Per Capita")
plt.title("Kansas vs US Average Alcohol Consumption Over Time")
plt.legend()
plt.tight_layout()
plt.savefig(str(charts / "kansas_vs_us_trend.png"))
plt.show()



# This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question. This will get you familar with working with datasets and asking questions, researching APIs and gathering datasets. If you get stuck here, please email me!
#
# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.