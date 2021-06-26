from flask import *

app = Flask(__name__)


@app.route("/")
def start():
    title="This is a homepage for Dictionary"
    text="Please, use /dictionary to go to dictionary"

    return render_template("homepage.html", title=title,text=text)

@app.route("/dictionary")
def lib():
    list=['a','b','c','d','e','f','g','h' ,'i' ,'j', 'k' ,'l','m' ,'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return render_template("dictionary.html",list=list)
@app.route('/dictionary/<string:word>')
def dictionary(word):
    f=open("real_words.txt")
    words=f.read().splitlines()
    is_real_word=word in words
    count=0
    for w in words:
        if w.startswith(word):
            count+=1
    list=['a','b','c','d','e','f','g','h' ,'i' ,'j', 'k' ,'l','m' ,'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return render_template("picked.html",words=words,list=list,word=word,is_real_word=is_real_word,count=count)

