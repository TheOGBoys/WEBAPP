from flask import Blueprint, render_template

#AIL INI 17.12.22
views = Blueprint('views', __name__) 

@views.route('/')
def home():
    return render_template("home.html")
#AIL END 17.12.22