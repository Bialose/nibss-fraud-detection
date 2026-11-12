#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set a clean visual style for all charts
sns.set_style('whitegrid')

df = pd.read_csv(r"C:\Users\Judywealth\Documents\nibss_fraud_dataset_Project.csv")
df


# # EDA & Visualization

# In[2]:


df.isnull().sum() # check for missing Valuse


# In[3]:


df.duplicated().sum() # Handle duplicate


# In[4]:


print(df['fraud_technique'].isnull().sum())  # how many missing in fraud_techniue
print(df['fraud_technique'].value_counts())   # what values exist in Fraud_techniue


# In[5]:


# Handle missing fraud-technique values without misclassifying fraud cases.
# Legitimate transactions receive "Legitimate".
# Fraudulent transactions with no recorded technique receive "Unknown".
df.loc[(df['is_fraud'] == 0) & (df['fraud_technique'].isna()), 'fraud_technique'] = 'Legitimate'
df.loc[(df['is_fraud'] == 1) & (df['fraud_technique'].isna()), 'fraud_technique'] = 'Unknown'


# In[6]:


# Check unique values in each column
print("Unique values in is_fraud:", df['is_fraud'].unique())


# In[7]:


fraud_only = df[df['is_fraud'] == 1]


# In[8]:


print(df['is_fraud'].value_counts())
# shows how many fraud vs legitimate transactions we have


# In[9]:


print(df['is_fraud'].value_counts(normalize=True) * 100)
# shows the percentage split between fraud and legitimate


# In[10]:


print(df['is_fraud'].value_counts(normalize=True) * 100)
# shows the percentage split between fraud and legitimate


# plt.figure(figsize=(10,6))
# sns.countplot(x='fraud_technique', data=fraud_only, color='skyblue')
# 
# plt.title("Distribution of Fraud Techniques (Fraud Cases Only)")
# plt.xlabel("Fraud Technique")
# plt.ylabel("Number of Fraudulent Transactions")
# plt.xticks(rotation=45)
# plt.show()
# 
# 
# 

# In[11]:


print(df.columns)


# ## Additional Visualizations
# 

# In[12]:


from matplotlib.ticker import FuncFormatter

# -----------------------------
# Prepare Data
# -----------------------------
fraud_label_map = {
    0: 'Legitimate',
    1: 'Fraudulent'
}

class_counts = (
    df['is_fraud']
    .map(fraud_label_map)
    .fillna(df['is_fraud'].astype(str))
    .value_counts()
)

# Keep consistent order
class_counts = class_counts.reindex(
    ['Legitimate', 'Fraudulent']
).dropna()

# Calculate percentages
percentages = (class_counts / class_counts.sum()) * 100

# -----------------------------
# Visualization
# -----------------------------
sns.set_theme(style="whitegrid", context="talk")

fig, ax = plt.subplots(figsize=(10, 6))

colors = ['#2E86AB', '#E74C3C']

bars = sns.barplot(
    x=class_counts.index,
    y=class_counts.values,
    palette=colors,
    ax=ax
)

# Apply logarithmic scale
ax.set_yscale('log')

# Add labels
for i, bar in enumerate(ax.patches):
    height = bar.get_height()

    ax.annotate(
        f'{height:,.0f}\n({percentages.iloc[i]:.2f}%)',
        (
            bar.get_x() + bar.get_width() / 2,
            height
        ),
        ha='center',
        va='bottom',
        fontsize=11,
        fontweight='bold',
        xytext=(0, 8),
        textcoords='offset points'
    )

# Formatting
ax.set_title(
    'Fraudulent vs Legitimate Transactions (Log Scale)',
    fontsize=18,
    fontweight='bold',
    pad=15
)

ax_xlabel(
    'Transaction Classification',
    fontsize=13
)

ax.set_ylabel(
    'Number of Transactions (Log Scale)',
    fontsize=13
)

# Format y-axis with commas
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f'{int(x):,}')
)

# Remove top and right borders
sns.despine()

plt.tight_layout()
plt.show()


# In[13]:


# Example: count fraud techniques
# Count fraud techniques (replace 'FraudTechnique' with your actual column name)
fraud_counts = df['fraud_technique'].value_counts()

# Remove "Legitimate" from the counts
fraud_counts = fraud_counts.drop('Legitimate', errors='ignore')

# Plot as pie chart
plt.figure(figsize=(8,8))
plt.pie(
    fraud_counts,
    labels=fraud_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Set2.colors
)
plt.title("Distribution of Fraud Techniques (Fraud Cases Only)")
plt.show()


# In[14]:


channel_summary = df.groupby(['channel','is_fraud']).size().reset_index(name='count')
print(channel_summary)
# Displaying legitimate & fraud transaction 0 to 1


# In[15]:


# Visualization 2: Fraud rate by transaction channel
# Mean of a binary is_fraud column gives the proportion of fraud records.
# Multiply by 100 to express the result as a percentage.

channel_fraud_rate = (
    df.groupby('channel', dropna=False)['is_fraud']
      .mean()
      .mul(100)
      .sort_values(ascending=False)
      .reset_index(name='fraud_rate_pct')
)

# Remove missing channel labels from the chart and label them explicitly if present.
channel_fraud_rate['channel'] = channel_fraud_rate['channel'].fillna('Unknown')

plt.figure(figsize=(9, 5))
ax = sns.barplot(
    data=channel_fraud_rate,
    x='channel',
    y='fraud_rate_pct',
    color='darkorange'
)

plt.title('Fraud Rate by Transaction Channel')
plt.xlabel('Transaction Channel')
plt.ylabel('Fraud Rate (%)')

# Add percentage labels above each bar.
for bar in ax.patches:
    height = bar.get_height()
    ax.annotate(
        f'{height:.2f}%',
        (bar.get_x() + bar.get_width() / 2, height),
        ha='center',
        va='bottom',
        xytext=(0, 4),
        textcoords='offset points'
    )

plt.tight_layout()
plt.show()

# Display the values used in the chart for accurate reporting.
display(channel_fraud_rate)


# In[16]:


# Filter only fraud cases
fraud_only = df[df['is_fraud'] == 1]

# Count fraud cases per merchant category
fraud_counts = fraud_only['merchant_category'].value_counts()

# Normalize fraud counts to range [0,1] for color mapping
norm = plt.Normalize(fraud_counts.min(), fraud_counts.max())

# Define a custom colormap: green → light red → dark red
from matplotlib import cm
cmap = cm.get_cmap('RdYlGn_r')  # reversed Red-Yellow-Green

colors = cmap(norm(fraud_counts.values))

# Plot pie chart
plt.figure(figsize=(8,8))
plt.pie(
   fraud_counts,
   labels=fraud_counts.index,
   autopct='%1.1f%%',
   startangle=140,
   colors=colors
)

plt.title("Fraud Distribution by Merchant Category (Color-coded by Severity)")
plt.show()


# In[17]:


# Show the first 10 values in the column
print(df['day_of_week'].head(10))
# in the result, the first row represents days of the week, then the second row shows how many times it appears


# In[18]:


# Keep only values 0–6 (assuming 0=Monday, 6=Sunday)
df = df[df['day_of_week'].isin(range(0,7))]

# Map numbers to day names
day_map = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

df['day_of_week'] = df['day_of_week'].map(day_map)


# In[19]:


# Filter only fraud cases (assuming is_fraud == 1 means fraud)
fraud_only = df[df['is_fraud'] == 1]

plt.figure(figsize=(10,5))
sns.countplot(
    x='day_of_week',
    data=fraud_only,
    color='red'   # single color since only fraud is shown
)

plt.title('Fraud by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Fraud Count')
plt.show()


# In[20]:


# Filter only fraud cases (assuming is_fraud == 1 means fraud)
fraud_only = df[df['is_fraud'] == 1]

plt.figure(figsize=(8,5))
sns.countplot(
    x='age_group',
    data=fraud_only,
    color='red'   # single color since only fraud is shown
)

plt.title('Fraud by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Fraud Count')
plt.show()


# In[21]:


print(df['age_group'].unique())


# In[23]:


df.to_csv('nibss_fraud_cleaned.csv', index=False)
# saves your cleaned and analyzed dataset as a CSV file
# this file will be imported into Power BI for dashboard building
print('File exported successfully!')


# In[ ]:


import os
print(os.getcwd())


# In[ ]:




