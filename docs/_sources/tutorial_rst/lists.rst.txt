
Lists
=====

reST supports several types of lists, including unordered lists, ordered lists, nested lists, and definition lists. Below are examples of each type, with detailed explanations.

Basic Usage
-----------------

Unordered Lists
~~~~~~~~~~~~~~~~
To create an unordered list, use one of the following symbols: `*`, `-`, or `+`. These symbols can be used interchangeably to represent bullet points. 

The most commonly used symbol is `*`, but you can choose any of the three symbols depending on your preference or style guide.

Example:

.. code-block:: rst

    * Item 1
    * Item 2
    * Item 3

All three symbols will render as bullet points, but it is a good practice to pick one symbol for consistency throughout your document.

Ordered Lists
~~~~~~~~~~~~~
To create an ordered list, use numbers followed by a period (`.`). Each item in the list will be numbered automatically.

Note: The numbering you use when creating the list doesn't have to be sequential. Sphinx will automatically renumber the items in order.

Example:

.. code-block:: rst

    1. First item
    2. Second item
    3. Third item

Even if you use `1.` for all items, Sphinx will correctly number them starting from 1.

Nested Lists
~~~~~~~~~~~~
Nested lists can be created by indenting items under their parent item. Each level of nesting should be indented by at least two spaces or one tab.

Example:

.. code-block:: rst

    * Level 1 Item 1
      * Level 2 Item 1.1
      * Level 2 Item 1.2
    * Level 1 Item 2
      1. Level 2 Ordered Item 2.1
      2. Level 2 Ordered Item 2.2

This example shows both unordered and ordered nested items. You can mix and match different types of lists (unordered and ordered) within nested levels.

Definition Lists
~~~~~~~~~~~~~~~~
A definition list is used to pair terms with their definitions. In this type of list, the term is followed by a colon (`:`) and the definition is placed on the next indented line.

Example:

.. code-block:: rst

    Python
        : A high-level programming language.

    reStructuredText
        : A lightweight markup language used in technical documentation.

    Sphinx
        : A documentation generator that uses reStructuredText.

Key Points:
- There should be no blank line between a term and its definition.
- Each definition is indented by at least one space or tab.
- You can have multiple definitions for a single term if needed.

For example, if a term has multiple definitions or explanations, you can repeat the pattern:

.. code-block:: rst

    Python
        : A high-level programming language.
        : Widely used for web development, data science, and automation.
