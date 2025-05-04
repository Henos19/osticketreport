from sqlalchemy import func
from app.models import UserEmail
from app.database import db

def group_domain_names():
    domain_expr = func.substring_index(UserEmail.address, '@', -1)

    results = (
        db.session.query(
            domain_expr.label('domain'),
            func.count().label('total')
        )
        .group_by(domain_expr)
        .order_by(func.count().desc())
        .all()
    )

    return results

