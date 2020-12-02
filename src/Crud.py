"""
This script contain all functions about CRUD system
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from ManageDatabase import ManageDatabase
from User import User
import sys
# initializations
app = Flask(__name__)

# settings
app.secret_key = "iethae8oohoocohSieXiich3o"
md = ManageDatabase()
md.create_scheme()

# routes
@app.route('/')
def Index():
    data = md.get_all_users()
    print(data)
    return render_template('index.html', users = data)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        user = User(name = request.form['name'],lastname = request.form['lastname'],birthday = request.form['birthday'],cellphone = request.form['cellphone'],email = request.form['email'])
        md.insert_user(user)
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_domain(id):
    user_tmp = md.get_user(id)
    data = [ user_tmp.get_id(), user_tmp.get_name(), user_tmp.get_lastname(),user_tmp.get_birthday(),user_tmp.get_cellphone(),user_tmp.get_email() ]
    return render_template('edit-user.html', user = data)

@app.route('/update/<id>', methods=['POST'])
def update_domain(id):
    if request.method == 'POST':
        user = User(id,name = request.form['name'],lastname = request.form['lastname'],birthday = request.form['birthday'],cellphone = request.form['cellphone'],email = request.form['email'])
        md.update_user(user)
        return redirect(url_for('Index'))

@app.route('/delete/<id>', methods = ['POST','GET'])
def delete_domain(id):
    md.delete_user(id)
    return redirect(url_for('Index'))