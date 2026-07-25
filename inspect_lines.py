with open('diet_render.html', encoding='utf-8', errors='ignore') as f:
    diet = f.read()

# Print lines from navbar down to content
lines = diet.split('\n')
in_body = False
for i, line in enumerate(lines, 1):
    if '<body' in line:
        in_body = True
    if in_body:
        print(f"{i:4d}: {line}")
