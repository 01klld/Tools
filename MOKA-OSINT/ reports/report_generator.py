from jinja2 import Environment, FileSystemLoader
import os

def generate_report(output_file, data):
    env = Environment(loader=FileSystemLoader('reports/templates'))
    template = env.get_template('report_template.html')
    report_content = template.render(data=data)
    
    with open(output_file, 'w') as file:
        file.write(report_content)
