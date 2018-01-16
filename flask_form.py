"""### Zadanie 3
(4 pkt)

Używając Flaska, napisz stronę, która spełni następujące założenia:

1. Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
    * `name`: nazwę produktu (string),
    * `description`: opis produktu (string),
    * `price`: cenę produktu (float).

2. Po wejściu metodą POST:
    * zweryfikuje poprawność danych (ich typy),
    * zapisze te dane do bazy danych do tabeli `Items` (tabela z zadania 1),
    * jeśli którakolwiek dana będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat o błędzie.

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.
"""


from flask import Flask, request, render_template

from mysql.connector import connect

app = Flask(__name__)


cnx = connect(user="root", password="coderslab",
                   host="localhost", database="exam_2")
cursor = cnx.cursor()


@app.route("/", methods=["GET", "POST"])
def put_item():
    if request.method == "GET":
        return render_template("ex3.html")
    else:
        name = request.form["name"]
        desc = request.form["desc"]
        try:
            price = float(request.form["price"])
        except Exception:
            print("Nie udalo sie dodac produktu")
            return "Nie udało się dodać produktu!"

        if price < 10000000 and len(name) < 41 and isinstance(desc, str) and isinstance(name, str):
            insert_item = "INSERT INTO Items(name, description, price) VALUES ('{}', '{}', {})"
            cursor.execute(insert_item.format(name, desc, price))
            cnx.commit()
            return "OK"
        else:
            return "Nie udało się dodać produktu!"

try:
    app.run(debug=True)
finally:
    cursor.close()
    cnx.close()
