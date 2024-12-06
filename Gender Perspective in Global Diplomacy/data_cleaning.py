import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/selinwork/Documents/Ironhack/Ironhack_Week_3/Personal Project/gender_diplomacy.csv')

# Dropped country code and cname code columns
df = df.drop(["ccode_send", "ccodealp_send", "ccode_receive", "ccodealp_receive"], axis=1)

# Filter out rows where gender is not equal to 99
filtered_df = df[df['gender'] != 99]

# Map gender values to their corresponding labels
gender_mapping = {1: "female", 0: "male"}
filtered_df["gender"] = filtered_df["gender"].map(gender_mapping)

# Save the cleaned data to a new CSV file
filtered_df.to_csv("clean_data.csv", index=False)

# Gender distribution of diplomats globally from 1968 to 2019
gender_counts_percentage = round(gender_counts.apply(lambda x: x / x.sum() * 100, axis=1),2)

# *** Female representatives distributed regionally ***

region_map = {0: 'Africa', 1: 'Asia', 2: 'Central and North America(including the West Indies)', 
              3: 'Europe(including Russia)', 4: 'Middle East including Egypt and Turkey', 
              5: 'Nordic Countries', 6: 'Oceania', 7: 'South America', 9999: 'Missing'}
# Map the region codes to region names
subset['region_name'] = subset['region_send'].map(region_map)

# Group by region and gender, then count the occurrences
region_gender_counts = subset.groupby(['region_name', 'gender']).size().unstack()

# Normalize the counts to get percentages
region_gender_percentage = region_gender_counts.apply(lambda x: x / x.sum() * 100, axis=1)

# Female representatives in highest and lowest 10 countries 
df_countries1_filtered = df_countries1[df_countries1.index != 'Missing']

min_value = df_countries1_filtered.min()
country_with_min_value = df_countries1_filtered.idxmin()
max_value = df_countries1_filtered.max()
top_10_countries = df_countries1_filtered.nlargest(10)
bottom_10_countries = df_countries1_filtered.nsmallest(10)

# Gender comparison of the diplomats between GME(Greater Middle East) ond Non GME
# 0 = Not GME, 1 = GME 
# Non GME received from GME or Non GME's

# Group by GME_receive and GME_send, then count the occurrences of each gender
GME_gender_distribution = subset.groupby(['GME_receive', 'GME_send', 'gender']).size().unstack().fillna(0)

# Rename columns for better readability
GME_gender_distribution.columns = ['Female', 'Male']

# Map G8 Countries and find the female distribution

G8_mapping = {1: 'United States of America', 2: 'Canada', 3: 'United Kingdom of Great Britain and Northern Ireland', 4: 'France', 5: 'Germany', 6: 'Italy', 7: 'Japan', 8: 'Russia'}
G8_gender = subset["gender"].map(G8_mapping)
G8_gender_distribution = subset[subset['cname_send'].isin(G8_mapping.values())].groupby(['cname_send', 'gender']).size().unstack().fillna(0)

from scipy.stats import chi2_contingency
import seaborn as sns

# Create a contingency table between two categorical datas
contingency_table = pd.crosstab(subset['title'], subset['gender'])

# Perform the chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Print the results
print(f"Chi-squared: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

# Adding another dataset for Tableau
filtered_df.to_excel("clean_tablau.xlsx", index=False)