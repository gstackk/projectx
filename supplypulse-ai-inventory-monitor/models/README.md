# dbt Models

SupplyPulse follows a layered dbt architecture.

```text
Raw Inventory Data
         ↓
    stg_inventory
         ↓
  int_daily_velocity
         ↓
  fct_stockout_risk
         ↓
     mart_alerts
```

## Model Overview

| Model | Purpose |
|---------|---------|
| stg_inventory | Cleans and standardizes raw inventory data |
| int_daily_velocity | Calculates daily inventory consumption velocity |
| fct_stockout_risk | Calculates inventory risk levels and stockout predictions |
| mart_alerts | Produces business-ready inventory alerts |

## Business Flow

### stg_inventory

Creates a clean inventory layer for downstream transformations.

### int_daily_velocity

Calculates average inventory consumption trends.

### fct_stockout_risk

Computes:

- Risk Level
- Days Remaining
- Predicted Stockout Date

### mart_alerts

Creates business-ready alerts for operations teams and dashboard users.
