from contextlib import redirect_stdout
from typing import List
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.datastructures import FileStorage
import json
from pydoc import render_doc
from flask import Flask, redirect, render_template, url_for, flash, request, jsonify
from collections import OrderedDict


app = Flask(__name__, template_folder='C:/Users/hanna/own/templates')

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/songsorters", methods=['GET', 'POST'])
def songsorters():
    return render_template("sorters.html")

if __name__ == "__main__":
    app.run("0.0.0.0")
