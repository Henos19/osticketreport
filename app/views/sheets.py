from flask import Blueprint, send_file, request

from app.views.utils.create_sheet import create_sheet

from datetime import datetime, timedelta

sheets = Blueprint('sheets', __name__)


@sheets.route('/excel/tickets.xlsx')
def export_tickets():
    office = request.args.get('office')
    init_date = request.args.get('initDate')
    end_date = request.args.get('endDate')

    if init_date == "":
        init_date = datetime.now().date() - timedelta(days=7)
    else:
        init_date = datetime.strptime(init_date, "%Y-%m-%d")


    if end_date == "":
        end_date = datetime.now().date()
    else:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    output = create_sheet(office, init_date, end_date)

    return send_file(
        output,
        download_name="tickets.xlsx",
        as_attachment=True,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )