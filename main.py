from json import dumps
from flask import Flask, render_template, request, redirect, jsonify,Blueprint
from routers.user_controller import user_controller
import pandas as pd
data_frame = pd.read_csv('./jobs.csv')
app = Flask(__name__)
app.register_blueprint(user_controller, url_prefix='/user')
@app.route("/",methods=["GET"])
def get_items():
    return jsonify([])
app.run(debug=True,host='0.0.0.0')