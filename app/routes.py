from flask import render_template, request
import csv
import os

CSV_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'leaked_data.csv')

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/check-leak', methods=['POST'])
    def check_leak():
        query = request.form.get('query')

        if not query:
            return "No input provided", 400

        leaks = []
        try:
            with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row.get('value', '').strip().lower() == query.strip().lower():
                        leaks.append({
                            'platform': row.get('platform', 'N/A'),
                            'details': row.get('details', 'N/A')
                        })
        except FileNotFoundError:
            return "Error: leaked_data.csv not found.", 500
        except Exception as e:
            return f"An error occurred: {e}", 500

        return render_template('result.html', query=query, leaks=leaks)
