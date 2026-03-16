from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("phishing_model.pkl","rb"))

# Feature extraction function
def extract_features(url):

    UrlLength = len(url)
    NumDots = url.count('.')
    NumDash = url.count('-')
    AtSymbol = url.count('@')
    NumUnderscore = url.count('_')
    NoHttps = 0 if "https" in url else 1
    PathLength = len(url.split('/')) - 3


    features = [[UrlLength,NumDots,NumDash,AtSymbol,NumUnderscore,NoHttps,PathLength]]

    return features


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():

    url = request.form['url']

    features = extract_features(url)

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Legitimate Website ✅"
    else:
        result = "Phishing Website ⚠️"

    return render_template("index.html",prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)