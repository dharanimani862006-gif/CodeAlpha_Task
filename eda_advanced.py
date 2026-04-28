import pandas as pd


print("📂 Loading dataset...")
data = pd.read_csv("books_advanced.csv")


# -----------------------------------
# DATA OVERVIEW
# -----------------------------------
print("\n🔍 Dataset Preview:")
print(data.head())

print("\n📊 Dataset Shape:")
print("Rows:", data.shape[0], "| Columns:", data.shape[1])


# -----------------------------------
# CLEANING DATA
# -----------------------------------
print("\n🧹 Cleaning data...")

# Clean price
data["Price"] = (
    data["Price"]
    .str.replace("£", "", regex=True)
    .str.replace("Â", "", regex=True)
    .astype(float)
)

# Convert rating to numbers
rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
data["Rating"] = data["Rating"].map(rating_map)


# -----------------------------------
# BASIC STATISTICS
# -----------------------------------
print("\n📈 Basic Statistics:")
print(data.describe())


# -----------------------------------
# CATEGORY CREATION (NEW IDEA 🔥)
# -----------------------------------
print("\n🏷️ Creating price categories...")

def price_category(price):
    if price < 20:
        return "Low Price"
    elif price < 40:
        return "Medium Price"
    else:
        return "High Price"

data["Price Category"] = data["Price"].apply(price_category)


# -----------------------------------
# GROUP ANALYSIS
# -----------------------------------
print("\n📊 Books count by Rating:")
print(data["Rating"].value_counts())

print("\n💰 Average Price per Rating:")
print(data.groupby("Rating")["Price"].mean())

print("\n🏷️ Price Category Count:")
print(data["Price Category"].value_counts())


# -----------------------------------
# TOP & BOTTOM DATA
# -----------------------------------
print("\n🏆 Top 5 Expensive Books:")
print(data.sort_values(by="Price", ascending=False).head())

print("\n📉 Cheapest 5 Books:")
print(data.sort_values(by="Price").head())


# -----------------------------------
# INSIGHTS SECTION (VERY IMPORTANT 🔥)
# -----------------------------------
print("\n🧠 INSIGHTS:")

avg_price = data["Price"].mean()
print(f"👉 Average book price is: {avg_price:.2f}")

most_common_rating = data["Rating"].mode()[0]
print(f"👉 Most common rating is: {most_common_rating}")

high_price_count = len(data[data["Price"] > 40])
print(f"👉 Number of high priced books: {high_price_count}")


# -----------------------------------
# SAVE CLEANED DATA
# -----------------------------------
data.to_csv("eda_processed_data.csv", index=False, encoding="utf-8-sig")

print("\n✅ Advanced EDA Completed!")
print("📁 Cleaned file saved as eda_processed_data.csv")