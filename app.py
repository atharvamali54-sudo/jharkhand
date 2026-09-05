from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/university')
def university():
    return render_template('university.html')

@app.route('/industry')
def industry():
    return render_template('industry.html')

if __name__ == '__main__':
    app.run(debug=True)
