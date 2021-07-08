from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.Book import Book
from logic.Document import Document
from logic.Person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)

list_person = list()


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
    identity = request.form['identity']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    data = '%s: %s, %s' % (identity, last_name, first_name)
    list_person.append(Person(id=int(identity), name=first_name, last_name=last_name))
    return render_template('hello.html', value=data)


@app.route('/people')
def people():
    return render_template('people.html', value=list_person)


@app.route('/book')
def book():
    aut1 = Person(id=112233, name="Christopher", last_name="M.Bishop")
    book = Book(code="0387310738", title="Pattern Recognition and Machine Learning", editorial="Springer",
                pages=738, authors=[aut1], theme="Information Science and Statistics", isbn="978-0387310732")
    return render_template('book.html', value=str(book).split('\n'))


@app.route('/document')
def document():
    aut1 = Person(id=1234567, name="Edwin", last_name="Puertas")
    doc = Document(code="0234456", title="New Document", editorial="Springer",
                   pages=100, authors=[aut1], theme="Statistics")
    return render_template('document.html', value=str(doc))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()