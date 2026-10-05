# Nassau Candy Distributor — Product Profitability Analysis

## Project Overview

This project analyzes the sales, costs, gross profit, and profitability of products sold by Nassau Candy Distributor. The objective is to identify product-level and division-level profitability patterns and understand how costs relate to sales performance.

## Objectives

* Analyze sales, cost, and gross profit.
* Calculate gross margin percentage and profit per unit.
* Compare profitability across product lines and divisions.
* Identify products with low gross margins.
* Analyze profit concentration using a Pareto-style analysis.
* Develop an interactive dashboard for business insights.

## Tools & Technologies

* Python
* Pandas and NumPy
* Matplotlib and Seaborn
* Plotly
* Streamlit
* Jupyter Notebook

## Project Structure

* `data/` — Dataset
* `notebooks/` — Data cleaning and exploratory analysis
* `outputs/` — Analysis outputs and charts
* `report/` — Project reports
* `app.py` — Interactive Streamlit dashboard
* `requirements.txt` — Python dependencies

## Key Performance Indicators

* Total Sales
* Total Gross Profit
* Gross Margin Percentage
* Profit per Unit
* Revenue and Profit Contribution
* Product and Division Performance

## How to Run

1. Install the required packages:
   `python -m pip install -r requirements.txt`
2. Start the dashboard:
   `python -m streamlit run app.py`

## Limitations

The analysis depends on the accuracy and completeness of the supplied dataset. Margin thresholds are exploratory assumptions and should not be treated as official company targets.

## Conclusion

This project provides an interactive framework for exploring product profitability, division performance, cost relationships, and profit concentration. Specific business recommendations should be based on the verified results of the analysis.
