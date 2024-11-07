from flask import Flask, render_template, request, redirect, url_for 
#Flask: application itself, render_template: allows us to work with html files, request: access post request data and form data from html file, redirect: allows us to redirect to different endpoints, url_for: allows us to get url for respective endpoints dynamically so we don;t have to do that manually

app = Flask(__name__, template_folder="templates") #templates directory is where html files will be located

#define basic end point

todos = [] #list of tasks/todos. Each todo will be a dict item like this ->  {"todo": "taskName", "done": True}

@app.route("/") #route / leads to index
def index(): #index function renders html template
    return render_template("index.html", todos=todos) #pass todos to index.html file

@app.route("/add", methods=["POST"]) 
def add():
    todo = request.form['todo'] #todo will be whatever we get from that html file
    todos.append({"task": todo, "done": False}) #add a new task/todo to list of todos, since this is a list of dict items, append a new dict item to list
    return redirect(url_for("index")) #then automatically redirect to index

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index): #changing existing task
    todo = todos[index] #todo we wanna edit is toda at this index
    if request.method == "POST":
        todo['task'] = request.form["todo"] #todo task will be equal to whatever we have in the form
        return redirect(url_for("index")) #then automatically redirect to index
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done'] #unchecking
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)