def exists_word(word, instance):
    result = []
    index = 0

    # Verifica se a fila não está vazia antes de começar a busca
    while index < len(instance):
        list_words = []
        search = instance.search(index)

        for line_num, line in enumerate(search["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                list_words.append({"linha": line_num})

        if list_words:
            result.append({
                "palavra": word,
                "arquivo": search["nome_do_arquivo"],
                "ocorrencias": list_words,
            })

        index += 1

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
