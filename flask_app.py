from flask import Flask
import os
import logging, logging.config, yaml

def initialise_main():
    logging.config.dictConfig(yaml.load(open('logging.yaml')))
    logfile = logging.getLogger('file')
    logconsole = logging.getLogger('console')
    # logfile.debug("Debug write on FILE")
    # logconsole.debug("Debug write on CONSOLE")
    logging.basicConfig(filename='beebot_flask_server.log',level=logging.INFO)

def main():
    logging.info('test')
    app = Flask(__name__)
    FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    FLASK_PORT = os.environ.get('FLASK_PORT', '3000')

    @app.route("/")
    def hello():
        # import ipdb; ipdb.set_trace()
        app.logger.info('')
        return "Hello World!"

    app.run(host=FLASK_HOST, port=FLASK_PORT)


if __name__ == '__main__':
    initialise_main()
    main()

