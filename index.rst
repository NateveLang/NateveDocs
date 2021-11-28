
Introducing Nateve
==================

Nateve is a new general domain programming language open source inspired by languages like Python, C++, JavaScript, and Wolfram Mathematica.

Nateve is an transpiled language. Its first transpiler, Adam, is fully built using Python 3.8.

Nateve principal features
-------------------------

1. Simple and easy to use
^^^^^^^^^^^^^^^^^^^^^^^^^

Just install the package and start coding.

2. Intuitive and easy to understand
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quickly understand the language and its features.

3. 100% free and open source
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The language is free and open source. You can use it for any purpose. See the `license <LICENSE>`_.

4. 100% customizable
^^^^^^^^^^^^^^^^^^^^

You can customize the language to your needs. You can make your own language from scratch. See the `Welcome to Nateve templates <#welcome-to-nateve-templates>`_ section for more information.

Welcome to Nateve templates
---------------------------

Nateve Language includes a set of templates that can be used to customize Nateve. Templates are Python modules included in the templates subpackage. You can also create your own templates.

A template is a Python module that contains a set of words translations, functions definitions, and many other customizations. Every template can be used to customize Nateve. You just need to import the template with the ``using`` command and then use the template in the Nateve source code.

Learn more about templates in the `templates use <#using-templates>`_ section.

Why use Nateve templates?
-------------------------

1. Customization
^^^^^^^^^^^^^^^^

You can customize the language to your needs. Feel free to create your own templates or modify existing templates.

2. Team work
^^^^^^^^^^^^

Your team can work together using different languages in the same file or project. For example, you can start coding in English and then switch to French.

It makes it easier to work together. Different team members can work on the same project using their native languages.

3. Easy to share
^^^^^^^^^^^^^^^^

Your templates can be used by other developers. You can easily share your templates with the community.

Options of command line
-----------------------


#. ``build``\ : Transpile Nateve source code to Python 3.8
#. ``run``\ : Run Nateve source code
#. ``transpile``\ : Transpile Nateve source code to an executable file (.exe)
#. ``run-init-loop``\ : Run Nateve source code with an initial source and a loop source
#. `set-time-unit`: Set Adam time unit to seconds or miliseconds (default: milisecond)
#. ``-v``\ : Activate verbose mode

Nateve Tutorial
---------------

In this tutorial, we will learn how to use Nateve step by step.

Step 0: Learn the basics
^^^^^^^^^^^^^^^^^^^^^^^^

We recommend read the README.md file.

Step 1: Installation
^^^^^^^^^^^^^^^^^^^^

Recommend Installation:

Clone the repo
~~~~~~~~~~~~~~

.. code-block:: bash

   $> git clone https://github.com/NateveLang/Adam.git

Add to path
~~~~~~~~~~~

Add your favorite templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Step 2: Create a new Nateve file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   $> cd my-project
   $> COPY CON main.nate

Quick start examples
^^^^^^^^^^^^^^^^^^^^

Hello World program
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   print("Hello, World!")

Is prime? program
~~~~~~~~~~~~~~~~~

.. code-block:: python

   def is_prime(n) {
       if n == 1 {
           return False
       }
       for i in range(2, n) {
           if n % i == 0 {
               return False
           }
       }
       return True
   }

   n = ninput("Enter a number: ")

   if is_prime(n) {
       print("It is a prime number.")
   }
   else {
       print("It is not a prime number.")
   }

Comments
^^^^^^^^

If you want to comment your code, you can use:

.. code-block:: bash

   ~ This is a single line comment ~

   ~
       And this a multiline comment
   ~

Variables
^^^^^^^^^

This language uses variables. For declaring variables, you just need to write the name of the variable and the value of the variable.

For example:

.. code-block:: python

   a = 1                          ~ Interger ~
   b = 1.0                        ~ Float ~
   c = 1 + 2j                     ~ Complex ~
   d = "hello"                    ~ String ~
   e = True                       ~ Boolean ~
   f = [1,2,3]                    ~ Vector ~
   g = (1,2)                      ~ Tuple ~
   h = Polynomial("1 +2x +x^2")   ~ Polynomial ~
   i = $
   | 1 1 2 3 4 |
   | 0 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   $                              ~ Matrix ~

Nateve allows data type as Integer, Float, Complex, Boolean, String, Tuple, None, Vector, Polynomial and Matrix.

Vectors
^^^^^^^

The Vectors allow to use all the data types before mentioned, as well as lists and functions.

Also, they allow to get an item through the next notation:

.. code-block:: python

   value_list = [1,2,3,4,5]
   value_list2 = [0,1,0,1,0]

   print(value_list[0])                ~ Output: 1 ~
   print(value_list[0 : 4])            ~ Output: [1 2 3 4] ~

   print(value_list.dot(value_list2))  ~ Output: 6 ~

   print(value_list.add(value_list2))  ~ Output: [1 3 3 5 5] ~

Matrices
^^^^^^^^

The Matrices are a special type of vectors of vectors.

.. code-block:: python

   a = $
   | 1 5 |
   | 0 2 |
   $

   b = $
   |0 1|
   |1 0|
   $

   print(a)
   ~ Output:
   | 1 5 |
   | 0 2 |
   ~

   c = a.dot(b)
   print(c)
   ~ Output:
   | 5 1 |
   | 2 0 |
   ~

   d = a.plus(b)
   print(d)
   ~ Output:
   | 1 6 |
   | 1 2 |
   ~

Functions
^^^^^^^^^

For declaring a function, you have to use the next syntax:

.. code-block:: python

   def example_function(argument1, argument2, ...) {
       ~ sentence1 ~
       ~ sentence2 ~
       ...
       return Return_Value
   } 

   example_function(argument1, argument2, ...) ~ Call the function ~

Conditionals
^^^^^^^^^^^^

Regarding the conditionals, the syntax structure is:

.. code-block:: python

   if condition {
       ~ consequence ~
   }
   elif condition {
       ~ other_consequence ~
   }
   ...
   else {
       ~  default_consequence ~
   }

For example:

.. code-block:: python

   if x <= 1 and x % 3 == 0 {
       a = 0
   }
   elif x == 9 {
       a = 1
   }
   else {
       a = 2
   }

Loops
^^^^^

In order to use loops, you have to use the next syntax:

While Loop
~~~~~~~~~~

.. code-block:: python

   while condition {
       ~ sentence1 ~
       ~ sentence2 ~
       ...
   }

For Loop
~~~~~~~~

.. code-block:: python

   for iterator in iterable {
       ~ sentence1 ~
       ~ sentence2 ~
       ...
   }

Using Templates
---------------

One of the most important features of Nateve is the use of templates. Templates are a way to write code in a more readable way. They are words translations written in Python. In order to use templates, you just have to write the protected word "using", and then, write the name of the template. For example:

.. code-block:: c++

   using "template_name"

Nateve includes the following standard templates:


#. ``"english"``\ : This template is used to write the code of the program in English. It is the default template.
#. ``"spanish"``\ : This template is used to write the code of the program in Spanish.
#. ``"french"``\ : This template is used to write the code of the program in French.

You also can use your own templates. Just create a file with the name of the template and write the code of the template in the file. Here is a blank template:

.. code-block:: python

   # The name of the transpiler. This line is required. Do not change it.
   transpiler_name = "adam"

   """
   The following code is the translation of the code.
   You can write your code here and modify the content of the variables.
   Do not change the name of the variables.
   """

   # All the symbols that the transpiler uses.
   mayusc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   alphabet = mayusc + mayusc.lower() + "_"
   digits = "0123456789"
   alphanum = alphabet + digits
   blanks = "/t /n"
   strings = ["'", '"', '"""', "'''"]
   matrices = "$"
   vectors = "[]"
   embedded = "°"
   commentaries = "~"
   floating = "."
   one_char_symbols = "+-*/%=<>()[]{}#@,."
   two_char_symbols = ["//", "==", "<=", ">="]

   # All the data types that the transpiler uses.
   FLOAT = "float"
   INT = "int"
   COMPLEX = "complex"
   STRING = "string"
   DOCSTRING = "docstring"
   NULL = "none"
   MATRIX = "matrix"
   VECTOR = "vector"

   # All the keywords that the transpiler uses.
   USE, INCLUDE = "using", "include"
   IMPORT, FROM, AS, PASS, IN = "import", "from", "as", "pass", "in"
   IF, ELIF, ELSE = "if", "elif", "else"
   TRY, EXCEPT, WITH = "try", "except", "with"
   WHILE, FOR, BREAK, CONTINUE = "while", "for", "break", "continue"
   OPERATOR, RETURN = "def", "return"
   CLASS, SELF = "class", "self"
   AND, OR, NOT, TRUE, FALSE = "and", "or", "not", "True", "False"

   # All the status codes that the transpiler uses.
   embedding = 200
   identifier = 300
   eof = 400

   # All extra functions that the transpiler uses. Feel free to add your own functions.
   # The string special_functions is used to write these functions.
   # You can use variables in it using the fstring notation.
   special_functions = f"""
   def ninput(prompt = '', default = ''):
       return float(input(prompt, default))

   def binput(prompt = '', default = ''):
       return bool(input(prompt, default))

   def update_std():
       subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])
   """

Some Examples
-------------

Example 1
^^^^^^^^^

.. code-block:: python

   ~Nateve Example 1~

   update_std()  ~update std library~

   for i in range(2) {
       print(i)
   }

   install("matplotlib")

   try {
       print(2/0)
   }

   except {
       print("xd")
   }

Output:

.. code-block:: bash

   0
   1
   matplotlib successfully installed
   xd

Example 2
^^^^^^^^^

.. code-block:: python

   ~Nateve Example 2~

   theta = pi/3
   print(sin(theta), cos(theta), tan(theta))

   p = sin_serie
   print(p.eval(theta))

   derive(p)

   print(p.eval(theta))

   import numpy as np
   x = "hello"
   c = Matrix("""
   | 1 1 2 3 4 |
   | 0 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   """)
   c.display()

   a = Vector("[ 1 2 3 4 5 6 30 0 9]")
   a.display()

Output:

.. code-block:: bash

   0.8660254037844386 0.5000000000000001 1.73205080756887
   0.8660254037844386
   0.5000000000000001
   | 1 1 2 3 4 |
   | 0 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   [ 1 2 3 4 5 6 30 0 9 ]

Example 3
^^^^^^^^^

.. code-block:: python

   ~Nateve Example 3~

   using "spanish"

   theta = pi/3
   imprime(sen(theta), cos(theta), tan(theta))

   p = serie_sen
   imprime(p.eval(theta))

   deriva(p)

   imprime(p.eval(theta))

   importa numpy como np
   x = "hello"
   c = Matriz("""
   | 1 1 2 3 4 |
   | 0 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   """)
   c.display()

   a = Vector("[ 1 2 3 4 5 6 30 0 9]")
   a.display()

Output:

.. code-block:: bash

   0.8660254037844386 0.5000000000000001 1.73205080756887
   0.8660254037844386
   0.5000000000000001
   | 1 1 2 3 4 |
   | 0 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   | 1 1 2 3 4 |
   [ 1 2 3 4 5 6 30 0 9 ]

Example 4
^^^^^^^^^

.. code-block:: python

   ~Nateve Example 4~

   using "spanish"

   amo_Nateve = verdadero

   si  amo_Nateve == verdadero {
       imprime("Yo amo Nateve!")
   }

   delocontrario {
       imprime("Odio Nateve :c")
   }

   usando "english"

   if 1 < 3 {
       print("Try Nateve!")
   }
   else {
       print("NO")
   }

   using "french"

   v = "Bonjour"
   imprimer(v, "Nateve!")

Output:

.. code-block:: bash

   Yo amo Nateve!
   Try Nateve!
   Bonjour Nateve!

Example 5
^^^^^^^^^

.. code-block:: python

   ~Nateve Example 5~

   include "example4.nate"

   using "spanish"

   imprime("Nateve example 5")

Output:

.. code-block:: bash

   Yo amo Nateve!
   Try Nateve!
   Bonjour Nateve!
   Nateve example 5

Example 6
^^^^^^^^^

.. code-block:: python

   ~Nateve Example 6~

   using "spanish"

   incluye "example5.nate"

   a = $
   | 1 5 |
   | 0 2 |
   $

   b = $
   |0 1|
   |1 0|
   $

   imprime("a = ")
   imprime(a)

   imprime("b = ")
   imprime(b)

   c = a.dot(b)

   imprime("a * b =")
   imprime(c)

   imprime("a + b =")
   print(a.plus(b))

   d = [1, 2, 3, 4, 5]
   imprime(d)

   e = [0, 1, 0, 1, 0]
   imprime(e)

   f = d.dot(e)
   imprime(f)

   g = d.plus(e)
   imprime(g)

   ~ using spanish, "y" means "and".
   Then, we need to use other template like french ~

   using "french"

   definir r(x, y, z){
   retourner $
   |x|
   |y|
   |z|
   $
   }

   x, y, z = 1, 5, 3

   j = r(x, y, z)

   imprimer(j)

   k = $
   |2 0 0|
   |0 2 0|
   |0 0 2|
   $

   imprimer(k.dot(j))

Output:

.. code-block:: bash

   Yo amo Nateve!
   Try Nateve!
   Bonjour Nateve!
   Nateve example 5
   a =
   | 1 5 |
   | 0 2 |

   b =
   | 0 1 |
   | 1 0 |

   a * b =
   | 5 1 |
   | 2 0 |

   a + b =
   | 1 6 |

   [1, 2, 3, 4, 5]
   [0, 1, 0, 1, 0]
   6
   [1, 3, 3, 5, 5]
   | 1 |
   | 5 |
   | 3 |

   | 2 |
   | 10 |
   | 6 |

Feedback
--------

I would really appreciatte your feedback. You can submit a new issue.

Contribute
----------

This is an **opensource** project, everyone can contribute and become a member of the community of **Nateve**.

Why be a member of the Nateve community?
----------------------------------------

1. A simple and understandable code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The source code of Adam is made with Python 3.8, a language easy to learn, also good practices are a priority for this project.

2. A great potencial
^^^^^^^^^^^^^^^^^^^^

This project has a great potential to be the next programming language for education, to develop the quantum computing, and to develop the AI.

3. Simple
^^^^^^^^^

One of the main purposes of this programming language is to create an easy-to-learn language, which at the same time is capable of being used for many different purposes.

4. Respect for diversity
^^^^^^^^^^^^^^^^^^^^^^^^

Everybody is welcome, it does not matter your genre, experience or nationality. Anyone with enthusiasm can be part of this project. Anyone from the most expert to the that is beginning to learn about programming, marketing, design, or any career.

How to start contributing?
--------------------------

There are multiply ways to contribute, since sharing this project, improving the brand of SigmaF, helping to solve the bugs or developing new features and making improves to the source code.


* 
  **Share this project**\ : You can put your star in the repository, use the topic `nateve <https://github.com/topics/nateve>`_ or talk about this project. You can use the hashtag #Nateve in Twitter, LinkedIn or any social network too.

* 
  **Improve the brand of Nateve**\ : If you are a marketer, designer or writer, and you want to help, you are welcome.

* 
  **Help to solve the bugs**\ : if you find one bug notify us an issue. On this we can all improve this language.

* 
  **Developing new features**\ : If you want to develop new features or making improvements to the project, you can do a fork to the ``dev`` branch (here are the ultimate develops) working there, and later do a `\ ``pull request`` <https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_ to ``dev`` branch in order to update **Nateve**.

NQS inside
==========

NQS: Natural Quantum Script. A special domain programming language that aims to simplify the first contact with quantum computing
---------------------------------------------------------------------------------------------------------------------------------

Natural Quantum Script is a special domain programming language that aims to simplify the first contact with quantum computing for people who have prior knowledge in quantum circuits, but not in quantum software development.

Scripts written in NQS seek to visually resemble quantum circuits as much as possible. For example:

.. code-block:: bash

   q0 q1
   X
   H
   .--- X
   c1

NQS is based on Qiskit, but seeks to go mainstream in the future. This is an OS project whose initial goal was to make it easier to write basic scripts in Qiskit and to bridge the gap for people who don't dare to delve into quantum computing.

Eggdriver Standard Library
==========================

Most of Nateve functions, variables and classes are implemented in the **Eggdriver Standard Library**.

In this section we will see how to use the Eggdriver Standard Library features.

1. clearConsole
---------------

Clear the console.

.. code-block:: python

   clearConsole() # clear the console

2. display
----------

Display a text in the console each certain number of milliseconds, while a condition is true.
The default condition is ``True``.    

.. code-block:: python

   display("Hello world!", 1000, 1 > 0) # display the text "Hello world!" for 1 second

Each 1 second:

.. code-block:: bash

   Hello world!

3. e
----

The Euler number with 73 digits of precision.

e =  2.7182818284590452353602874713526624977572470936999595749669676277240766303

4. get
------

Get an input, with a tag.

.. code-block:: python

   >>> input_string = get("my-console-application")
   $my-console-application> Hi
   >>> input_string
   'Hi'

5. inf
------

The computable infinity used for limits calculation.

inf = 10 ** 11

6. itself
---------

The identity function.

.. code-block:: python

   >>> itself(10)
   10

7. pg
-----

Print content in white and get an input with a tag. The default tag is 'egg'.

.. code-block:: python

   >>> input_string = pg('Hello world!', "my-console-application")
   Hello world!
   $my-console-application> Hi
   >>> input_string
   'Hi'

8. pi
-----

The number pi with 73 digits of precision.

pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062

9. ProgressBar
--------------

A progress bar pip-like for console implementations.

.. code-block:: python

   >>> bar = ProgressBar()
   >>> bar.iterate(printPercent = True)
   |████████████████████████████████|      100%

ProgressBar.bar
^^^^^^^^^^^^^^^

Returns a ProgressBar as a text, with a certain length and percent of progress.

.. code-block:: python

   >>> p_bar = ProgressBar()
   >>> text = p_bar.bar(0.5, 16)
   >>> text
   |████████        |      50%

ProgressBar.display
^^^^^^^^^^^^^^^^^^^

Display a progress bar in the console, with a certain length and percent of progress, waiting a certain number of milliseconds.
You can also set the ``printPercent`` parameter to ``True`` to print the percent of progress.

.. code-block:: python

   >>> p_bar = ProgressBar()
   >>> p_bar.display(0.75, 16, 1000, printPercent = False)
   |████████████    |

ProgressBar.iterate
^^^^^^^^^^^^^^^^^^^

iterate(self, function = clearConsole, printPercent = False):
For each percent of progress, display a progress bar in the console, with length 32 and a sleeping time of 24 milliseconds.
You can choose a function to execute at each iteration.

.. code-block:: python

   p_bar = ProgressBar()

   def my_function():
       print("Hello world!")
       clearConsole()

   p_bar.iterate(my_function, printPercent = True)

Iteration 25:

.. code-block:: bash

   Hello world!
   |████████                        |      100%

Last iteration:

.. code-block:: bash

   Hello world!
   |████████████████████████████████|      100%

10. put
-------

Print content in a certain eggdriver color. The default color is white. You can set the color to "" to reset the color.
You can also set an ending string using the ``end`` parameter.

.. code-block:: python

   put("Hi", "", ";")

.. code-block:: bash

   Hi;

11. R
-----

The Reals numbers set.

R = [-inf, inf]

12. series_inf
--------------

The computable infinity used for series calculation.

series_inf = 500

13. sleep
---------

Wait a certain number of milliseconds.

.. code-block:: python

   sleep(1000) # sleep for 1 second

14. sysCommand
--------------

Execute a python command. (Currently only for Windows).

.. code-block:: python

   sysCommand("-m pip install --upgrade pip") # execute the command "py -m pip install --upgrade pip"

Templates Standard Library
==========================
