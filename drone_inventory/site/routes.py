from flask import Blueprint, render_template
from flask_login import login_required
site = Blueprint('site',__name__, template_folder='site_templates')

"""
blueprint config
the first arguement, 'site' is the the blueprint's name
which is used by flasks routing system

the second arguement, __name__, is the blueprints import name,
which flask uses to locate the blueprint resources

the last arguement, 'template_folder' is the blueprints html template folder
which tellls the blueprint which html files to use for specific routes
"""

@site.route('/') #main page : a route is just the url
def home():
    return render_template('index.html') 

@site.route('/profile')
def profile():
    return render_template('profile.html')