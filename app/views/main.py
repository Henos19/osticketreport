from flask import Blueprint, render_template, jsonify
from app.models import Ticket
from app.views.utils.group_domain_names import group_domain_names
from app.views.utils.group_all_tickets_from_domain import group_all_tickets_from_domain

main = Blueprint('main', __name__)


@main.route('/test')
def test_view():
    tickets = Ticket.query.all()

    return render_template('test.html', tickets=tickets)


@main.route('/')
def index():
    domains = group_domain_names()

    return render_template('home.html', domains=domains)


@main.route('/graph-data')
def get_graph_data():
    all_tickets = group_all_tickets_from_domain()

    labels = [row[0] for row in all_tickets]
    values = [row[1] for row in all_tickets]

    return jsonify({'labels': labels, 'values': values})
