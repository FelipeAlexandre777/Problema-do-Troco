def troco_guloso(valor, moedas=(100, 50, 25, 10, 5, 1)):
    """
    Calcula o troco utilizando o algoritmo guloso.

    valor: valor do troco em centavos.
    moedas: denominações disponíveis em ordem decrescente.

    Retorna um dicionário com a quantidade de cada moeda.
    """

    if not isinstance(valor, int) or isinstance(valor, bool) or valor < 0:
        raise ValueError("O valor deve ser um inteiro não negativo.")

    if any(not isinstance(m, int) or isinstance(m, bool) or m <= 0 for m in moedas):
        raise ValueError("As moedas devem ser inteiros positivos.")

    if list(moedas) != sorted(moedas, reverse=True):
        raise ValueError("As moedas devem estar em ordem decrescente.")

    restante = valor
    resultado = {}

    for moeda in moedas:
        quantidade, restante = divmod(restante, moeda)

        if quantidade > 0:
            resultado[moeda] = quantidade

    if restante != 0:
        raise ValueError("Não foi possível formar o valor exato.")

    return resultado