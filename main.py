from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1><p>My name is Rutuj Kiran Chordiya and this is a basic Flask web application that I've created to test out various Devops tools and practices using AWS services only.</p>"

if __name__ == '__main__':
    app.run(debug=True,)