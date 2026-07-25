import os
import re

with open('dash_render.html', encoding='utf-8', errors='ignore') as f:
    dash = f.read()

with open('diet_render.html', encoding='utf-8', errors='ignore') as f:
    diet = f.read()

print("==================== LINK TAGS ====================")
print("DASHBOARD LINK TAGS:")
for l in re.findall(r'<link[^>]+>', dash):
    print("  ", l)

print("DIET LINK TAGS:")
for l in re.findall(r'<link[^>]+>', diet):
    print("  ", l)

print("\n==================== INLINE BORDERS / HR / STYLES IN DIET ====================")
for line in diet.split('\n'):
    if any(k in line.lower() for k in ['border', 'hr', 'style', 'outline', 'shadow', 'main', 'nav']):
        print("  Line:", line.strip())
