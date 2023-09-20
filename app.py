from flask import Flask,render_template, redirect, url_for,request

app = Flask(__name__,static_url_path='/static')

@app.route("/")
def base():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/generate",methods=["GET","POST"])
def generate():
    search_text = request.form.get("search_text")
    return f'You entered: {search_text}'




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)