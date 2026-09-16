# WordPress: The Media Library at Scale

WordPress's Media Library handles uploads, automatic thumbnail generation, and a searchable grid view out of the box, no plugin required. For most content sites, that's the entire feature, already done.

```php
$attachment_id = media_handle_upload('file', $post_id);
$url = wp_get_attachment_url($attachment_id);
$thumb = wp_get_attachment_image_url($attachment_id, 'medium');
```

The first real scaling problem is almost always local disk space and server bandwidth once a site has thousands of images. The standard fix is offloading storage to S3-compatible object storage via a plugin, without changing how editors interact with the Media Library at all:

```bash
wp plugin install amazon-s3-and-cloudfront --activate
wp media-offload run
```

From that point, uploads still go through the same familiar interface, but files are transparently stored on and served from object storage instead of the server's own disk.

The second common scaling problem is image processing itself: generating several thumbnail sizes for every upload is CPU-intensive at volume, which is usually addressed by offloading resizing to a CDN's on-the-fly image service rather than pre-generating every size on upload.

## When to reach for this

Any WordPress site with more than a handful of images, which is nearly all of them. Even a small brochure site benefits from the automatic thumbnail sizes and searchable grid this provides for free.

## When it's the wrong fit

A site with genuinely enormous media needs (video hosting, a media-heavy application at real scale) is usually better served by a dedicated media platform integrated via API, rather than stretching the Media Library far past what it was designed for.

> **Under the hood:** WordPress generates its thumbnail sizes using PHP's GD or Imagick extension, whichever is available on the server, at upload time. That single design decision, resizing eagerly rather than lazily, is exactly why large media libraries eventually need the offloading strategies described above: the cost is paid once per upload, but paid by every upload.
