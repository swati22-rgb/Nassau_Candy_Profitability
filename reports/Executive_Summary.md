# Executive Summary

## Product Line Profitability & Margin Performance Analysis

**Company:** Nassau Candy Distributor

### 1. Project Overview

This project analyzes the sales, manufacturing costs, gross profit, and product profitability of Nassau Candy Distributor using Python and an interactive Streamlit dashboard. The analysis focuses on identifying profitable products, comparing divisions, examining gross margins, and understanding profit concentration.

### 2. Dataset Overview

The dataset contains 10,194 records and 18 columns, covering transactions from January 1, 2025, to December 31, 2025. The dataset contains sales, cost, gross profit, units sold, product details, division information, and order dates.

### 3. Key Findings

* **Total Sales:** $141,783.63
* **Total Cost:** $48,340.83
* **Total Gross Profit:** $93,442.80
* **Overall Gross Margin:** 65.91%
* **Total Units Sold:** 38,654

The Chocolate division generated $131,692.90 in sales and $88,824.62 in gross profit. It accounted for approximately 92.88% of total sales and 95.06% of total gross profit.

The Other division generated $9,663.25 in sales and $4,333.45 in gross profit, while the Sugar division generated $427.48 in sales and $284.73 in gross profit.

The product **Wonka Bar - Scrumdiddlyumptious** generated the highest gross profit, at $19,357.50. **Kazookles** had the lowest gross margin among the product groups with positive sales, at approximately 7.69%.

The five highest-profit product groups collectively contributed approximately 95.06% of total positive product profit, indicating that profitability is concentrated in a small number of products.

### 4. Tools and Methodology

Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Streamlit were used for data validation, feature engineering, exploratory data analysis, product and division comparisons, margin analysis, and interactive visualization.

Gross margin was calculated as gross profit divided by sales, multiplied by 100. Product-level margins were calculated using aggregated profit and sales.

### 5. Business Recommendations

* Review the pricing, manufacturing costs, and sales strategy for low-margin products, particularly Kazookles.
* Investigate the factors contributing to the Chocolate division's high share of revenue and profit.
* Monitor product-level gross margins regularly.
* Use profit-concentration analysis to support inventory planning and product portfolio reviews.
* Validate recommendations against demand, operating expenses, and other business information before making decisions.

### 6. Conclusion

The analysis indicates that the Chocolate division and a small group of products account for most of the recorded gross profit. The Streamlit dashboard provides an interactive way to explore product profitability, compare divisions, and identify products that may need further cost or pricing review.

**Note:** Gross profit is not the same as net profit because operating expenses and other business costs are not included in this analysis.
