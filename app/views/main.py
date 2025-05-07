from flask import Blueprint, render_template
from app.models import Ticket
from app.views.utils.group_domain_names import group_domain_names

main = Blueprint('main', __name__)


@main.route('/test')
def test_view():
    tickets = Ticket.query.all()

    return render_template('test.html', tickets=tickets)


@main.route('/')
def index():
    domains = group_domain_names()

    return render_template('home.html', domains=domains)

