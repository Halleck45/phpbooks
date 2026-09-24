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

    var css = [
        ':root { --site-bar-height: 60px; }',
        'html { scroll-padding-top: var(--site-bar-height); }',
        'body { padding-top: var(--site-bar-height); }',
        '.site-bar { position: fixed; top: 0; left: 0; right: 0; z-index: 200; box-sizing: border-box;',
        '  height: var(--site-bar-height); display: flex; align-items: center; gap: 28px; padding: 0 28px;',
        '  background-color: var(--bg); border-bottom: 1px solid var(--table-border-color);',
        '  font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif; font-size: 1.5rem; }',
        '.site-bar a { color: var(--fg); text-decoration: none; }',
        '.site-bar .site-bar-name { font: 500 1.9rem/1 "Fraunces", "Iowan Old Style", Georgia, serif; letter-spacing: -0.01em; }',
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
            '<a class="site-bar-name" href="' + home + '">PHP, to read</a>' +
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
