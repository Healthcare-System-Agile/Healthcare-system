from flask import Flask, render_template_string, request

app = Flask(__name__)

MODULES = [
    "Production Management",
    "Batch Tracking",
    "Quality Control",
    "Inventory Management",
    "Approval Workflow",
    "Dashboard and Notifications",
]

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Healthcare Solutions</title>
    <style>
        body {
            font-family: Arial;
            max-width: 850px;
            margin: 40px auto;
            padding: 20px;
            background: #f4f7fb;
        }
        .panel {
            background: white;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
            box-sizing: border-box;
            padding: 12px;
        }
        button {
            background: #1769aa;
            color: white;
            padding: 12px 20px;
            border: 0;
            border-radius: 6px;
            cursor: pointer;
        }
        li { padding: 7px; }
    </style>
</head>
<body>
    <h1>AI Healthcare Solutions Delivery System</h1>
    <p>TraceLink-inspired pharmaceutical solution generator</p>
    <div class="panel">
        <h2>Describe your requirements</h2>
        <form method="post">
            <textarea
                name="requirement"
                placeholder="Describe your medicine manufacturing needs..."
                required
            >{{ requirement }}</textarea>
            <p><button type="submit">Generate Solution</button></p>
        </form>
        {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
    </div>
    {% if modules %}
    <div class="panel">
        <h2>Generated Solution Modules</h2>
        <ul>
        {% for module in modules %}
            <li>{{ module }}</li>
        {% endfor %}
        </ul>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    modules = None
    error = None
    requirement = ""

    if request.method == "POST":
        requirement = request.form.get("requirement", "").strip()
        if not requirement:
            error = "Please enter your requirements."
        else:
            modules = MODULES

    return render_template_string(
        PAGE,
        requirement=requirement,
        modules=modules,
        error=error,
    )

if __name__ == "__main__":
    app.run(debug=True)
