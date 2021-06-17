from flask import Flask,request,render_template


app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')
database={'ashu_shota_don':'9876381859'}


@app.route('/form_login',methods=['post','get'])

def login():

    name1=request.form['username']
    hgt = request.form['height']
    wgt = request.form['weight']
    out = float(wgt)*100
    outs=out/float(hgt)
    outss=outs/float(hgt)
    outsss=outss*100
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='invalid user')

    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='invalid password')
        else:
            if outsss>24:
                return render_template('login.html',bmi='do workout your bmi should be lie between 19-24 and your bmi is {}'.format(outsss))
            if outsss < 19:
                return render_template('login.html', bmi='eat something buddy your bmi ,your bmi should be lie between 19-24 your bmi is {}'.format(outsss))
            else:
                return render_template('login.html',bmi='you are perfectly fit your bmi is between 19-24 {}'.format(outsss))

if __name__== '__main__':
    app.run()