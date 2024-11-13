

Tables
======

reST allows you to create tables in various formats, with the two most common types being **simple tables** and **grid tables**.

Simple Tables
--------------
Simple tables are ideal for displaying small amounts of data with minimal alignment needs. These tables use the `=` symbol to create separation lines between the header and the content.

Example:

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

.. code-block:: rst

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

In this example:
- The `=` symbol is used to create boundaries between the header and the data rows.
- Columns are separated by spaces.
- The `=` symbol is placed at the top and bottom of the table to indicate the table's boundaries.

Simple tables are straightforward to create, but they do not provide control over column width or precise alignment.

Grid Tables
------------
Grid tables are more suitable for complex tables where precise alignment and column width control are required. These tables use `+` for corners and intersections, `-` for horizontal lines, and `|` for vertical lines. The `=` symbol is used to separate header rows from data rows.

Example:

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      | ...      |
+------------------------+------------+----------+----------+



.. code-block:: rst

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | ...        | ...      | ...      |
    +------------------------+------------+----------+----------+

In this example:
- The `+` symbol marks the intersections of the table, such as the corners and the points where vertical and horizontal lines meet.
- The `-` symbol is used for horizontal lines separating rows.
- The `|` symbol separates the columns.
- The `=` symbol is used to separate the header row from the data rows.

Grid tables provide better control over the layout and alignment, making them ideal for more detailed or structured tables.

Comparison Between Simple and Grid Tables
-----------------------------------------
- **Simple Tables**:
  - Easy to create and read.
  - Suitable for smaller tables with simpler data.
  - Limited control over column width and alignment.
  
- **Grid Tables**:
  - Suitable for more complex tables with precise alignment requirements.
  - Provide better control over the layout, especially column widths.
  - Require more characters to define the structure but offer better readability for larger tables.

Both types of tables serve different purposes. Simple tables are perfect for basic content, while grid tables excel in more structured or detailed tables where precise control over formatting is necessary.
