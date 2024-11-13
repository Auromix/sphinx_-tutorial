# 🐫 Sphinx Tutorial

Welcome to the **Sphinx Tutorial** repository! This guide provides an in-depth introduction to using the Sphinx documentation generator, with practical examples of commonly used `.rst` syntax and comprehensive instructions for creating well-structured documentation.

## 🧐 Overview

Sphinx is a powerful documentation generation tool, initially developed for the Python community to build Python documentation but now widely used for various programming languages and complex project documentation. Sphinx is especially effective for large-scale projects requiring features like multi-language support, cross-referencing, and structured organization.

### Key Features of Sphinx

1. **Automated Documentation Generation**: Parses code comments, particularly Python docstrings, to automatically generate API documentation.
2. **Multiple Output Formats**: Outputs to formats like HTML, LaTeX (for PDF), and EPUB.
3. **Extensive Extensions and Plugins**: Provides plugins for indexing, mathematical notation, charts, code highlighting, and custom extensions.
4. **Multi-Language Support**: Allows easy internationalization and localization, enabling multi-language documentation.
5. **Cross-Project Referencing**: Facilitates cross-referencing across documents and code, making it ideal for structured, large-scale projects.

Sphinx is commonly used for generating API documentation, software manuals, tutorials, and knowledge bases. By writing reStructuredText files and using Sphinx’s tools, you can create structured and comprehensive documentation for your projects.

## 📋 Repository Contents

This repository includes:

- **Example Files**: `.rst` files that demonstrate essential Sphinx syntax and formatting options.
- **Build Guide**: Step-by-step instructions for configuring and building Sphinx documentation for your project.

## 👉 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Auromix/sphinx_tutorial.git
cd sphinx_tutorial
```

### 2. Install Sphinx

Install Sphinx and any necessary dependencies:

```bash
# Install Sphinx
pip install -U sphinx
```

```bash
# Install Material Sphinx theme
pip install git+https://github.com/bashtage/sphinx-material.git
# Install sphinxawesome-theme
pip install sphinxawesome-theme
```

Check the installed version:

```bash
sphinx-quickstart --version
```

### 3. Build the Documentation

The **examples** are located under the `docs` directory. Users can try generating the HTML files for this repository to see the documentation in action. Navigate to the `docs` folder and build the HTML files with the following commands:

```bash
cd docs
make html
```

To view the generated documentation, use:

```bash
xdg-open build/html/index.html
```

For specific usage details and syntax demonstrations, refer to the individual `.rst` files in the `docs` directory.

## 😎 Use Sphinx in Your Project

If you need to set up Sphinx for your own project, follow these steps:

1. **Create a `docs` directory** in the project root to house the Sphinx project files.

   ```bash
   cd <YOUR_PROJECT_ROOT_DIR>
   sphinx-quickstart docs
   ```

   This initializes the Sphinx project with a basic structure. Follow the prompts to configure directories, project details, and settings.

2. **Build the Documentation**:
   After configuring the `.rst` files, navigate to the `docs` folder and run:

   ```bash
   make html
   ```

   This command generates HTML documentation in the `_build/html` directory.

## 📜 License

```text
Copyright 2023-2024 Herman Ye@Auromix

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific
language governing permissions and limitations under the License.
```
