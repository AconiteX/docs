# see: https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'SWG Source'
copyright = '2020, SWG Source'
author = 'SWG Source'

extensions = [
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

html_static_path = ['_static']
