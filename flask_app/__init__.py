from flask import Flask, render_template, request
import pickle
import pandas as pd

model = None
with open('model.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/measure')
def measure():
    return render_template('measure.html')

@app.route('/result')
def result():
    height = request.args.get("height")
    weight = request.args.get("weight")
    # print(height, weight)

    X = [[height, weight]]
    y_pred = model.predict(X)

    answer = f'당신의 키 : {height}, 당신의 몸무게 : {weight}, 최적의 바지 사이즈 = {round(y_pred[0][0])}'
    return render_template('result.html', answer = answer)


if __name__ == '__main__':
    app.run(debug = True)