from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# GST Verify Route
@app.route("/verify")
def verify():
    gstin = request.args.get("gstin")

    url = f"https://gst-return-status.p.rapidapi.com/free/gstin/{gstin}"   # ⚠️ yaha correct endpoint dalna hai

    headers = {
	"x-rapidapi-key": "4ed8201f08mshd71c9fe2e71734ap17e0d6jsn559706f3e3f2",
	"x-rapidapi-host": "gst-return-status.p.rapidapi.com",
	"Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, params={"gstin": gstin})

        if response.status_code == 200:
            try:
                data = response.json()
                return jsonify(data)
            except:
                return jsonify({
                    "error": "Invalid JSON response",
                    "raw": response.text
                })
        else:
            return jsonify({
                "error": "API Error",
                "status_code": response.status_code,
                "details": response.text
            })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)