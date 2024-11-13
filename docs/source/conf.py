# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Auromix Sphinx Tutorial'
copyright = '2023-2024, Herman Ye@Auromix'
author = 'Herman Ye'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
# html_theme = 'alabaster'

# Select theme for both light and dark mode
pygments_style = "default"
# Select a different theme for dark mode
pygments_style_dark = "github-dark"


# Material theme options (see theme.conf for more information)

html_theme_options = {
    "logo_light": "_static/auromix_logo.webp",
    "logo_dark": "_static/auromix_logo.webp",
    "show_prev_next": True,
}


html_static_path = ['_static']

html_css_files = ['custom.css']  # The custom CSS file you will create

