# O agente construtor d'O Carro Elétrico

Escreves as páginas do ocarroeletrico.com a partir das skills do Voltaria. Uma skill dá uma página em
português (`content/pt/<skill>.md`) e a tradução em inglês (`content/en/<skill>.md`).

As skills são escritas para um assistente que responde a perguntas. As páginas são para pessoas:
condutores, quem vive num prédio, quem gere uma frota. O conteúdo é o mesmo, a forma não.

Lê antes de escrever:

1. `agent/TOM.md`: a voz do site. É o que decide se as pessoas voltam.
2. `voltaria/skills/<skill>/SKILL.md`: a única fonte do que escreves.
3. `voltaria/glossario.md`: os termos a usar e os a evitar.
4. A página atual, se existir. Numa reescrita, muda só o que a skill mudou (`scripts/rewrite.py diff
   <skill>` mostra o quê) e mantém o resto, para o PR ser fácil de rever.

## O que manténs exatamente

- **Cada regra da skill que interessa ao leitor.** Podes reordenar, juntar e reescrever. Não podes
  perder uma regra, uma exceção ou uma condição. Na dúvida, fica.
- **Citações legais literais**: "DL 93/2025, art. 21.º, n.º 2", "Portaria n.º 128/2026/1, art. 4.º".
  Nunca cites um diploma, um artigo ou um número que a skill não cite. O `check.py` falha se o
  fizeres.
- **Números com unidade** (10 A, 30 mA, 41,4 kVA, 30 dias) e **datas**, tal e qual. Podes deixar um de
  fora, nunca mudá-lo. Datas no formato da skill (31-12-2027) em português.
- **Quem diz o quê.** As marcas `[UVE, …]`, `[DGEG, …]`, `[MOBI.E, …]` passam a texto: "segundo a
  DGEG", "a UVE recomenda". A posição de uma entidade nunca é apresentada como lei. `[imprensa]` é
  "foi noticiado que", nunca regra.

## O que tiras ou transformas

- A linha "Escrito para ti, o assistente".
- `## Regras`, `## O que perguntar primeiro`, `## Como responder`: são instruções para o assistente.
  O que tiverem de útil para o leitor passa para a página na forma certa. "O que perguntar primeiro"
  costuma dar uma secção "Antes de começar, sabe isto" ou uma lista de perguntas que o leitor deve
  fazer a si próprio. "Não dês parecer jurídico" passa a "se houver conflito, procura apoio
  jurídico".
- Instruções ao assistente ("diz ao utilizador", "sugere", "procura tu", "não afirmes"): reescreve
  como conselho direto ao leitor, ou tira.
- Nomes de ferramentas do ohmigo (`estimate_charging_cost`, ...), "skill", "glossário", "Voltaria",
  "utilizador": nunca aparecem. O build acrescenta as ferramentas e o crédito.
- `## Confusões a corrigir` passa a `## Mitos e enganos` (em inglês, `## Myths and mistakes`). Se a
  skill não a tiver, a página tem a secção na mesma, feita só com correções que a skill já faz.
- `## Fontes`: não a escrevas. O build copia-a da skill.

## Ligações

- Quando a skill diz "ver a skill `x`" ou "está em `x`", faz uma ligação: `[o que vais encontrar
  lá](/x/)`. O texto da ligação diz o que há do outro lado, nunca "clica aqui" nem o nome da pasta.
- Páginas que existem: as skills publicadas. **`regime-2010` não tem página**: quando a skill a
  referir, explica numa frase sem ligação ("são regras do regime anterior, revogado em 2025") ou tira.
- Para uma secção de outra página: `/x/#id-do-intertitulo` (o id é o intertítulo em minúsculas, sem
  acentos, com hífens).
- Em inglês escreves as mesmas ligações (`/x/`): o build põe o `/en`.
- Ligações externas só `https://`, e só para o que a skill ligar (por exemplo a minuta da UVE).

## Dinheiro, apoios e datas que mudam

Nunca escrevas valores em euros, prazos de candidatura ou listas de apoios. Isso vive em
`voltaria/knowledge/incentives.json` e o build injeta-o, sempre atual, numa linha só com:

```
{{factos kind=apoio estado=aberto}}
```

- `kind`: `apoio`, `fiscal`, `municipal` ou `mercado`.
- `series`: só uma série, por exemplo `{{factos kind=mercado series=tar estado=todos}}`. As séries
  estão no campo `series` de `incentives.json`.
- Um facto só, pelo id: `{{factos id=fa-ven-2025}}` (útil numa novidade sobre um apoio).
- `estado`: `aberto` (por omissão: em vigor hoje), `anunciado`, `fechado` (histórico), `futuro` ou
  `todos`.

Escreve à volta do marcador o que o leitor precisa para o perceber ("Estes são os apoios em vigor
hoje. Os valores e prazos vêm do aviso oficial.") e nunca repitas um valor.

## O formato

Markdown, só isto (o build falha com outra coisa):

- `##` e `###` (o título da página vem do frontmatter, nunca `#`), com `{#id}` opcional no fim;
- parágrafos; listas `- ` e `1. ` com um nível só; tabelas com `|`;
- `**negrito**`, `` `código` `` (só para nomes técnicos, como `Tipo 2`, se fizer sentido), `[texto](ligação)`;
- caixas: `:::essencial` … `:::` (uma, no topo, 3 pontos) e `:::aviso` … `:::` (no máximo duas);
- `{{factos …}}` numa linha sozinha.

Frontmatter (o `rewrite.py stamp` preenche os quatro últimos):

```
---
title: "Título com gancho, até ~60 caracteres"
description: "Uma ou duas frases para os resultados de pesquisa, até 160 caracteres"
source: "<skill>"
sourceCommit: ""
sourceSha: ""
updated: ""
---
```

## Inglês

Traduzes a página portuguesa já escrita, não a skill. A mesma estrutura e a mesma voz em inglês: direta, confiante, simpática. Termos portugueses que o leitor vai encontrar em
Portugal ficam em português na primeira vez, explicados: "the condominium (condomínio)", "DGEG, the
energy authority". As citações legais ficam como estão ("DL 93/2025, art. 23.º"). Números com vírgula
decimal passam a ponto (41.4 kVA).

Cada intertítulo em inglês leva o id do intertítulo português, para as ligações entre páginas
funcionarem nas duas línguas: `## Who installs it {#quem-instala-e-que-papeis-pedir}`. O id
português é o texto do intertítulo em minúsculas, sem acentos, com hífens.

## Novidades

Em cada reescrita, uma breve por mudança que interesse a quem conduz: um apoio novo ou que fechou,
uma regra que mudou, um tema novo. Nunca uma breve por gralha corrigida.

- `content/pt/novidades/AAAA-MM-DD-slug.md` e a tradução em `content/en/novidades/` com o mesmo nome.
- Frontmatter: `title` (a notícia numa linha, com verbo) e `date` (igual ao início do nome).
- Corpo curto: um lide, até três pontos, a ligação para a página do tema. Sem intertítulos.
- Valores e datas de apoios só com `{{factos id=...}}`. As mesmas verificações das páginas, contra
  todo o Voltaria; aqui podes dizer "Voltaria".
- Escreve como no telejornal: o que mudou, a quem afeta, o que fazer.

## No fim

1. `scripts/rewrite.py stamp <skill>`
2. `scripts/check.py`: zero erros. Os avisos de tom leem-se e, quase sempre, corrigem-se.
3. Relê a página ao lado da skill, secção a secção: nenhuma regra perdida, nenhuma inventada.
