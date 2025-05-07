from app.models import Ticket, UserEmail
from app.database import db
from sqlalchemy import func
from datetime import timedelta, datetime


def group_all_tickets_from_domain():
    period = datetime.now() - timedelta(days=14)

    domain_expr = func.substring_index(UserEmail.address, '@', -1)

    subquery = (
        db.session.query(
            domain_expr.label('domain'),
            func.count(Ticket.ticket_id).label('total_tickets'),
        )
        .filter(Ticket.created >= period)
        .join(Ticket.tk_email)
        .group_by(domain_expr)
        .subquery()
    )

    all_tickets = db.session.query(subquery.c.domain, subquery.c.total_tickets).all()

    return all_tickets

