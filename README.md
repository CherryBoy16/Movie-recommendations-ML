# Movie-recommendations-ML
This is a Movie Recommendation System built using Flask and Machine Learning. The system takes movie name, user ID, and rating as input and provides movie recommendations based on a trained model.

🚀 How It Works?

User Input:
The user enters a movie name, user ID, and rating in the web application.
Data Processing:
The input is converted into numerical form and passed to a trained RandomForestRegressor model.
Prediction:
The model predicts a recommendation score and returns a list of recommended movies.
Display Output:
The recommended movies are displayed on the web page.
🛠️ Tech Stack Used

Python
Flask (Backend Framework)
Scikit-Learn (Machine Learning)
NumPy & Pandas (Data Processing)
HTML & CSS (Frontend)
📂 Project Structure

📁 Movie-Recommendation
│── app.py                  # Flask Backend  
│── movie_recommendation.pkl # Trained Machine Learning Model  
│── templates/  
│   └── index.html           # Frontend (HTML Page)  
│── static/  
│   └── style.css            # Stylesheet  
│── requirements.txt         # Dependencies  
│── README.md                # Project Documentation  
🔧 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/movie-recommendation.git  
cd movie-recommendation  
2️⃣ Install Dependencies
pip install -r requirements.txt  
3️⃣ Run the Application
python app.py  
The Flask server will start, and you can access the app at:
http://127.0.0.1:8080/


This project is open-source and free to use under the MIT License.

