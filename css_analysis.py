"""
Computed CSS analysis tool.
Prints the exact computed background colors for each layout zone:
  1. The body background
  2. The navbar background  
  3. The space between navbar and first content element
  4. The first content element's background
  5. The last content element's background
  6. The body background again (page bottom)

This simulates what the browser renders to identify color transitions
that appear as horizontal "separator lines."
"""

# Hardcode CSS variable values from style.css
CSS_VARS = {
    '--ds-bg-primary':    '#0B1220',   # body background
    '--ds-bg-secondary':  '#111827',   # navbar background
    '--ds-card-bg':       '#182235',   # ds-card background
    '--ds-border':        '#273449',   # border color
    '--ds-accent-primary':'#3B82F6',
    '--ds-accent-secondary':'#6366F1',
}

def resolve(val):
    for k, v in CSS_VARS.items():
        val = val.replace(f'var({k})', v)
    return val

print("=" * 65)
print("COMPUTED BACKGROUND COLOR ANALYSIS")
print("=" * 65)
print()
print("Layer                         DASHBOARD         LOCKED DIET")
print("-" * 65)

# Zone 1: body
body_bg = CSS_VARS['--ds-bg-primary']
print(f"body (background-color)       {body_bg}       {body_bg}")

# Zone 2: navbar
nav_bg  = CSS_VARS['--ds-bg-secondary']
nav_border = CSS_VARS['--ds-border']
print(f"nav.ds-navbar (bg)            {nav_bg}       {nav_bg}")
print(f"nav.ds-navbar (border-bottom) {nav_border}         {nav_border}")

# Zone 3: container  (direct child of body after nav)
# base.html: <div class="container py-5">
# Bootstrap .container has no background-color set  => inherits body = #0B1220
container_bg = f"transparent (inherits body={body_bg})"
print(f"div.container (bg)            TRANSPARENT       TRANSPARENT")

# Zone 4: FIRST CHILD of container
#  Dashboard:   ds-glow-container (position:relative; z-index:1; NO background-color)
#  Locked Diet: ds-glow-container text-center py-4 mb-5  (same -- NO background-color)
print()
print("First child of container:")
dash_first_bg  = "TRANSPARENT (no background set)"
diet_first_bg  = "TRANSPARENT (no background set)"
print(f"  Dashboard ds-glow-container: {dash_first_bg}")
print(f"  Diet      ds-glow-container: {diet_first_bg}")

print()
print("=" * 65)
print("KEY INSIGHT: Background colors are identical.")
print()
print("THEREFORE the visual separator is NOT caused by background transitions.")
print()
print("CONCLUSION: The separator must come from one of:")
print("  A) A border property on an element")
print("  B) A CSS pseudo-element with visible content (::before / ::after)")
print("  C) A box-shadow producing a line")
print("  D) An element height/min-height causing spacing")
print()

print("=" * 65)
print("PSEUDO-ELEMENT ANALYSIS: .ds-glow-primary::before")
print("=" * 65)
print()
print("CSS rule (style.css L375-386):")
print(".ds-glow-primary::before {")
print("    content: '';")
print("    position: absolute;")
print("    top: 50%;")
print("    left: 50%;")
print("    transform: translate(-50%, -50%);")
print("    width: 150%;")
print("    height: 150%;")
print("    background: radial-gradient(circle, rgba(59,130,246,0.15) 0%, rgba(11,18,32,0) 70%);")
print("    z-index: -1;")
print("    pointer-events: none;")
print("}")
print()
print("DASHBOARD: <div class='ds-glow-primary'></div>  <-- IS INSIDE ds-glow-container")
print("  Result: ::before renders INSIDE ds-glow-container, gradient bleeds UPWARD toward navbar.")
print()
print("LOCKED DIET: <div class='ds-glow-primary' style='opacity: 0.8;'></div>")
print("  Same structure. Gradient still bleeds upward.")
print()
print("=" * 65)
print("CRITICAL FINDING: The separator is NOT from the glow.")
print()
print("Let's check the .ds-glow-container geometry:")
print()
print("  Dashboard:  <div class='ds-glow-container mb-5'>")
print("    - position: relative; z-index: 1;")
print("    - Has ds-glow-primary CHILD that renders gradient")
print("    - The gradient CENTER is at 50% of the container height")
print("    - The container starts IMMEDIATELY as first child of .container.py-5")
print("    - py-5 = padding-top: 3rem = 48px before the container starts")
print()
print("  Locked Diet: <div class='ds-glow-container text-center py-4 mb-5'>")
print("    - SAME position/z-index")
print("    - Has ds-glow-primary CHILD that renders gradient")
print("    - py-4 adds padding-top: 1.5rem = 24px INSIDE the glow container")
print()
print("=" * 65)
print("INVESTIGATION OF NAVBAR BORDER:")
print()
print("  .ds-navbar { border-bottom: 1px solid #273449; }")
print()
print("  DASHBOARD: The first ds-glow-container element sits flush with")
print("  the container's py-5 padding. The radial gradient from ds-glow-primary::before")
print("  extends to height:150% of the parent, which might reach toward the navbar.")
print()
print("  LOCKED DIET: SAME structure as dashboard now (post-fix).")
print()
print("  QUESTION: Does ds-glow-container on Dashboard extend behind the navbar?")
print("  Answer: YES, because position:relative z-index:1 within .container.py-5")
print("  which starts below the navbar. The gradient bleeds visually upward into")
print("  the padding zone, making the navbar border INVISIBLE (blends with gradient).")
print()
print("  On LOCKED DIET page - IF the gradient is weaker or positioned differently,")
print("  the navbar border-bottom (#273449) remains VISIBLE against the dark body")
print("  background (#0B1220), creating the appearance of a separator line.")
print()
print("=" * 65)
print("CONCLUSION:")
print()
print("The 'separator below navbar' IS the navbar's own border-bottom: 1px solid #273449.")
print("On the Dashboard, it is visually masked by the radial gradient glow.")
print("On the Locked Diet page, the gradient is smaller/weaker, revealing the border.")
print()
print("The ds-glow-primary on DASHBOARD has no opacity restriction.")
print("The ds-glow-primary on LOCKED DIET has style='opacity: 0.8;'")
print()
print("KEY DIFFERENCE:")
print("  Dashboard glow:      opacity: 1.0 (full strength gradient)")
print("  Locked Diet glow:    opacity: 0.8 (slightly reduced)")
print()
print("However this 0.2 opacity difference is minor.")
print()
print("DEEPER QUESTION: Are there other structural differences?")
print()
print("Dashboard glow-container has NO py-* padding -> gradient center at element top")
print("Locked Diet glow-container has py-4 -> gradient center pushed DOWN 24px from top")
print("=> The gradient's center is pushed DOWN, meaning LESS gradient coverage near navbar")
print("=> The 1px #273449 border is more visible on the Diet page than on Dashboard.")
