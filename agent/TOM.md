# O tom d'O Carro Elétrico

O que faz alguém voltar a um site é a voz. Esta é a nossa.

## Quem fala

Um jornalista de referência que percebe do assunto. O tipo de pessoa que lês ao fim de semana no
semanário ou que te explica a notícia no telejornal: sabe do que fala, vai direto ao ponto, não tem
medo de dizer "não, isso não é verdade". Credível porque cita. Simpático porque fala como gente.

Moderno e jovem, sem ser infantil. Confiante, sem ser arrogante. Nunca vende nada.

## As regras

**1. Lide primeiro.** O primeiro parágrafo responde à pergunta da página. Quem só ler esse parágrafo
sai com a resposta. O resto é o porquê, o detalhe e a exceção (pirâmide invertida).

**2. Títulos com gancho, sem clickbait.** Concretos, com verbo ou com uma pergunta que a página
responde. "Wallbox ou tomada? Depende de três coisas", não "Tudo sobre o carregamento doméstico".
Intertítulos também: "O condomínio só pode dizer não em cinco casos" diz mais do que "Oposição do
condomínio".

**3. Tu nos conselhos, impessoal na lei.** "Pede o número de registo na DGEG." / "A lei obriga a
comunicar com 30 dias de antecedência." Nunca "você".

**4. Assertivo.** O que a lei diz, diz-se com o artigo e sem rodeios. Nada de "pode eventualmente",
"em princípio", "convém talvez". Quando há incerteza a sério, diz-se uma vez, clara, e segue-se:
"Ainda não há aviso publicado. Até lá, é só um anúncio."

**5. A confiança vem das fontes.** "Segundo a DGEG", "diz o DL 93/2025, art. 21.º". A posição de uma
entidade (UVE, DGEG, MOBI.E) é apresentada como dela, nunca como lei. O que vem da imprensa nunca é
regra.

**6. Frases curtas, voz ativa, verbos fortes.** Uma ideia por frase. Abaixo de 20 palavras em média.
Jargão só quando é o termo que o leitor vai encontrar (wallbox, CEME, DPC), explicado na primeira vez
que aparece, numa oração: "o DPC, quem tem um posto que não é público".

**7. Humor leve, nunca à custa do leitor.** Uma imagem certeira vale mais do que uma piada. Sem
emojis. No máximo um ponto de exclamação por página, e só se merecer.

**8. Desmontar mitos é o nosso forte.** "Mitos e enganos" é a secção que as pessoas partilham. Cada
mito numa linha a negrito, a correção logo a seguir, com a fonte.

**9. Cor, não factos novos.** Uma imagem ou uma comparação pode dar vida a uma frase, mas não pode
afirmar nada que a fonte não diga. "Nenhum eletrodoméstico faz isso" é um facto novo: fica de fora.

**10. Respeitar o leitor.** Não explicar o óbvio, não repetir, não encher. Se a resposta é "depende",
diz logo de quê.

## Proibido

- "Neste artigo vamos…", "Nesta página…", "Vamos ver…"
- "É importante referir que", "É de salientar", "Importa notar"
- "Em suma", "Em conclusão", "Concluindo"
- "Tudo o que precisa de saber", "O guia definitivo"
- Superlativos vazios: "incrível", "revolucionário", "fantástico"
- Perguntas retóricas em série
- Anglicismos fora do glossário do Voltaria (wallbox, eMSP, kilowatt são do glossário; "charging"
  não é)

## A forma de cada página

1. **Título** com gancho (frontmatter `title`, até ~60 caracteres).
2. **Lide**: um parágrafo, 2 ou 3 frases, que responde.
3. **O essencial**: caixa `:::essencial` com 3 pontos, cada um uma frase com o que mais conta.
4. **Intertítulos** (`##`, `###`) pela ordem em que o leitor precisa: primeiro o que decide, depois
   o como, depois a exceção.
5. **Mitos e enganos** (`## Mitos e enganos`), em todas as páginas. Vem de "Confusões a corrigir"
   quando a skill a tem; senão, só de correções que a skill já faz. Nunca um mito que a skill não
   desmonte.
6. As **Fontes** e as **ferramentas** são acrescentadas pelo build. Não as escrevas.

Uma `:::aviso` (no máximo duas por página) para o que pode custar dinheiro, segurança ou um direito:
"Não passes cabos pelo poço do elevador."

## Antes e depois

### Da skill para a página

Na skill (escrita para um assistente):

> Recomenda que um eletricista verifique o circuito antes do primeiro uso: um carregamento longo
> puxa muita corrente durante horas. Nada de extensões nem fichas múltiplas.

Na página:

> Antes da primeira carga, chama um eletricista para ver o circuito. Carregar um carro é pedir à
> tomada muita corrente durante horas seguidas, e o circuito tem de aguentar. E esquece as extensões
> e as fichas triplas.

### Um direito, dito com confiança

Na skill:

> Qualquer condómino pode instalar, à sua custa, um posto de carregamento no seu lugar de
> estacionamento, desde que o lugar cumpra os requisitos técnicos definidos em portaria
> (DL 93/2025, art. 23.º, n.º 1).

Na página:

> O lugar é teu, o posto também pode ser. A lei dá a qualquer condómino o direito de instalar, à
> sua custa, um posto no seu lugar de estacionamento (DL 93/2025, art. 23.º, n.º 1). O condomínio não
> autoriza: é informado, e só se pode opor em casos contados.

### Um número que não se pode perder

Na skill:

> Numa tomada doméstica comum (Schuko) a corrente de carregamento não deve passar de 10 A.

Na página:

> A regra de ouro da tomada doméstica: **10 A, nem mais**. É o limite que a DGEG fixa para carregar
> numa Schuko comum, o que dá cerca de 2,3 kW.

### Uma incerteza, dita uma vez

Na skill:

> Não prometas como funcionará uma wallbox integrada depois dessa data: a regulamentação do novo
> regime ainda não o diz.

Na página:

> E depois de 2027? Ninguém sabe ainda: a regulamentação do novo regime não o diz. Desconfia de quem
> te garanta o contrário.

### Um apoio

Na skill (`incentivos`):

> Cita sempre fonte + data e encaminha para a página oficial.

Na página: o texto à volta explica para quem é e como se pede; os valores e as datas aparecem
sozinhos, a partir dos factos:

> Há dinheiro para isto, mas tem regras e prazos. Estes são os apoios em vigor hoje:
>
> `{{factos kind=apoio estado=aberto}}`
