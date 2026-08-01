from datetime import datetime
from bson import ObjectId

from app import mongo


class Task:
    """Small helper class that wraps the tasks collection in MongoDB."""

    @staticmethod
    def create_task(data):
        task_data = {
            'title': data['title'],
            'description': data.get('description', ''),
            'priority': data.get('priority', 'medium'),
            'deadline': data.get('deadline'),
            'status': 'pending',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
            'history': [],
        }
        task_id = mongo.db.tasks.insert_one(task_data).inserted_id
        return task_id

    @staticmethod
    def get_all_tasks():
        return list(mongo.db.tasks.find())

    @staticmethod
    def get_task_by_id(task_id):
        return mongo.db.tasks.find_one({'_id': ObjectId(task_id)})

    @staticmethod
    def update_task(task_id, update_data):
        # keep a little history when the status changes
        if 'status' in update_data:
            history_entry = {
                'action': 'Status changed to %s' % update_data['status'],
                'timestamp': datetime.utcnow(),
            }
            mongo.db.tasks.update_one(
                {'_id': ObjectId(task_id)},
                {'$push': {'history': history_entry}},
            )
        update_data['updated_at'] = datetime.utcnow()
        result = mongo.db.tasks.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': update_data},
        )
        return result.modified_count > 0

    @staticmethod
    def delete_task(task_id):
        result = mongo.db.tasks.delete_one({'_id': ObjectId(task_id)})
        return result.deleted_count > 0

    @staticmethod
    def get_tasks_by_status(status):
        return list(mongo.db.tasks.find({'status': status}))

    @staticmethod
    def get_tasks_by_priority(priority):
        return list(mongo.db.tasks.find({'priority': priority}))
