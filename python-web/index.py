from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trabajo')
def trabajo():
    return render_template('trabajo.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/plantilla')
def plantilla():
    return render_template('plantilla.html')
if __name__=='__name__':
    app.run()
