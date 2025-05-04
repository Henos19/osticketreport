from flask import Blueprint, render_template
from app.models import Ticket, UserEmail

main = Blueprint('main', __name__)


@main.route('/')
def index():
    addresses = UserEmail.query.all()

    return render_template('index.html', addresses=addresses)

