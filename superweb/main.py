from wsgiref.simple_server import make_server

import falcon

from superweb.resources import ToDo, JsonHello, ToDoList, ToDoJsonList

app = falcon.API()

todo = ToDo()
json_hello = JsonHello()
todo_list = ToDoList()
json_todo_list = ToDoJsonList()

app.add_route('/todo/add', todo)
app.add_route('/todo/', todo_list)
app.add_route('/json_hello', json_hello)
app.add_route('/json_todo_list', json_todo_list)

if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    print("Serving on port 8000...")
    httpd.serve_forever()
