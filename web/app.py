from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.book import Book
from logic.document import Document
from logic.person import Person
from logic.ado import ADO

app = Flask(__name__)
bootstrap = Bootstrap(app)
# list_person = list()


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
    ado = ADO()
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # data = ' %s, %s ' % (last_name, first_name)
    # list_person.append(Person(name=first_name, last_name=last_name))
    sql = "INSERT INTO person (idperson, name, last_name) VALUES (%s, %s, %s)"
    values = (int(id_person), first_name, last_name)
    data = ado.dml(sql=sql, val=values)
    return render_template('hello.html', value=data)


@app.route('/people')
def people():
    ado = ADO()
    data = ado.query("SELECT idperson, name, last_name FROM gestion_spe.person")
    return render_template('people.html', value=data)


@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/book_result')
def book_result():
    aut1 = Person(name="Christopher", last_name="M.Bishop")
    book = Book(code="0387310738", title="Pattern Recognition and Machine Learning", editorial="Springer",
                pages=738, authors=[aut1], theme="Information Science and Statistics", isbn="978-0387310732")
    return render_template('book_result.html', value=str(book).split('\n'))


@app.route('/document')
def document():
    aut1 = Person(name="Edwin", last_name="Puertas")
    doc = Document(code="0234456", title="New Document", editorial="Springer",
                   pages=100, authors=[aut1], theme="Statistics")
    return render_template('document.html', value=str(doc))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()