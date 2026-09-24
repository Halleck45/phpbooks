# WordPress: The Media Library at Scale

The Media Library handles uploads, thumbnail generation, and a searchable grid out of the box, with no plugin. **For most content sites, that is the whole feature, already done.**

```php
$attachment_id = media_handle_upload('file', $post_id);
$url = wp_get_attachment_url($attachment_id);
$thumb = wp_get_attachment_image_url($attachment_id, 'medium');
```

The first scaling problem is almost always local disk space and bandwidth, once a site holds thousands of images. The standard fix offloads storage to S3-compatible object storage through a plugin, and editors keep the same interface:

```bash
wp plugin install amazon-s3-and-cloudfront --activate
wp media-offload run
```

From then on, uploads go through the same screen, and files are stored on and served from object storage instead of the server's disk.

The second problem is image processing itself. Generating several thumbnail sizes for every upload is CPU-heavy at volume, and the usual answer is to let a CDN resize on the fly instead of pre-generating every size at upload time.

## When to reach for this

Any WordPress site with more than a handful of images, which is nearly all of them. Even a small brochure site gets the automatic thumbnail sizes and the searchable grid for free.

## When it's the wrong fit

Video hosting, or a media-heavy application at real scale. A dedicated media platform integrated through its API serves that better than a Media Library stretched far past its design.

> **Under the hood:** WordPress generates thumbnail sizes at upload time with PHP's GD or Imagick extension, whichever the server has. Resizing eagerly rather than lazily is why large libraries eventually need the offloading described above: the cost is paid once per upload, but paid by every upload.
