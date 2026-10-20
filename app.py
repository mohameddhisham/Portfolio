"""Synthetic retail orders for the Sales Dashboard demo.

Deterministic (fixed seed) so the dashboard always shows the same numbers.
Pure pandas/numpy — no Streamlit imports, so it can be tested on its own.
"""
import numpy as np
import pandas as pd

REGIONS = {
    "Cairo": 0.32,
    "Giza": 0.18,
    "Alexandria": 0.16,
    "Delta": 0.14,
    "Upper Egypt": 0.12,
    "Canal": 0.08,
}

CHANNELS = {"Website": 0.45, "Mobile App": 0.38, "Marketplace": 0.17}

CATEGORIES = {
    "Electronics": dict(
        p=0.28, price=4500, cost=0.78,
        products=["Smart Watch", "Wireless Earbuds", "4K Monitor", "Bluetooth Speaker"],
    ),
    "Home & Kitchen": dict(
        p=0.22, price=1800, cost=0.66,
        products=["Air Fryer", "Coffee Maker", "Vacuum Cleaner", "Blender Set"],
    ),
    "Fashion": dict(
        p=0.20, price=750, cost=0.52,
        products=["Running Shoes", "Denim Jacket", "Leather Wallet", "Cotton Hoodie"],
    ),
    "Beauty": dict(
        p=0.12, price=420, cost=0.48,
        products=["Skincare Set", "Perfume 100ml", "Hair Dryer", "Makeup Kit"],
    ),
    "Grocery": dict(
        p=0.10, price=350, cost=0.84,
        products=["Olive Oil Pack", "Coffee Beans 1kg", "Snack Box", "Protein Bars"],
    ),
    "Sports": dict(
        p=0.08, price=900, cost=0.64,
        products=["Yoga Mat", "Dumbbell Set", "Fitness Tracker", "Water Bottle"],
    ),
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
