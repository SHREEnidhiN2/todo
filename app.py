# #pip install flask
# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# tasks = []  #list of tasks


# @app.route('/')
# def home():
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add_task():
#     task = request.form.get('task')
#     if task:
#         tasks.append(task)
#     return redirect('/')

# @app.route('/delete/<int:index>')
# def delete_task(index):
#     if 0 <= index < len(tasks):
#         tasks.pop(index)
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)
