# Rolling 12-Month Sales Analysis

## Objective

The Rolling 12-Month Sales analysis calculates cumulative revenue over the most recent 12-month period. This approach smooths short-term fluctuations and provides a clearer view of long-term sales performance.

## Implementation

A SQL window function is used to compute the rolling total by ordering sales chronologically and summing revenue over the current month and the previous eleven months.

## Business Value

* Identifies long-term sales trends.
* Reduces the impact of seasonal variations.
* Supports forecasting and executive decision-making.
* Helps compare sustained performance across different time periods.

## Output

The query returns:

* Full Date
* Monthly Revenue
* Rolling 12-Month Revenue

This metric can be integrated into dashboards and reports to monitor business growth over time.
