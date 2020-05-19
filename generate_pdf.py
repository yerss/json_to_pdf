from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from charts import getVetricalBarChart
from information import biin, fullname_director, director_iin, company_oked, registered_date, company_size, \
    legal_address, nds, licenses, contacts, all_taxes, wrong_address, inactive, false_company, tax_violation, \
    invalid_reg, bankrupt, bankrupt_completed, bankrupt_at_stage, leaving_restriction, courtcase_company, \
    enforcement_debt, tax_debt, goszakup_reliable, goszakup_unreliable, samruk_reliable, samruk_unreliable, \
    gos_contracts, nadloc, i_courtcases, i_terror_excluded, i_pedophil, i_terror_active, i_missing, i_alimony, \
    i_leaving_restriction, i_enforcement_debt, i_enforcement_document, i_criminal
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

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, biin)
    textWidth = stringWidth(biin, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["detail"]["biin"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, fullname_director)
    textWidth = stringWidth(fullname_director, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["detail"]["fullname_director"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, director_iin)
    textWidth = stringWidth(director_iin, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["iin_director"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, company_oked)
    textWidth = stringWidth(company_oked, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["oked_and_activity"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, registered_date)
    textWidth = stringWidth(registered_date, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["detail"]["date_registration"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, company_size)
    textWidth = stringWidth(company_size, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["detail"]["krp_name_ru"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, legal_address)
    textWidth = stringWidth(legal_address, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["full_address"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, nds)
    textWidth = stringWidth(nds, font_bold, 8)
    pdf.drawString(textWidth + 40, y, f'{data["nds"]}')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, licenses)
    textWidth = stringWidth(licenses, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, f'{data["licenses"]}')

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
    pdf.drawString(textWidth + 40, y, f'{data["sum_taxes_str"]} тг')

    table = tax_table(data["taxes_str"], data["percentage_table_str"])
    table.wrap(0, 0)
    table.drawOn(pdf, 50, 50)

    chart = getVetricalBarChart(data["taxes_int"])
    chart.wrap(0, 0)
    chart.drawOn(pdf, 50, 250)

    pdf.showPage()

    # Second page
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

    # Благонадежность
    y -= 38
    pdf.setFont(font_bold, 12)
    pdf.drawString(40, y, f'Благонадежность:')

    # Предприятие
    y -= 25
    pdf.setFont(font_bold, 9)
    pdf.drawString(40, y, f'Предприятие:')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, wrong_address)
    textWidth = stringWidth(wrong_address, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['wrong_address'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, inactive)
    textWidth = stringWidth(inactive, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['inactive'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, false_company)
    textWidth = stringWidth(false_company, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['false_company'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, invalid_reg)
    textWidth = stringWidth(invalid_reg, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['invalid_reg'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, tax_violation)
    textWidth = stringWidth(tax_violation, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['tax_violation'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, bankrupt)
    textWidth = stringWidth(bankrupt, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['bankrupt'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, bankrupt_completed)
    textWidth = stringWidth(bankrupt_completed, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['c_bankrupt_completed'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, bankrupt_at_stage)
    textWidth = stringWidth(bankrupt_at_stage, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['c_bankrupt_at_stage'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, leaving_restriction)
    textWidth = stringWidth(leaving_restriction, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['c_leaving_restriction'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, courtcase_company)
    textWidth = stringWidth(courtcase_company, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['c_courtcases'])

    # y -= 15
    # pdf.setFont(font_bold, 8)
    # pdf.drawString(40, y, )
    # textWidth = stringWidth(, font_bold, 8)
    # pdf.setFont(font, 8)
    # pdf.drawString(textWidth + 40, y)

    # Финансы
    y -= 25
    pdf.setFont(font_bold, 9)
    pdf.drawString(40, y, f'Финансы:')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, tax_debt)
    textWidth = stringWidth(tax_debt, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['c_tax_debt'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, enforcement_debt)
    textWidth = stringWidth(enforcement_debt, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['c_enforcement_debt'])

    # Закупки
    y -= 25
    pdf.setFont(font_bold, 9)
    pdf.drawString(40, y, f'Закупки:')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, goszakup_reliable)
    textWidth = stringWidth(goszakup_reliable, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['goszakup_reliable'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y,goszakup_unreliable )
    textWidth = stringWidth(goszakup_unreliable, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['goszakup_unreliable'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, samruk_reliable)
    textWidth = stringWidth(samruk_reliable, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['samruk_reliable'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, samruk_unreliable)
    textWidth = stringWidth(samruk_unreliable, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['samruk_unreliable'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, gos_contracts)
    textWidth = stringWidth(gos_contracts, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['gos_contracts'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, nadloc)
    textWidth = stringWidth(nadloc, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['nadloc'])

    # Руководитель
    y -= 25
    pdf.setFont(font_bold, 9)
    pdf.drawString(40, y, f'Руководитель:')

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_criminal)
    textWidth = stringWidth(i_criminal, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_criminal'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_enforcement_document)
    textWidth = stringWidth(i_enforcement_document, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_enforcement_document'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_enforcement_debt)
    textWidth = stringWidth(i_enforcement_debt, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_enforcement_debt'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_leaving_restriction)
    textWidth = stringWidth(i_leaving_restriction, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_leaving_restriction'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_alimony)
    textWidth = stringWidth(i_alimony, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_alimony'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_missing)
    textWidth = stringWidth(i_missing, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_missing'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_pedophil)
    textWidth = stringWidth(i_pedophil, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_pedophil'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_terror_active)
    textWidth = stringWidth(i_terror_active, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_terror_active'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_terror_excluded)
    textWidth = stringWidth(i_terror_excluded, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_terror_excluded'])

    y -= 15
    pdf.setFont(font_bold, 8)
    pdf.drawString(40, y, i_courtcases)
    textWidth = stringWidth(i_courtcases, font_bold, 8)
    pdf.setFont(font, 8)
    pdf.drawString(textWidth + 40, y, data['i_courtcases'])

    pdf.save()
