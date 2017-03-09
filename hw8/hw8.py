from flask import Flask, json, request, abort, jsonify
from flask_wtf import FlaskForm
import locale
from wtforms import StringField, PasswordField, validators, ValidationError


app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'qwerty',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})


def password_validator(form, field):
    if field.data != form.data['password']:
        raise ValidationError('Неправильный пароль')


class UserForm(FlaskForm):
    email = StringField('Email',validators=[
        validators.Email(),
        validators.InputRequired(message='Поле не может быть пустым')
    ])
    password = PasswordField('Пароль', validators=[
        validators.InputRequired(message='Поле не может быть пустым'),
        validators.length(min=6), validators.EqualTo('password_confirmation', message='Пароли должны совпадать')
    ])
    password_confirmation = PasswordField('Подтверждение пароля')


# По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']

@app.route('/locales')
def print_locales():
      return jsonify({locl: locale.locale_alias[locl] for locl in ['ru', 'en', 'it']})


# По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму


@app.route('/sum/<int:first>/<int:second>')
def summing(first, second):
    return str(first + second)


# По адресу /greet/<user_name> должен получать имя пользователя,
# возвращать текст 'Hello, имя_которое_прислали'

@app.route('/greet/<user_name>')
def greet_user(user_name):
    return 'Hello, %s' % user_name


# По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают.
# Возрващать пользователю json вида: "status" - 0 или 1 (если ошибка валидации),
# "errors" - список ошибок, если они есть, или пустой список.

@app.route('/form/user', methods=['POST'])
def post_data():
    status = 0
    if request.method == 'POST':
        user_form = UserForm(request.form)
        if not user_form.validate():
            status = 1
    return jsonify({'status': status, 'errors': user_form.errors})


# По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files.
# Файлы можно туда положить любые текстовые. А если такого нет - 404


@app.route('/serve/<path:filename>', methods=['GET'])
def get_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run()