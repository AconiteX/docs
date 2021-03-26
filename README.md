# SWG Source Documentation
[![Documentation Status](https://readthedocs.org/projects/aconitedocs/badge/?version=latest)](https://aconitedocs.readthedocs.io/en/latest/?badge=latest)

This repository houses the documentation for SWG Source. The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and rendered via [ReadTheDocs](https://readthedocs.org/). The browsable documentation is available at [docs.swgsource.com](http://docs.swgsource.com) which is an alias to the ReadTheDocs swgsource.readthedocs.io site.

## Structure and Syntax
Every page in the documentation is housed inside the `docs` directory. Documentation pages are written using the plain text markup language [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (the `.rst` files).

* How is navigation changed??
* Documentation pages should be organized into sub-directories by section (top most header) (e.g. all pages under "Getting Started" should go in `docs/getting-started`). The only files in `/docs/` are the index and configuration files.
* Images should be placed in `docs/_images/section` (e.g. `docs/_images/getting-started/screenshot1.jpg`) which can then be referenced in rst like: `a`. The only files in the root `_images` folder are system-referenced.
* For syntax examples for special context blocks like the `NOTICE` block, see the raw .rst files already in use.
* Diagram Visualizations are generated from [Graphviz](https://graphviz.org/). For implementation examples, see the [Sphinx Graphviz Extension Documentation](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html).

## Editing or Contributing
To contribute, simply add or edit a file in the `docs` directory and submit via pull request. When a pull request is merged, ReadTheDocs will automatically rebuild the documentation with the new changes and add them to the documents site, so no additional steps are required.

To test your changes locally and render the documentation pages as they will appear when you commit, clone the repository and navigate to the `docs` folder inside the docs repository (which would be `clone-path/docs/docs`) and run `make html`. The compiled files will be placed in `_build/html/` where you can open them with your browser locally to preview the changes. GitHub also renders .rst files, but certain syntax will not appear as it would when built by Sphinx and under the ReadTheDocs theme.

Depending on what you're trying to do, you may need to install Sphynx (and Python if you don't have it) via `pip install sphinx`. If you are using the SWG Source VM, you just need to install Sphinx. You can refer, generally, to the [ReadTheDocs Documentation](https://docs.readthedocs.io/en/stable/index.html) or the [Sphinx Documentation](https://www.sphinx-doc.org/en/master/) to determine how to achieve a specific goal or ask Aconite in the [SWG Source Discord](https://discord.gg/Va8e6n8).

## Bug Reports
If you notice a problem, typo, etc. in any of the documentation, please create a [GitHub Issue](https://github.com/SWG-Source/docs/issues).
