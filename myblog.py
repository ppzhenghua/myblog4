from app import create_app,db
from app.models import User, Post
from flask_script import Shell
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from flask_bootstrap import Bootstrap

app=create_app()
manager = Manager(app)
bootstrap=Bootstrap(app)

@app.shell_context_processor
def make_shell_context():
    return {app:'app','db': db, 'User': User, 'Post': Post}

manager.add_command("shell",Shell(make_context=make_shell_context, use_ipython=True))
manager.add_command("db", MigrateCommand)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
    manager.run()


