from flask import Blueprint, render_template
from app.models import Ticket, TicketData
from app.database import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

