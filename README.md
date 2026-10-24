# relational-synth-key-forge

## Français

Générer des tables synthétiques reliées sans clé étrangère orpheline.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m relational_synth_key_forge examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Génère des tables synthétiques dans l’ordre topologique d’un DAG de clés étrangères. Le contrat relationnel est exécutable : les tests insèrent les sorties dans SQLite avec foreign_keys activé.

### Limites

Schéma et distributions fournis, clés simples, graphes sans cycle ; pas d’apprentissage depuis données privées ni de garantie de réalisme, confidentialité ou compatibilité complète SQL.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Generate linked synthetic tables without orphan foreign keys.

Synthetic data; no network access or secret required.

```sh
python -m relational_synth_key_forge examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Generates synthetic tables in topological order of a foreign-key DAG. The relational contract is executable: tests insert outputs into SQLite with foreign_keys enabled.

### Limits

Caller-supplied schema and distributions, simple keys and acyclic graphs; no learning from private data or realism, privacy or full SQL-compatibility guarantee.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Generar tablas sintéticas relacionadas sin claves foráneas huérfanas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m relational_synth_key_forge examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Genera tablas sintéticas en orden topológico de un DAG de claves foráneas. El contrato es ejecutable: las pruebas insertan resultados en SQLite con foreign_keys activado.

### Límites

Esquema y distribuciones suministrados, claves simples y grafos acíclicos; sin aprendizaje de datos privados ni garantía de realismo, privacidad o compatibilidad SQL completa.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.sqlite.org/foreignkeys.html
