Nigeria-Inter-Bank-Settlement-System (NIBSS) fraud Analytics
> Exploring Financial Transaction Patterns and Fraud Indicators Using Python

---

## ⚙️ Project Overview

Financial fraud remains a major challenge for financial institutions, payment service providers and businesses operating in digital financial environments.

Identifying suspicious transaction patterns and understanding where fraudulent activities occur can help businesses improve monitoring, strengthen risk management and make better-informed decisions.

This project explores a financial transaction dataset containing 1,000,000 transaction records and 29 columns using Python.

The objective is to investigate transaction behavior, examine fraudulent and legitimate transactions, identify patterns across payment channels and customer segments, and communicate findings through data analysis and visualizations.

The project demonstrates an end-to-end exploratory data analysis workflow, from data inspection and cleaning to analysis, visualization and reporting.


---

## Business Problem

  Financial institutions process large volumes of transactions across multiple payment channels.

However, understanding the distribution and characteristics of fraudulent transactions can be challenging without proper data exploration.

This project addresses the following questions:

What proportion of transactions are classified as fraudulent?
How are fraudulent transactions distributed across payment channels?
Which transaction channels account for the highest number of reported fraud cases?
What patterns can be observed across merchant categories?
How do fraudulent transactions vary across customer age groups?
Are there differences in fraudulent activity across days of the week?
What data quality issues should be considered before further analysis or predictive modelling? 

-----
## Project Objectives
  
   * Inspect and understand the structure of the transaction dataset.
   * Identify missing values and duplicate records.
   * Examine the distribution of fraudulent and legitimate transactions.
   * Analyze fraud patterns across transaction channels.
   * Investigate transaction patterns across merchant categories.
   * Explore fraud distribution across customer age groups and weekdays.
   * Explore fraud distribution across customer age groups and weekdays.
   * Identify data quality considerations and opportunities for further investigation.
-----

  ## Dataset Information
| *Attribute*       |            *Description* |
| :---            |  :---   
| Dataset	          |        NIBSS Fraud Dataset |
| Source            |            	Kaggle |
| Creator	          |      Josiah Endurance Owolabi |
| Records           |            1,000,000 |
| Columns	          |                29 |
| Target            |        variable	is_fraud |
| Analysis type     |     	Exploratory Data Analysis |
| License           |            CC BY-SA 4.0 |

-----

## Tools Used
1. Python
2. Jupyter Notebook
4. Pandas
5. Numpy
6. Matplotlib
7. Seaborn

-----

Original Dataset: [NIBSS Fraud Dataset on Kaggle](https://www.kaggle.com/datasets/hendurhance/nibsss-fraud-dataset)

The dataset is used for portfolio and educational purposes. Please refer to the original Kaggle page for the dataset's attribution and licensing details

------

## Key Findings
1. 1 million transaction records analyzed.
2. 3,000 fraudulent transactions identified.
3. 0.3% of transactions were labelled fraudulent.
4. Mobile recorded the highest fraud count, with 1,496 cases.
5. No fully duplicated rows were detected.


---

## Project Workflow

The analysis followed these stages:

##  1. Data Loading and Inspection
Imported the dataset into Python.
Examined the number of rows and columns.
Reviewed column names and data types.
Inspected sample records.
##  2. Data Quality Assessment
Checked for missing values.
Investigated duplicate records.
Examined inconsistencies in relevant fields.
Considered appropriate handling of missing fraud-related information.
##  3. Exploratory Data Analysis

Investigated the distribution of fraudulent transactions across:

* Fraudulent versus legitimate transactions.
* Transaction channels.
* Merchant categories.
* Customer age groups.
* Days of the week.
* Available fraud technique classifications.
## 4. Data Visualisation

Created visual representations to make transaction patterns easier to understand and communicate.

## 5. Findings and Recommendations

Summarised the observations, highlighted data quality considerations and identified opportunities for more advanced fraud analysis.

## Fraud Distribution Across Transaction Channels

The highest fraud case counts were observed in the following channels:

| Transaction       |     Channel	Fraud Cases |
| :---              |    :---                 |
| Mobile            |           1,496 |
| Web	              |            687 |
| POS	              |            551 |
| IB	              |            168 |
| ECOM	            |            76 |
| ATM	              |            22 |


## Important observation: 
Mobile transactions accounted for the highest number of fraud cases in the dataset. However, fraud counts alone do not establish that a channel is riskier. Transaction volumes and fraud rates by channel should also be examined.

-----------

## Data Quality Observation

The fraud_technique column contained 997,000 missing values.

This requires careful interpretation because missing information should not automatically be treated as a confirmed fraud classification.

-----------

## Repository Structure
```
nibss-transaction-fraud-analysis/ 
│
├── README.md 
├── data_dictionary.md 
├── requirements.txt 
├── .gitignore 
│ 
├── notebooks/ 
│ └── NIBSS_Transaction_Analysis.ipynb
│ 
├── data/ 
│  ├── raw/ 
│   └── processed/ 
│
├── reports/ 
│  ├── findings.md 
│  └── figures/ 
│ 
└── src/ 
      └── analysis.py
```

-----
## About the Analyst

Emmanuel Ejike | Junior Data Analyst

I am an aspiring data analyst with practical experience in banking operations and foundational knowledge of Python, SQL, Microsoft Excel and Power BI.

My interest lies in using data to uncover patterns, solve business problems and support informed decision-making, particularly within financial services and business operations.

I am continuously developing my analytical skills through practical projects involving data cleaning, exploratory analysis, reporting and visualisation.
------

## Areas of Interest:

*  Data Cleaning and Preparation
*  Exploratory Data Analysis
*  Financial Data Analysis
*  Fraud Pattern Investigation
*  SQL Data Analysis
*  Business Reporting

---
## Let's Connect

I welcome opportunities to collaborate on data analysis, data cleaning and reporting projects.

- 🔗 linkedin- (https://www.linkedin.com/in/emmanuel-ejike-690319314)
- 💼 Link to Project- (https://colab.research.google.com/drive/1A7ZILuiKjDPdEucTW7sX8uNuUjnyMNer#scrollTo=be3874b5-d76f-4e53-988c-cd426cb29ab2)
- 📧 ejemmanuelejike@hotmail.com
----

## Dataset Attribution and Licence

Dataset: NIBSS Fraud Dataset
Creator: Josiah Endurance Owolabi
Source: https://www.kaggle.com/datasets/hendurhance/nibsss-fraud-dataset
Licence: Creative Commons Attribution-ShareAlike 4.0 International

The dataset is attributed to its original creator. Any distributed adaptations of the dataset must comply with the applicable CC BY-SA 4.0 requirements.

This project is independent and is not affiliated with or endorsed by the dataset creator.

---

