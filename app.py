from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from models.user import User
import datetime
from bson import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = '6cf33ee1e56cea559886c225561a9672'

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['polling_db']
polls_collection = db['polls']

@app.route('/')
def index():
    polls = list(polls_collection.find())
    return render_template('index.html', polls=polls)

@app.route('/create_poll', methods=['GET', 'POST'])
def create_poll():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        question = request.form['question']
        options = request.form.getlist('option')
        poll_data = {
            'question': question,
            'options': {opt: 0 for opt in options},
            'created_at': datetime.datetime.utcnow(),
            'created_by': session['username']
        }
        polls_collection.insert_one(poll_data)
        return redirect(url_for('index'))
    return render_template('create_poll.html')

# Inside your Flask application
# @app.route('/vote/<int:poll_id>', methods=['GET', 'POST'])
# def polls(poll_id):
#     poll = Poll.query.get_or_404(poll_id)
#     if request.method == 'POST':
#         option = request.form.get('option')
#         if option and option in [poll.option1, poll.option2, poll.option3, poll.option4]:
#             vote = Vote(poll_id=poll_id, option=option)
#             db.session.add(vote)
#             db.session.commit()
#             return redirect(url_for('index'))
#         else:
#             return 'Invalid option', 400
#     return render_template('polls.html', poll=poll)


@app.route('/poll/<poll_id>', methods=['GET', 'POST'])
def view_poll(poll_id):
    poll = polls_collection.find_one({'_id': ObjectId(poll_id)})
    if not poll:
        flash('Poll not found.', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        selected_option = request.form.get('option')  # Use request.form.get() to safely retrieve the value
        if selected_option:  # Check if selected_option is not None or empty
            polls_collection.update_one(
                {'_id': ObjectId(poll_id)},
                {'$inc': {f'options.{selected_option}': 1}}
            )
            flash('Vote counted successfully!', 'success')
            return redirect(url_for('index' ))
        else:
            flash('Please select an option before submitting.', 'error')
            return redirect(url_for('index'))

    return render_template('view_poll.html', poll=poll)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.register(username, password):
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'error')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
