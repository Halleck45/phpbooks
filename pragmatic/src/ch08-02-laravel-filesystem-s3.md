# Laravel: Filesystem Abstraction and S3-Compatible Storage

Laravel's `Storage` facade wraps [League/Flysystem](ch02-06-league-flysystem-standalone.md) (see that chapter for the standalone version of the same idea) behind a simple, disk-agnostic API. The same code writes to your local disk in development and to S3 in production, decided entirely by configuration.

```php
// config/filesystems.php
'disks' => [
    's3' => [
        'driver' => 's3',
        'key' => env('AWS_ACCESS_KEY_ID'),
        'secret' => env('AWS_SECRET_ACCESS_KEY'),
        'region' => env('AWS_DEFAULT_REGION'),
        'bucket' => env('AWS_BUCKET'),
    ],
],
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

Switching `'driver' => 's3'` to `'driver' => 'local'` for local development, or to a DigitalOcean Spaces or Cloudflare R2 endpoint in production, changes nothing else in the application code.

## When to reach for this

Any feature involving user uploads: avatars, attachments, generated PDFs, exported reports. This is the default, boring, correct way to handle files in a Laravel app, and boring is exactly what you want here.

## When it's the wrong fit

A request for full sharing, sync, and collaboration features (see [Nextcloud](ch08-01-nextcloud-ready-made-drive.md)) rather than simple upload-and-retrieve. `Storage` handles files; it doesn't give you sharing links, version history, or a sync client.

> **Under the hood:** `temporaryUrl()` generates a pre-signed URL, a link with a cryptographic signature and expiration baked into the query string, that S3 validates itself without any request touching your Laravel app. That's why serving a private file this way doesn't cost your server any bandwidth at all.
