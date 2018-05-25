from flask import render_template
from app import main


@main.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
