
# Macro Engine v2
# Sources:
# Reuters
# ForexFactory
# Investing
# DailyFX
# Forexlive
# FXStreet
# CoinDesk
# Cointelegraph
# CryptoPanic
# Binance
# CME
# CFTC
# EIA
# OPEC
# Kitco
# USDA
# PBoC
# Fed
# ECB
# BoJ
# BoE
# BoC

# Slot format:
# timestamp|asset|type|impact|source|headline

# type:
# NEWS
# CFTC
# CME
# CENTRAL_BANK
# COMMODITY
# CRYPTO






















import os
from datetime import datetime

slots = [
    "09:30|CADJPY|CENTRAL_BANK|HIGH|BOJ|BOJ hawkish statement",
    "10:00|DXY|NEWS|HIGH|Reuters|US CPI beats estimates",
    "11:00|XAUUSD|CFTC|MEDIUM|CFTC|Commercial longs increased",
    "12:00|BTCUSD|CME|HIGH|CME|Open interest surges",
    "13:00|USDCAD|COMMODITY|HIGH|EIA|Oil inventories fall",
    "14:00|AUDUSD|NEWS|MEDIUM|China|China PMI weakens",
    "15:00|EURUSD|CENTRAL_BANK|HIGH|ECB|Lagarde speech begins",
    "16:00|GBPUSD|CENTRAL_BANK|HIGH|BOE|BoE policy statement",
    "17:00|USDJPY|NEWS|HIGH|Reuters|US yields jump",
    "18:00|ETHUSD|CRYPTO|MEDIUM|CoinDesk|Ethereum ETF rumours",
    "19:00|WTI|COMMODITY|HIGH|OPEC|Production cut extended",
    "20:00|XAGUSD|COMMODITY|MEDIUM|Kitco|Silver demand rises",
    "21:00|CORN|COMMODITY|MEDIUM|USDA|Crop yield lowered",
    "22:00|DXY|CME|HIGH|FedWatch|Rate cut odds fall"
]

os.makedirs("data", exist_ok=True)

for i in range(14):
    with open(f"data/MACRO_SLOT_{i+1}.txt", "w") as f:
        f.write(slots[i])

print("Macro slots updated")
