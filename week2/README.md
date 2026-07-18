# Week 2 - dbt Core

## What I Built

- Staging layer validation
Intermediate models
- int_orders_with_items
- int_orders_incremental
- Incremental model
- Generic + singular tests
- Documentation
- Macros
Mart model
- fct_orders

## Result

Full dbt build passing.

Source → Staging → Intermediate → Mart

## Business Purpose

Transform raw ecommerce data into trusted analytics-ready datasets for reporting and decision making.

## Architecture

Source

↓

Staging

↓

Intermediate

↓

Mart

## Skills Learned

- ref() and DAGs
- Generic tests
- Singular tests
- Documentation
- Materializations
- Incremental models
- Jinja
- Macros
- Mart modeling
