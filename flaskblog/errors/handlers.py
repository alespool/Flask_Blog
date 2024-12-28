from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    """
    Handler for 404 errors. Renders the 404.html template and returns a 404 status code.
    """
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    """
    Handler for 403 errors. Renders the 403.html template and returns a 403 status code.
    """
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    """
    Handler for 500 errors. Renders the 500.html template and returns a 500 status code.
    """
    return render_template('errors/500.html'), 500