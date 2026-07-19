# SupplyPulse Architecture

raw.inventory_snapshots
        ↓
stg_inventory
        ↓
int_daily_velocity
        ↓
fct_stockout_risk
        ↓
mart_alerts

## raw.inventory_snapshots
Stores inventory snapshots exactly as received.

## stg_inventory
Cleans category names, trims strings, fixes datatypes, removes duplicates.

## int_daily_velocity
Calculates 7-day rolling average sales and days_of_stock_remaining.

## fct_stockout_risk
Classifies inventory risk levels.

## mart_alerts
Contains only actionable stockout alerts.
