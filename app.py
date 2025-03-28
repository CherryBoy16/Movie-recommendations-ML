from flask import Flask, request, render_template
import pickle
import numpy as np
with open("movie_recommendation.pkl", "rb") as f:
    model = pickle.load(f)
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict_recommendations():
    try:
        movie_id = int(request.form.get('movie_id'))  
        user_id = int(request.form.get('user_id')) 
        rating = float(request.form.get('rating')) 
        recommendation_score = model.predict(np.array([[movie_id, user_id, rating]]))[0]
        if recommendation_score > 8:
            recommended_movies = "Inception, Interstellar, The Dark Knight"
        elif recommendation_score > 6:
            recommended_movies = "Iron Man, Avengers, Doctor Strange"
        else:
            recommended_movies = "Titanic, The Notebook, The Fault in Our Stars"
        return render_template('index.html', result=recommended_movies)
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")
if __name__ == '__main__':
    app.run(debug=True, port=8080)
