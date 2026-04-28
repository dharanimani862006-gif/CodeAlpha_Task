import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("books_advanced.csv")

# Clean Price column (IMPORTANT FIX)
data["Price"] = data["Price"].str.replace("£", "").str.replace("Â", "").astype(float)

# Clean Rating (convert text to number)
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

data["Rating"] = data["Rating"].map(rating_map)

# Set style
sns.set(style="darkgrid")

# -------------------------
# GRAPH 1: Price distribution
# -------------------------
plt.figure(figsize=(8,5))
sns.histplot(data["Price"], bins=10, color="blue")
plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# -------------------------
# GRAPH 2: Rating vs Price
# -------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(x="Rating", y="Price", data=data, color="red")
plt.title("Rating vs Price Analysis")
plt.show()

# -------------------------
# GRAPH 3: Average price per rating
# -------------------------
avg_price = data.groupby("Rating")["Price"].mean()

plt.figure(figsize=(8,5))
avg_price.plot(kind="bar", color="green")
plt.title("Average Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price")
plt.show()

print("✅ Visualization completed successfully!")