from flaskr import create_app


app = create_app()

@app.route("/")
def a():
    return "ali"

if __name__ == "__main__":
    app.run()
