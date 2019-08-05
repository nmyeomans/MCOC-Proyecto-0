# MCOC-Proyecto-0
Perdida de significación
===============
A partir de los videos estudiados, podemos darnos cuenta de que la interpretación de números flotantes en un computador es diferente a la de numero enteros. El comportamiento de los códigos binarios en un computador tiene un numero de dígitos que representan de forma significativa su valor. Sin embargo, hay una cierta perdida de significancia que se genera, es por esto que se generó números al azar a través de Python por medio del comando random.random(), con el objetivo de utilizar el numero como un arreglo con un tipo de dato definido.

1.Arreglo con tipo de dato dtype=np.float16

2.Arreglo con tipo de dato dtype=np.float32.

3.Arreglo con tipo de dato dtype=np.float64.

Para cada uno de estos arreglos se evidencio la perdida de significación a partir del error que es calculado como:

Error (%) = (|Valor flotante como array - Valor aleatorio|) /( Valor aleatorio )

Además, se realizó el cálculo de la raíz cuadrada en cada caso con el fin de alterar los valores y ver su influencia en el error, comparándolos respecto al valor original obtenido a través del programa.



Resultados
==============
ttps://raw.githubusercontent.com/nmyeomans/MCOC-Proyecto-0/blob/master/loss-of-significace.PNG

