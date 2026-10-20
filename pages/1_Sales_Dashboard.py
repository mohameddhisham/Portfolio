import sys
from datetime import timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ----------------------------------------------------------------------------
# SYNTHETIC DATA — deterministic (fixed seed), so the numbers never change.
# ----------------------------------------------------------------------------
REGIONS = {
    "Cairo": 0.32, "Giza": 0.18, "Alexandria": 0.16,
    "Delta": 0.14, "Upper Egypt": 0.12, "Canal": 0.08,
}
CHANNELS = {"Website": 0.45, "Mobile App": 0.38, "Marketplace": 0.17}
CATEGORIES = {
    "Electronics": dict(p=0.28, price=4500, cost=0.78,
                        products=["Smart Watch", "Wireless Earbuds", "4K Monitor", "Bluetooth Speaker"]),
    "Home & Kitchen": dict(p=0.22, price=1800, cost=0.66,
                           products=["Air Fryer", "Coffee Maker", "Vacuum Cleaner", "Blender Set"]),
    "Fashion": dict(p=0.20, price=750, cost=0.52,
                    products=["Running Shoes", "Denim Jacket", "Leather Wallet", "Cotton Hoodie"]),
    "Beauty": dict(p=0.12, price=420, cost=0.48,
                   products=["Skincare Set", "Perfume 100ml", "Hair Dryer", "Makeup Kit"]),
    "Grocery": dict(p=0.10, price=350, cost=0.84,
                    products=["Olive Oil Pack", "Coffee Beans 1kg", "Snack Box", "Protein Bars"]),
    "Sports": dict(p=0.08, price=900, cost=0.64,
                   products=["Yoga Mat", "Dumbbell Set", "Fitness Tracker", "Water Bottle"]),
}
MONTH_FACTOR = {1: .92, 2: .90, 3: 1.02, 4: .98, 5: 1.00, 6: .97,
                7: .95, 8: .99, 9: 1.05, 10: 1.08, 11: 1.45, 12: 1.18}


def generate_orders(seed: int = 2026) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    days = pd.date_range("2025-01-01", "2026-09-30", freq="D")
    t = np.arange(len(days))
    month_f = np.array([MONTH_FACTOR[m] for m in days.month])
    weekend_f = np.where(days.dayofweek.isin([4, 5]), 1.25, 1.0)  # Fri/Sat
    lam = 140 * (1 + 0.0011 * t) * month_f * weekend_f
    lam = np.where(days == pd.Timestamp("2025-11-28"), lam * 2.2, lam)  # Black Friday
    counts = rng.poisson(lam)

    date = np.repeat(days.to_numpy(), counts)
    n = len(date)

    cats = list(CATEGORIES)
    category = rng.choice(cats, size=n, p=[CATEGORIES[c]["p"] for c in cats])
    product = np.empty(n, dtype=object)
    price = np.empty(n)
    cost_ratio = np.empty(n)
    for c, meta in CATEGORIES.items():
        m = category == c
        k = int(m.sum())
        product[m] = rng.choice(meta["products"], size=k)
        price[m] = meta["price"] * rng.lognormal(0, 0.35, size=k)
        cost_ratio[m] = meta["cost"]
    price = np.round(price, -1).clip(min=50)

    qty = rng.choice([1, 2, 3], size=n, p=[0.70, 0.22, 0.08])
    discount = rng.choice([0, .05, .10, .15, .20], size=n, p=[.50, .20, .15, .10, .05])

    gross = price * qty
    revenue = gross * (1 - discount)
    cost = gross * cost_ratio

    return pd.DataFrame(
        {
            "order_id": np.arange(100000, 100000 + n),
            "date": pd.to_datetime(date),
            "region": rng.choice(list(REGIONS), size=n, p=list(REGIONS.values())),
            "channel": rng.choice(list(CHANNELS), size=n, p=list(CHANNELS.values())),
            "category": category,
            "product": product,
            "qty": qty,
            "revenue": revenue.round(2),
            "profit": (revenue - cost).round(2),
        }
    )


st.set_page_config(
    page_title="Retail Sales Dashboard | Mohamed Hisham",
    page_icon="📈",
    layout="wide",
)

TEAL, INDIGO, AMBER, ROSE, BLUE, VIOLET = (
    "#0d9488", "#4f46e5", "#d97706", "#e11d48", "#2563eb", "#7c3aed",
)
PALETTE = [TEAL, INDIGO, AMBER, ROSE, BLUE, VIOLET]

st.markdown(
    """
<style>
.block-container {padding-top: 1.6rem;}
[data-testid="stMetric"] {background:linear-gradient(135deg,#111a2b,#0d1424);
    border:1px solid #1f2a44; border-top:4px solid #0d9488; border-radius:12px;
    padding:.9rem 1.1rem;}
div[data-testid="column"]:nth-of-type(2) [data-testid="stMetric"] {border-top-color:#4f46e5;}
div[data-testid="column"]:nth-of-type(3) [data-testid="stMetric"] {border-top-color:#d97706;}
div[data-testid="column"]:nth-of-type(4) [data-testid="stMetric"] {border-top-color:#e11d48;}
h3 {margin-top:.4rem;}
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load() -> pd.DataFrame:
    return generate_orders()


def egp(x: float) -> str:
    if abs(x) >= 1e6:
        return f"EGP {x / 1e6:.2f}M"
    if abs(x) >= 1e3:
        return f"EGP {x / 1e3:.1f}K"
    return f"EGP {x:,.0f}"


def pct_delta(cur: float, prev: float):
    return None if not prev else f"{(cur - prev) / prev * 100:+.1f}%"


def style(fig: go.Figure, height: int = 340) -> go.Figure:
    fig.update_layout(
        template="plotly_dark",
        height=height,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        colorway=PALETTE,
        legend=dict(orientation="h", y=1.12, x=0),
    )
    fig.update_xaxes(gridcolor="rgba(255,255,255,0.07)")
    fig.update_yaxes(gridcolor="rgba(255,255,255,0.07)")
    return fig


df = load()
min_d, max_d = df["date"].min().date(), df["date"].max().date()

# --- Sidebar filters ----------------------------------------------------------
with st.sidebar:
    st.header("Filters")
    picked = st.date_input(
        "Date range",
        value=(max_d - timedelta(days=179), max_d),
        min_value=min_d,
        max_value=max_d,
    )
    regions = st.multiselect("Region", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
    categories = st.multiselect("Category", sorted(df["category"].unique()), default=sorted(df["category"].unique()))
    channels = st.multiselect("Channel", sorted(df["channel"].unique()), default=sorted(df["channel"].unique()))

if not isinstance(picked, (tuple, list)) or len(picked) != 2:
    st.info("Pick an end date to see the dashboard.")
    st.stop()

start, end = picked
length = (end - start).days + 1
prev_end = start - timedelta(days=1)
prev_start = start - timedelta(days=length)


def window(s, e) -> pd.DataFrame:
    return df[
        (df["date"].dt.date >= s)
        & (df["date"].dt.date <= e)
        & df["region"].isin(regions)
        & df["category"].isin(categories)
        & df["channel"].isin(channels)
    ]


cur, prev = window(start, end), window(prev_start, prev_end)

# --- Header ---------------------------------------------------------------------
st.page_link("app.py", label="Back to portfolio", icon="⬅️")
st.title("Retail Sales Performance")
st.caption(f"{start:%d %b %Y} – {end:%d %b %Y} · compared with the previous {length} days")

if cur.empty:
    st.warning("No orders match these filters. Widen the selection in the sidebar.")
    st.stop()


def kpis(d: pd.DataFrame):
    rev, orders = d["revenue"].sum(), len(d)
    return rev, orders, (rev / orders if orders else 0), (d["profit"].sum() / rev if rev else 0)


c_rev, c_ord, c_aov, c_mar = kpis(cur)
p_rev, p_ord, p_aov, p_mar = kpis(prev)

k1, k2, k3, k4 = st.columns(4)
k1.metric("Revenue", egp(c_rev), pct_delta(c_rev, p_rev))
k2.metric("Orders", f"{c_ord:,}", pct_delta(c_ord, p_ord))
k3.metric("Avg. order value", f"EGP {c_aov:,.0f}", pct_delta(c_aov, p_aov))
k4.metric("Profit margin", f"{c_mar * 100:.1f}%", f"{(c_mar - p_mar) * 100:+.1f} pp" if p_ord else None)

# --- Trend ----------------------------------------------------------------------
st.subheader("Revenue & profit trend")
freq = "W" if length > 90 else "D"
ts = (
    cur.set_index("date")
    .resample(freq)
    .agg(revenue=("revenue", "sum"), profit=("profit", "sum"))
    .reset_index()
)
trend = go.Figure()
trend.add_trace(go.Scatter(x=ts["date"], y=ts["revenue"], name="Revenue", mode="lines",
                           line=dict(color=TEAL, width=2.5), fill="tozeroy",
                           fillcolor="rgba(13,148,136,0.18)"))
trend.add_trace(go.Scatter(x=ts["date"], y=ts["profit"], name="Profit", mode="lines",
                           line=dict(color=AMBER, width=2.5)))
st.plotly_chart(style(trend, 360))

# --- Category / channel -----------------------------------------------------------
left, right = st.columns([3, 2])
with left:
    st.subheader("Revenue by category")
    cat = cur.groupby("category", as_index=False)["revenue"].sum().sort_values("revenue")
    fig = px.bar(cat, x="revenue", y="category", orientation="h", text_auto=".3s")
    fig.update_traces(marker_color=INDIGO, textposition="outside")
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    st.plotly_chart(style(fig))
with right:
    st.subheader("Sales by channel")
    ch = cur.groupby("channel", as_index=False)["revenue"].sum()
    fig = px.pie(ch, names="channel", values="revenue", hole=0.62, color_discrete_sequence=PALETTE)
    fig.update_traces(textinfo="percent", marker=dict(line=dict(color="#0a0f1a", width=2)))
    st.plotly_chart(style(fig))

# --- Region / products ------------------------------------------------------------
left, right = st.columns([2, 3])
with left:
    st.subheader("Revenue by region")
    reg = cur.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    fig = px.bar(reg, x="region", y="revenue", text_auto=".3s")
    fig.update_traces(marker_color=TEAL, textposition="outside")
    fig.update_layout(xaxis_title=None, yaxis_title=None)
    st.plotly_chart(style(fig, 360))
with right:
    st.subheader("Top products")
    top = (
        cur.groupby(["product", "category"], as_index=False)
        .agg(revenue=("revenue", "sum"), units=("qty", "sum"), profit=("profit", "sum"))
        .assign(margin=lambda d: d["profit"] / d["revenue"] * 100)
        .sort_values("revenue", ascending=False)
        .head(8)
    )
    st.dataframe(
        top[["product", "category", "units", "revenue", "margin"]],
        hide_index=True,
        column_config={
            "product": "Product",
            "category": "Category",
            "units": st.column_config.NumberColumn("Units", format="%d"),
            "revenue": st.column_config.ProgressColumn(
                "Revenue (EGP)", format="%d", min_value=0, max_value=float(top["revenue"].max())
            ),
            "margin": st.column_config.NumberColumn("Margin", format="%.1f%%"),
        },
    )

# --- Footer -----------------------------------------------------------------------
st.download_button(
    "Download filtered data (CSV)",
    cur.to_csv(index=False).encode("utf-8"),
    file_name="filtered_orders.csv",
    mime="text/csv",
)
st.caption(
    "Demo dashboard built on a synthetic sample dataset (~130K generated orders, EGP) "
    "to showcase analysis and visualization skills. Not real company data."
)
