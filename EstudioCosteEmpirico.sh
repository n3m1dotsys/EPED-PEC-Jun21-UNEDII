
#!/bin/bash

# === Inputs ===
# SRC_DIR=$PWD/src
BIN_DIR=/bin
MAIN=es/uned/lsi/eped/pract2020_2021/Main
JAVA_HOME_JDK=/usr/lib/jvm/default
TMP_FOLDER=$PWD/juego_de_pruebas_2021/tmp
NUMBER_TESTS=5000

echo "BQ_ENQ"

echo "1000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqenq_1.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "2000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqenq_2.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "3000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqenq_3.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "4000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqenq_4.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "5000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqenq_5.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "6000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqenq_6.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "BQ_DEQ"

echo "1000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqdeq_1.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "2000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqdeq_2.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "3000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqdeq_3.dat" "$PWD/test/salida.dat")
    echo "$out"
done


echo "4000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqdeq_4.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "5000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqdeq_5.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "6000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bqdeq_6.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "BST_ENQ"

echo "1000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstenq_1.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "2000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstenq_2.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "3000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstenq_3.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "4000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstenq_4.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "5000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstenq_5.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "6000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstenq_6.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "BST_DEQ"

echo "1000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstdeq_1.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "2000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstdeq_2.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "3000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstdeq_3.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "4000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstdeq_4.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "5000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstdeq_5.dat" "$PWD/test/salida.dat")
    echo "$out"
done

echo "6000 pacientes"

for ((c=1; c<=$NUMBER_TESTS; c++))
do
    out=$("$JAVA_HOME_JDK/bin/java" -cp "$TMP_FOLDER$BIN_DIR:juego_de_pruebas_2021/lib/TAD_modified.jar" "$MAIN" BQ "$PWD/test/bstdeq_6.dat" "$PWD/test/salida.dat")
    echo "$out"
done

rm $PWD/test/salida.dat