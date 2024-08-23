from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY']= 'dghsdghs3478dsfhuy4hjhkdfjflddkl'

menu = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Обратная связь', 'url': 'contact'},
    {'name': 'О ВУЗе', 'url': 'about'}
]

@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 1:
            flash("Сообщение отправлено успешно", category='success')
            print(request.form)
        else:
            flash("Ошибка отправки", category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route('/about')
def about():
    print(url_for("about"))
    return render_template("about.html", title='О ВУЗе', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)




