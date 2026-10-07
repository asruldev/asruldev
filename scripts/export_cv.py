"""Export the shared resume data as a selectable-text PDF and printable HTML."""
from pathlib import Path
import json
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'cv/resume.json').read_text())
output = ROOT / 'output/pdf/Asrul_Harahap_CV_ATS.pdf'
output.parent.mkdir(parents=True, exist_ok=True)
styles = {
 'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=20, leading=23, spaceAfter=3),
 'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=10.5, leading=14, spaceAfter=3),
 'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=3),
 'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceBefore=8, spaceAfter=5, textColor=colors.HexColor('#19344a')),
 'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=9, leading=12, spaceBefore=4, spaceAfter=3),
 'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9, leading=12, leftIndent=10, firstLineIndent=-8, spaceAfter=3),
}
story=[]
html=[]
def add(text, style, tag='p'):
 story.append(Paragraph(escape(text), styles[style]))
 html.append(f'<{tag} class="{style}">{escape(text)}</{tag}>')
add(data['name'],'name','h1')
add(data['title'],'title')
add(data['contact'],'body')
add(data['links'],'body')
for section in data['sections']:
 add(section['heading'],'heading','h2')
 for item in section['items']:
  if 'title' in item: add(item['title']+' | '+item['date'],'role')
  if 'text' in item: add(item['text'],'body')
  for bullet in item.get('bullets',[]): add('- '+bullet,'bullet')
SimpleDocTemplate(str(output), pagesize=A4, rightMargin=40, leftMargin=40, topMargin=32, bottomMargin=32, title='Asrul Harahap - Frontend Engineer CV', author=data['name']).build(story)
css='''body{font:12px/1.4 Arial,sans-serif;color:#17212b;max-width:714px;margin:32px auto;padding:0 24px}h1{font-size:27px;margin:0 0 4px}h2{font-size:14px;color:#19344a;margin:12px 0 5px}p{margin:3px 0}.title,.role{font-weight:bold}.role{margin-top:7px}.bullet{padding-left:12px;text-indent:-10px}button{padding:10px 16px;margin-bottom:20px;cursor:pointer}@page{size:A4;margin:12mm}@media print{body{margin:0;padding:0;font-size:9pt}button,nav{display:none}h2,.role{break-after:avoid}p{break-inside:avoid}}'''
(ROOT/'cv/index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Asrul Harahap - ATS CV</title><style>'+css+'</style><button onclick="window.print()">Export PDF / Print</button><main>'+''.join(html)+'</main><script src="hidden-access.js"></script></html>')
print(output)
