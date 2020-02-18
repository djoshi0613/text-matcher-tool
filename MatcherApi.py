import flask
from flask import render_template, request

from StringMatcher import calculateSimilarityIndex

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        text1 = request.form['text1']
        print(text1)
        text2 = request.form['text2']

        similarity_index = calculateSimilarityIndex(text1, text2)
        return 'Similarity scale is %s' % similarity_index
    else:
        return render_template("home.html")

app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)