from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.book import Book
from logic.document import Document
from logic.person import Person
from logic.ado import ADO

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_update/<id_person>', methods=['GET'])
def person_update(id_person):
    return render_template('person_update.html', id_person=id_person)


@app.route('/person_detail', methods=['POST'])
def person_detail():
    ado = ADO()
    op = request.form['op']
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if op == 'I':
        sql = "INSERT INTO person (idperson, name, last_name) VALUES (%s, %s, %s)"
        values = (int(id_person), first_name, last_name)
        data = ado.dml(sql=sql, val=values, op='I')
    elif op == 'U':
        sql = 'UPDATE person SET name={0}{2}{0}, last_name={0}{3}{0} WHERE idperson={1}'.format('"', int(id_person),
                                                                                                first_name, last_name)
        data = ado.dml(sql=sql, op='U')
    return render_template('person_detail.html', value=data)


@app.route('/person_delete/<id_person>', methods=['GET'])
def person_delete(id_person):
    ado = ADO()
    sql = 'DELETE FROM person WHERE idperson={0}'.format(int(id_person))
    data = ado.dml(sql=sql, op='D')
    return render_template('person_detail.html', value=data)


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


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()