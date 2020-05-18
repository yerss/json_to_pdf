from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def tax_table(taxes_str, percentage_table):
    # table style
    pdfmetrics.registerFont(TTFont('Arial', 'fonts/arial.ttf'))
    data = [['Год', 'Налоговые отчисления', '%']]
    for key in taxes_str:
        data.append([f'{key} г.', f'{taxes_str[key]} тг', percentage_table[key]])

    style = [
        ('BACKGROUND', (0, 0), (3, 0), colors.cornflowerblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTNAME', (2, 0), (-1, -1), 'Arial-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (1, 0), (-1, -1), 150),
        ('RIGHTPADDIG', (0, 0), (-1, -1), 150),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
        ('LINEABOVE', (0, 1), (-1, -1), 0.5, colors.black)
    ]

    for i in range(2, len(data)):
        if '-' in data[i][2]:
            bc = colors.red
        else:
            bc = colors.green
        style.append(('TEXTCOLOR', (2, i), (-1, i), bc))

    table = Table(data)
    table.setStyle(TableStyle(style))
    return table