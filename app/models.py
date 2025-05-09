from app.database import db


class Ticket(db.Model):
    __tablename__ = 'ost_ticket'

    ticket_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('ost_user_email.user_id'))
    created = db.Column(db.DateTime)
    closed = db.Column(db.DateTime)
    number = db.Column(db.Integer)


    tk_data = db.relationship('TicketData', lazy=True)
    tk_email = db.relationship('UserEmail', lazy=True)
    tk_name = db.relationship('UserName', lazy=True)
    tk_title = db.relationship('TicketTitle', lazy=True)


class TicketData(db.Model):
    __tablename__ = 'ost_ticket__cdata'

    ticket_id = db.Column(db.Integer, db.ForeignKey('ost_ticket.ticket_id'), primary_key=True)
    subject = db.Column(db.String(255))


class UserEmail(db.Model):
    __tablename__ = 'ost_user_email'

    user_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))


class UserName(db.Model):
    __tablename__ = 'ost_user'

    id = db.Column(db.Integer, db.ForeignKey('ost_ticket.user_id'), primary_key=True)
    name = db.Column(db.String(64))


class TicketTitle(db.Model):
    __tablename__ = 'ost__search'

    object_id = db.Column(db.Integer, db.ForeignKey('ost_ticket.ticket_id'), primary_key=True)
    content = db.Column(db.String(255))
