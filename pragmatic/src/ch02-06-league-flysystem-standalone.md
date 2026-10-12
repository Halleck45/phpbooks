# File Storage Without Buying Into a Framework: League/Flysystem

Reading and writing files sounds simple until "files" means the local disk in development, S3 in production, and FTP for one stubborn client. **Flysystem is a filesystem abstraction: you code against one interface and choose where the files live in configuration.** It is also the library behind Laravel's `Storage` facade (see [Laravel: Filesystem Abstraction and S3-Compatible Storage](ch08-02-laravel-filesystem-s3.md)), available here with no framework attached.

```bash
composer require league/flysystem-aws-s3-v3
```

```php
<?php
require 'vendor/autoload.php';

use League\Flysystem\Filesystem;
use League\Flysystem\AwsS3V3\AwsS3V3Adapter;
use Aws\S3\S3Client;

$client = new S3Client([
    'region' => 'us-east-1',
    'version' => 'latest',
]);

$adapter = new AwsS3V3Adapter($client, 'my-bucket');
$filesystem = new Filesystem($adapter);

$filesystem->write('reports/2026-09.csv', $csvContents);
$exists = $filesystem->fileExists('reports/2026-09.csv');
$filesystem->delete('reports/2025-01.csv');
```

Swapping the adapter for a local disk in development is a one-line change:

```php
use League\Flysystem\Local\LocalFilesystemAdapter;

$adapter = new LocalFilesystemAdapter(__DIR__ . '/storage');
$filesystem = new Filesystem($adapter);
```

The rest of the code, `write()`, `fileExists()`, `delete()`, does not change.

## When to reach for this

A script, a worker, or a small service that reads or writes files and has to behave the same locally and in production, without "local disk" or "S3" hard-coded into the business logic.

## When it's the wrong fit

Inside Laravel, use the `Storage` facade instead of installing Flysystem separately. It is already there, already configured per environment, and it is the same library with a friendlier API on top.

> **Under the hood:** Flysystem defines a small interface (`write`, `read`, `delete`, `fileExists`, and a handful of others) and lets each adapter implement it however the underlying storage works. That is ordinary interface-based polymorphism, the same idea behind PHP's built-in interfaces, applied to a problem developers hit often enough to deserve a library.
