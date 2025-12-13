from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-leak', methods=['POST'])
def check_leak():
    query = request.form.get('query')  # accepts email or phone

    if not query:
        return "No input provided", 400

    leaks = []
    with open('leaked_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['value'].strip().lower() == query.strip().lower():
                leaks.append({
                    'platform': row['platform'],
                    'details': row['details']
                })

    return render_template('result.html', query=query, leaks=leaks)


if __name__ == '__main__':
    app.run(debug=True)
