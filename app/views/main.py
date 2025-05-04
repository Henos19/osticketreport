from flask import Blueprint, render_template
from app.models import Ticket

main = Blueprint('main', __name__)


@main.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

