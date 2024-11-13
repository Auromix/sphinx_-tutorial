
Block
=====

Code Block
-----------
In reStructuredText (reST), you can display code with syntax highlighting by specifying the programming language and optionally adding a caption to the code block. This is especially useful when sharing code snippets in a specific language and providing additional context or a title.

Short Code Snippet
~~~~~~~~~~~~~~~~~~~~~~~~~~~
To show a short code snippet inline, you can use backticks:

Example:

.. code-block:: rst

    ``matrix=np.zeros((n,n))``

This renders as ``matrix=np.zeros((n,n))`` in the documentation.

Longer Code Blocks
~~~~~~~~~~~~~~~~~~~~~~~~
For longer code blocks, use the `.. code-block::` directive, followed by the language tag (e.g., `python`), to enable syntax highlighting and optionally add a caption:

Example:

.. code-block:: python
    :caption: Example Python Code

    def hello_world():
    print("Hello, world!")

::

    .. code-block:: python
        :caption: Example Python Code

        def hello_world():
        print("Hello, world!")

Explanation:

- **`.. code-block::`**: This directive starts the code block.

- **Language tag (e.g., `python`)**: The language tag enables syntax highlighting specific to the chosen programming language. You can replace `python` with any other language tag (e.g., `java`, `cpp`, `html`) depending on the language of the code.

- **`:caption:`**: This option allows you to add a caption or title above the code block. This helps provide context or describe the purpose of the code example.

Quote Block
-----------
A quote block is used to display a quoted passage or citation. To create a blockquote in reST, start the block with two colons (`::`), followed by the quoted text.

Example:

::

    This is a blockquote.
    It can span multiple lines.

:: 

    ::

        This is a blockquote.
        It can span multiple lines.


Explanation:

- The `::` symbol begins the quote block. The quoted text follows, and it can span multiple lines.

Note Block
----------
Note blocks provide additional information, tips, or clarifications. These blocks are commonly used for helpful suggestions in documentation.

Example:

.. note::

   This is a tip on how to use this feature.

Tip Block
----------
A tip block is used to give advice or suggestions that improve efficiency or ease of use.

Example:

.. tip::

   Use this shortcut to increase your productivity.

Warning Block
-------------
A warning block highlights important cautionary information to alert the reader about potential risks.

Example:

.. warning::

   Be cautious when performing this action, as it could overwrite your data.

Attention Block
---------------
An attention block is used to highlight important information, often related to critical points or specific conditions.

Example:

.. attention::

   Please note that this feature is only available under certain conditions.

Caution Block
-------------
A caution block provides warnings about potential dangers or system failures, helping users to avoid making harmful mistakes.

Example:

.. caution::

   Be careful! This action could cause the system to crash.


Custom Block
-----------------------
In Sphinx, you can customize **admonition blocks** (such as custom alerts, notes, or warnings) to enhance the readability of your documentation. 

To do this, you can use the `.. admonition::` directive to create custom blocks. You can also specify the type of block using the `:name:` parameter.

Steps to Customize Admonition Blocks:

1. **Define Custom Styles**
   
   First, you need to define custom styles in your Sphinx project’s `conf.py` configuration file. You can achieve this by customizing the CSS. For example, you can add a custom class to change the appearance.

   In `conf.py`, make sure the `html_static_path` and `html_css_files` are enabled:

   .. code-block:: python
       
       html_static_path = ['_static']
       html_css_files = ['custom.css']  # The custom CSS file you will create
   

2. **Create a Custom CSS File**

   Create a file named `custom.css` and place it in the `/_static/` directory. Then, define custom styles in that file. For example:

   .. code-block:: css

        .admonition.custom {
            background-color: #f0f8ff;
            border-left: 4px solid #0099cc;
            padding: 10px;
            font-size: 14px;
        }
        .admonition.custom .admonition-title {
            color: #0099cc;
            font-weight: bold;
        }


   This CSS will give the custom admonition block a light blue background and a blue left border.

3. **Use .. admonition:: to Create Custom Blocks**

   You can use the `.. admonition::` directive in your `.rst` files to insert the custom block. Here’s how to do it:
    ::

        .. code-block:: rst

            .. admonition:: Custom Block
                :class: custom

                This block is an example of a custom admonition. 
                You can put any content here that you'd like to highlight.


   In this example, `Custom Block` is the title of the block, and `:class: custom` applies the style defined in `custom.css`.

4. **Check Result**

.. admonition:: Custom Block
   :class: custom

   This block is an example of a custom admonition. 
   You can put any content here that you'd like to highlight.


This is the content of a custom admonition block. You can put whatever content you want to display here.

1. **Title**: The title of the custom admonition block will appear at the top of the block, bold and in blue.
2. **Content**: The content of the block will appear below the title with the background color and border style you set.

This way, you can create any type of custom admonition block and give it a personalized style.