# coding=utf-8

# this method try to mitigate some problems in the dataset:
# a) products in wrong categories: they will be moved to the correct one;
# b) similar products that belong to more than one category: they will be moved to the most specific category.

def adjust_category(name, category):
    name = name.split(' ')
    first = name[0]

    if (category == 'Acessórios de Tecnologia / Acessório Celulares Smartphones'):
        if ('capa' == first):
            return 'Acessórios de Tecnologia / Acessório Celulares Smartphones / Capas e Estojos'

    if (category == 'Acessórios de Tecnologia / Acessório Celulares Smartphones / Peças e Componentes'):
        if (first == 'cartao' and 'memoria' in name):
            return 'Acessórios de Tecnologia / Acessórios Câmeras e Filmadoras / Cartões de memória'

    if (category == 'Acessórios de Tecnologia / Acessório Celulares Smartphones / Películas Protetoras'):
        if ('capa' == first):
            return 'Acessórios de Tecnologia / Acessório Celulares Smartphones / Capas e Estojos'

    if (category == 'Acessórios de Tecnologia / Acessório Peças Componentes Computador'):
        if ('tela' == first):
            return 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / Telas para reposição'

    if (category == 'Acessórios de Tecnologia / Acessório Periféricos Informática / Cabos e Adaptadores'):
        if (first == 'cabo' and 'hdmi' in name):
            return 'Acessórios de Tecnologia / Acessório Televisão Home Theaters / Cabos e Conectores'

    if (category == 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / Fontes'):
        if ('conector' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Cabos e Adaptadores'

    if (category == 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / HD Interno'):
        if ('externo' in name):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / HD Externo'

    if (category == 'Acessórios de Tecnologia / Acessório Periféricos Informática / HD Externo'):
        if ('interno' in name):
            return 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / HD Interno'

    if (category == 'Automotivo / Acabamento / Tuning'):
        if ('interruptor' == first):
            return 'Automotivo / Elétrico / Interruptores'

    if (category == 'Automotivo / Acessórios'):
        if ('apoio' == first):
            return 'Automotivo / Acabamento / Tuning'

    if (category == 'Automotivo / Acessórios / Auxiliar de Partida'):
        if ('rele' == first):
            return 'Automotivo / Peças / Motor de partida'

    if (category == 'Automotivo / Iluminação / Kits'):
        if ('kit' == first and 'xenon' in name):
            return 'Automotivo / Iluminação / Lâmpadas'

    if (category == 'Automotivo / Óleos e Fluídos / Óleos'):
        if ('ar' in name):
            return 'Automotivo / Peças / Filtro de Ar'

    if (category == 'Automotivo / Peças / Amortecedor'):
        if ('manete' == first):
            return 'Automotivo / Peças / Manete'

    if (category == 'Automotivo / Peças / Bomba de Água'):
        if ('oleo' in name):
            return 'Automotivo / Peças / Bomba de Óleo'

    if (category == 'Automotivo / Peças / Cabos de Vela'):
        if ('bronzina' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'

    if (category == 'Automotivo / Peças / Filtro de Ar'):
        if ('oleo' in name or 'combustivel' in name or 'agua' in name):
            return 'Automotivo / Óleos e Fluídos / Óleos'

    if (category == 'Automotivo / Peças / Motor de partida'):
        if ('bronzina' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'

    if (category == 'Automotivo / Peças / Pastilha de Freio'):
        if ('disco' == first and 'freio' in name):
            return 'Automotivo / Peças / Sapata de Freio'

    if (category == 'Automotivo / Peças / Pistão'):
        if ('bronzina' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'

    if (category == 'Automotivo / Peças / Porta'):
        if ('macaneta' == first):
            return 'Automotivo / Peças / Maçaneta'

    if (category == 'Automotivo / Peças / Virabrequim'):
        if ('vela' in name):
            return 'Automotivo / Peças / Cabos de Vela'

    if (category == 'Automotivo / Peças / Ventuinhas'):
        if ('bronzina' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'

    if (category == 'Bebês e Crianças / Decoração / Tapetes'):
        if (not 'infantil' in name):
            return 'Móveis e Decoração / Decoração / Tapetes'

    if (category == 'Cama Mesa e Banho / Cama / Colchas e Cobre Leitos'):
        if ('jogo' == first):
            return 'Cama Mesa e Banho / Cama / Jogos de Cama'

    if (category == 'Casa e Segurança / Banheiros / Acessórios'):
        if ('banheira' == first):
            return 'Casa e Segurança / Banheiros / Banheiras'

    if (category == 'Cuidados com a Saúde / Ótica / Óculos de Leitura'):
        if ('armacao' == first):
            return 'Cuidados com a Saúde / Ótica / Armações'

    if (category == 'Ferramentas e Jardim / Corte e Desbaste / Abrasivos e Utensílios de Corte'):
        if ('serra' == first):
            return 'Ferramentas e Jardim / Corte e Desbaste / Serras'

    if (category == 'Ferramentas e Jardim / Fixação e Perfuração / Ferragens'):
        if ('soquete' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Soquetes'

    if (category == 'Informática / Suprimentos / Toners'):
        if ('cartucho' == first):
            return 'Informática / Suprimentos / Cartuchos e Garrafas'

    if (category == 'Instrumentos Musicais / Instrumentos de Corda / Acessórios de Cordas'):
        if ('encordoamento' == first):
            return 'Instrumentos Musicais / Instrumentos de Corda / Encondoamentos'

    if (category == 'Moda / Calçados / Rasteiras'):
        if ('sandalia' == first):
            return 'Moda / Calçados / Sandálias'

    if (category == 'Moda / Calçados / Tênis'):
        if ('sapatenis' == first):
            return 'Moda / Calçados / Sapatênis'

    if (category == 'Móveis e Decoração'):
        if ('quadro' == first):
            return 'Móveis e Decoração / Decoração / Quadros e Molduras'

    if (category == 'Móveis e Decoração / Área Externa / Cadeiras'):
        if ('poltrona' == first):
            return 'Móveis e Decoração / Área Externa / Sofás e Poltronas'

    if (category == 'Móveis e Decoração / Cozinha / Armários de Cozinha'):
        if ('cozinha' == first):
            return 'Móveis e Decoração / Cozinha / Cozinhas completas'

    if (category == 'Móveis e Decoração / Decoração / Almofadas e Futons'):
        if ('capa' == first):
            return 'Cama Mesa e Banho / Decoração / Capas de almofada'

    if (category == 'Móveis e Decoração / Decoração / Quadros e Molduras'):
        if ('placa' == first):
            return 'Móveis e Decoração / Decoração / Objetos decorativos'

    if (category == 'Móveis e Decoração / Decoração / Tapetes'):
        if ('infantil' in name):
            return 'Bebês e Crianças / Decoração / Tapetes'

    if (category == 'Móveis e Decoração / Escritório / Mesas'):
        if ('escrivaninha' == first):
            return 'Móveis e Decoração / Escritório / Escrivaninhas'

    if (category == 'Móveis e Decoração / Escritório / Escrivaninhas'):
        if ('mesa' == first):
            return 'Móveis e Decoração / Escritório / Mesas'

    if (category == 'Móveis e Decoração / Quarto / Camas'):
        if ('infantil' in name):
            return 'Bebês e Crianças / Móveis para Bebês / Camas'

    if (category == 'Móveis e Decoração / Quarto / Guarda-roupas'):
        if ('infantil' in name):
            return 'Móveis e Decoração / Infantil / Guarda-roupas'

    if (category == 'Móveis e Decoração / Sala de Jantar / Balcão'):
        if ('buffet' == first):
            return 'Móveis e Decoração / Sala de Jantar / Buffets'

    if (category == 'Móveis e Decoração / Sala de Jantar / Conjuntos de Mesa e Cadeira de Jantar'):
        if ('mesa' == first):
            return 'Móveis e Decoração / Sala de Jantar / Mesas de Jantar'

    if (category == 'Móveis e Decoração / Sala de Jantar / Mesas de Jantar'):
        if ('conjunto' == first):
            return 'Móveis e Decoração / Sala de Jantar / Conjuntos de Mesa e Cadeira de Jantar'

    if (category == 'Papelaria / Adesivos / Acessórios para scrapbook'):
        if ('decoupage' == first):
            return 'Papelaria / Artes / Artesanato'

    if (category == 'Papelaria / Adesivos / Stickers'):
        if ('adesivo' == first):
            return 'Móveis e Decoração / Decoração / Adesivos'

    if (category == 'Papelaria / Artes / Artesanato'):
        if ('adesivo' == first):
            return 'Móveis e Decoração / Decoração / Adesivos'

    if (category == 'Papelaria / Papéis e Pastas / Papéis'):
        if ('fita' == first):
            return 'Papelaria / Adesivos / Fitas adesivas'

    if (category == 'Relógios e Joias / Joias / Anéis'):
        if ('alianca' == first):
            return 'Relógios e Joias / Joias / Alianças'

    if (category == 'Telefonia'):
        if ('fone' == first):
            return 'Acessórios de Tecnologia / Acessório Áudio Portátil Fones Ouvido / Fones de Ouvido'

    if (category == 'Utilidades domésticas / Faqueiros e Talheres / Facas avulsas'):
        if ('churrasco' in name):
            return 'Utilidades domésticas / Linha para Churrasco / Conjuntos de Talheres e Facas Avulsas'

    if (category == 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / Peças de Reposição'):
        if ('teclado' == first or 'mouse' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Teclados e Mouses'
        if ('cabo' == first or 'adaptador' == first or 'conector' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Cabos e Adaptadores'

    if (category == 'Acessórios de Tecnologia / Acessório Periféricos Informática / Carregadores e Baterias'):
        if ('fonte' == first):
            return 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / Fontes'
        if ('conector' == first or 'cabo' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Cabos e Adaptadores'

    if (category == 'Acessórios de Tecnologia / Acessório Periféricos Informática / Peças para Reposição'):
        if ('teclado' == first or 'mouse' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Teclados e Mouses'
        if ('carregador' == first or 'bateria' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Carregadores e Baterias'
        if ('cabo' == first or 'adaptador' == first or 'conector' == first):
            return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Cabos e Adaptadores'
        if ('tela' == first):
            return 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / Telas para reposição'
        if ('fonte' == first):
            return 'Acessórios de Tecnologia / Acessório Peças Componentes Computador / Fontes'

    if (category in ['Automotivo / Motociclismo / Peças', 'Automotivo / Motociclismo / Acessórios']):
        if ('amortecedor' == first):
            return 'Automotivo / Peças / Amortecedor'
        return 'Automotivo / Motociclismo / Peças e Acessórios'

    if (category == 'Automotivo / Peças / Bomba de Óleo'):
        if ('bronzina' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'
        if ('agua' in name):
            return 'Automotivo / Peças / Bomba de Água'

    if (category == 'Bebês e Crianças / Móveis para Bebês / Camas'):
        if ('berco' == first):
            return 'Bebês e Crianças / Móveis para Bebês / Berços'
        if ('comoda' == first):
            return 'Móveis e Decoração / Quarto / Cômodas'
        if ('guarda' == first):
            return 'Móveis e Decoração / Infantil / Guarda-roupas'

    if (category == 'Cama Mesa e Banho / Decoração / Tapetes'):
        if ('infantil' in name):
            return 'Bebês e Crianças / Decoração / Tapetes'
        return 'Móveis e Decoração / Decoração / Tapetes'

    if (category == 'Ferramentas e Jardim / Ferramentas Manuais / Chaves'):
        if ('bronzina' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'
        if ('soquete' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Soquetes'
        if ('broca' == first):
            return 'Ferramentas e Jardim / Fixação e Perfuração / Ferragens'
        if ('macho' == first):
            return 'Ferramentas e Jardim / Ferramentas Manuais / Vira-Machos'

    if (category == 'Moda / Bolsas e Acessórios / Bijuterias'):
        if ('brinco' == first):
            return 'Relógios e Joias / Joias / Brincos'
        if ('pulseira' == first or 'tornozeleira' == first):
            return 'Relógios e Joias / Joias / Pulseiras e Tornozeleiras'
        if ('colar' == first or 'gargantilha' == first):
            return 'Relógios e Joias / Joias / Colares e Gargantilhas'
        if ('pingente' == first):
            return 'Relógios e Joias / Joias / Pingentes'
        if ('porta' == first and 'joia' in name):
            return 'Relógios e Joias / Joias / Porta Joias e Acessórios'
        if ('anel' == first):
            return 'Relógios e Joias / Joias / Anéis'
        if ('alianca' == first):
            return 'Relógios e Joias / Joias / Alianças'

    if (category == 'Móveis e Decoração / Decoração / Adesivos'):
        if (first == 'faixa' and 'parede' in name and 'infantil' in name):
            return 'Bebês e Crianças / Decoração / Papéis de Parede'
        if ('papel' == first):
            return 'Móveis e Decoração / Decoração / Papéis de Parede'

    if (category == 'Músicas Filmes e Séries / Colecionáveis / Roupas e Acessórios'):
        if ('camiseta' in name and 'feminino' in name):
            return 'Moda / Moda feminina / Camisetas'
        if ('camiseta' in name and 'masculino' in name):
            return 'Moda / Moda masculina / Camisetas'

    if (category == 'Acessórios de Tecnologia / Acessório Celulares Smartphones / Caixas de Som'):
        return 'Eletrônicos / Caixas de Som e Dock Stations / Caixas Portáteis e Dock Stations'

    if (category == 'Acessórios de Tecnologia / Acessório Games / Fones de Ouvido e Headsets'):
        return 'Acessórios de Tecnologia / Acessório Áudio Portátil Fones Ouvido / Fones de Ouvido'

    if (category == 'Acessórios de Tecnologia / Acessório Games / Teclados e Mouses'):
        return 'Acessórios de Tecnologia / Acessório Periféricos Informática / Teclados e Mouses'

    if (category == 'Automotivo / Elétrico / Soquetes'):
        return 'Ferramentas e Jardim / Ferramentas Manuais / Soquetes'

    if (category == 'Automotivo / Peças / Bronzinas'):
        return 'Ferramentas e Jardim / Ferramentas Manuais / Bronzinas'

    if (category == 'Brinquedos / Diversão ao Ar Livre / Bicicletas'):
        return 'Esporte e Lazer / Ciclismo e Bikes / Bicicletas'

    if (category == 'Brinquedos / Fantasias e Acessórios / Fantasias'):
        return 'Moda / Fantasias'

    if (category == 'Casa e Segurança / Materiais Elétricos / Soquetes'):
        return 'Ferramentas e Jardim / Ferramentas Manuais / Soquetes'

    if (category == 'Cama Mesa e Banho / Decoração / Almofadas'):
        return 'Móveis e Decoração / Decoração / Almofadas e Futons'

    if (category == 'Cama Mesa e Banho / Decoração / Cortinas e Persianas'):
        return 'Móveis e Decoração / Decoração / Cortinas e Persianas'

    if (category == 'Esporte e Lazer / Acessórios Esportivos / Óculos de sol'):
        return 'Moda / Óculos / Óculos de sol'

    if (category == 'Esporte e Lazer / Tênis e Calçados / Tênis'):
        return 'Moda / Calçados / Tênis'

    if (category == 'Móveis e Decoração / Infantil / Camas'):
        return 'Bebês e Crianças / Móveis para Bebês / Camas'

    if (category == 'Papelaria / Materiais Escolares / [Mochilas escolares]'):
        return 'Malas Mochilas e Acessórios / Mochilas / Escolar'

    if (category == 'Utilidades domésticas / Acessórios para Banheiro / Lixeiras'):
        return 'Utilidades domésticas / Lixeiras'

    if (category == 'Utilidades domésticas / Acessórios para Lavanderia / Lixeiras'):
        return 'Utilidades domésticas / Lixeiras'

    if (category == 'Utilidades domésticas / Decore e Organize / Relógio de Parede'):
        return 'Móveis e Decoração / Decoração / Relógios'

    if (category == 'Utilidades domésticas / Faqueiros e Talheres / Até 30 peças'):
        return 'Utilidades domésticas / Faqueiros e Talheres / Jogos de Talher'

    if (category == 'Utilidades domésticas / Faqueiros e Talheres / De 31 a 60 peças'):
        return 'Utilidades domésticas / Faqueiros e Talheres / Jogos de Talher'

    if (category == 'Utilidades domésticas / Faqueiros e Talheres / Mais de 60 peças'):
        return 'Utilidades domésticas / Faqueiros e Talheres / Jogos de Talher'

    return category
