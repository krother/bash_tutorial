# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bash Tutorial'
copyright = '2024, Kristian Rother'
author = 'Kristian Rother'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxcontrib.cairosvgconverter',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

language = 'ls'

# ---- Options for HTML output ----
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'academis_sphinx_theme'
html_theme_path = ['themes']
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"

html_sidebars = {
    '**': [
        #'about.html',
        #'localtoc.html',
        #'navigation.html',
        #'searchbox.html',
    ]
}
html_theme_options = {
    'logo': 'academis.png',
    'github_user': 'krother',
    'github_repo': 'bash_tutorial',
    'show_relbar_top' : True,
    'show_relbar_bottom' : True,
}

# ---- Options for PDF output ----

latex_elements = {
    'preamble': "\linespread{1.25}",
}