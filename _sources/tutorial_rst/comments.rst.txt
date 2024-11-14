
Comments
=================

In reStructuredText (.rst) files, comments are a useful way to add notes, annotations, or other content that should not appear in the final output. Comments are initiated with two dots `..`, and everything following them on the same line (or in the same block) is treated as a comment.

**Basic Comment Syntax**

To add a comment, simply use the following syntax:

::

    ..  This is a comment
        This content will not appear in the final document.
        Comments can span multiple lines and can include detailed explanatory text.


This example shows that comments can span multiple lines, and any content written after `..` will be ignored by Sphinx during the rendering process.

**Example with Normal Text**

::

    Normal text without `..` will be visible in the final document.

