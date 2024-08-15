duvidas_e_questoes = dict()

acoes_fundos_indices_bdrs = dict()


duvidas_e_questoes['Sobre a api:'] = """
    Fornece informações detalhadas sobre cotações de ações, fundos, índices e BDRs permitindo que você obtenha um 
 resumo de todos os tickers disponíveis. Ela oferece flexibilidade para ordenar, filtrar e buscar os tickers 
 que você deseja."""

duvidas_e_questoes['O que são ações?'] = """
Ações são títulos que representam uma fração do valor das companhias ou sociedades anônimas. Ou seja, uma ação é
 como se fosse um pedaço de uma empresa.
    Ações representam frações de companhias de capital aberto, ou seja, aquelas empresas que são negociadas na
Bolsa de Valores.
    As ações ordinárias(ON) garantem o direito ao voto ao sócio nas assembleias da empresa. As preferenciais(PN) 
não têm direito a voto, mas tem prioridade no momento de receber os proventos.
    Os fundos são compostos por um grupo de investidores que se unem com o objetivo de aplicar seus recursos de 
maneira conjunta no mercado financeiro e de capitais.
    Assim, os rendimentos são distribuídos entre os participantes, de acordo com a proporção do valor depositado 
por cada um."""

duvidas_e_questoes['O que são BDRs?'] = """
    Conhecidos pela sigla BDR, os Brazilian Depositary Receipts são certificados que representam ações emitidas por 
empresas em outros países, mas que são negociados aqui, no pregão da B3. É como se fossem valores mobiliários 
lastreados em papéis de companhias estrangeiras e, desde setembro de 2020, também brasileiras.
    Quem adquire um BDR, portanto, não compra diretamente as ações da empresa no exterior. Em vez disso, investe 
em títulos representativos desses papéis. Essas ações existem de fato lá fora, e precisam ficar depositadas e 
bloqueadas em uma instituição financeira que atua como custodiante – ou seja, que faz a guarda delas.
    Já quem assegura o funcionamento de todo esse sistema é também uma instituição financeira, chamada de 
depositária, que é a responsável por emitir os BDRs no Brasil."""

duvidas_e_questoes['O que são os índices das Bolsas de Valores?'] = """
    Índices das Bolsas de Valores funcionam como cestas de ações que medem o desempenho de empresas 
específicas dentro do mercado financeiro.
    Eles são extremamente relevantes para investidores e analistas, pois refletem as tendências do mercado, a saúde 
econômica de setores ou até mesmo de um país inteiro.
    Cada índice segue critérios próprios, focando em aspectos como capitalização de mercado, liquidez e setor de 
atuação das empresas."""

duvidas_e_questoes['Para que servem os índices da bolsa?'] = """
    Eles são usados como benchmarks (metas de rentabilidade) para 
comparar o desempenho de carteiras de investimentos, possibilitando uma análise mais aprofundada das tendências do 
mercado e auxiliando na formulação de estratégias de investimento.
    Ao acompanhar um índice, os investidores podem entender melhor o movimento geral do mercado sem precisar analisar 
cada ação individualmente. Abaixo, separamos alguns dos principais índices de mercado para você conhecer sua 
composição e racional."""

acoes_fundos_indices_bdrs['ticker parameters traducer'] = {
    'name': "Nome do ticker",
    'close': "Preço de fechamento",
    'change': "Variação percentual",
    'change_abs': "Variação no preço absoluto",
    'volume': "Volume de negociação",
    'market_cap_basic': "Capitalização de mercado",
    'sector': "Setor da ação",
}

acoes_fundos_indices_bdrs['ameaning tickers'] = {
    'Preço de fechamento': "O preço de fechamento de um ativo é o último preço em que ele foi negociado numa sessão.",
    'Variação percentual': """
        Elas são a base dos cálculos financeiros e a partir deste entendimento é que surgem por exemplo outros 
     entendimentos como o da própria taxa de juros. Seu conceito básico é bastante simples, trata-se de uma 
     comparação evolutiva em determinado espaço de tempo entre dois valores podendo o seu resultado ser 
     negativo ou positivo.""",
    'Volume na Bolsa de Valores': "Quando falamos em Bolsa, o volume está relacionado ao fluxo de negociações",
    'Capitalização de mercado': """A capitalização de mercado, ou market cap, é o valor total em dólares das ações 
     em circulação de uma empresa cotada na bolsa.""",
}

acoes_fundos_indices_bdrs['all sectors traducer'] = {
    'Retail Trade': "Comércio Varejista",
    'Energy Minerals': "Minerais Energéticos",
    'Health Services': "Serviços de Saúde",
    'Utilities': "Utilidades",
    'Finance': "Finanças",
    'Consumer Services': "Serviços ao Consumidor",
    'Consumer Non-Durables': "Bens de Consumo Não Duráveis",
    'Non-Energy Minerals': "Minerais não Energéticos",
    'Commercial Services': "Serviços Comerciais",
    'Distribution Services': "Serviços de Distribuição",
    'Transportation': "Transporte",
    'Technology Services': "Serviços de Tecnologia",
    'Process Industries': "Indústrias de Processo",
    'Communications': "Comunicações",
    'Producer Manufacturing': "Manufatura de Produtores",
    'null': "Outros",
    'Miscellaneous': "Diversos",
    'Electronic Technology': "Tecnologia Eletrônica",
    'Industrial Services': "Serviços Industriais",
    'Health Technology': "Tecnologia de Saúde",
    'Consumer Durables': "Bens de Consumo Duráveis",
}
