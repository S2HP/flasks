from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def start():
    return render_template('ee.html')

@app.route('/sveiki')
def sveiki():
    visi_vardi = ['lapsene', 'Jānis', 'pasaule']
    return render_template('sveiki.html', vards=visi_vardi)

@app.route('/sveiki/<vards>')
def sveiki1(vards):
    visi_vardi = ['lapsene', 'Jānis', 'pasaule', vards]
    return render_template('sveiki.html', vards=visi_vardi)




if __name__ == '__main__':
    app.run(threaded=True, port=5000)