import re

with open('templates/base/base.html', encoding='utf-8') as f:
    base = f.read()

with open('templates/dashboard/dashboard.html', encoding='utf-8') as f:
    dash = f.read()

with open('templates/tools/calorie.html', encoding='utf-8') as f:
    calorie = f.read()

with open('static/css/style.css', encoding='utf-8') as f:
    css = f.read()

print("=== BASE.HTML BORDERS & SEPARATORS ===")
for line in base.split('\n'):
    if any(k in line.lower() for k in ['border', 'hr', 'navbar', 'container', 'style']):
        print("  ", line.strip())

print("\n=== CALORIE.HTML BORDERS & SEPARATORS ===")
for line in calorie.split('\n'):
    if any(k in line.lower() for k in ['border', 'hr', 'style', 'glow', 'glass']):
        print("  ", line.strip())

print("\n=== STYLE.CSS BORDERS & SEPARATORS ===")
for line in css.split('\n'):
    if any(k in line.lower() for k in ['border-top', 'border-bottom', 'hr', 'navbar']):
        print("  ", line.strip())
