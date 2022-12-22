from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json
from .manager import *


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/fixcode', methods=['GET', 'POST'])
@login_required
def generateCode():
    if request.method == "POST":
        
        language = request.form["language"]
        text = request.form["code"]

        response = generateCodeAI(text, language)

        return render_template("fixcode.html", result=response, user=current_user)

    result = request.args.get("result")
    return render_template("fixcode.html", result=result, user=current_user)
