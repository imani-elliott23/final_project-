from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Load workouts from a JSON file
def load_workouts():
    if os.path.exists('workouts.json'):
        with open('workouts.json', 'r') as file:
            return json.load(file)
    return []

# Save workouts to a JSON file
def save_workouts(workouts):
    with open('workouts.json', 'w') as file:
        json.dump(workouts, file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_workout', methods=['POST'])
def add_workout():
    workouts = load_workouts()
    workout = {
        'date': request.form['date'],
        'exercise': request.form['exercise'],
        'duration': request.form['duration'],
        'notes': request.form['notes']
    }
    workouts.append(workout)
    save_workouts(workouts)
    return redirect(url_for('home'))

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = load_workouts()
    return jsonify(workouts)

@app.route('/delete_workout/<int:index>', methods=['DELETE'])
def delete_workout(index):
    workouts = load_workouts()
    if 0 <= index < len(workouts):
        workouts.pop(index)
        save_workouts(workouts)
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error'}), 400

if __name__ == '__main__':
    app.run(debug=True)