import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '46ca2defb01cc7f0b122f36e6ca22e1x'

baixados = os.path.join(app.root_path, 'static/videos_baixados')
os.makedirs(baixados, exist_ok=True)

from YT import routes