# Atividade de Código Distribuido



**Descrição da Atividade**

Este projeto tem como objetivo aplicar o algoritmo de paralelização para resolver o problema da multiplicação de matrizes, utilizando a arquitetura Cliente/Servidor com comunicação via protocolo TCP. A proposta envolve comparar o desempenho das abordagens sequencial, paralela e distribuída, medindo o tempo de execução de cada uma em milissegundos.

Tecnologias Utilizadas

Linguagem: Python

Arquitetura: Cliente/Servidor

Protocolo de Comunicação: TCP

IDE recomendada: qualquer que suporte Python (ex: VS Code, PyCharm, etc.)



**Estrutura do Projeto**

servidor.py – Código responsável por receber dados do cliente, realizar a multiplicação de matrizes e retornar o resultado.

cliente.py – Código que envia as matrizes para o servidor, recebe o resultado e mede o tempo de execução distribuída.

sequencial_paralelo.py – Implementação da multiplicação de matrizes de forma sequencial e também com paralelização local utilizando threads/processos.

tempoAlgoritmos.txt – Arquivo que contém os tempos registrados das execuções sequencial, paralela e distribuída para fins de comparação.
