from app.bootstrap import bootstrap
from flask_script import Manager, Server, Shell

app = bootstrap()
manager = Manager(app)

manager.add_command("runserver", Server(host="0.0.0.0", port=5000, threaded=True))

if __name__ == "__main__":
    manager.run()