import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
file_path='/Users/sricharan/Downloads/movie_recommendation_dataset.xlsx'
df = pd.read_excel(file_path)
required_columns = ["movie_id", "movie_name", "user_id", "rating", "recommendation_score"]
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Missing required columns: {set(required_columns) - set(df.columns)}")
df["movie_name"] = df["movie_name"].str.lower()
X = df[["movie_id", "user_id", "rating"]]
y = df["recommendation_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
with open("movie_recommendation.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model trained and saved as movie_recommendation.pkl")
