from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ARE YOU READY TO BOX?!'

@app.route('/play')
def play():
    return render_template("index.html", num = 3, color = "blue")

@app.route('/play/<int:num>')
def playnum(num):
    return render_template("index.html", num = num, color = "blue")

@app.route('/play/<int:num>/<color>')
def playground(num, color):
    return render_template("index.html", num = num, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.