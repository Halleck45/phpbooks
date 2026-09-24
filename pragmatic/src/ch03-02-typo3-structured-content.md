# TYPO3: Structured Content at Enterprise Scale

Some content sites are not a blog with a few pages. They are a few thousand pages across a dozen departments, in six languages, with an approval workflow before anything goes live. **TYPO3 is a CMS built for that scale**: a content tree, fine-grained permissions, and multilingual support (see [Shipping Multi-Language, Multi-Site](ch13-00-shipping-multi-language-multi-site.md)) designed in from the start, not bolted on.

```bash
composer create-project typo3/cms-base-distribution my-site
cd my-site
./vendor/bin/typo3 setup
```

Content lives in a page tree. Each page is built from "content elements," structured blocks (text, images, a form, an embedded plugin) that editors arrange without touching code. When the built-in set doesn't cover a client's need, you extend the vocabulary with a custom element:

```php
<?php
// Configuration/TCA/Overrides/tt_content.php
use TYPO3\CMS\Core\Utility\ExtensionManagementUtility;

ExtensionManagementUtility::addTcaSelectItem(
    'tt_content',
    'CType',
    ['label' => 'Team Member Card', 'value' => 'teammember_card'],
);
```

Permissions are set per page and per user group. A regional editor manages their department's branch of the tree and cannot touch anyone else's.

## When to reach for this

Large institutional or enterprise sites: universities, government agencies, multinational companies. Content ownership is spread across teams, and the editorial workflow is a requirement rather than a nice-to-have.

## When it's the wrong fit

A small business site or a single-editor blog. TYPO3's structure is the whole value at scale and pure overhead below it. WordPress ships the same result faster for a simpler brief.

> **Under the hood:** TYPO3's TCA (Table Configuration Array) is a large PHP array that describes how each content type behaves: its fields, their validation, how they render in the backend. It is metadata-driven UI generation, a pattern that shows up again in [API Platform's admin panels](ch05-03-api-platform-auto-admin.md), applied to editorial content instead of API resources.
