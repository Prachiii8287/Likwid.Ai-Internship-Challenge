# ### app.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from customer_utils import process_excel_file, get_dashboard_data
# from google_sheets import sync_to_sheet, sync_from_sheet
# import os

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/upload", methods=["POST"])
# def upload_file():
#     file = request.files.get("file")
#     if not file:
#         return jsonify({"error": "No file uploaded"}), 400

#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)

#     process_excel_file(filepath)
#     sync_to_sheet()
#     return jsonify({"message": "File processed successfully"})

# @app.route("/dashboard", methods=["GET"])
# def dashboard():
#     data = get_dashboard_data()
#     return jsonify(data)

# @app.route("/sync", methods=["GET"])
# def sync():
#     sync_from_sheet()
#     return jsonify({"message": "Synced from Google Sheet"})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from customer_utils import process_excel_file, get_dashboard_data
from google_sheets import sync_to_sheet, sync_from_sheet
import os

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Create upload directory if not exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route (useful for checking if API is running)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running!"})

# Upload Excel file route
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        process_excel_file(filepath)
        sync_to_sheet()
        return jsonify({"message": "File processed and synced successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Dashboard data route
@app.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        data = get_dashboard_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Sync data from Google Sheets
@app.route("/sync", methods=["GET"])
def sync():
    try:
        sync_from_sheet()
        return jsonify({"message": "Data synced from Google Sheets successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
