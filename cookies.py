# from flask import Flask, render_template, url_for, request, make_response
#
# app = Flask(__name__)
#
# menu = [{"title":"Главная", "url":"/"},
#         {"title":"Добавить статью", "url":"/add_post"}]
#
# @app.route("/")
# def index():
#     return "<h1>Main page</h1>"
#
# @app.route("/login")
# def login():
#     log = ""
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
#     res = make_response(f"<h1>Форма авторизации</h1><p>logged: {log}")
#     res.set_cookie("logged", "yes", 30*24*3600)
#     return res
#
# @app.route("/logout")
# def logout():
#     res = make_response("<p>Вы больше не авторизованы!</p>")
#     res.set_cookie("logged", "", 0)
#     return res
#
# if __name__ == "__main__":
#     app.run(debug=True)
