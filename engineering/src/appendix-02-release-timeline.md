# Appendix B: Release Timeline

PHP ships one feature release per year, in late November. Each branch then receives two years of active support, bug fixes and security fixes both, followed by two years of security-only support: four years of support in total from release to end of life. The table below is the same one printed in [Governance and Versions](ch08-governance-and-versions.md), reproduced here on its own for quick reference.

| Version | Released | Active support ends | Security support ends |
|---|---|---|---|
| PHP 8.2 | 8 Dec 2022 | 31 Dec 2024 | 31 Dec 2026 |
| PHP 8.3 | 23 Nov 2023 | 31 Dec 2025 | 31 Dec 2027 |
| PHP 8.4 | 21 Nov 2024 | 31 Dec 2026 | 31 Dec 2028 |
| PHP 8.5 | 20 Nov 2025 | 31 Dec 2027 | 31 Dec 2029 |

Source: [php.net/supported-versions.php](https://php.net/supported-versions.php), checked 2026-09-17. This page updates as new versions ship and old ones retire; treat the table above as a snapshot taken on that date, and check the live page directly before making a decision that depends on an exact date.

## What "active" and "security-only" actually mean

During active support, a branch receives both bug fixes and security fixes, and is the version the PHP project itself recommends running. Once active support ends, a branch moves to security-only support: it will still receive a fix for a newly discovered vulnerability, but not for an ordinary, non-security bug. Once security support ends, a branch receives nothing further from the project, regardless of what is found in it afterward. A production deployment still running a branch past its security-support end date is not a deployment with an outdated feature set; it is a deployment with no path to a fix for whatever is discovered in it next.

## Reading this table against what is actually running

[Governance and Versions](ch08-governance-and-versions.md) and [Where PHP Is the Wrong Choice](ch09-wrong-choice.md) both use the same, separate figure for context: as of 2026-09-17, W3Techs found 64.1 percent of PHP-running websites on the 8.x line this table covers, 28.1 percent still on the 7.x line, whose last branch left security support in November 2022, and 7.8 percent still on PHP 5.x, unsupported since 2018 or 2019. This table describes what the PHP project commits to shipping and supporting. It does not describe what your own organization, or a vendor's, is actually running, which is a fact only a direct check of that specific deployment can establish.

## As of September 2026

PHP 8.6 had not shipped as of this writing. This book does not project a release date for it, in keeping with the same discipline applied to every other figure here: an announced plan is described as announced, not treated as a fact until it ships. The one confirmed detail tied to that release is covered in [Cost](ch07-cost.md): PHP License version 4 applies starting with PHP 8.6, superseding License 3.01, which governs the versions this table currently treats as supported.
