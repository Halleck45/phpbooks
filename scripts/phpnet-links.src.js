/*
 * php.net links for mdBook.
 *
 * Turns every call to a PHP built-in function into a link to its page in the
 * php.net manual: in highlighted PHP code blocks, and in inline code such as
 * `array_map()`. Methods, static calls, variables, namespaced functions,
 * function declarations, strings and comments are left alone.
 *
 * DO NOT EDIT the copies in <book>/theme/: edit scripts/phpnet-links.src.js
 * and run `make phpnet-links` (scripts/build-phpnet-links.py). mdBook only
 * ships additional-js files that live inside the book folder, hence one
 * generated copy per book.
 *
 * Function list: __SOURCE__ (__COUNT__ functions).
 */
(function () {
    'use strict';

    var NAMES = '__NAMES__';
    // Functions whose manual page does not follow the "underscore to hyphen" rule.
    var SLUGS = __SLUGS__;
    // Manual translations published on php.net, keyed by <html lang>.
    var MANUALS = {
        en: 'en', de: 'de', es: 'es', fr: 'fr', it: 'it', ja: 'ja',
        pt: 'pt_BR', 'pt-br': 'pt_BR', ru: 'ru', tr: 'tr', uk: 'uk', zh: 'zh'
    };

    var known = Object.create(null);
    NAMES.split(' ').forEach(function (name) { known[name] = true; });

    var pageLang = (document.documentElement.lang || 'en').toLowerCase();
    var manual = MANUALS[pageLang] || MANUALS[pageLang.split('-')[0]] || 'en';

    var CALL = /[A-Za-z_][A-Za-z0-9_]*(?=\s*\()/g;
    var NOT_A_CALL = /(?:->|::|\$|[A-Za-z0-9_]\\|\b(?:function|new)\s+&?\s*)$/;
    // Inline code may quote another language: there, `s.trim()` or `Math.pow()`
    // is a method call, while in a PHP block the dot is the concatenation operator.
    var METHOD_CALL = /\.$/;
    var SKIPPED = '.hljs-string, .hljs-comment, .hljs-meta, a';

    function url(name) {
        var slug = SLUGS[name] || name.replace(/_/g, '-');
        return 'https://www.php.net/manual/' + manual + '/function.' + slug + '.php';
    }

    function textNodes(root) {
        var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
        var nodes = [];
        var offset = 0;
        var node;
        while ((node = walker.nextNode())) {
            nodes.push({ node: node, start: offset });
            offset += node.nodeValue.length;
        }
        return nodes;
    }

    function nodeAt(nodes, index) {
        for (var i = nodes.length - 1; i >= 0; i--) {
            if (nodes[i].start <= index) { return nodes[i]; }
        }
        return null;
    }

    function linkify(code, inline) {
        var nodes = textNodes(code);
        var text = nodes.map(function (n) { return n.node.nodeValue; }).join('');
        var found = [];
        var match;

        CALL.lastIndex = 0;
        while ((match = CALL.exec(text))) {
            var name = match[0].toLowerCase();
            if (!known[name]) { continue; }
            var before = text.slice(Math.max(0, match.index - 40), match.index);
            if (NOT_A_CALL.test(before) || (inline && METHOD_CALL.test(before))) { continue; }
            var holder = nodeAt(nodes, match.index);
            if (!holder) { continue; }
            // highlight.js never splits an identifier, so the name sits in one text node.
            if (match.index + name.length > holder.start + holder.node.nodeValue.length) { continue; }
            var parent = holder.node.parentElement;
            if (parent && parent !== code && parent.closest(SKIPPED) && code.contains(parent.closest(SKIPPED))) { continue; }
            found.push({ node: holder.node, at: match.index - holder.start, name: name, label: match[0] });
        }

        // Last match first, so that splitting a text node keeps earlier offsets valid.
        for (var i = found.length - 1; i >= 0; i--) {
            var hit = found[i];
            var target = hit.node.splitText(hit.at);
            target.splitText(hit.label.length);
            var a = document.createElement('a');
            a.className = 'phpnet-link';
            a.href = url(hit.name);
            a.target = '_blank';
            a.rel = 'noopener';
            a.title = hit.label + '() · php.net';
            target.parentNode.replaceChild(a, target);
            a.appendChild(target);
        }
        return found.length;
    }

    function run() {
        var style = document.createElement('style');
        style.textContent =
            'code a.phpnet-link, code a.phpnet-link:link, code a.phpnet-link:visited {' +
            ' color: inherit; text-decoration: none;' +
            ' border-bottom: 1px dotted rgba(128, 128, 128, 0.7); }' +
            'code a.phpnet-link:hover { border-bottom: 1px solid currentColor; }' +
            '@media print { code a.phpnet-link { border-bottom: 0 !important; } }';
        document.head.appendChild(style);

        var blocks = document.querySelectorAll('pre > code.language-php, :not(pre) > code');
        Array.prototype.forEach.call(blocks, function (code) {
            if (code.closest('a')) { return; }
            linkify(code, code.parentElement.tagName !== 'PRE');
        });
    }

    // mdBook loads custom scripts after book.js, which highlights synchronously:
    // by the time this runs, the code blocks already carry their hljs spans.
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', run);
    } else {
        run();
    }
})();
