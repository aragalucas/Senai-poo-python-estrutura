class Pessoa:
    def __str__(self) -> str:
        return {
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.texto} "
            f"\nSexo: {self.sexo.caracter}"
            f"\nEndereço: {self.endereco}"
        }