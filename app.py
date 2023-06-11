from src import app,app_debug

if __name__ == "__main__":
    app.run(debug=app_debug,port=8080, host="0.0.0.0")
