# compara hashs
import hashlib


def komparator(arquivo1, arquivo2):
    """função que compara a integridade dos arquivos"""
    hash1 = hashlib.new('sha256')  # optei por sha256
    hash2 = hashlib.new('sha256')

    # abre o arquivo para passá-lo ao método update
    with open(arquivo1, 'rb') as f:
        hash1.update(f.read())
    with open(arquivo2, 'rb') as f:
        hash2.update(f.read())

    # compara os hash, qualquer byte diferente, será detectado;
    if hash1.digest() == hash2.digest():
        print('Os arquivos são iguais')
    else:
        print('Os arquivos não são iguais')

if __name__ == '__main__':
    arquivo1 = str(input('Informe o nome do arquivo(com a extensão): '))
    arquivo2 = str(input('Informe o nome de outro arquivo(com a extensão): '))
    komparator(arquivo1, arquivo2)