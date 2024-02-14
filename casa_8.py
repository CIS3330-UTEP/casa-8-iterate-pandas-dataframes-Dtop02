import pandas as pd

# # Read the CSV file into a DataFrame
df = pd.read_csv('big-mac-full-index.csv')

# # Iterate through the DataFrame rows using iterrows()
for i,r in df.iterrows():
#     # Access each row's data using row[column_name]
    print(r['name'], r['local_price'])

#6  Using apply()
    print(df.apply(lambda r: r['name'], axis = 1))

