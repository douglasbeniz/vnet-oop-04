class Foo(object):
    # você não poderia usar <self.> ou <cls.> aqui fora da definicao,
    #   eles não significariam nada

    # este e um atributo de classe
    thing = 'a_thing'

    def __init__(self, bar):
        # quando se quer que outros métodos chamados nesta instância de <Foo> tenham
        #  acesso a <bar>, então crio um atributo <self> apontando para ele
        self.bar = bar

    @classmethod
    def two_things(cls):
        # eh possivel acessar atributos de classe, como <thing>
        # porem, nao se pode acessar atributos de instancia , como <bar>
        print(cls.thing)        # OK
        print(self.bar)         # ERROR!

objFoo = Foo("teste")
objFoo.two_things()
