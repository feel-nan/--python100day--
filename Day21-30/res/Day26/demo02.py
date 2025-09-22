from docx import Document
from docx.document import Document as Doc



employees = [
  {
    'name': 'Bob',
    'id': '1',
    'department': 'Sales',
    'age': 30,
    'sdate': '2015-03-29',
    'salary': 70000,
    'bonus': 5000,
    'company': 'ABC Inc.'
  },
  {
    'name': 'Alice',
    'id': '2',
    'department': 'Engineering',
    'age': 28,
    'sdate': '2016-07-15',
    'salary': 80000,
    'bonus': 6000,
    'company': 'ABC Inc.'
  },
  {
    'name': 'John',
    'id': '3',
    'department': 'Marketing',
    'age': 35,
    'sdate': '2014-11-23',
    'salary': 75000,
    'bonus': 5500,
    'company': 'ABC Inc.'
  }
]

for emp_dict in employees:
    doc = Document()
    for p in doc.paragraphs:
        if '{' not in p.text:
            continue
        for run in p.runs:
            if '{' in run.text:
                continue
            start, end = run.text.find('{'), run.text.find('}')
            key, place_holder = run.text[start + 1:end], run.text[start:end + 1]
            run.text = run.text.replace(place_holder, emp_dict.get[key])
    doc.save(f"{emp_dict['name']}.docx")