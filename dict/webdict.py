from flask import Flask,render_template
from flask import request
from mydict import Youdao
app = Flask(__name__)

@app.route('/showdict', methods=['GET'])
def showdict():
    username = request.args.get('word')
    y = Youdao(username)
    if  y.istypo():
        typo = y.gettypos()
        return render_template("showdict1.html",username=username, typo=typo)
    ch = y.getch()
    ee = y.geten()
    bl = y.getbilng()
    rel = y.getrels()
    pho = y.getphone()
    phr = y.getphrase()
    syno = y.getsyno()
    print(syno)
    sen = y.getsentence()

    return render_template("showdict.html",
                           username=username,
                           ch=ch, ee=ee,bl=bl, rel=rel, pho=pho, phr=phr, syno=syno,sen=sen)

@app.route('/', methods=['POST', 'GET'])
def dict_form():
    if request.method == "POST":
        username = request.form['word']
        print(username)
        return redirect(url_for('showdict',
                                username=username
                                ))
    return render_template("dict.html")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')
