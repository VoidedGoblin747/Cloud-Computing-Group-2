from flask import render_template, request, redirect, url_for, jsonify
from datetime import datetime

from app import app
from app.models import Task


@app.route('/')
def index():
    """Dashboard - show all tasks."""
    tasks = Task.get_all_tasks()
    # high priority first, then soonest deadline
    priority_order = {'high': 0, 'medium': 1, 'low': 2}
    tasks.sort(key=lambda x: (priority_order.get(x.get('priority', 'medium'), 2),
                              x.get('deadline') or '9999-12-31'))
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_data = {
            'title': request.form['title'],
            'description': request.form.get('description', ''),
            'priority': request.form.get('priority', 'medium'),
            'deadline': request.form.get('deadline'),
        }
        # make sure the deadline is a real date, otherwise ignore it
        if task_data['deadline']:
            try:
                datetime.strptime(task_data['deadline'], '%Y-%m-%d')
            except ValueError:
                task_data['deadline'] = None
        Task.create_task(task_data)
        return redirect(url_for('index'))
    return render_template('add_task.html')


@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.get_task_by_id(task_id)
    if not task:
        return redirect(url_for('index'))

    if request.method == 'POST':
        update_data = {
            'title': request.form['title'],
            'description': request.form.get('description', ''),
            'priority': request.form.get('priority', 'medium'),
            'deadline': request.form.get('deadline'),
            'status': request.form.get('status', 'pending'),
        }
        Task.update_task(task_id, update_data)
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)


@app.route('/delete/<task_id>')
def delete_task(task_id):
    Task.delete_task(task_id)
    return redirect(url_for('index'))


@app.route('/complete/<task_id>')
def complete_task(task_id):
    Task.update_task(task_id, {'status': 'completed'})
    return redirect(url_for('index'))


# ---- JSON API (Goal #2 - APIs on App Engine) ----

@app.route('/api/tasks', methods=['GET'])
def api_get_tasks():
    tasks = Task.get_all_tasks()
    for task in tasks:
        task['_id'] = str(task['_id'])
        if isinstance(task.get('created_at'), datetime):
            task['created_at'] = task['created_at'].strftime('%Y-%m-%d %H:%M')
        if isinstance(task.get('updated_at'), datetime):
            task['updated_at'] = task['updated_at'].strftime('%Y-%m-%d %H:%M')
    return jsonify(tasks)


@app.route('/api/tasks/<task_id>', methods=['GET'])
def api_get_task(task_id):
    task = Task.get_task_by_id(task_id)
    if task:
        task['_id'] = str(task['_id'])
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404


@app.route('/api/tasks', methods=['POST'])
def api_create_task():
    data = request.json
    task_id = Task.create_task(data)
    return jsonify({'id': str(task_id), 'message': 'Task created successfully'}), 201


@app.route('/api/tasks/<task_id>', methods=['PUT'])
def api_update_task(task_id):
    data = request.json
    Task.update_task(task_id, data)
    return jsonify({'message': 'Task updated successfully'})


@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    Task.delete_task(task_id)
    return jsonify({'message': 'Task deleted successfully'})


@app.route('/health')
def health():
    return 'ok', 200
