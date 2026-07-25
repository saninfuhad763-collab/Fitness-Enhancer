const { chromium } = require('playwright');

const SESSION_KEY = '59m7yy8tsx3q94iyraqvb54pnni7atey';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
  });

  // Inject the Django session cookie directly
  await context.addCookies([{
    name: 'sessionid',
    value: SESSION_KEY,
    domain: '127.0.0.1',
    path: '/',
    httpOnly: true,
    secure: false,
  }]);

  const page = await context.newPage();

  // ========================
  // 1. LOCKED DIET PAGE
  // ========================
  await page.goto('http://127.0.0.1:8000/tools/calories/', { waitUntil: 'networkidle' });
  
  const dietTitle = await page.title();
  const dietUrl = page.url();
  console.log('Diet page title:', dietTitle);
  console.log('Diet page URL:', dietUrl);

  await page.screenshot({ path: 'screenshots/diet_locked_BEFORE.png', fullPage: false });
  console.log('BEFORE screenshot saved: diet_locked_BEFORE.png');

  // ===================== 
  // FULL COMPUTED STYLE AUDIT on Diet page
  // =====================

  const navStyles = await page.evaluate(() => {
    const nav = document.querySelector('nav.ds-navbar');
    const cs = window.getComputedStyle(nav);
    const rect = nav.getBoundingClientRect();
    return {
      tagName: nav.tagName, className: nav.className,
      backgroundColor: cs.backgroundColor,
      borderBottom: cs.borderBottom,
      borderBottomColor: cs.borderBottomColor,
      borderBottomWidth: cs.borderBottomWidth,
      marginBottom: cs.marginBottom,
      boxShadow: cs.boxShadow,
      rectBottom: Math.round(rect.bottom),
    };
  });
  console.log('\n=== DIET NAV STYLES ===');
  console.log(JSON.stringify(navStyles, null, 2));

  const containerStyles = await page.evaluate(() => {
    const c = document.querySelector('div.container.py-5');
    if (!c) return { error: 'no container.py-5' };
    const cs = window.getComputedStyle(c);
    const rect = c.getBoundingClientRect();
    return {
      tagName: c.tagName, className: c.className,
      backgroundColor: cs.backgroundColor,
      borderTop: cs.borderTop,
      paddingTop: cs.paddingTop,
      marginTop: cs.marginTop,
      rectTop: Math.round(rect.top),
    };
  });
  console.log('\n=== DIET CONTAINER STYLES ===');
  console.log(JSON.stringify(containerStyles, null, 2));

  const firstContentStyles = await page.evaluate(() => {
    const c = document.querySelector('div.container.py-5');
    if (!c) return { error: 'no container' };
    const first = c.firstElementChild;
    if (!first) return { error: 'no first child' };
    const cs = window.getComputedStyle(first);
    const rect = first.getBoundingClientRect();
    return {
      tagName: first.tagName, 
      className: first.className,
      id: first.id,
      innerHTML_snippet: first.outerHTML.substring(0, 300),
      backgroundColor: cs.backgroundColor,
      borderTop: cs.borderTop,
      paddingTop: cs.paddingTop,
      marginTop: cs.marginTop,
      rectTop: Math.round(rect.top),
    };
  });
  console.log('\n=== DIET CONTAINER FIRST CHILD STYLES ===');
  console.log(JSON.stringify(firstContentStyles, null, 2));

  // Scan ALL elements for visible horizontal borders on DIET
  const allBorders = await page.evaluate(() => {
    const results = [];
    document.querySelectorAll('*').forEach(el => {
      const cs = window.getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      if (rect.width < 400) return;  // only wide elements
      
      const btw = parseFloat(cs.borderTopWidth);
      const bbw = parseFloat(cs.borderBottomWidth);
      
      // include if border exists and is visible (not transparent)
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
          rectBottom: Math.round(rect.bottom),
          rectWidth: Math.round(rect.width),
        });
      }
    });
    return results;
  });

  console.log('\n=== ALL DIET PAGE ELEMENTS WITH VISIBLE BORDERS ===');
  allBorders.forEach(el => {
    console.log(`  y=${el.rectTop} <${el.tagName} class="${el.className.trim()}">`);
    if (el.top_border !== 'none') console.log(`    border-top: ${el.top_border}`);
    if (el.bottom_border !== 'none') console.log(`    border-bottom: ${el.bottom_border}`);
  });

  // ========================
  // 2. DASHBOARD PAGE  
  // ========================
  await page.goto('http://127.0.0.1:8000/users/dashboard/', { waitUntil: 'networkidle' });
  
  const dashTitle = await page.title();
  console.log('\nDashboard title:', dashTitle);
  await page.screenshot({ path: 'screenshots/dashboard_BEFORE.png', fullPage: false });
  console.log('Dashboard screenshot saved.');

  const dashBorders = await page.evaluate(() => {
    const results = [];
    document.querySelectorAll('*').forEach(el => {
      const cs = window.getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      if (rect.width < 400) return;
      
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
          tagName: el.tagName, className: el.className.substring(0, 100),
          top_border: hasTopBorder ? `${btw}px ${cs.borderTopStyle} ${cs.borderTopColor}` : 'none',
          bottom_border: hasBottomBorder ? `${bbw}px ${cs.borderBottomStyle} ${cs.borderBottomColor}` : 'none',
          rectTop: Math.round(rect.top),
          rectWidth: Math.round(rect.width),
        });
      }
    });
    return results;
  });

  console.log('\n=== ALL DASHBOARD ELEMENTS WITH VISIBLE BORDERS ===');
  dashBorders.forEach(el => {
    console.log(`  y=${el.rectTop} <${el.tagName} class="${el.className.trim()}">`);
    if (el.top_border !== 'none') console.log(`    border-top: ${el.top_border}`);
    if (el.bottom_border !== 'none') console.log(`    border-bottom: ${el.bottom_border}`);
  });

  await browser.close();
  console.log('\nDone.');
})();
