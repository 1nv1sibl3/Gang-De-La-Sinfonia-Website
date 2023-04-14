from flask import Flask, render_template 
import os

app = Flask(__name__)

app.template_folder = 'static/'
app.static_folder = 'assets/'
app.static_url_path = 'assets/'


@app.route('/')
def home():
    print(os.system('ls'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8004, debug=True)