# Stocker des fichiers sans adopter un framework : League/Flysystem

Lire et écrire des fichiers paraît simple jusqu'à ce que « fichiers » signifie le disque local en développement, S3 en production et du FTP pour un client entêté. **Flysystem est une abstraction de système de fichiers : vous codez contre une seule interface et vous choisissez dans la configuration où vivent les fichiers.** C'est aussi la bibliothèque derrière la façade `Storage` de Laravel (voir [Laravel : abstraction de système de fichiers et stockage compatible S3](ch08-02-laravel-filesystem-s3.md)), disponible ici sans aucun framework attaché.

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

Passer à un disque local en développement se fait en changeant l'adaptateur, une ligne :

```php
use League\Flysystem\Local\LocalFilesystemAdapter;

$adapter = new LocalFilesystemAdapter(__DIR__ . '/storage');
$filesystem = new Filesystem($adapter);
```

Le reste du code, `write()`, `fileExists()`, `delete()`, ne bouge pas.

## Quand le choisir

Un script, un worker ou un petit service qui lit ou écrit des fichiers et doit se comporter de la même façon en local et en production, sans « disque local » ni « S3 » codés en dur dans la logique métier.

## Quand ce n'est pas le bon outil

Dans Laravel, utilisez la façade `Storage` au lieu d'installer Flysystem à part. Elle est déjà là, déjà configurée par environnement, et c'est la même bibliothèque avec une API plus aimable par-dessus.

> **Sous le capot :** Flysystem définit une petite interface (`write`, `read`, `delete`, `fileExists` et quelques autres) et laisse chaque adaptateur l'implémenter comme le stockage sous-jacent le permet. C'est du polymorphisme par interface tout ce qu'il y a de plus ordinaire, la même idée que derrière les interfaces natives de PHP, appliquée à un problème que les développeurs rencontrent assez souvent pour mériter une bibliothèque.
