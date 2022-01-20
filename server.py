from flask import Flask,render_template

app = Flask(__name__)

@app.route('/play' , methods=['GET'])
def nivel1():
    return render_template("index.html")

@app.route('/play/<int:num>' , methods=['GET'])
def nivel2(num):
    return render_template("index1.html",numero=num)

@app.route('/play/<int:num>/<color>', methods=['GET'])
def nivel3(num,color):
    return render_template("index2.html",numero=num, col=color)

if __name__ == "__main__":
    app.run(debug=True)
