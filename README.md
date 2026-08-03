<p align="center">
  <a href="https://codecov.io/gh/CodyCBakerPhD/recipes"><img src="https://codecov.io/gh/CodyCBakerPhD/recipes/graph/badge.svg" alt="Coverage"></a>
</p>

# Recipes

Structured YAML recipe/ingredient database and Python meal planning software for our household.

This repository is the source of truth for the recipe and ingredient content (`docs/recipes`, `docs/ingredients`)
and for the `como_recipes` Python package (recipe/ingredient data model, registration, CLI, and desktop app).

The [`como_recipes` website](https://github.com/CodyCBakerPhD/como_recipes) keeps its own synced copy of the YAML
content to build and deploy the static site from.

## Installation

To install and run the app, use the [CoMo Launcher](https://github.com/CodyCBakerPhD/como_apps_launcher_public/releases).

## Development

```bash
pip install -e .[all]
pytest tests
```

## Adding a recipe

Open a [new recipe request](https://github.com/CodyCBakerPhD/recipes/issues/new?template=new_recipe.yaml) or add a
YAML file directly to `docs/recipes` following the format described in `docs/recipes/README.md`.
