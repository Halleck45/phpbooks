# Laravel : Breeze, Fortify et Jetstream

**Laravel apporte trois réponses officielles à « ajoutez une connexion », étagées selon ce que vous voulez recevoir tout fait.**

**Breeze** installe des fichiers de vues et des contrôleurs dans votre projet. Vous obtenez l'inscription, la connexion, la réinitialisation du mot de passe et la vérification de l'e-mail, sous forme de code qui vous appartient et que vous pouvez modifier tout de suite.

```bash
composer require laravel/breeze --dev
php artisan breeze:install blade
npm install && npm run dev
php artisan migrate
```

**Fortify** implémente la même logique d'authentification en paquet purement backend, sans aucune vue. Il est fait pour un front sur mesure ou pour une API.

```bash
composer require laravel/fortify
php artisan vendor:publish --provider="Laravel\Fortify\FortifyServiceProvider"
php artisan migrate
```

**Jetstream** s'appuie sur Fortify et ajoute une coquille d'application complète : gestion d'équipes, jetons d'API, authentification à deux facteurs, et un front au choix en Livewire ou en Inertia. Il vise les produits SaaS qui ont besoin de comptes et d'équipes dès le premier jour.

```bash
composer require laravel/jetstream
php artisan jetstream:install livewire
npm install && npm run build
php artisan migrate
```

## Lequel choisir

Breeze pour une application classique où vous voulez voir et adapter le code d'authentification tout de suite. Fortify quand le front est Inertia, une application mobile ou du sur mesure qui n'a que faire des vues de Breeze. Jetstream quand le produit est multi-tenant ou organisé par équipes et que vous bâtiriez cette structure de toute façon.

## Quand ce n'est pas le bon outil

Un site vitrine d'une page sans comptes utilisateurs, ou un projet où les rôles intégrés de WordPress (voir [WordPress : rôles, capacités et mots de passe d'application](ch04-03-wordpress-roles-capabilities.md)) couvrent déjà le besoin sans ajouter de framework.

> **Sous le capot :** les trois paquets s'appuient sur la façade `Hash` de Laravel, qui utilise par défaut bcrypt ou argon2id. Les deux algorithmes sont lents à dessein, pour que la force brute sur des empreintes volées reste hors de portée. Vous n'appelez jamais de fonction de hachage ; le garde d'authentification le fait à chaque connexion.
