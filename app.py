from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']

        # Check if the file is empty
        if file.filename == '':
            return render_template('index.html', message='No selected file')

        # Check if the file is a CSV
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)

            # Display the DataFrame in the HTML template
            return render_template('index.html', table=df.to_html(classes='data', header='true'))

        else:
            return render_template('index.html', message='Invalid file format. Please upload a CSV file.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
