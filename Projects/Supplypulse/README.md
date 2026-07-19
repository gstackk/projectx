# SupplyPulse

## Problem

Inventory teams often discover stockout risks too late, leading to lost sales and poor customer experience.

## Solution

SupplyPulse is a dbt-powered inventory monitoring system that predicts stockout risk using current inventory levels and sales velocity.

## Data Architecture

Supplypulse_project1
    ↓
stg_inventory
    ↓
int_daily_velocity
    ↓
fct_stockout_risk
    ↓
mart_alerts

## Models

### stg_inventory
- Data cleaning
- Type casting
- Duplicate removal
- Data quality filtering

### int_daily_velocity
- 7-day rolling sales average
- Days of stock remaining calculation

### fct_stockout_risk
- CRITICAL (<2 days)
- HIGH (<5 days)
- MEDIUM (<10 days)
- LOW (>=10 days)

### mart_alerts
- Actionable inventory alerts
- Only HIGH and CRITICAL inventory risks

## Data Quality Tests

- not_null
- unique_combination_of_columns
- accepted_values
- assert_no_negative_stock
- mart_alerts_has_rows

## How To Run

dbt build

dbt test

dbt docs generate

dbt docs serve
