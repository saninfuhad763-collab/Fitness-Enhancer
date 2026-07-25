import html.parser
import re

with open('dash_render.html', encoding='utf-8', errors='ignore') as f:
    dash = f.read()

with open('diet_render.html', encoding='utf-8', errors='ignore') as f:
    diet = f.read()

def get_container_content(html):
    start = html.find('<div class="container py-5">')
    if start == -1:
        return ""
    start += len('<div class="container py-5">')
    end = html.rfind('</div>\n\n  <script>')
    if end == -1:
        end = html.rfind('</div>')
    return html[start:end]

dash_c = get_container_content(dash)
diet_c = get_container_content(diet)

print("=== DASHBOARD CONTAINER CONTENT ===")
for line in dash_c.split('\n')[:25]:
    if line.strip():
        print(line)

print("\n... [middle omitted] ...\n")

for line in dash_c.split('\n')[-25:]:
    if line.strip():
        print(line)

print("\n==================================================")
print("=== DIET CONTAINER CONTENT ===")
for line in diet_c.split('\n')[:25]:
    if line.strip():
        print(line)

print("\n... [middle omitted] ...\n")

for line in diet_c.split('\n')[-25:]:
    if line.strip():
        print(line)
