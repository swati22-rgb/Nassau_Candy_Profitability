
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Nassau Candy Profitability",
    page_icon="🍬",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Nassau Candy Distributor.csv"

st.title("🍬 Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Performance Analysis")

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)

    data["Order Date"] = pd.to_datetime(
        data["Order Date"], errors="coerce"
    )
    data["Ship Date"] = pd.to_datetime(
        data["Ship Date"], errors="coerce"
    )

    numeric_cols = ["Sales", "Cost", "Gross Profit", "Units"]
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    data["Gross_Margin_%"] = (
        data["Gross Profit"] /
        data["Sales"].where(data["Sales"] != 0)
    ) * 100

    data["Profit_Per_Unit"] = (
        data["Gross Profit"] /
        data["Units"].where(data["Units"] != 0)
    )

    return data

try:
    df = load_data()
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

valid_dates = df["Order Date"].dropna()

if valid_dates.empty:
    st.error("No valid Order Date values found in the dataset.")
    st.stop()

min_date = valid_dates.min().date()
max_date = valid_dates.max().date()

date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

divisions = sorted(df["Division"].dropna().unique().tolist())
selected_divisions = st.sidebar.multiselect(
    "Select Division",
    divisions,
    default=divisions
)

margin_values = df["Gross_Margin_%"].replace(
    [np.inf, -np.inf], np.nan
).dropna()

margin_limit = float(np.clip(
    margin_values.quantile(0.05), -100, 100
)) if not margin_values.empty else 0.0

min_margin = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    min_value=-100.0,
    max_value=100.0,
    value=margin_limit,
    step=5.0
)

product_search = st.sidebar.text_input(
    "Search Product",
    placeholder="Enter product name..."
)

# Apply filters
filtered = df.copy()

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        filtered["Order Date"].dt.date.between(start_date, end_date)
    ]

filtered = filtered[
    filtered["Division"].isin(selected_divisions)
]

filtered = filtered[
    filtered["Gross_Margin_%"].ge(min_margin)
    & filtered["Gross_Margin_%"].notna()
]

if product_search.strip():
    filtered = filtered[
        filtered["Product Name"].str.contains(
            product_search.strip(), case=False, na=False
        )
    ]

if filtered.empty:
    st.warning("No records match these filters. Try changing the filters.")
    st.stop()

# KPI calculations
total_sales = filtered["Sales"].sum()
total_profit = filtered["Gross Profit"].sum()
total_cost = filtered["Cost"].sum()
total_units = filtered["Units"].sum()

overall_margin = (
    total_profit / total_sales * 100 if total_sales != 0 else 0
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"${total_sales:,.2f}")
c2.metric("Gross Profit", f"${total_profit:,.2f}")
c3.metric("Gross Margin", f"{overall_margin:.2f}%")
c4.metric("Total Units", f"{total_units:,.0f}")

st.divider()

# Product-level summary
product_summary = filtered.groupby(
    ["Product Name", "Division"], dropna=False
).agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Gross Profit", "sum"),
    Total_Cost=("Cost", "sum"),
    Total_Units=("Units", "sum")
).reset_index()

product_summary["Gross_Margin_%"] = (
    product_summary["Total_Profit"] /
    product_summary["Total_Sales"].where(
        product_summary["Total_Sales"] != 0
    )
) * 100

product_summary["Profit_Per_Unit"] = (
    product_summary["Total_Profit"] /
    product_summary["Total_Units"].where(
        product_summary["Total_Units"] != 0
    )
)

# Tabs
overview, division_tab, diagnostics, concentration = st.tabs([
    "📊 Profitability Overview",
    "🏢 Division Performance",
    "🔎 Cost & Margin Diagnostics",
    "📈 Profit Concentration"
])

with overview:
    st.subheader("Top 10 Products by Gross Profit")

    top_products = product_summary.nlargest(10, "Total_Profit")

    fig = px.bar(
        top_products.sort_values("Total_Profit"),
        x="Total_Profit",
        y="Product Name",
        color="Division",
        orientation="h",
        title="Top Products by Gross Profit"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Product Profitability Table")

    st.dataframe(
        product_summary.sort_values(
            "Total_Profit", ascending=False
        ).round(2),
        use_container_width=True,
        hide_index=True
    )

with division_tab:
    st.subheader("Sales and Profit by Division")

    division_summary = filtered.groupby("Division").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Gross Profit", "sum"),
        Total_Cost=("Cost", "sum"),
        Total_Units=("Units", "sum")
    ).reset_index()

    division_summary["Gross_Margin_%"] = (
        division_summary["Total_Profit"] /
        division_summary["Total_Sales"].where(
            division_summary["Total_Sales"] != 0
        )
    ) * 100

    fig = px.bar(
        division_summary,
        x="Division",
        y=["Total_Sales", "Total_Profit"],
        barmode="group",
        title="Revenue vs Gross Profit by Division"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(
        division_summary.round(2),
        use_container_width=True,
        hide_index=True
    )

with diagnostics:
    st.subheader("Cost vs Sales")

    fig = px.scatter(
        filtered,
        x="Sales",
        y="Cost",
        color="Division",
        hover_data=["Product Name", "Gross Profit"],
        title="Cost vs Sales Relationship"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Lowest-Margin Products")

    st.dataframe(
        product_summary.sort_values(
            "Gross_Margin_%", ascending=True
        ).head(20).round(2),
        use_container_width=True,
        hide_index=True
    )

with concentration:
    st.subheader("Cumulative Gross Profit Contribution")

    pareto = product_summary[
        product_summary["Total_Profit"] > 0
    ].sort_values("Total_Profit", ascending=False).copy()

    if not pareto.empty and pareto["Total_Profit"].sum() > 0:
        pareto["Cumulative_Profit_%"] = (
            pareto["Total_Profit"].cumsum()
            / pareto["Total_Profit"].sum()
        ) * 100

        fig = px.line(
            pareto,
            x="Product Name",
            y="Cumulative_Profit_%",
            markers=True,
            title="Cumulative Profit Contribution by Product"
        )
        fig.add_hline(y=80, line_dash="dash")
        fig.update_layout(xaxis_tickangle=-60)
        st.plotly_chart(fig, use_container_width=True)

        products_for_80 = (
            pareto["Cumulative_Profit_%"] < 80
        ).sum() + 1

        st.write(
            f"Products needed to reach approximately 80% "
            f"of positive product profit: {products_for_80}"
        )
    else:
        st.info("No positive product profit is available for this selection.")

st.caption(
    "Analysis is based on the selected filters. "
    "Margin thresholds are exploratory and not company-defined targets."
)