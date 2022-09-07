from midtransclient import Snap, CoreApi
from flask import Blueprint

config = Blueprint('config', __name__)

snap = Snap(
    is_production=False,
    server_key='SB-Mid-server-dLoBlXm83ImsdCjGhyx7vQYr',
    client_key='SB-Mid-client-zI2gfIxl_2lJFl7X',
)

core = CoreApi(
    is_production=False,
    server_key='SB-Mid-server-dLoBlXm83ImsdCjGhyx7vQYr',
    client_key='SB-Mid-client-zI2gfIxl_2lJFl7X',
)
