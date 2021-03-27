from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/showbio', methods=['GET'])
def showbio():
    username = request.args.get('username')
    age = request.args.get('age')
    email = request.args.get('email')
    hobbies = request.args.get('hobbies')
    AA = ["NICE\n",'AA\n','fffff\n','12345678\n']
    test=''
    for a in AA:
        test+=a

    return render_template("showbio.html",
                           username=username,
                           age=age,
                           email=email,
                           hobbies=hobbies,
                           test=test)

@app.route('/form', methods=['POST', 'GET'])
def bio_data_form():
    if request.method == "POST":
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        hobbies = request.form['hobbies']
        #test = request.form['test']
        return redirect(url_for('showbio',
                                username=username,
                                age=age,
                                email=email,
                                hobbies=hobbies,
                                test=test))
    return render_template("bioform.html")

if __name__ =="__main__":
    app.run(debug=True, port=39003, host='0.0.0.0')
