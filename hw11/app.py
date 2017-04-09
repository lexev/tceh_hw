from flask import Flask
from views import tags_views, posts_views
import config
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(tags_views)
    app.register_blueprint(posts_views)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
