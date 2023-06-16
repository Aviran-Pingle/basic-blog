from flask import Flask

from routes import bp


def main():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.run()


if __name__ == '__main__':
    main()
