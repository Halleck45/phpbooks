# File Storage Without Buying Into a Framework: League/Flysystem

Reading and writing files sounds simple until "files" means local disk in development, S3 in production, and maybe FTP for one stubborn client. Flysystem is a filesystem abstraction: write your code against one interface, and swap where the files actually live by changing configuration, not code. It's also, notably, the exact library powering Laravel's `Storage` facade (see [Laravel: Filesystem Abstraction and S3-Compatible Storage](ch08-02-laravel-filesystem-s3.md)), available here with no framework attached.

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

Swapping the adapter to a local disk for development is a one-line change:

```php
use League\Flysystem\Local\LocalFilesystemAdapter;

$adapter = new LocalFilesystemAdapter(__DIR__ . '/storage');
$filesystem = new Filesystem($adapter);
```

The rest of the code, `write()`, `fileExists()`, `delete()`, doesn't change at all.

## When to reach for this

A script, worker, or small service that reads or writes files and needs to work the same way locally and in production, without hard-coding "local disk" or "S3" into the business logic.

## When it's the wrong fit

Inside Laravel, use the `Storage` facade instead of installing Flysystem separately; it's already there, already configured per environment, and it's the exact same library with a friendlier API layered on top.

> **Under the hood:** Flysystem defines a small interface (`write`, `read`, `delete`, `fileExists`, and a handful of others) and lets each adapter implement it however the underlying storage actually works. That's ordinary interface-based polymorphism, the same idea behind PHP's own built-in interfaces, applied to a problem developers hit constantly enough to be worth a dedicated library.
