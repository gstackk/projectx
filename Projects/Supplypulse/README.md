
# SupplyPulse

Inventory stockout prediction platform.

## Problem

Operations teams discover stockouts too late.

## Solution

Predict inventory risk using sales velocity and stock levels.

## Data Flow

raw.inventory_snapshots
→ stg_inventory
→ int_daily_velocity
→ fct_stockout_risk
→ mart_alerts
