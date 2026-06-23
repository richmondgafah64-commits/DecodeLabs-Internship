import pandas as pd 
df = pd.read_excel("Cleaned Dataset.xlsx")
#It removes duplicates and missing values from the dataset and saves the cleaned data to a new excel file
df = df.drop_duplicates()
#Removes empty rows from the dataset
df = df.dropna()
#show the cleaned dataset
print(df.head())
#it saves the cleaned data to a new excel file
df.to_excel("final_cleaned.xlsx", index=False)
print("Cleaning completed!")
