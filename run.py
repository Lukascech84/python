from app import app
from flask_babel import Babel

babel = Babel(app)

app.run(host="0.0.0.0", port=8080, debug=True)
