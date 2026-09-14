# Chaînes, nombres, dates et JSON

**PHP est livré avec une grande bibliothèque standard, faite de fonctions bien plus que de méthodes.** Vous n'appelez pas `$s.upper()` mais `strtoupper($s)`, parce qu'il n'y a ni classe String, ni classe Number, ni receveur : les valeurs entrent en arguments et les résultats sortent en valeurs de retour. Une fois cette convention acceptée, la bibliothèque est vaste, rapide, et documentée fonction par fonction sur php.net, où chaque page donne la signature, le journal des changements par version, et des exemples qui valent la lecture.

Les noms, en revanche, sont incohérents : `strlen` voisine avec `str_replace`, `array_key_exists` prend la clé en premier là où `in_array` prend l'aiguille en premier, `strpos` et `array_search` renvoient `false` en cas d'échec alors que `preg_match` renvoie 0. C'est le résidu de trente ans de croissance, et il ne disparaîtra pas. **L'autocomplétion de votre éditeur et la page php.net sont le remède**, bien plus que la mémorisation, et au bout d'une semaine vous ne remarquez plus ces écarts.

## Les chaînes sont des octets

Une chaîne PHP est une suite d'octets, et non de points de code ou de graphèmes. Il en découle que `strlen('é')` vaut 2, que `strrev('héllo')` massacre l'accent, et que `substr` peut couper un caractère multi-octets en deux.

```php
<?php
declare(strict_types=1);

$word = 'café';

echo strlen($word), PHP_EOL;      // 5
echo mb_strlen($word), PHP_EOL;   // 4
echo strtoupper($word), PHP_EOL;  // CAFé
echo mb_strtoupper($word), PHP_EOL; // CAFÉ
```

**Pour tout texte qu'un humain lira, utilisez la famille `mb_`** : `mb_strlen`, `mb_substr`, `mb_strtoupper`, `mb_str_pad`, et depuis PHP 8.4 `mb_trim`, `mb_ucfirst` et `mb_lcfirst`. Elles supposent UTF-8 par défaut, et les fonctions nues restent utiles pour ce pour quoi elles ont été conçues : données binaires, protocoles ASCII, hachages, et tout ce où l'octet est vraiment l'unité.

Pour tout ce qui dépend de la langue de l'utilisateur, l'extension `intl` enveloppe ICU : `Normalizer` pour ramener formes composées et décomposées à une forme canonique, `Collator` pour trier « é » à côté de « e » selon la langue du lecteur, `NumberFormatter` pour les devises et les pluriels, `IntlDateFormatter` pour des dates écrites comme un lecteur français ou japonais les attend.

Les utilitaires du quotidien sont ceux de n'importe quel langage, avec des noms PHP :

```php
<?php
declare(strict_types=1);

$path = '/var/log/app.log';

var_dump(str_contains($path, 'log'));      // true (PHP 8.0)
var_dump(str_starts_with($path, '/var'));  // true
var_dump(str_ends_with($path, '.log'));    // true

echo implode(', ', ['a', 'b', 'c']), PHP_EOL;    // a, b, c
print_r(explode('/', trim($path, '/')));         // ['var', 'log', 'app.log']
echo str_pad('7', 3, '0', STR_PAD_LEFT), PHP_EOL; // 007
echo ucfirst('php'), PHP_EOL;                    // Php
echo sprintf('%05.2f|%-6s|%03d', 3.14159, 'ok', 7), PHP_EOL; // 03.14|ok    |007
echo number_format(1234567.891, 2), PHP_EOL;     // 1,234,567.89
```

`sprintf` est celui du C, `printf` affiche au lieu de renvoyer, et `number_format` est ce que vous utilisez avant de découvrir `NumberFormatter`.

Deux syntaxes gèrent le texte sur plusieurs lignes. **Le heredoc interpole, le nowdoc non**, et les deux retirent l'indentation du marqueur de fin :

```php
<?php
declare(strict_types=1);

$name = 'Ada';

$greeting = <<<TXT
    Hello, {$name}.
    Welcome back.
    TXT;

$raw = <<<'TXT'
    Hello, {$name}. This stays literal.
    TXT;

echo $greeting, PHP_EOL, $raw, PHP_EOL;
```

<img src="images/ch10-bytes-vs-characters.png" alt="Le mot café dessiné deux fois : en haut, cinq cases d'octets séparées, l'accent à cheval sur deux d'entre elles, mesurées par une règle ordinaire étiquetée strlen ; en bas, quatre tuiles de caractères mesurées par une règle étiquetée mb_strlen" width="560">

## Expressions régulières

PHP utilise PCRE, le même dialecte que Perl et proche de ce qu'acceptent le module `re` de Python et JavaScript. Le motif est une chaîne entre délimiteurs, en général `/` ou `~`, suivis de modificateurs. **Ajoutez le modificateur `u` dès que le texte est en UTF-8**, sans quoi `.` correspond à un seul octet et `\w` ignore les lettres accentuées.

```php
<?php
declare(strict_types=1);

$line = 'Order #4521 shipped to Zoé on 2026-03-14';

if (preg_match('/#(?<id>\d+).*on (?<date>\d{4}-\d{2}-\d{2})/u', $line, $m)) {
    echo $m['id'], ' ', $m['date'], PHP_EOL; // 4521 2026-03-14
}

echo preg_replace('/\s+/u', ' ', "too   many\n\nspaces"), PHP_EOL;

echo preg_replace_callback(
    '/\d+/',
    fn (array $m): string => (string) ($m[0] * 2),
    'a1 b22 c333',
), PHP_EOL; // a2 b44 c666
```

`preg_match` renvoie 1, 0, ou `false` si le motif est mal formé. Les groupes nommés se retrouvent dans le tableau de résultat sous leur nom. `preg_split`, `preg_quote` et `preg_match_all` complètent la famille.

## Les nombres

**`int` est un entier signé sur 64 bits, et quand il déborde, PHP bascule silencieusement en `float`**, sans exception ni retour à zéro. Ce comportement convient à un compteur et devient faux pour un identifiant ou un montant.

```php
<?php
declare(strict_types=1);

var_dump(PHP_INT_MAX + 1);    // float(9.223372036854776E+18)
var_dump(intdiv(7, 2));       // int(3)
var_dump(7 / 2);              // float(3.5), division always yields float unless exact
var_dump(7 % 2);              // int(1)
var_dump(2 ** 10);            // int(1024)
var_dump(fdiv(1, 0));         // float(INF), where 1 / 0 throws DivisionByZeroError

var_dump(0.1 + 0.2 === 0.3);                             // false
var_dump(abs(0.1 + 0.2 - 0.3) < PHP_FLOAT_EPSILON);      // true
var_dump(round(2.5), round(3.5), round(-2.5));           // 3, 4, -3: half away from zero
```

Les flottants sont des doubles IEEE 754, avec les réserves habituelles. `round` arrondit par défaut la moitié en s'éloignant de zéro et accepte une constante de mode pour l'arrondi bancaire. **L'argent, c'est soit des entiers dans la plus petite unité (les centimes), soit de la précision arbitraire** : `bcadd`, `bcmul` et consorts travaillent sur des chaînes, et PHP 8.4 les enveloppe dans `BcMath\Number`, un objet immuable qui supporte les opérateurs.

```php
// PHP 8.4
$price = new BcMath\Number('19.99');
$total = $price * 3;
echo $total, PHP_EOL; // 59.97
```

Pour l'aléatoire, `rand()` et `mt_rand()` sont rapides mais prévisibles. **Tout ce qui touche à la sécurité passe par `random_int`, `random_bytes` ou la classe `Random\Randomizer`** (PHP 8.2), adossés au générateur cryptographique du système d'exploitation.

```php
<?php
declare(strict_types=1);

echo random_int(1, 6), PHP_EOL;                 // a fair die
echo bin2hex(random_bytes(16)), PHP_EOL;        // 32 hex chars, a fine token

$r = new Random\Randomizer();
echo $r->getInt(1, 100), PHP_EOL;
print_r($r->shuffleArray([1, 2, 3, 4]));
echo $r->getBytesFromString('abcdef0123456789', 8), PHP_EOL; // PHP 8.3
```

## Les dates

**Utilisez `DateTimeImmutable` plutôt que `DateTime`.** Les deux existent et partagent une interface, mais la version mutable est un piège : `$date->modify('+1 day')` modifie `$date` sur place et le renvoie, donc chaque référence à cet objet se décale avec lui. La version immuable renvoie un nouvel objet et laisse l'original tranquille, comme vous l'attendez de `java.time` en Java ou de `datetime` en Python.

```php
<?php
declare(strict_types=1);

date_default_timezone_set('UTC');

$start = new DateTimeImmutable('2026-03-14 09:30', new DateTimeZone('Europe/Paris'));
$end = $start->modify('+2 weeks')->setTime(18, 0);

echo $start->format(DateTimeInterface::ATOM), PHP_EOL; // 2026-03-14T09:30:00+01:00
echo $end->format('D, d M Y H:i'), PHP_EOL;            // Sat, 28 Mar 2026 18:00

$diff = $start->diff($end);
echo $diff->days, ' days, ', $diff->h, ' hours', PHP_EOL; // 14 days, 8 hours

$parsed = DateTimeImmutable::createFromFormat('d/m/Y', '01/07/2026');
echo $parsed->getTimestamp(), PHP_EOL;

$inTokyo = $start->setTimezone(new DateTimeZone('Asia/Tokyo'));
echo $inTokyo->format('H:i T'), PHP_EOL; // 17:30 JST

foreach (new DatePeriod($start, new DateInterval('P1D'), 3) as $day) {
    echo $day->format('l'), PHP_EOL; // Saturday, Sunday, Monday, Tuesday
}
```

L'analyseur derrière `new DateTimeImmutable('...')` et `modify()` accepte des expressions en anglais (`'next monday'`, `'first day of last month'`) et toutes les formes ISO courantes. `DateInterval` utilise les durées ISO 8601 (`P1Y2M3DT4H`). Le fuseau par défaut vient de `php.ini` ; le régler sur UTC au début du point d'entrée et convertir aux frontières est la pratique habituelle. Les codes de format sont propres à PHP (`Y-m-d H:i:s`), pas ceux de `strftime`, dépréciée en 8.1.

<img src="images/ch10-immutable-dates.png" alt="À gauche : une page de calendrier étiquetée DateTime avec une flèche qui se replie sur elle-même, la même page raturée avec une nouvelle date et un visage inquiet ; à droite : une page étiquetée DateTimeImmutable qui reste intacte pendant qu'une page neuve avec la nouvelle date apparaît à côté" width="560">

## JSON

`json_encode` et `json_decode` sont intégrés et rapides. **Passez `JSON_THROW_ON_ERROR` à chaque fois**, sans quoi un échec renvoie `false` ou `null` et vous le découvrez trois fonctions plus loin.

```php
<?php
declare(strict_types=1);

$payload = ['id' => 4521, 'tags' => ['php', 'json'], 'total' => 59.97, 'note' => null];

$json = json_encode($payload, JSON_THROW_ON_ERROR | JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
echo $json, PHP_EOL;

$asArray = json_decode($json, true, flags: JSON_THROW_ON_ERROR);   // nested arrays
$asObject = json_decode($json, flags: JSON_THROW_ON_ERROR);        // stdClass objects
echo $asArray['tags'][0], ' ', $asObject->tags[1], PHP_EOL;         // php json

var_dump(json_validate('{"ok": true}')); // true (PHP 8.3), without building the tree
```

Le deuxième argument de `json_decode` choisit entre tableaux associatifs et `stdClass`. Les tableaux sont ce que la plupart du code attend. Les objets de vos propres classes se sérialisent via l'interface `JsonSerializable` : implémentez `jsonSerialize(): mixed` et renvoyez la forme de tableau voulue. Le sens inverse, JSON vers objet typé, n'est pas dans le langage ; bibliothèques et frameworks s'en chargent.

Un écueil mérite sa propre phrase, et [Les tableaux](ch04-arrays.md) explique pourquoi : **un tableau dont les clés ne sont pas `0, 1, 2...` s'encode en objet JSON et non en liste.** Comme `array_filter` laisse des trous et que `json_encode` les voit, votre API renvoie `{"0": ..., "2": ...}` là où vous attendiez une liste, à moins de passer le tableau dans `array_values()` avant de l'encoder.

Les grands entiers survivent à l'aller-retour tant qu'ils tiennent sur 64 bits ; au-delà, décodez avec `JSON_BIGINT_AS_STRING`. Les flottants s'écrivent avec jusqu'à 17 chiffres significatifs par défaut (`serialize_precision`), donc `0.1` reste `0.1`.

## Fichiers et flux

`file_get_contents` et `file_put_contents` lisent ou écrivent un fichier entier en un appel, et acceptent des URL et des enveloppes de flux aussi bien que des chemins. Pour travailler ligne par ligne, il y a le trio à la C `fopen`/`fgets`/`fclose`, ou `SplFileObject`, qui est itérable :

```php
<?php
declare(strict_types=1);

$path = __DIR__ . '/notes.txt';
file_put_contents($path, "one\ntwo\nthree\n");

foreach (new SplFileObject($path) as $n => $line) {
    if ($line !== '') {
        echo $n, ': ', rtrim($line), PHP_EOL;
    }
}

$stdin = fopen('php://stdin', 'r');
$buffer = fopen('php://memory', 'r+');
fwrite($buffer, 'scratch');
rewind($buffer);
echo fread($buffer, 100), PHP_EOL;
```

`__DIR__` est le dossier du fichier courant ; sans lui, les chemins relatifs se résolvent par rapport au répertoire de travail, qui sous un serveur web est rarement celui que vous croyez. Les enveloppes `php://` exposent les flux standard, des tampons mémoire et des fichiers temporaires à travers les mêmes fonctions que les vrais fichiers, et `file_get_contents('https://...')` fonctionne quand `allow_url_fopen` est activé, même si pour du vrai HTTP vous voudrez `curl` ou un client PSR-18.

## Validation, hachage, URI

`filter_var` valide et assainit des scalaires avec un jeu de filtres intégrés, sans dépendance :

```php
<?php
declare(strict_types=1);

var_dump(filter_var('ada@example.org', FILTER_VALIDATE_EMAIL)); // the string, or false
var_dump(filter_var('42', FILTER_VALIDATE_INT));                // int(42)
var_dump(filter_var('yes', FILTER_VALIDATE_BOOL, FILTER_NULL_ON_FAILURE)); // true

$hash = password_hash('correct horse battery staple', PASSWORD_DEFAULT);
var_dump(password_verify('correct horse battery staple', $hash)); // true
echo hash('sha256', 'payload'), PHP_EOL;
```

**`password_hash` choisit l'algorithme, génère le sel et encode le tout dans une seule chaîne**, que `password_verify` relit. Ces deux fonctions couvrent l'ensemble de la question des mots de passe, et `PASSWORD_DEFAULT` migre vers des algorithmes plus solides au fil des versions sans que vous changiez une ligne. `hash` couvre le reste, de `sha256` à `xxh3`, et `hash_hmac` signe.

Depuis PHP 8.5, les URL passent par un vrai analyseur plutôt que par l'approximatif `parse_url` :

```php
// PHP 8.5
$uri = new Uri\Rfc3986\Uri('https://example.org:8443/docs/intro?lang=fr#top');
echo $uri->getHost(), ' ', $uri->getPort(), ' ', $uri->getPath(), PHP_EOL;
// example.org 8443 /docs/intro
```

`Uri\WhatWg\Url`, dans la même extension, applique les règles des navigateurs plutôt que celles de la RFC, pour les cas où vous devez tomber d'accord avec ce que fera un `<a href>`.

Telle est la partie de la bibliothèque standard que vous toucherez au cours d'une semaine ordinaire. La question suivante est ce que PHP vous donne quand l'entrée n'est plus une chaîne dans une variable mais une requête HTTP, et [Une requête web, sans framework](ch11-web-request.md) y répond sans la moindre bibliothèque.
