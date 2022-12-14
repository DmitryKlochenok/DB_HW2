# УРОК 16 Задание 8
# В этом финальном задании вам нужно
# применить знания о моделях для создания 3 представлений,
# которые реализуют запросы на создание, добавление, удаление.

"""
    # Задание
    # Шаг 1.
    # ######
    # Создайте представение для эндпоинта GET /guides
    # которое возвращает список всех гидов со всеми полями
    # в формате JSON
    #
    #
    # Шаг 2.
    # ######
    # - Создайте представение для эндпоинта GET /guides/{id}
    # которое возвращает одного гида со всеми полями
    # в формате JSON в соответствии с его id
    #
    # Шаг 3.
    # ######
    # Создайте представение для эндпоинта
    # GET /guides/{id}/delete`, которое удаляет
    # одного гида в соответствии с его `id`
    #
    # Шаг 4.
    # ######
    # Создайте представление для эндпоинта POST /guides
    #  которое добавляет в базу данных гида, при получении
    # следующих данных:
    # {
    #     "surname": "Иванов",
    #     "full_name": "Иван Иванов",
    #     "tours_count": 7,
    #     "bio": "Провожу экскурсии",
    #     "is_pro": true,
    #     "company": "Удивительные экскурсии"
    # }
    # Шаг 5.
    # ######
    # - Допишите представление из шага 1 для фильтрации так,
    # чтобы при получении запроса типа /guides?tours_count=1
    # возвращались гиды с нужным количеством туров.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from guides_sql import CREATE_TABLE, INSERT_VALUES
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
app.app_context().push()
db = SQLAlchemy(app)
with db.session.begin():
    db.session.execute(text(CREATE_TABLE))
    db.session.execute(text(INSERT_VALUES))


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)

# TODO напишите роуты здесь
@app.route("/guides")
def guides_page(charset='utf-8'):
    query = Guide.query.all()
    result = []
    for item in query:
        result.append({
            'surname': item.surname,
            'full_name': item.full_name,
            'tours_count': item.tours_count,
            'bio': item.bio,
            'is_pro': item.is_pro,
            'company': item.company
        })

    return json.dumps(result).encode(charset)
# которое возвращает список всех гидов со всеми полями
# в формате JSON

@app.route("/guides/<int:id>")
def guide_id_page(id):
    pass
# которое возвращает одного гида со всеми полями
# в формате JSON в соответствии с его id

@app.route("/guides/<int:id>/delete")
def delete_guide_page(id):
    pass
# которое удаляет
# одного гида в соответствии с его `id`

@app.route("/guides", methods = ["POST"])
def post_guide_page():
    pass
# Создайте представление для эндпоинта POST /guides
    #  которое добавляет в базу данных гида, при получении
    # следующих данных:
    # {
    #     "surname": "Иванов",
    #     "full_name": "Иван Иванов",
    #     "tours_count": 7,
    #     "bio": "Провожу экскурсии",
    #     "is_pro": true,
    #     "company": "Удивительные экскурсии"
    # }


@app.route("/guides/<int:tk>")
def guides_search_page(tk):
    pass
 # - Допишите представление из шага 1 для фильтрации так,
    # чтобы при получении запроса типа /guides?tours_count=1
    # возвращались гиды с нужным количеством туров.

if __name__ == "__main__":
    app.run()
