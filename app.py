from connexion.resolver import RestyResolver
import connexion
from flask_injector import FlaskInjector
from injector import Binder
from services.provider import ItemsProvider




if __name__ =='__main__':
    app = connexion.App(__name__,host = '0.0.0.0',port= 9090, specification_dir='swagger/')
    app.add_api('first_api.yaml', resolver=RestyResolver('api'))
    app.run()