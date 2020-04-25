from sklearn import tree
import csv
import sys
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data',methods=['POST'])
def runModel():
    data = request.get_json()
    features = []
    labels = []
    with open('./static/daily.csv', newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            date = row[0].split("-")
            features.append(date)
            labels.append(row[1])


    clf = tree.DecisionTreeClassifier();

    clf.fit(features, labels)

    return str(clf.predict([[data['year'],data['month'],data['day']]])).split("[")[1].split("]")[0].split("'")[1]
    
    

if __name__ == "__main__":
    app.run(debug=True)

