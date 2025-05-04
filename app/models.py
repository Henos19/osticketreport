from app.database import db


class Ticket(db.Model):
    __tablename__ = 'ost_ticket'

    ticket_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    isanswered = db.Column(db.String(255))

    tk_data = db.relationship('TicketData', backref='Ticket', lazy=True)
    tk_email = db.relationship('User', backref='Ticker', lazy=True)


class TicketData(db.Model):
    __tablename__ = 'ost_ticket__cdata'

    ticket_id = db.Column(db.Integer, db.ForeignKey('ost_ticket.ticket_id'), primary_key=True)
    subject = db.Column(db.String(255))


class User(db.Model):
    __tablename__ = 'ost_user_email'

    user_id = db.Column(db.Integer, db.ForeignKey('ost_ticket.user_id'), primary_key=True)
    address = db.Column(db.String(255))

