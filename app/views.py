import flask
from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
from app import app
import pandas as pd

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/hypothesis')
def hypothesis():
    return render_template("hypothesis.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    df = pd.read_csv("C:\\Users\\rober\\VSProject\\StrokePrediction\\data\\data.csv")
    column = request.form['column']
    if not column:
        return render_template("data.html", tables=[df.to_html(classes='data')])
    return render_template("data.html", tables=[df[column].to_html(classes='data')]) 
