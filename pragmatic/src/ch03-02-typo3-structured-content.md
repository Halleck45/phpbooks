# TYPO3: Structured Content at Enterprise Scale

Some content sites aren't a blog with a few pages: they're a few thousand pages, across a dozen departments, in six languages, with an editorial workflow that needs approvals before anything goes live. TYPO3 is a CMS built for exactly that scale, with a content tree, granular permissions, and multilingual support (see [Shipping Multi-Language, Multi-Site](ch13-00-shipping-multi-language-multi-site.md)) designed in from the start rather than bolted on.

```bash
composer create-project typo3/cms-base-distribution my-site
cd my-site
./vendor/bin/typo3 setup
```

Content lives in a page tree, and each page is built from "content elements," structured blocks (text, images, a form, an embedded plugin) that editors arrange without touching code. Developers extend that vocabulary with custom content elements when the built-in set doesn't cover a client's need:

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

Permissions are set per page, per user group, so a regional editor can manage their department's section of the tree without being able to touch anyone else's.

## When to reach for this

Large institutional or enterprise sites: universities, government agencies, multinational companies, where content ownership is genuinely distributed across teams and the editorial workflow itself is a requirement, not a nice-to-have.

## When it's the wrong fit

A small business site or a single-editor blog. TYPO3's structure is the entire value proposition at scale and unnecessary overhead below it; WordPress ships the same kind of result faster for a simpler brief.

> **Under the hood:** TYPO3's TCA (Table Configuration Array) is a large PHP array describing how each content type behaves: which fields it has, how they're validated, how they render in the backend. It's effectively metadata-driven UI generation, a pattern that shows up again in [API Platform's approach to admin panels](ch05-03-api-platform-auto-admin.md), just applied to editorial content instead of API resources.
