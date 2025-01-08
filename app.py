import os
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the TODO API!'})

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('task')
    todos.append({'id': len(todos) + 1, 'task': todo})
    return jsonify({'message': 'Todo added!'})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return jsonify({'message': 'Todo deleted!'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)
