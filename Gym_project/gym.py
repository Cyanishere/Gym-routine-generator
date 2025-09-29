from flask import Flask, render_template, request   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)
df = pd.read_csv('megaGymDataset.csv', index_col='Title')
Bodyparts = df.BodyPart.value_counts().index.tolist()
best_exercises_dict = dict()
for i in Bodyparts:
    Top_10 = df[df['BodyPart']==i].sort_values('Rating',ascending=False)[0:10]
    best_exercises_dict[i] = Top_10.index.tolist()

@app.route('/')
def index():
    return render_template('gym_input.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('TDEE.html')

@app.route('/routine',methods=["GET", "POST"])
def routine():
    global best_exercises_dict
    selected_part = None
    if request.method == "POST":
        selected_part = request.form.get("part")
    return render_template('routine.html',parts_dict=best_exercises_dict,selected_part=selected_part)


if __name__ == '__main__':
    app.run(debug=True)