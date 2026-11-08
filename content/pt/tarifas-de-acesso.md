---
title: "Tarifas de acesso: o posto que ninguém usa também paga a rede"
description: "Na MOBI.E, a TAR ME só cobra por kWh. Fora dela, e para todos a partir de 2028, a potência entra na conta. O que muda para os OPC e como baixar o custo."
source: "tarifas-de-acesso"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "1ac5aec1a0ebd9b0b891e75398b66be8912bb3ad5e5285d617804a379f7bac5f"
updated: "2026-11-08"
---

Nos postos da MOBI.E, a tarifa de acesso às redes (TAR) cobra-se só por kWh e paga-a o condutor, até
31-12-2027. Fora da MOBI.E, e para todos a partir de 1-1-2028, o OPC paga a TAR normal, que tem termos
de potência. Um posto rápido com pouco uso passa a pagar a rede mesmo nos dias em que ninguém carrega.

:::essencial
- **Na MOBI.E**, a TAR ME só tem preços por kWh: um posto que quase não é usado não paga a potência que tem.
- **Em BTE e MT, fora da MOBI.E**, um só quarto de hora a plena potência fixa a potência contratada para os 12 meses seguintes.
- **O custo fixo da rede passa do condutor para o OPC**, que o tem de recuperar no preço: com poucos carregamentos, isso dá muito por kWh.
:::

## Antes de fazer contas, responde a cinco perguntas {#antes-de-fazer-contas}

As respostas dizem que TAR paga o teu posto e o que a faz subir.

1. **O posto está integrado na MOBI.E?** E, se está, vai sair antes do fim do período transitório?
2. **Em que nível de tensão está ligado?** BTN (até 41,4 kVA), BTE (baixa tensão acima de 41,4 kVA) ou MT (com posto de transformação próprio).
3. **Que potência têm os postos**, e há gestão de potência ou uma bateria (BESS)?
4. **Quantos kWh vendes por mês, e a que horas?** O consumo em horas de ponta pesa muito.
5. **O posto tem uma ligação só para ele**, ou está numa instalação com outros consumos (uma loja, um condomínio, uma empresa), talvez com um sub-CPE?

## O que é a TAR, e o que não é {#o-que-e-a-tar}

A tarifa de acesso às redes paga o uso das redes de transporte e de distribuição e os custos de
política energética (CIEG). A ERSE fixa-a todos os anos, em dezembro, para o ano seguinte e por nível
de tensão (Regulamento Tarifário). O ORD, quem gere a rede de distribuição, fatura-a ao comercializador,
que a passa para a fatura do cliente.

**A TAR é só a parte da rede.** Além dela, o OPC paga a energia, a margem do comercializador e os
impostos. E como os preços mudam todos os anos, confirma sempre de que ano é o preço com que fazes
contas.

Tem até quatro termos, conforme o nível de tensão (Regulamento Tarifário, arts. 44.º, 45.º, 52.º e
54.º):

| Termo | BTN | BTE e MT |
|---|---|---|
| Potência contratada (por dia) | O escalão escolhido no contrato | **A máxima potência tomada nos últimos 12 meses**, incluindo o mês da fatura |
| Potência em horas de ponta (por kW e por dia) | Não tem | A energia em horas de ponta a dividir pelas horas de ponta do período |
| Energia ativa (por kWh, por período horário) | Sim | Sim |
| Energia reativa | Não | Sim |

Em BTE não há escalões: pode contratar-se qualquer potência acima de 41,4 kVA. Mas a potência
contratada não pode passar a potência requisitada da ligação, segundo o manual de ligações da E-REDES.

### O quarto de hora que manda {#potencia-tomada}

Em BTE e MT, o que se paga como potência contratada é a máxima potência tomada. E a potência tomada
é o maior valor da potência ativa média em qualquer período ininterrupto de 15 minutos (Regulamento Tarifário, art. 44.º).
Conta a média desses 15 minutos, não o pico instantâneo: uma sessão curta pesa pelo que puxou, em
média, nesse quarto de hora.

:::aviso
**Um quarto de hora fica na fatura um ano.** Em BTE e MT, um só período de 15 minutos a plena potência num mês fixa a potência contratada para os 12 meses seguintes.
:::

### Horas de ponta: poucas e caras {#horas-de-ponta}

No ciclo semanal do continente, as horas de ponta são 5 h por dia útil na hora legal de inverno e 3 h
na de verão, e não há ponta aos fins de semana. No ciclo diário são 4 h por dia, todos os dias
(Regulamento Tarifário, Quadro 8). O preço por kW da potência em horas de ponta é muito mais alto do
que o da potência contratada.

## Na MOBI.E: a rede paga-se ao kWh {#na-mobi-e}

Nos postos integrados na MOBI.E, a energia dos carregamentos paga uma TAR própria, a TAR da mobilidade
elétrica (TAR ME). Tem **só preços por kWh**, em opção bi-horária ou tri-horária, sem potência
contratada nem potência em horas de ponta (Regulamento Tarifário, arts. 57.º e 58.º).

- **Como se chega ao kWh.** A ERSE converte os preços de potência da TAR em BTN em preços por kWh, por
  período horário, com base no perfil de consumo da rede de mobilidade elétrica. A razão, segundo a
  ERSE: a carga, os carros, varia no tempo e no espaço.
- **Há quatro variantes**, conforme o nível de tensão da ligação do posto: BT, MT, AT e MAT. Todas
  partem da TAR em BTN, e as de tensão mais alta tiram o uso das redes que não usam.
- **Quem fatura a quem.** O ORD fatura a TAR ME ao comercializador que abastece o CEME (Regulamento n.º
  7/2026, art. 10.º). O CEME, quem vende a energia ao condutor na MOBI.E, passa-a para a fatura do
  condutor, à parte da tarifa do OPC.

**O que isto dá ao OPC:** o custo fixo da rede de um posto MOBI.E paga-o o condutor, ao kWh. Um posto
rápido que quase não é usado não paga a potência que tem. Só há custo de rede quando há carregamentos.

### Tem prazo, e não há sucessora à vista {#tem-prazo}

A TAR ME só se aplica durante o período transitório, que o DL 155/2026 alargou até 31-12-2027. E só às
entregas dos CEME em postos que continuem integrados na MOBI.E, segundo a ERSE. O DL 93/2025 não prevê
uma TAR própria para os postos fora da MOBI.E, e até 6 de novembro de 2026 não encontrámos nenhuma
proposta da ERSE nesse sentido.

## Fora da MOBI.E: a potência entra na conta {#fora-da-mobi-e}

Fora da MOBI.E, o OPC contrata a eletricidade do posto a um comercializador, como qualquer instalação
de consumo (DL 93/2025, art. 9.º), e paga a TAR normal do nível de tensão. Já é assim hoje para quem
desintegra o posto da MOBI.E. A partir de 1-1-2028, é assim para todos.

**Em BTN**, nos postos AC até 41,4 kVA no total, o termo de potência é o do escalão escolhido. É um
custo fixo conhecido, e baixa-se mudando de escalão.

**Em BTE e MT**, nos postos DC e nos parques com muitos postos, entram os dois termos de potência:

- **Potência contratada**: o maior quarto de hora dos últimos 12 meses. Num posto de 150 kW que chegue
  uma vez aos 150 kW em média de 15 minutos, paga-se 150 kW por dia durante um ano, haja carregamentos
  ou não.
- **Potência em horas de ponta**: cada kWh vendido nessas horas pesa muito, porque o preço por kW é
  várias vezes o da potência contratada.

O resultado: o custo fixo da rede passa do condutor, que o pagava ao kWh, para o OPC, que o paga ao
kW. O OPC tem de o recuperar no preço que cobra. Num posto com poucos carregamentos, isso dá muito por
kWh.

## E o condutor? Paga sempre, muda é onde {#e-o-condutor}

A TAR não é só assunto de quem opera ou detém postos: acaba sempre no preço do carregamento. Na MOBI.E, vem na
fatura do CEME, à parte da tarifa do OPC. Fora da MOBI.E, não a pagas à parte: está dentro do preço do
OPC ou do eMSP, quem te vende carregamentos por cartão ou app em postos de vários OPC. E num posto com
poucos carregamentos, depois de 2027, o custo fixo da rede tem de caber no preço de cada kWh.

Como se paga um carregamento num posto público está em [carregar na rua](/carregamento-publico/).

## A conta de um posto com pouco uso {#a-conta}

Para saber quanto pesa a TAR normal num posto em BTE ou MT, faz a conta a um mês de 30 dias, com os
preços do ano:

1. **Termo fixo** = potência contratada (kW) × preço da potência contratada × 30.
2. **Potência em horas de ponta** = (kWh em horas de ponta ÷ horas de ponta do mês) × preço da potência em horas de ponta × 30.
3. **Energia** = kWh de cada período × preço da energia ativa desse período.
4. **Custo de rede por kWh** = a soma dos três ÷ kWh vendidos no mês.

Na MOBI.E, a conta é mais curta: kWh de cada período × preço da TAR ME desse período.

O termo fixo não depende dos kWh. Daí a regra: **abaixo de um certo consumo mensal, a TAR normal sai
mais cara por kWh do que a TAR ME, e quanto menos uso, pior**. Acima desse consumo, a TAR normal pode
até sair mais barata, porque a energia ativa em BTE e MT é mais barata por kWh do que a TAR ME.

Os preços da TAR deste ano, publicados pela ERSE, e um exemplo já feito com eles para um posto
rápido, cada um com a fonte e a data em que foi verificado:

{{factos kind=mercado series=tar}}

A conta é uma estimativa e vale o que valem os pressupostos: a potência de pico, os kWh por mês e a
parte do consumo em horas de ponta. O valor real depende do ciclo, da opção tarifária e do
comercializador. E não diz se deves investir: mostra o que pesa e o que a faz mudar. Para a fazer com
os teus números, usa as ferramentas no fim da página.

### Quem mais sente a mudança {#quem-mais-sente-a-mudanca}

- **Postos rápidos em locais de passagem rara.**
- **Redes municipais ou de cobertura**, instaladas para cumprir metas e não pela procura.
- **Parques com muitos postos numa só ligação em BTE ou MT**, que raramente estão todos ocupados.

## Seis formas de baixar o custo {#formas-de-baixar-o-custo}

Cada uma mexe numa parte diferente da conta. Qual compensa depende do posto, do uso e da ligação.

- **Limitar a potência com gestão de carga** (OCPP, carregamento inteligente). O que conta é a média
  de 15 minutos na ligação. Por isso, limitar o total do parque baixa a potência contratada dos 12
  meses seguintes.
- **Cortar os picos com uma bateria (BESS).** A bateria fornece os picos e a rede vê uma potência
  menor.
- **Fugir às horas de ponta.** Preços mais altos ou potência limitada nessas horas baixam a potência
  em horas de ponta.
- **Ficar na MOBI.E até ao fim do período transitório**, a 31-12-2027, enquanto a TAR ME existir.
- **Juntar o posto a uma instalação com outros consumos**, um supermercado, por exemplo. O termo fixo
  é partilhado, mas o pico do posto soma-se ao da instalação, e a potência tomada é a do total.
- **Em BTN, escolher o escalão pelo uso real**, e não pela potência máxima dos postos.

Como funcionam a gestão de carga, o OCPP e as baterias estacionárias está em [tecnologia de
carregamento](/tecnologia-de-carregamento/).

:::aviso
**Baixar a potência no contrato, sozinho, não resolve.** Mudar para um escalão ou uma potência mais baixa sem limitar a potência dos postos não serve de nada. Em BTE e MT, a potência contratada volta a subir com o primeiro pico.
:::

## Sub-CPE: o termo de potência vai atrás {#sub-cpe}

O sub-CPE é um ponto de entrega interno, com código próprio, dentro de uma instalação já ligada à
rede. Não foge ao termo de potência.

- **Paga todos os termos da TAR**, menos a energia reativa, ao nível de tensão da instalação onde está
  (Regulamento n.º 7/2026, art. 99.º).
- **Em BTE e MT**, a potência contratada é a máxima potência tomada medida no ponto interno. **Em
  BTN**, é o escalão contratado com o comercializador do sub-CPE, que não pode ser superior ao da
  instalação principal.
- **A instalação principal paga a TAR sobre o consumo por diferença**, o chamado ponto de medição
  virtual. Em BTN, a instalação principal fica no escalão igual ou logo acima da máxima potência
  tomada desse ponto virtual nos últimos 12 meses (art. 98.º).

[Quem pede um sub-CPE, como, e quanto custa](/sub-cpe/).

## Mitos e enganos {#mitos-e-enganos}

- **"A TAR ME acaba no fim de 2026."** Não. Os documentos da ERSE de 2025 falam de um período
  transitório até 31-12-2026, mas o DL 155/2026 alargou-o até 31-12-2027.
- **"O sub-CPE só paga a energia e a potência em horas de ponta."** Era a proposta da ERSE de 2025. O
  texto aprovado não ficou assim: o ponto interno paga todos os termos da TAR, menos a energia
  reativa (Regulamento n.º 7/2026, art. 99.º).
- **"A TAR é o que custa a eletricidade do posto."** É só a parte da rede. Faltam a energia, a margem
  do comercializador e os impostos.
- **"Uma sessão curta a 150 kW fixa 150 kW para o ano."** Conta a média de 15 minutos, não o pico
  instantâneo (Regulamento Tarifário, art. 44.º). Um quarto de hora inteiro a plena potência, esse
  sim, chega.
- **"Baixo a potência contratada e pago menos."** Só se limitares também a potência dos postos. Em BTE
  e MT, o primeiro pico volta a subi-la.
- **"Depois de 2027 vai haver uma TAR própria para os postos fora da MOBI.E."** O DL 93/2025 não a
  prevê, e até 6 de novembro de 2026 não encontrámos nenhuma proposta da ERSE nesse sentido. Se alguém
  te falar de uma, pede a fonte.
- **"O condutor paga sempre a TAR à parte."** Só na MOBI.E, na fatura do CEME. Fora dela, está dentro
  do preço do OPC ou do eMSP.
