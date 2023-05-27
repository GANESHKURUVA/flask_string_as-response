from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/firsttemplate')
def firsttemplate():
    return render_template('firsttemplate.html')


@FAI.route('/data_send')
def data_send():
    return render_template('data_send.html',name='GANESH',age=21)


if __name__=='__main__':
    FAI.run(debug=True)
