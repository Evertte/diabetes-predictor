# 🩺 Diabetes Prediction Web App

This is a machine learning project that predicts whether an individual is likely to have diabetes based on personal health information. The prediction is powered by a trained classification model, and the interface is built using [Streamlit](https://streamlit.io/), making it easy to use and share with others.

## 🔍 Features

- Predict diabetes likelihood based on:
  - Gender
  - Age
  - Hypertension
  - Heart Disease
  - BMI
  - HbA1c Level
  - Blood Glucose Level
  - Smoking History
- Clean and intuitive Streamlit web interface
- Instant feedback with visual alerts
- Easy to deploy and share with friends

## 🧠 Model

The model was trained using a dataset containing labeled examples of individuals with and without diabetes. It includes health-related features and lifestyle habits. The model was serialized using `joblib` and loaded into the app for real-time inference.

## 📦 Technologies Used

- Python
- Pandas, scikit-learn
- Streamlit
- Joblib

## 🚀 How to Run the App

1. Clone this repository:
   ```bash
   git clone https://github.com/Evertte/diabetes-prediction-app.git
   cd diabetes-prediction-app
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the file `Diabetes_prediction.pkl` is in the same directory as `app.py`.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
├── app.py                   # Streamlit web app
├── Diabetes_prediction.pkl  # Trained model file
├── README.md                # Project README
└── requirements.txt         # Python dependencies
```

## 🌐 Deploy

You can deploy this app on:

- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [Render](https://render.com)
- [Railway](https://railway.app)
- [Heroku](https://heroku.com)

Let me know if you want a deployment guide!

## 📬 Contact

For questions or feedback, feel free to reach out via [GitHub Issues](https://github.com/Evertte/diabetes-prediction-app/issues) or email me directly.

---
