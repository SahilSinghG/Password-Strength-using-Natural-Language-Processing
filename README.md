# 🔐 Password Strength Prediction using NLP

## 📌 Project Overview

Passwords are the first line of defense in digital security. Weak passwords are highly vulnerable to brute-force attacks, dictionary attacks, and other security threats. Identifying the strength of a password can help users create more secure credentials.

This project builds a Machine Learning model that predicts the strength of a password using Natural Language Processing (NLP) techniques. The model analyzes patterns in passwords and classifies them into different strength categories.

The project demonstrates a complete machine learning workflow, including data preprocessing, feature extraction, model training, evaluation, and deployment through an interactive web application.

## Project Structure

<img width="722" height="462" alt="image" src="https://github.com/user-attachments/assets/79af7584-d2f6-47a8-a539-4017b87a4796" />

## 🎯 Problem Statement

The goal of this project is to build a classification model that can automatically determine whether a password is:

Weak
Medium
Strong

The model learns patterns from historical password data and predicts password strength based on character composition, length, and structural patterns.

## 📊 Dataset

The dataset used in this project contains approximately 670,000 passwords with labeled strength values.

Dataset Features
Column	Description
password	The password text
strength	Label indicating password strength
Strength Labels
Value	Meaning
0	Weak
1	Medium
2	Strong

<img width="960" height="686" alt="image" src="https://github.com/user-attachments/assets/8fc75eea-ca0c-492b-9a68-b43a5a9f1c6d" />


This dataset allows the model to learn patterns such as:

Presence of numbers
Use of special characters
Character combinations
Password length patterns

## 🧠 Machine Learning Approach

The project follows a standard NLP classification pipeline.

1️⃣ Data Loading

The dataset is loaded into a Pandas DataFrame for preprocessing and analysis.

df = pd.read_csv("data.csv")

2️⃣ Data Cleaning

Missing values were removed to ensure data consistency.

df.dropna(inplace=True)

3️⃣ Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand the distribution of password strength classes.

Visualizations such as count plots were used to inspect the dataset balance.

<img width="828" height="671" alt="image" src="https://github.com/user-attachments/assets/e8d1f7ed-5d2a-4b26-a381-8385a88565eb" />

4️⃣ Feature Extraction (TF-IDF)

Machine learning algorithms cannot process raw text directly. Therefore, passwords were converted into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency).

Character-level vectorization was used so that the model can learn patterns like:

numbers
symbols
uppercase characters
repeated patterns
vectorizer = TfidfVectorizer(analyzer="char")
X = vectorizer.fit_transform(passwords)

5️⃣ Train-Test Split

The dataset was divided into training and testing sets.

Training Data (80%) – used to train the model
Testing Data (20%) – used to evaluate performance
train_test_split(X, y, test_size=0.2, random_state=42)

## 🤖 Models Used

Several classification algorithms were tested.

Logistic Regression

A linear model commonly used for classification tasks.

Multinomial Naive Bayes

A probabilistic model particularly effective for text classification problems.

<img width="726" height="267" alt="image" src="https://github.com/user-attachments/assets/0112be77-9fae-4a41-b3b6-6c64d40209e9" />

Among these models, Logistic Regression performed best for this NLP problem due to its efficiency with text-based feature distributions.

## 📈 Model Performance

The model achieved very high performance on the test dataset.

Typical results:

Accuracy: 84%

Evaluation metrics used:

Accuracy
Precision
Recall
F1 Score

<img width="683" height="221" alt="image" src="https://github.com/user-attachments/assets/94df24b5-57f6-489d-8daf-751e2306a035" />

These metrics confirm that the model successfully learns patterns associated with strong and weak passwords.

## 💾 Model Saving

The trained model and TF-IDF vectorizer were saved using pickle for later use in the deployed application.

pickle.dump(model, open("model.pkl","wb"))
pickle.dump(vectorizer, open("vectorizer.pkl","wb"))

## 🌐 Deployment

The trained model was deployed using Streamlit, allowing users to interact with the model through a web interface.

Users can input a password and receive an instant prediction of its strength.

Example workflow:

User enters password → Model processes text → Prediction returned

Example:

Input: P@ssw0rd123
Output: Strong

<img width="1417" height="578" alt="image" src="https://github.com/user-attachments/assets/81c89046-da15-47f0-8898-a8d8107aba32" />


## 🚀 How to Run the Project

Clone the repository
git clone https://github.com/SahilSinghG/Password-Strength-using-Natural-Language-Processing.git

Install dependencies
pip install -r requirements.txt
Run the Streamlit application
streamlit run app/app.py

The application will open in your browser.

## 🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Matplotlib
Seaborn

## 📌 Key Skills Demonstrated

This project highlights several important data science skills:

Natural Language Processing (NLP)
Text Feature Engineering
TF-IDF Vectorization
Machine Learning Classification
Model Evaluation
Model Deployment with Streamlit

## 📊 Future Improvements

Possible improvements include:

Implementing deep learning models such as LSTM or Transformers
Adding password entropy calculations
Integrating password security recommendations
Deploying the application using Docker or FastAPI

## 👨‍💻 Author

Sahil Singh

Machine Learning & Data Science Enthusiast

GitHub:
https://github.com/SahilSinghG
