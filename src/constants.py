# coding=utf-8

# constants

BAD_WORDS = {'para', 'de', 'com', 'em', 'do', 'da', 'a', 'o', 'e', 'ate', 'as', 'os', 'das', 'dos', 'por', 'sem', 'na', 'no', 'nas', 'nos', 'ref', 'c', 'p', 'the'}

CONSOLE = {'xbox 360': 1, 'ps3': 2, 'ps4': 3, 'psp': 4, 'wii': 5, 'ps2': 6, '3ds': 7, 'vita': 8, 'ds': 9, 'xbox one': 10}

COLORS = {'branco', 'preto', 'azul', 'vermelho', 'rosa', 'verde', 'cinza', 'cromado', 'prata', 'amarelo', 'marrom', 'bege', 'laranja', 'dourado', 'transparente', 'incolor'}

CUP = {'agua': 1, 'champanhe': 2, 'vinho': 3, 'sobremesa': 4, 'suco': 5, 'cerveja': 6}

DEVICE = {'smartphone': 1, 'notebook': 2, 'pc': 3, 'tablet': 4}

FEMALE_MALE = {'preta': 'preto', 'branca': 'branco', 'vermelha': 'vermelho', 'decorativa': 'decorativo', 'dianteira': 'dianteiro', 'traseira': 'traseiro', 'eletrica': 'eletrico', 'cromada': 'cromado', 'dupla': 'duplo', 'redonda': 'redondo', 'alta': 'alto', 'termica': 'termico', 'plastica': 'plastico', 'personalizada': 'personalizado', 'feminina': 'feminino', 'exclusiva': 'exclusivo', 'amarela': 'amarelo', 'completa': 'completo', 'interna': 'interno', 'masculina': 'masculino', 'eletronica': 'eletronico', 'dentada': 'dentado', 'protetora': 'protetor', 'fixa': 'fixo', 'quadrada': 'quadrado', 'longa': 'longo', 'externa': 'externo', 'media': 'medio', 'pequena': 'pequeno', 'compacta': 'compacto', 'giratoria': 'giratorio', 'esportiva': 'esportivo', 'limpa': 'limpo', 'acustica': 'acustico', 'ponteira': 'ponteiro', 'junta': 'junto', 'churrasqueira': 'churrasqueiro', 'manta': 'manto', 'importada': 'importado', 'nova': 'novo', 'progressiva': 'progressivo', 'reta': 'reto', 'metalica': 'metalico', 'outra': 'outro'}

GENDER = {'feminino': 1, 'femme': 1, 'woman': 1, 'infantil': 2, 'bebe': 2, 'crianca': 2, 'masculino': 3, 'homme': 3, 'men': 3}

GROUP = ['kit', 'conjunto', 'jogo', 'aparelho', 'combo']

HEADER = 'name;brand;gender;room;vehicle;console;device;pet;mattress;cup;category\n'

INACTIVE = ['inativ', 'catalogar', 'sige']

MATTRESS = {'solteiro': 1, 'queen': 2, 'king': 3, 'infantil': 4, 'casal': 5}

MAX_VALID_PRICE = 100000

MIN_CATEGORY_SIZE = 50

PET = {'cao': 1, 'cachorro': 1, 'passaro': 2, 'ave': 2, 'reptil': 3, 'lagarto': 3, 'hamster': 4, 'roedor': 4, 'gato': 5}

PLURAL_SINGULAR = {'bracos': 'braco', 'pratos': 'prato', 'series': 'serie', 'carros': 'carro', 'kids': 'kid', 'zirconias': 'zirconia', 'colors': 'color', 'tacas': 'taca', 'princesas': 'princesa', 'pulseiras': 'pulseira', 'copos': 'copo', 'palhetas': 'palheta', 'prateleiras': 'prateleira', 'esportivas': 'esportiva', 'panelas': 'panela', 'unidades': 'unidade', 'facas': 'faca', 'pneus': 'pneu', 'folhas': 'folha', 'malas': 'mala', 'talheres': 'talher', 'acessorios': 'acessorio', 'shorts': 'short', 'aneis': 'anel', 'tintas': 'tinta', 'roupas': 'roupa', 'caes': 'cao', 'lampadas': 'lampada', 'moveis': 'movel', 'bocas': 'boca', 'molas': 'mola', 'metros': 'metro', 'banquetas': 'banqueta', 'litros': 'litro', 'chaves': 'chave', 'flores': 'flor', 'ferramentas': 'ferramenta', 'lugares': 'lugar', 'cadeiras': 'cadeira', 'gavetas': 'gaveta', 'pecas': 'peca', 'portas': 'porta', 'pernas': 'perna', 'luvas': 'luva', 'adesivos': 'adesivo', 'blocos': 'bloco', 'separadores': 'separador', 'potes': 'pote', 'rodas': 'roda', 'letras': 'letra', 'lencos': 'lenco', 'laminas': 'lamina', 'carimbos': 'carimbo', 'celulas': 'celula', 'polegadas': 'polegada', 'fios': 'fio', 'cores': 'cor', 'pinos': 'pino', 'capsulas': 'capsula', 'gatos': 'gato', 'fotos': 'foto', 'diamantes': 'diamante', 'tapetes': 'tapete', 'rodizios': 'rodizio', 'dentes': 'dente', 'pedras': 'pedra', 'girls': 'girl', 'leds': 'led', 'velocidades': 'velocidade', 'outros': 'outro', 'animais': 'animal', 'listras': 'listra', 'frutas': 'fruta', 'canais': 'canal', 'joias': 'joia', 'anos': 'ano', 'borboletas': 'borboleta', 'coracoes': 'coracao', 'pontas': 'ponta', 'todos': 'todo', 'outras': 'outra', 'bolinhas': 'bolinha', 'cordas': 'corda', 'pessoas': 'pessoa', 'convidados': 'convidado', 'masculinas': 'masculina', 'festas': 'festa', 'bolas': 'bola', 'alcas': 'alca', 'games': 'game', 'xicaras': 'xicara', 'comprimidos': 'comprimido', 'cameras': 'camera', 'cabelos': 'cabelo', 'cristais': 'cristal', 'rosas': 'rosa', 'cabos': 'cabo', 'cachos': 'cacho', 'gramas': 'grama', 'botoes': 'botao', 'ondas': 'onda', 'dados': 'dado', 'todas': 'toda', 'suprimentos': 'suprimento', 'camisas': 'camisa', 'almofadas': 'almofada', 'quadros': 'quadro', 'falantes': 'falante', 'brilhantes': 'brilhante', 'altas': 'alta', 'passaros': 'passaro', 'itens': 'item', 'caixas': 'caixa', 'bits': 'bit', 'fixas': 'fixa', 'chips': 'chip', 'decorativos': 'decorativo', 'coloridas': 'colorida', 'lentes': 'lente', 'garrafas': 'garrafa', 'tomadas': 'tomada', 'soquetes': 'soquete', 'atividades': 'atividade', 'sons': 'som', 'friends': 'friend', 'utensilios': 'utensilio', 'filtros': 'filtro', 'brinquedos': 'brinquedo', 'pontos': 'ponto', 'rolos': 'rolo', 'rolhas': 'rolha', 'decorativas': 'decorativa', 'brocas': 'broca', 'adultos': 'adulto', 'perolas': 'perola', 'tempos': 'tempo', 'puffs': 'puff', 'poltronas': 'poltrona', 'alimentos': 'alimento', 'impressoras': 'impressora', 'unhas': 'unha', 'costas': 'costa', 'formas': 'forma', 'detalhes': 'detalhe', 'conectores': 'conector', 'duas': 'dois', 'cosmos': 'cosmo', 'legumes': 'legume', 'deslizantes': 'deslizante', 'cartuchos': 'cartucho', 'tubos': 'tubo', 'estofados': 'estofado', 'colheres': 'colher', 'livros': 'livro', 'tiras': 'tira', 'estrelas': 'estrela', 'laterais': 'lateral', 'funcoes': 'funcao', 'coloridos': 'colorido', 'brancas': 'branca', 'capas': 'capa', 'graus': 'grau', 'linhas': 'linha', 'tvs': 'tv', 'discos': 'disco', 'figuras': 'figura', 'personagens': 'personagem', 'pares': 'par', 'halteres': 'halter', 'tigelas': 'tigela', 'modelos': 'modelo', 'guardanapos': 'guardanapo', 'divisorias': 'divisoria', 'bonecos': 'boneco', 'ponteiros': 'ponteiro', 'bastoes': 'bastao', 'cars': 'car', 'barras': 'barra', 'pesos': 'peso', 'oleos': 'oleo', 'banheiros': 'banheiro', 'smartphones': 'smartphone', 'tablets': 'tablet', 'notebooks': 'notebook', 'computadores': 'computador', 'enxovais': 'enxoval', 'capinhas': 'capa', 'capotas': 'capota', 'bordados': 'bordado', 'capacetes': 'capacete', 'fitas': 'fita', 'cortinas': 'cortina', 'capinha': 'capa', 'champagne': 'champanhe'}

ROOM = {'jantar': 1, 'escritorio': 2, 'estar': 3, 'sala': 4, 'banheiro': 5, 'lavanderia': 6, 'quarto': 7, 'externa': 8, 'infantil': 9, 'cozinha': 10}

VEHICLE = {'carro': 1, 'moto': 2, 'motocicleta': 2, 'motociclismo': 2}

WALMART_PROGRAM_ID = 12011

ZANOX_INDEX_AVAILABILITY = 17

ZANOX_INDEX_BRAND = 6

ZANOX_INDEX_CATEGORY = 11

ZANOX_INDEX_CATEGORY2 = 12

ZANOX_INDEX_EAN = 15

ZANOX_INDEX_ID = 1

ZANOX_INDEX_NAME = 2

ZANOX_INDEX_PRICE = 4

ZANOX_INDEX_PROGRAM_ID = 0
