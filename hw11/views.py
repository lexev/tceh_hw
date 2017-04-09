from flask import Blueprint, request, render_template,flash
from forms import PostForm, TagForm, UserForm
from database import db

posts_views = Blueprint('posts', __name__, url_prefix='/posts', template_folder='templates')
tags_views = Blueprint('tags', __name__, url_prefix='/tags', template_folder='templates')
user_views = Blueprint('users', __name__, url_prefix='/users', template_folder='templates')


@tags_views.route('/create/', methods=['POST'])
def create_tag():
    from models import Tag
    flash(request.form)
    form = TagForm(request.form)
    tag = Tag(tagname=form.tagname.data)
    db.session.add(tag)
    db.session.commit()
    return 'Тэг создан'


@posts_views.route('/create/', methods=['POST', 'GET'])
def create_post():
    from models import Post
    if request.method == 'POST':
        flash(request.form)
        form = PostForm(request.form)
        post = Post(**form.data)
        db.session.add(post)
        db.session.commit()
        return 'Пост создан!'
    posts = Post.query.all()
    return render_template('posts.txt', posts=posts)


@user_views.route('/create/', methods=['POST'])
def create_user():
    from models import User
    flash(request.form)
    form = UserForm(request.form)
    user = User(**form.data)
    db.session.add(user)
    db.session.commit()
    return 'Пользователь создан!'


@posts_views.route('/vis/')
def visible_posts():
    from models import Post
    posts = Post.query.filter(Post.is_visible == False).order_by(Post.date_created)
    return render_template('posts.txt', posts=posts)


@posts_views.route('/slug/<slug>/')
def show_by_slug(slug):
    from models import Post
    post = Post.query.filter(Post.slugfield == slug)
    return render_template('posts.txt', posts=post)


@tags_views.route('/vis/')
def visible_tags():
    from models import Tag
    tags = Tag.query.all()
    return render_template('tags.txt', tags=tags)
