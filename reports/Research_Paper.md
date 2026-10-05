# Product Line Profitability & Margin Performance Analysis of Nassau Candy Distributor

## Abstract

This study examines product profitability and margin performance at Nassau Candy Distributor using transaction-level sales data. The analysis evaluates revenue, manufacturing costs, gross profit, gross margin, product performance, and division-level contributions. Python-based data analysis and an interactive Streamlit dashboard are used to identify profitability patterns and support business decision-making. The findings highlight the importance of monitoring low-margin products and understanding the concentration of profit among product lines.

**Keywords:** Product Profitability, Gross Margin, Sales Analysis, Cost Analysis, Python, Streamlit, Business Intelligence

## 1. Introduction

Profitability analysis helps businesses understand which products generate the greatest financial contribution and which may require further investigation. Sales revenue alone does not indicate whether a product is profitable because manufacturing costs also affect financial performance.

This project analyzes Nassau Candy Distributor's sales dataset to compare products and divisions based on sales, cost, gross profit, and gross margin. An interactive dashboard is developed to make the results easier to explore.

## 2. Problem Statement

A business may generate substantial sales while some products deliver relatively low profit margins. Without product-level and division-level analysis, it can be difficult to identify low-margin products, understand profit concentration, and determine where further cost or pricing reviews may be beneficial.

The project addresses this problem through structured data validation, profitability calculations, exploratory analysis, and interactive visualization.

## 3. Objectives

1. Examine the quality and consistency of the supplied dataset.
2. Calculate gross margin percentage and profit per unit.
3. Identify products with high gross profit and products with low margins.
4. Compare sales, costs, and gross profit across divisions.
5. Analyze how profit is distributed among product groups.
6. Develop an interactive dashboard for exploring profitability performance.
7. Provide data-supported recommendations for further business investigation.

## 4. Dataset Description

The dataset contains 10,194 records and 18 original columns. Important fields include Order ID, Order Date, Ship Date, Division, Region, Product Name, Sales, Units, Gross Profit, and Cost.

The dataset supports transaction-level, product-level, and division-level analysis. Data validation includes checking missing values, duplicate rows, date validity, numeric values, and consistency between recorded gross profit and calculated gross profit.

The supplied dataset is the primary source of information for this study.

## 5. Methodology

### 5.1 Data Cleaning and Validation

The dataset was loaded into Python using Pandas. Date fields were converted to datetime format, and numerical columns were checked for invalid or unexpected values. Duplicate rows and missing values were examined.

Recorded gross profit was compared with calculated gross profit to identify discrepancies.

### 5.2 Feature Engineering

The following metrics were calculated:

**Gross Profit**

Gross Profit = Sales − Cost

**Gross Margin Percentage**

Gross Margin (%) = (Gross Profit ÷ Sales) × 100

**Profit per Unit**

Profit per Unit = Gross Profit ÷ Units

**Revenue Contribution**

Revenue Contribution (%) = (Product Sales ÷ Total Sales) × 100

**Profit Contribution**

Profit Contribution (%) = (Product Gross Profit ÷ Total Gross Profit) × 100

These calculations are interpreted carefully when sales or units are zero, since the corresponding ratios may be undefined.

### 5.3 Exploratory Data Analysis

The analysis includes summary statistics, sales and profit comparisons, monthly trends, product rankings, division comparisons, and a scatter plot of sales against cost.

Products are compared using aggregated sales and gross profit. Product-level gross margin is calculated from aggregated gross profit divided by aggregated sales, rather than by simply averaging transaction-level margins.

### 5.4 Profit Concentration Analysis

Product groups are sorted by gross profit, and cumulative profit contribution is calculated. This helps assess whether a relatively small group of products accounts for a large share of the recorded gross profit.

### 5.5 Dashboard Development

A Streamlit dashboard was developed with four main sections:

* Profitability Overview
* Division Performance
* Cost and Margin Diagnostics
* Profit Concentration

Users can filter results by order date, division, minimum gross margin, and product name.

## 6. Results and Discussion

### 6.1 Overall Financial Performance

The analysis calculates total sales, total cost, total gross profit, gross margin, and units sold. These indicators provide an overview of recorded sales performance and the difference between sales revenue and manufacturing cost.

Gross profit should not be interpreted as net profit because operating expenses, taxes, and other costs are not included in the supplied analysis.

### 6.2 Division-Level Performance

Division-level aggregation allows comparison of sales revenue, gross profit, costs, and gross margins. The Chocolate division represents the largest share of recorded revenue and gross profit in the analyzed dataset.

This concentration makes division-level monitoring useful, while further investigation would be needed to understand the causes of differences between divisions.

### 6.3 Product-Level Profitability

Product rankings identify products with high gross profit and products with comparatively low gross margins. The analysis identifies **Wonka Bar - Scrumdiddlyumptious** as the leading product by gross profit among the analyzed product groups.

**Kazookles** is identified as a low-margin product in the analysis. Its pricing, manufacturing cost, and sales performance may warrant further review. However, a low gross margin alone does not establish that a product should be discontinued.

### 6.4 Profit Concentration

The Pareto-style analysis shows that gross profit is concentrated among a small number of product groups. The five highest-profit product groups collectively contribute approximately 95.06% of the recorded total positive product profit in the reported analysis.

This result supports monitoring the financial performance of leading products while also examining the sustainability and risk of relying heavily on a limited set of products.

### 6.5 Cost and Margin Diagnostics

The cost-versus-sales visualization helps explore the relationship between recorded sales and manufacturing costs. Margin-risk categories are used as exploratory indicators to identify products for further review.

The margin thresholds are analytical assumptions for this project, not official company targets. The findings do not independently establish the causes of low margins or prove that changing prices or costs would improve profitability.

## 7. Business Recommendations

1. **Review low-margin products:** Investigate manufacturing costs, selling prices, discounts, and demand before making changes.
2. **Monitor leading products:** Track the sales and gross profit contribution of products that account for a large share of total profit.
3. **Compare divisions regularly:** Review revenue, gross profit, and gross margin together rather than evaluating divisions using sales alone.
4. **Improve cost visibility:** Investigate unusual cost-to-sales relationships and validate unexpected records.
5. **Use the dashboard for monitoring:** Apply filters to compare periods, divisions, and products.
6. **Extend the analysis:** Incorporate operating expenses, inventory information, pricing history, and demand data when available to support more comprehensive decisions.

## 8. Limitations

The analysis depends on the accuracy and completeness of the supplied dataset. Cost is treated as the manufacturing cost represented in the dataset; it may not include every business expense.

Gross margin does not measure net profitability. Correlations or visual patterns between sales and costs do not establish causation. Product recommendations should also consider demand, inventory, strategic importance, and other information not covered in this study.

The margin-risk thresholds are exploratory and should not be treated as company-defined standards.

## 9. Conclusion

This project demonstrates how Python-based analysis can be used to evaluate product profitability, compare divisions, examine cost relationships, and study profit concentration. The Streamlit dashboard makes these results accessible through interactive filters, charts, and tables.

The findings provide a foundation for further investigation into low-margin products and dependence on leading product groups. Decisions concerning pricing, product rationalization, and cost control should be made only after validating the findings and considering additional business information.

## 10. Tools and Technologies

* Python 3
* Pandas and NumPy
* Matplotlib and Seaborn
* Plotly
* Streamlit
* Jupyter Notebook

## References

1. The supplied Nassau Candy Distributor dataset.
2. Pandas documentation: https://pandas.pydata.org/docs/
3. Streamlit documentation: https://docs.streamlit.io/
4. Plotly Python documentation: https://plotly.com/python/
