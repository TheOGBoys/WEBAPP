from website import create_app

app = create_app()

#AIL INI 17.12.22
#@app.route("/")
#def home():
#    return "this is the home page"
#AIL END 17.12.22

if __name__ == '__main__':
    app.run(debug=True, port=8000)