from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel  # Changed to linear_kernel for better performance
import pandas as pd

app = Flask(__name__)

# Load the merged CSV file
df = pd.read_csv("merged_csv.csv")

# Preprocess the data
corpus = df['Question'].fillna("").tolist()  # Fill NaN values with empty strings
answers = df['Answer'].tolist()

# Vectorize the corpus
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

def get_response(query):
    # Vectorize the query
    query_vec = vectorizer.transform([query])
    
    # Calculate cosine similarity between query vector and corpus vectors
    cosine_similarities = linear_kernel(query_vec, X).flatten()  # Changed to linear_kernel
    
    # Get index of most similar question
    idx = cosine_similarities.argsort()[-1]
    
    # Return corresponding answer
    return answers[idx]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_query = request.form["user_query"]
    response = get_response(user_query)
    return response

if __name__ == "__main__":
    app.run(debug=True)
