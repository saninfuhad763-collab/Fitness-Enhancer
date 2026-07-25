with open('diet_render.html', encoding='utf-8', errors='ignore') as f:
    diet = f.read()

lines = diet.split('\n')
for i, line in enumerate(lines, 1):
    if any(term in line.lower() for term in ['border', 'hr', 'linear-gradient', 'radial-gradient', 'outline', 'shadow', 'ds-glow', 'ds-glass']):
        print(f"Line {i:3d}: {line.strip()[:120]}")
