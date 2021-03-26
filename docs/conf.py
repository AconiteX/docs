# Sphynx Config Info: https://www.sphinx-doc.org/en/master/usage/configuration.html
# Theme Config Info: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

project = 'SWG Source'
copyright = '2020, SWG Source'
author = 'SWG Source'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
html_theme_options = {
  'logo_only': True,
  'display_version': False,
  'style_external_links': True,
  'includehidden': False,
  'titles_only': True,
  'show_sphinx': False,
}
html_static_path = ['_static']
html_logo = "logo.svg"
def setup(app):
    app.add_css_file('style.css')
