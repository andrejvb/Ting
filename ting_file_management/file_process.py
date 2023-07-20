from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines = txt_importer(path_file)

    file_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines,
    }

    try:
        instance.search(instance.items.index(file_dict))
        print(f"Arquivo '{path_file}' já foi processado anteriormente.\n")
        return None
    except ValueError:
        instance.enqueue(file_dict)
        print(file_dict)


def remove(instance):
    if len(instance.items) == 0:
        print('Não há elementos')
        return

    removed_file = instance.dequeue()
    print(f'Arquivo {removed_file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        print(metadata)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
