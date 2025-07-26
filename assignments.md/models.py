from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    principal = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    term_months = db.Column(db.Integer)
    emi = db.Column(db.Float)
    payments = db.relationship("Payment", backref="loan", lazy=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey("loan.id"), nullable=False)
    amount = db.Column(db.Float)
    payment_date = db.Column(db.Date)