from flask import Blueprint, send_file, request

from app.views.utils.create_sheet import create_sheet

from datetime import datetime, timedelta

sheets = Blueprint('sheets', __name__)


@sheets.route('/excel/tickets.xlsx')
def export_tickets():
    office = request.args.get('office', '')
    date_period = request.args.get('date', timedelta(days=7))

    output = create_sheet(office, date_period)

    return send_file(
        output,
        download_name="tickets.xlsx",
        as_attachment=True,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )