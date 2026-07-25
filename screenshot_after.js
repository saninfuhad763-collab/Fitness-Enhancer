const { chromium } = require('playwright');

const SESSION_KEY = '59m7yy8tsx3q94iyraqvb54pnni7atey';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
  });

  await context.addCookies([{
    name: 'sessionid',
    value: SESSION_KEY,
    domain: '127.0.0.1',
    path: '/',
    httpOnly: true,
    secure: false,
  }]);

  const page = await context.newPage();

  // Diet page AFTER
  await page.goto('http://127.0.0.1:8000/tools/calories/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: 'screenshots/diet_locked_AFTER.png', fullPage: false });
  console.log('AFTER screenshot saved: diet_locked_AFTER.png');

  // Verify styles visually
  const allBorders = await page.evaluate(() => {
    const results = [];
    document.querySelectorAll('*').forEach(el => {
      const cs = window.getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      if (rect.width < 400) return;  // only wide elements
      
      const btw = parseFloat(cs.borderTopWidth);
      const bbw = parseFloat(cs.borderBottomWidth);
      const btAlpha = cs.borderTopColor.includes('rgba') 
        ? parseFloat(cs.borderTopColor.split(',')[3]) : 1;
      const bbAlpha = cs.borderBottomColor.includes('rgba')
        ? parseFloat(cs.borderBottomColor.split(',')[3]) : 1;
        
      const hasTopBorder = btw > 0 && cs.borderTopStyle !== 'none' && btAlpha > 0;
      const hasBottomBorder = bbw > 0 && cs.borderBottomStyle !== 'none' && bbAlpha > 0;
      
      if (hasTopBorder || hasBottomBorder) {
        results.push({
          tagName: el.tagName,
          className: el.className.substring(0, 100),
          top_border: hasTopBorder ? `${btw}px ${cs.borderTopStyle} ${cs.borderTopColor}` : 'none',
          bottom_border: hasBottomBorder ? `${bbw}px ${cs.borderBottomStyle} ${cs.borderBottomColor}` : 'none',
          rectTop: Math.round(rect.top),
        });
      }
    });
    return results;
  });

  console.log('\n=== ALL DIET PAGE ELEMENTS WITH VISIBLE BORDERS (AFTER FIX) ===');
  allBorders.forEach(el => {
    console.log(`  y=${el.rectTop} <${el.tagName} class="${el.className.trim()}">`);
    if (el.top_border !== 'none') console.log(`    border-top: ${el.top_border}`);
    if (el.bottom_border !== 'none') console.log(`    border-bottom: ${el.bottom_border}`);
  });

  await browser.close();
  console.log('\nDone.');
})();
