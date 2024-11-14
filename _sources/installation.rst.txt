🛠️ Installation
==========================
1. **Clone the Repository**

   .. code-block:: bash

       git clone https://github.com/Auromix/sphinx_tutorial.git
       cd sphinx_tutorial

2. **Install Sphinx**

   Install Sphinx and necessary dependencies:

   .. code-block:: bash

       # Install Sphinx
       pip install -U sphinx

   Install the required themes:

   .. code-block:: bash

       # Install Material Sphinx theme
       pip install git+https://github.com/bashtage/sphinx-material.git
       # Install sphinxawesome-theme
       pip install sphinxawesome-theme

3. **Build the Documentation**

   To generate the HTML files for this repository, navigate to the `docs` directory and run the following command:

   .. code-block:: bash

       cd docs
       make html


   To view the generated documentation, use:

   .. code-block:: bash

       xdg-open build/html/index.html

   For specific usage details and syntax demonstrations, refer to the individual `.rst` files in the `docs` directory.

4. **Build for github pages**


