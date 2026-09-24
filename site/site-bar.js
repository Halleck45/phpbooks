// The landing page's header, repeated at the top of every book so a reader can
// get back to the other books. Each book links this file from theme/ (symlink)
// through additional-js. The books sit at <book>/ and their French edition at
// <book>/fr/, so the landing page is one or two levels above the book root.
//
// The bar is fixed across the whole window; mdBook's sidebar, menu bar and
// chapter arrows are pushed below it by --site-bar-height.
(function () {
    var fr = document.documentElement.lang === 'fr';
    var home = (typeof path_to_root === 'string' ? path_to_root : '') + (fr ? '../../' : '../');
    var labels = fr
        ? { books: 'Les livres', manual: 'Le manuel' }
        : { books: 'The books', manual: 'The manual' };

    // Inline so the bar needs no asset path; fill follows the mdBook theme.
    var logo = '<svg class="site-bar-logo" viewBox="4 11 590 334" aria-hidden="true" focusable="false">' +
        '<path fill="currentColor" fill-rule="evenodd" d="M425.4 337.8C415.4 322.2 387.9 307.2 353 298.5C339.6 295.1 317.9 291 313.4 291C312.2 291 310.8 290.6 310.5 290C310.2 289.5 310.7 285.2 311.6 280.5L313.3 272 L317.4 272.6C329.1 274.2 346.4 277.3 353.5 279.1C381.8 286.2 407.2 297 422 308.2C424.8 310.3 427.5 312 428 312C428.7 312 429 275.3 428.8 203.2L428.5 94.5 L425.1 87.5C417.3 71.6 393.5 54.3 366.2 44.6C350.8 39.1 315.2 31.1 312.8 32.6C312.4 32.9 312 47.9 312 66.1L312 99 L303 99L294 99 L294 55.5L294 12 L298 12C304.8 12 332 15.9 343.5 18.5C365.2 23.4 388.1 32.2 403.9 41.6C411.8 46.3 430 60.3 430 61.8C430.1 62.2 431.8 64.5 433.9 66.9L437.8 71.3 L446.6 62.2C466.9 41.7 499.8 26.4 541.9 18C553.9 15.7 582.3 12 588.7 12L593 12 L593 150.3L593 288.6 L579.8 289.9C540.8 293.7 506.9 302.2 481.5 314.5C465.7 322.1 456 329.5 450.6 337.9L446.6 344 L438 344L429.4 344 L425.4 337.8ZM456.9 306.6C481.3 290.4 525.8 276.7 567.2 272.5L574 271.8 L574 151.9L574 32.1 L570.2 32.6C534.7 37.5 508.5 45 485.8 56.7C468.2 65.8 456.1 76.8 450.2 89L447.5 94.5 L447.2 203.8C447 292.1 447.2 313 448.2 312.3C448.9 311.9 452.8 309.3 456.9 306.6ZM5 288.7C5 288.6 12.6 250.2 22 203.5C31.3 156.8 39 118.4 39 118.2C39 118 54.9 118 74.2 118.2C107.6 118.5 109.9 118.7 116.2 120.8C129.4 125.2 138 133.7 142.2 146.4C144.1 152.3 144.5 155.4 144.4 164.5C143.9 194.7 128.3 222.4 105.4 233.2C95.5 237.8 87.8 239 65.8 239C46.1 239 46 239 45.5 241.2C45.2 242.5 43.2 252.7 41 264C38.8 275.3 36.7 285.5 36.5 286.8C36 289 35.7 289 20.5 289C12 289 5 288.9 5 288.7ZM261 286.8C261.1 285.5 268.6 247.2 277.8 201.5L294.5 118.5 L326 118.2C345.7 118 360 118.4 364.2 119C382.5 122.1 395.4 134.2 399.1 151.8C402 166.1 398.1 188.2 389.7 204.5C384.5 214.6 372.4 227.1 363.3 231.8C352.2 237.6 344.3 239 321.8 239C306.6 239 301.8 239.3 301.4 240.3C301.2 241 298.8 252.1 296.2 265L291.5 288.5 L276.2 288.8L261 289.1 L261 286.8ZM145.2 237.8C145.5 237.1 153.1 199.5 162.1 154.2L178.5 72 L193.7 72C202.1 72 209 72.1 209 72.2C209 72.4 207 82.6 204.5 94.9C202 107.3 200 117.5 200 117.7C200 117.9 207.3 118 216.2 118C242 118 252.8 120.7 261.1 128.9C271.1 138.7 270.9 147.6 260.2 200L252.4 238.5 L237.2 238.8C228.8 238.9 222 238.8 222 238.5C222 238.2 225.4 220.9 229.6 200.2C237.9 158.6 238.4 153.2 234 148.5C230.4 144.6 225.9 143.9 209.6 144.2L194.7 144.5 L185.4 191C180.3 216.6 176 237.8 176 238.2C176 238.7 169 239 160.4 239C148.3 239 144.9 238.7 145.2 237.8ZM85.5 211.7C92.4 209.8 95.9 207.8 100.1 203.3C107.4 195.7 112.1 181.7 112.3 166.5C112.5 154.8 110.6 150.6 103.4 147C98.9 144.7 97.3 144.5 81.8 144.2L65.1 143.8 L64.5 146.2C63.8 149.2 51 213.3 51 213.9C51 214.8 80.8 213 85.5 211.7ZM341.9 211.5C355.4 207.4 362.4 198.1 366.4 178.7C370.6 158.6 366.5 147.8 353.9 145.1C347.9 143.8 320 143.6 320 144.9C320 145.4 317.1 160.1 313.5 177.5C309.9 195 307 210.4 307 211.8L307 214.3 L321.8 213.7C330.7 213.3 338.6 212.4 341.9 211.5Z"/></svg>';

    var css = [
        ':root { --site-bar-height: 60px; }',
        'html { scroll-padding-top: var(--site-bar-height); }',
        'body { padding-top: var(--site-bar-height); }',
        '.site-bar { position: fixed; top: 0; left: 0; right: 0; z-index: 200; box-sizing: border-box;',
        '  height: var(--site-bar-height); display: flex; align-items: center; gap: 28px; padding: 0 28px;',
        '  background-color: var(--bg); border-bottom: 1px solid var(--table-border-color);',
        '  font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif; font-size: 1.5rem; }',
        '.site-bar a { color: var(--fg); text-decoration: none; }',
        '.site-bar .site-bar-name { display: flex; align-items: center; }',
        '.site-bar .site-bar-logo { height: 34px; width: auto; flex: none; }',
        '.site-bar nav { margin-left: auto; display: flex; gap: 28px; }',
        '.site-bar nav a { color: var(--icons); }',
        '.site-bar nav a:hover, .site-bar .site-bar-name:hover { color: var(--links); }',
        '.sidebar, .nav-chapters { top: var(--site-bar-height); }',
        '#mdbook-menu-bar-hover-placeholder { top: var(--site-bar-height); }',
        '#mdbook-menu-bar.sticky, #mdbook-menu-bar-hover-placeholder:hover + #mdbook-menu-bar,',
        '#mdbook-menu-bar:hover, html.sidebar-visible #mdbook-menu-bar { top: var(--site-bar-height) !important; }',
        '@media (max-width: 480px) { .site-bar { padding: 0 16px; gap: 18px; } .site-bar nav { gap: 18px; } }',
        '@media print { .site-bar { display: none; } body { padding-top: 0; } }'
    ].join('\n');

    function mount() {
        if (document.querySelector('.site-bar')) return;

        var style = document.createElement('style');
        style.textContent = css;
        document.head.appendChild(style);

        var bar = document.createElement('header');
        bar.className = 'site-bar';
        bar.innerHTML =
            '<a class="site-bar-name" href="' + home + '" aria-label="PHP, to read">' + logo + '</a>' +
            '<nav aria-label="Site">' +
            '<a href="' + home + '#readers">' + labels.books + '</a>' +
            '<a href="' + home + '#reference">' + labels.manual + '</a>' +
            '</nav>';
        document.body.insertBefore(bar, document.body.firstChild);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', mount);
    } else {
        mount();
    }
})();
