from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = ""
<!DOCTYPE html>


<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    
    </head>

    <h1>"text below"</h1>
    
    <body>
        <form method='POST'>
             
             <label for="rot">Rotate by: </label>
            <input type="text" id="rot" name="rot" value=0 /><br />
            <textarea name="text">{0}</textarea><br />
            <button type="submit" value="submit">Submit Query</button>
    
      <!-- create your form here -->
    
    </body>

</html>


@app.route("/")
def index():
    return form.format('')

@app.route('/', methods=['POST'])

def encrypt():
	rot = request.form['rot']
	text = request.form['text']
	message = rotate_string(text, rot)
	return form.format(message) 

app.run()
