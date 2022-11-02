from app import app, jsonify, abort, make_response, request
from app.database.database import *


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/categories', methods=['GET'])
def get_all_categories():
    return jsonify({'categories': CATEGORIES})


@app.route('/categories/<int:categories_id>', methods=['GET'])
def get_category(categories_id):
    category = list(filter(lambda t: t['id'] == categories_id, CATEGORIES))
    if len(category) == 0:
        abort(404)
    else:
        return jsonify({'categories': category[0]})


@app.route('/categories', methods=['POST'])
def create_category():
    if not request.json or not 'category_name' in request.json:
        abort(400)
    category = {
        'id': CATEGORIES[-1]['id'] + 1,
        'category_name': request.json.get('category_name')
    }
    CATEGORIES.append(category)
    return jsonify({'category': category}), 201


@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': USERS[-1]['id'] + 1,
        'name': request.json.get('name')
    }
    USERS.append(user)
    return jsonify({'user': user}), 201


@app.route('/records', methods=['POST'])
def create_record():
    if not request.json:
        abort(400)
    fields_in = ['user_id', 'category_id', 'date_time', 'total']
    fields_in = list(filter(lambda t: t in request.json, fields_in))
    if len(fields_in) != 4:
        abort(400)
    category = list(filter(lambda t: t['id'] == request.json.get('category_id'), CATEGORIES))
    if len(category) == 0:
        abort(400)
    users = list(filter(lambda t: t['id'] == request.json.get('user_id'), USERS))
    if len(users) == 0:
        abort(400)
    record = {
        'id': RECORDS[-1]['id'] + 1,
        'user_id': request.json.get('user_id'),
        'category_id': request.json.get('category_id'),
        'date_time': request.json.get('date_time'),
        'total': request.json.get('total')
    }
    RECORDS.append(record)
    return jsonify({'record': record}), 201


@app.route('/records/<int:user_id>', methods=['GET'])
def get_record_by_user(user_id):
    record_by_user = list(filter(lambda t: t['user_id'] == user_id, RECORDS))
    if len(record_by_user) == 0:
        abort(404)
    else:
        return jsonify({'records_by_user': record_by_user})


@app.route('/records/<int:user_id>/<int:category_id>', methods=['GET'])
def get_record_by_user_and_category(user_id, category_id):
    record_by_user = list(filter(lambda t: t['user_id'] == user_id, RECORDS))
    if len(record_by_user) == 0:
        abort(404)
    record_by_category_and_user = list(filter(lambda t: t['category_id'] == category_id, record_by_user))
    if len(record_by_category_and_user) == 0:
        abort(404)
    else:
        return jsonify({'records_by_user_and_category': record_by_category_and_user})
