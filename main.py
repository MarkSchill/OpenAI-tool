from flask import Flask, render_template, request
app = Flask(__name__)

class IndexForm(Form):
    

@app.route('/', methods=['POST', 'GET'])
def route_index():
    err = None
    if request.method == 'POST':
        print(request.form.get('prompt'))

    return render_template('index.html', error=err)

if __name__ == '__main__':
    app.run()