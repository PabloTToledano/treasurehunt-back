#!/usr/bin/env python3

import connexion
from flask_cors import CORS

from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Treasure Hunt'})
CORS(app.app)

if __name__ == '__main__':
    app.run()


