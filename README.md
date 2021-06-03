# EPED-PEC-Jun21-UNEDII

Práctica para la asignatura Estrategias de Prgramación y Estructuras de Datos del grado en Ingeniería Informática de la UNED

## Estructura de ficheros

| Directorio o fichero                        | Contenido |
|:--------------------------------------------|:----------|
|```bin/```                                   | Directorio de salida para la compilación |
|```doc/```                                   | Documentación de la práctica: memoría (en pdf y fuente en LaTeX) y gráficos utilizaods en esta.|
|```juegos_de_pruebas_2021```                 | Módulo para la ejecución del juego de pruebas, y juego de pruebas ofrecido por el ED.|
|```src/```                                   | Código fuente de la práctica (es.uned.lsi.eped.pract2020_2021) + estructuras de dactos del ED (es.uned.lsi.eped.DataStructures).|
|```test/```                                  | Juegos de pruebas para el estudio del coste empírico + script en python para generarlos.|
|```Compile_Run_Test_2021_EST_V.00.[bat|sh]```| Script para compilar y ejecutar juego de pruebas |
|```errores*.txt```                           | Salidas de errores encontrados al ejecutar el juego de pruebas |
|```EstudioCosteEmpirico.sh```                | Script para ejecutar las pruebas para el estudio del coste empírico (solo en Linux y no se si Mac) |
|```costeEmpirico.py```                       | Script para el analisis de los resultados de la pureba de tiempo |
|```test_final.out```                         | Resultado del test utilizado en la memoria |

## Como ejecutar los tests del estudio de coste empírico

Si no están generados, primero hace falta generar los tests dentro de la carpeta ```test/```:

```bash
$ python3 gentest.py # dentro del directorio test/
```

Despues hace falta ejecutar el juego de pruebas y guardar los resultados en un fichero:

```bash
$ ./EstudioCosteEmpirico.sh > test.out # En el directorio raiz
```

Finalmente pasamos los resultados al analizador:

```bash
$ cat test.out | python3 costeEmpirico.py # En el directorio raiz
```

que generará los gráficos y te mostrará las tablas del analisis.

Si no se desea guardar la salida de los resultados del test, este se puede enviar directamente al analizador:

```bash
$ ./EstudioCosteEmpirico.sh | python3 costeEmpirico.py # En el directorio raiz
```

Se puede regular el número de ejecuciones de cada prueba alterando el parametro ```NUMBER_TESTS``` del fichero ```EstudioCosteEmpirico.sh``` teniendo en cuenta que incrementarlo por encima de 500 puede hacer que tarde una eternidad (5000 reiteraciones tarda alrededor más de 6 horas).