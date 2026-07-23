# 📂 Project Structure

```text
models/
│
├── staging
│   └── stg_inventory.sql
│
├── intermediate
│   └── int_daily_velocity.sql
│
└── marts
    ├── fct_stockout_risk.sql
    └── mart_alerts.sql
```

### Model Purpose

| Model | Purpose |
|---------|---------|
| stg_inventory | Cleans and standardizes raw inventory data |
| int_daily_velocity | Calculates inventory consumption velocity |
| fct_stockout_risk | Calculates stockout risk and days remaining |
| mart_alerts | Produces inventory alerts for business users |
