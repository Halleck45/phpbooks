# Laravel: Filesystem Abstraction and S3-Compatible Storage

Laravel's `Storage` facade wraps [League/Flysystem](ch02-06-league-flysystem-standalone.md) behind a disk-agnostic API. **The same code writes to the local disk in development and to S3 in production, and configuration alone decides which.**

```php
// config/filesystems.php
return [
    'disks' => [
        's3' => [
            'driver' => 's3',
            'key' => env('AWS_ACCESS_KEY_ID'),
            'secret' => env('AWS_SECRET_ACCESS_KEY'),
            'region' => env('AWS_DEFAULT_REGION'),
            'bucket' => env('AWS_BUCKET'),
        ],
    ],
];
```

```php
use Illuminate\Support\Facades\Storage;

// storing an uploaded file
$path = $request->file('avatar')->store('avatars', 's3');

// generating a temporary, signed download link
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(10));

// reading it back
$contents = Storage::disk('s3')->get($path);
```

Switch `'driver' => 's3'` to `'driver' => 'local'` for development, or point it at a DigitalOcean Spaces or Cloudflare R2 endpoint in production. Nothing else in the application changes.

## When to reach for this

Any feature with user uploads: avatars, attachments, generated PDFs, exported reports. This is the boring, correct way to handle files in a Laravel app, and boring is what you want here.

## When it's the wrong fit

A request for sharing, sync, and collaboration (see [Nextcloud](ch08-01-nextcloud-ready-made-drive.md)) rather than upload and retrieve. `Storage` handles files. It gives you no sharing links, no version history, no sync client.

> **Under the hood:** `temporaryUrl()` generates a pre-signed URL, a link with a cryptographic signature and an expiration baked into the query string, which S3 validates itself without any request reaching your Laravel app. Serving a private file this way costs your server no bandwidth at all.
