import os

basedir = os.path.abspath(os.path.dirname(__file__))

# giving access to the project in any OS we find ourselves in
# allow outside files/folders to have the ability to add to the project from
#the base directory

class Config():
    """
    we will set config variables for the flask App here.
    Using Enviroment variable where available, otherwise
    we will create the config variable(s) if not already done
    """
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'You will never guess...'
    SQLALCHEMY_DATABASE_URI= os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False #TURN OFF UPDATE MESSAGES FROM THE DATABASE
    