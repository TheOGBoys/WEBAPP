from website import create_app

app = create_app()

@app.route("/")
def home():
    return "this is the home page"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

