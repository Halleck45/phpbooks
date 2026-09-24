# Laravel : abstraction de système de fichiers et stockage compatible S3

La façade `Storage` de Laravel enveloppe [League/Flysystem](ch02-06-league-flysystem-standalone.md) derrière une API indifférente au support. **Le même code écrit sur le disque local en développement et sur S3 en production, et la configuration seule décide lequel.**

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

Remplacez `'driver' => 's3'` par `'driver' => 'local'` pour le développement, ou pointez-le vers un endpoint DigitalOcean Spaces ou Cloudflare R2 en production. Rien d'autre ne change dans l'application.

## Quand le choisir

Toute fonctionnalité avec des fichiers envoyés par les utilisateurs : avatars, pièces jointes, PDF générés, exports. C'est la façon ennuyeuse et correcte de gérer des fichiers dans une application Laravel, et l'ennui est précisément ce que vous cherchez ici.

## Quand ce n'est pas le bon outil

Une demande de partage, de synchronisation et de collaboration (voir [Nextcloud](ch08-01-nextcloud-ready-made-drive.md)) plutôt que d'envoi et de lecture. `Storage` gère des fichiers. Il ne vous donne ni liens de partage, ni historique des versions, ni client de synchronisation.

> **Sous le capot :** `temporaryUrl()` génère une URL pré-signée, un lien dont la signature cryptographique et la date d'expiration sont inscrites dans la chaîne de requête, et que S3 vérifie lui-même sans qu'aucune requête n'atteigne votre application Laravel. Servir un fichier privé de cette façon ne coûte aucune bande passante à votre serveur.
