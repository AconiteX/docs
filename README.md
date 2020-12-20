# SWG Source Documentation
[![Documentation Status](https://readthedocs.org/projects/aconitedocs/badge/?version=latest)](https://aconitedocs.readthedocs.io/en/latest/?badge=latest)

This repository houses the documentation for SWG Source. The documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/) and rendered via [ReadTheDocs](https://readthedocs.org/). The browsable documentation is available at [docs.swgsource.com](http://docs.swgsource.com) which is an alias to the ReadTheDocs swgsource.readthedocs.io site.

## Structure and Syntax
Every page in the documentation is housed inside the `docs` directory. Documentation pages are written using the plain text markup language [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (the `.rst` files). The index file (`index.rst`) houses the home page as well as the side bar navigation structure.

## Editing or Contributing
To contribute, simply add or edit a file in the `docs` directory and submit via pull request. When a pull request is merged, ReadTheDocs will automatically rebuild the documentation with the new changes and add them to the documents site, so no additional steps are required.

To test your changes locally and render the documentation pages as they will appear when you commit, clone the repository and navigate to the `docs` folder inside the docs repository (which would be `clone-path/docs/docs`) and run `make html`. The compiled files will be placed in `_build/html/` where you can open them with your browser locally to preview the changes. GitHub also renders .rst files, but certain changes may render differently depending on the markup syntax used.

Depending on what you're trying to do, you may need to install Sphynx (and Python if you don't have it) via `pip install sphinx`. If you are using the SWG Source VM, you just need to install Sphinx. You can refer, generally, to the [ReadTheDocs Documentation](https://docs.readthedocs.io/en/stable/index.html) or the [Sphinx Documentation](https://www.sphinx-doc.org/en/master/) to determine how to achieve a specific goal.

