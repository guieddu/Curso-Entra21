class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

    def mover(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} está latindo"

    def mover(self):
        return f"{self.nome} está correndo"

class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} está miando"

    def mover(self):
        return f"{self.nome} está andando"

class Passaro(Animal):
    def emitir_som(self):
        return f"{self.nome} está cantando"

    def mover(self):
        return f"{self.nome} está miando"

cachorro = Cachorro("Mel")
gato = Gato("Missi")
passaro = Passaro("Bem-te-vi")

print(cachorro.emitir_som()) 
print(cachorro.mover())

print(gato.emitir_som())
print(gato.mover())
print(passaro.emitir_som())