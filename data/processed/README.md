# Data Directory

## Overview

This document provides an overview of the dataset used in the NIBSS Transaction Fraud Analysis project.

The dataset contains 1,000,000 transaction records and 29 columns.

It is used to investigate transaction characteristics and patterns associated with fraudulent and legitimate transactions.

## Target Variable

| Column | Description | Role |
|---|---|---|
| `is_fraud` | Indicates whether a transaction is classified as fraudulent or legitimate. | Target variable |

## Other Variables

The dataset contains additional transaction, customer, merchant and risk-related fields.

These variables should be documented using their actual column names and definitions from the original dataset.

Before interpreting a variable, its meaning and measurement should be verified against the original dataset documentation.

## Missing Values

The initial analysis identified 997,000 missing values in `fraud_technique`.

Missing values should be investigated in relation to the target variable before any replacement or imputation is performed.

## Data Quality Considerations

- Check missing values in all columns.
- Investigate duplicate records.
- Verify data types.
- Check categorical inconsistencies.
- Confirm the meaning of risk-related variables.
- Investigate potential data leakage before predictive modelling.

## Important Note

This data dictionary is intended as a working reference. Detailed descriptions should be added for all 29 columns after confirming their definitions from the original dataset source.
