from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# store workouts temporarily in memory
workouts = []

@app.route("/")
def home():
    return render_template("index.html", workouts=workouts)

@app.route("/add", methods=["POST"])
def add_workout():
    workout = request.form.get("workout")
    duration = request.form.get("duration")

    if not workout or not duration:
        return "Please enter both workout and duration. <a href='/'>Go Back</a>"
    if not workout.replace(" ", "").isalpha():
        return "Workout must contain only letters. <a href='/'>Go Back</a>"

    try:
        duration = int(duration)
        if duration <= 0:
            return "Duration must be greater than 0. <a href='/'>Go Back</a>"
        workouts.append({"workout": workout, "duration": duration})
        return redirect(url_for("home"))
    except ValueError:
        return "Duration must be a number. <a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
