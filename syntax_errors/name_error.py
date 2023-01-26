"""
Python es bastante laxo con las normas de declaración/definición de variables. Esto en muchos otros lenguajes habría sido un error sintáctico al "compilar"
el código. El intérprete de Python, en este caso confía en que en algún momento la variable a se defina correctamente, así que ejecuta el programa, pero
cuando quiere hacer uso de la variable, ve que no está definida en su lista de variables, de ahí que lance un NameError al buscarla.
"""

a == 0
