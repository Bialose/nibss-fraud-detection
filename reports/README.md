# NIBSS Fraud Analysis: Findings and Business Insights

## 1. Executive Summary

This report presents the key observations from an exploratory analysis of a financial transaction dataset containing 1,000,000 records.

The objective was to investigate transaction patterns, understand the distribution of fraudulent transactions and identify areas that may require further investigation.

The analysis identified 3,000 transactions classified as fraudulent, representing 0.30% of the dataset.

Mobile transactions recorded the highest number of fraud cases among the examined payment channels.

These observations provide a foundation for further investigation into transaction behaviour and potential fraud risk indicators.

## 2. Transaction Overview

The dataset contains:

- 1,000,000 total transaction records.
- 997,000 legitimate transactions.
- 3,000 fraudulent transactions.
- 29 columns.
- No fully duplicated rows identified during the initial assessment.

### Key Observation

Fraudulent transactions represent a relatively small proportion of the dataset.

This imbalance is important when interpreting results and planning any future machine learning model.

A model that predicts every transaction as legitimate could achieve 99.70% accuracy while failing to identify any fraudulent transaction.

Therefore, accuracy alone would not be an appropriate measure of model performance.

## 3. Fraud Distribution by Transaction Channel

The analysis identified the following fraud case counts:

| Channel | Fraud Cases |
|---|---:|
| Mobile | 1,496 |
| Web | 687 |
| POS | 551 |
| IB | 168 |
| ECOM | 76 |
| ATM | 22 |

### Key Observation

Mobile recorded the highest number of fraudulent transactions, followed by Web and POS.

### Business Implication

These channels may deserve further investigation when reviewing transaction security and monitoring processes.

However, the number of fraud cases does not independently establish the risk level of a channel.

A proper comparison should consider the total number of transactions processed through each channel and calculate the corresponding fraud rate.

## 4. Data Quality Assessment

The initial assessment identified 997,000 missing values in the `fraud_technique` column.

This is an important data quality consideration.

Missing values should be interpreted carefully rather than automatically assigned a meaning.

For example, a missing fraud technique for a legitimate transaction may be expected, while a missing technique for a transaction labelled as fraudulent may require further investigation.

## 5. Class Imbalance

Fraudulent transactions account for 0.30% of all records.

This represents a highly imbalanced classification dataset.

### Why This Matters

In a future predictive modelling exercise, class imbalance may affect the model's ability to identify fraudulent transactions.

Potential evaluation metrics include:

- Precision
- Recall
- F1-score
- Confusion matrix
- Precision-Recall AUC

The appropriate metric should reflect the business cost of missed fraud cases and false alarms.

## 6. Recommendations for Further Analysis

Based on the initial findings, the following investigations are recommended:

1. Calculate fraud rates across all transaction channels.
2. Investigate transaction amounts across fraudulent and legitimate records.
3. Examine transaction activity by hour of the day.
4. Investigate fraud patterns across merchant categories.
5. Explore customer age groups and transaction behaviour.
6. Investigate missing values in fraud-related fields.
7. Examine possible relationships between risk-related variables and the fraud label.
8. Assess potential data leakage before predictive modelling.

## 7. Conclusion

The analysis provides an initial understanding of fraudulent transaction patterns within the dataset.

The findings highlight the importance of transaction channel analysis, data quality assessment and appropriate handling of class imbalance.

Further analysis and predictive modelling could provide additional insight into potential fraud indicators.

**Project Type:** Exploratory Data Analysis  
**Tools:** Python, Pandas, NumPy, Matplotlib and Jupyter Notebook  
**Analyst:** Emmanuel Ejike


