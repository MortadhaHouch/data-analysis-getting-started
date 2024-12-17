from json import dumps
from flask import Flask, render_template, request, redirect, jsonify,Blueprint
import pandas as pd
from routers.data_controller import data_controller
from routers.user_controller import user_controller
data_frame = pd.read_csv('./jobs.csv')
app = Flask(__name__)
app.register_blueprint(user_controller, url_prefix='/user')
app.register_blueprint(data_controller,url_prefix='/data')
@app.route("/",methods=["GET"])
def get_items():
    return jsonify([])
app.run(debug=True,port=3000,host='0.0.0.0')