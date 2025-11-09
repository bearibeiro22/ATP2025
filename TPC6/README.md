# TPC6
## Data: 21/10/2025
## Autor: Beatriz Maria Ferreira de Freitas Ribeiro A107272

Este TPC consistiu em criar um app para trabalhar com tabelas metereológicas com as seguintes funcionalidades:

* Carregar/Guardar a tabela metereológica num ficheiro de texto ".txt"
* Calcular a temperatura média e a amplitude térmica
* Procurar pela temperatura mínima da tabela, dia com maior precipitação, com precipitação superior a um valor
* "Dias ensolarados"

Nota: o ficheiro de texto "meteorologia.txt" é onde está guardada a tabela metereológica e guarda os seguintes dados, da seguinte forma:
     --> ano::mês::dia::tmin::tmax::precip

mais irformações:
* medias(t): calcula a média da temperatura diária
* minMin(t): temperatura mínima da tabela
* amplTerm(t): calcula a amplitude térmica diária
* maxChuva(t): dia e valor da maior qunatidade de precipitação
* diasChuvosos(t, p): calcula o totla de dias com precipitação assima de p
* maxPeriodoCalor(t, p): calcula o maior número consecutivo de dias com precipitação abaixo de p