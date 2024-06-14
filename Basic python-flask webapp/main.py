from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1><p><h2>My name is Rutuj Kiran Chordiya <br> </h2> </p> <p> <h4> This is a basic Flask web application that I've created to test out various Devops tools and practices like jenkins.</h4> </p>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
