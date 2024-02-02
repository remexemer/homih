# Homih

<p align="center">
    <em>Python CLI utilities to drive proficiency of development flow</em>
</p>

[![build](https://github.com/remexemer/homih/workflows/Build/badge.svg)](https://github.com/remexemer/homih/actions)
[![codecov](https://codecov.io/gh/remexemer/homih/branch/master/graph/badge.svg)](https://codecov.io/gh/remexemer/homih)
[![PyPI version](https://badge.fury.io/py/homih.svg)](https://badge.fury.io/py/homih)

---

**GitLab**: <a href="https://gitlab.com/tshsu/python/homih" target="_blank">https://gitlab.com/tshsu/python/homih</a>

**GitLab Pages**: <a href="https://tshsu.gitlab.io/python/homih" target="_blank">https://tshsu.gitlab.io/python/homih</a>

**GitHub**: <a href="https://github.com/remexemer/homih" target="_blank">https://github.com/remexemer/homih</a>

**GitHub IO**: <a href="https://remexemer.github.io/homih/" target="_blank">https://remexemer.github.io/homih/</a>

---

## Development

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system.

### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
hatch run lint
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
hatch version patch
```

```bash
hatch version minor
```

```bash
hatch version major
```

Your default Git text editor will open so you can add information about the release.

When you push the tag on GitHub, the workflow will automatically publish it on PyPi and a GitHub release will be created as draft.

## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
hatch run docs-serve
```

It'll automatically watch for changes in your code.

## License

This project is licensed under the terms of the MIT license.
