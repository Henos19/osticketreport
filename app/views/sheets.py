from flask import Blueprint, render_template
from flask import send_file
import pandas as pd
from io import BytesIO
from app.models import Ticket

sheets = Blueprint('sheets', __name__)


@sheets.route('/excel/tickets.xlsx')
def export_tickets():
    tickets = Ticket.query.all()
    data = [{
        'Data de Criação': tck.created,
        'Nome': tck.tk_name[0].name,
        'Conteúdo': tck.tk_title[0].content,
        'Ticket': tck.number,
        'Data de Finalzação': tck.closed,
    } for tck in tickets]

    df = pd.DataFrame(data)

    output = BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Customers')

    output.seek(0)

    return send_file(
        output,
        download_name="tickets.xlsx",
        as_attachment=True,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


