from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from charts import getVetricalBarChart
from information import biin, fullname_director, director_iin, company_oked, registered_date, company_size, \
    legal_address, nds, licenses, contacts, all_taxes
from tables import tax_table
enc = 'UTF-8'
font = 'Arial'
font_bold = 'Arial-Bold'
pdfmetrics.registerFont(TTFont(font, 'fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont(font_bold, 'fonts/arial_bold.ttf'))

# Content
fileName = 'Отчет Adata.kz.pdf'
documentTitle = 'Отчет Adata.kz'
image = 'images/logo.jpeg'

# create file
pdf = canvas.Canvas(fileName, pagesize=A4)
# set title
pdf.setTitle(documentTitle)


def generate(data):
    y = 800
    # date of report
    pdf.setFont(font_bold, 7)
    pdf.drawString(40, y, f'Отчет сформирован: {data["report_day"]}')
    y -= 15
    # reference to company
    pdf.drawString(40, y, f'https://adata.kz/counterparty/detail/{data["detail"]["biin"]}')
    y -= 5
    # logo
    pdf.drawInlineImage(image, 400, y, width=135, height=45)
    y -= 2
    pdf.line(30, y, 550, y)
    # short name
    y -= 43
    pdf.setFont(font_bold, 11)
    pdf.drawString(40, y, f'{data["detail"]["short_name"]}')

    y -= 25
    pdf.setFont('Arial-Bold', 12)
    pdf.drawString(40, y, f'Основная информация')
    pdf.setFont('Arial', 8)

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, biin)
    textWidth = stringWidth(biin, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["detail"]["biin"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, fullname_director)
    textWidth = stringWidth(fullname_director, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["detail"]["fullname_director"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, director_iin)
    textWidth = stringWidth(director_iin, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["iin_director"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, company_oked)
    textWidth = stringWidth(company_oked, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["oked_and_activity"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, registered_date)
    textWidth = stringWidth(registered_date, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["detail"]["date_registration"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, company_size)
    textWidth = stringWidth(company_size, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["detail"]["krp_name_ru"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, legal_address)
    textWidth = stringWidth(legal_address, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["full_address"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, nds)
    textWidth = stringWidth(nds, font_bold, 8)
    pdf.drawString(textWidth+40, y, f'{data["nds"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, licenses)
    textWidth = stringWidth(licenses, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["licenses"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, contacts)
    pdf.setFont(font, 8)
    pdf.drawString(90, y, f'e-mail: {data["contacts"]["email"]}')

    y -= 15
    pdf.drawString(90, y, f'вебсайт: {data["contacts"]["website"]}')

    y -= 15
    pdf.drawString(90, y, f'телефон: {data["contacts"]["telephone"]}')

    y -= 30
    pdf.setFont(font_bold, 11)
    pdf.drawString(40, y, 'Налоговые отчисления')
    pdf.setFont(font, 8)
    y -= 20
    pdf.setFont(font_bold, 9)
    pdf.drawString(40, y, all_taxes)
    textWidth = stringWidth(all_taxes, font_bold, 9)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth+40, y, f'{data["sum_taxes_str"]} тг')

    table = tax_table(data["taxes_str"], data["percentage_table_str"])
    table.wrap(0, 0)
    table.drawOn(pdf, 50, 50)

    chart = getVetricalBarChart(data["taxes_int"])
    chart.wrap(0, 0)
    chart.drawOn(pdf, 50, 250)
    pdf.save()
