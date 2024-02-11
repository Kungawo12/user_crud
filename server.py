from flask import Flask,render_template,request,redirect
from user import User
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all_users())

@app.route('/users/new')
def new():
    return render_template("new_users.html")

@app.route('/users/create', methods=['POST'])
def create():
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        }
    User.create(data)
    return redirect('/users')

@app.route('/users/<int:id>')
def show_user(id):
    data = { 
            "id":id
            }
    return render_template("show_user.html",user=User.show_user(data))

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit.html",user=User.show_user(data))

@app.route('/users/update/<int:id>',methods=["POST"])
def update(id):
    data = {
            'id': id,
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        }
    User.update(data)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')
    
if __name__ =="__main__":
    app.run(debug=True, port=5001)