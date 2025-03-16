#pip install flask flask-sqlalchemy
#database integrated
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'Task {self.id}: {self.content}'

# Create the database
with app.app_context():
    db.create_all()

# Home Page - Show Tasks
@app.route('/')
def home():
    tasks = Task.query.all()  # Fetch tasks from the database
    return render_template('index4.html', tasks=tasks)

# Add a New Task
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        new_task = Task(content=task_content)  # Create new task
        db.session.add(new_task)  # Add to database
        db.session.commit()  # Save changes
    return redirect('/')

# Delete a Task
@app.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get(id)  # Get task by ID
    if task:
        db.session.delete(task)  # Remove from database
        db.session.commit()  # Save changes
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
