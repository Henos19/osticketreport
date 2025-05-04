from flask import Blueprint, render_template
from app.models import Ticket, TicketData
from app.database import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    tickets = Ticket.query.options(db.joinedload(Ticket.tk_data)).all()

    return render_template('index.html', tickets=tickets)

