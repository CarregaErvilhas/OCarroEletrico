---
title: "NAP: que dados os postos têm de publicar, e como lá chegam"
description: "O Ponto de Acesso Nacional sem rodeios: o que o AFIR obriga os OPC a publicar, como os dados chegam à EADME e como se lê o NAP português."
source: "afir-nap"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "5079bf9a60c10d09236b4277ec4cbe3405fb494800b0539dd1ee494edca02701"
updated: "2026-11-08"
---

Cada Estado-membro tem um Ponto de Acesso Nacional (NAP), onde se publicam os dados dos postos de
carregamento: onde estão, que fichas têm, se estão livres e quanto custam. O AFIR obriga os OPC,
quem opera os postos públicos e semipúblicos, a pôr lá esses dados. Em Portugal, o NAP é gerido pelo
IMT-IP e alimentado pela MOBI.E, que recebe os dados dos OPC como EADME.

:::essencial
- **O NAP é um ponto de acesso, não uma base de dados central**: cada país tem o seu, e os OPC entregam-lhe os dados estáticos e dinâmicos de cada posto (AFIR, art. 20.º).
- **Em Portugal, os dados passam pela MOBI.E**: como EADME, recebe-os dos OPC e publica-os no NAP do IMT-IP, em DATEX II 3.3, com estado e preços.
- **Se és OPC**: dados estáticos até 24 horas depois de uma alteração, dinâmicos até um minuto depois, por DATEX II ou OCPI. Com os postos na plataforma da MOBI.E, não tens nada a fazer até ao fim do período transitório.
:::

## A Europa manda publicar, Portugal organiza, a MOBI.E opera {#tres-camadas}

O Regulamento (UE) 2023/1804, o AFIR, aplica-se diretamente em todos os Estados-membros. O art. 20.º
obriga a publicar os dados dos postos num Ponto de Acesso Nacional.

Cada regra sobre o NAP vem de uma de três camadas:

- **A obrigação europeia**: o AFIR.
- **A lei portuguesa**: o DL 93/2025 e o DL 155/2026.
- **A operação concreta do NAP**: a MOBI.E e o IMT-IP.

O AFIR fixa potências mínimas por nó da rede TEN-T e prazos de implantação. Para prazos, distâncias
e potências exatos, vai sempre à versão oficial: o
[texto do AFIR](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32023R1804) e os
decretos-lei. O resto do regulamento, e como se aplica em Portugal, está em
[o que o AFIR exige à rede de carregamento](/afir/).

## O que é um NAP, e o que não é {#o-que-e-um-nap}

Um Ponto de Acesso Nacional é a plataforma central de cada Estado-membro onde se publicam os dados
das infraestruturas de combustíveis alternativos, incluindo os postos de carregamento. A ideia não
nasceu com o AFIR. Já existia na Diretiva ITS 2010/40/UE e nas suas regulamentações delegadas (MMTIS,
RTTI, SRTI, SSTP), para dados de mobilidade em geral. O AFIR estendeu-a aos combustíveis
alternativos, sobretudo ao carregamento elétrico (art. 20.º).

- **Cada país tem o seu.** Não há um NAP europeu único.
- **É um ponto de acesso, não uma base de dados centralizada.** Agrega e disponibiliza os dados que
  os OPC, e outras entidades, lhe entregam.
- **Serve três propósitos**: os condutores encontram postos disponíveis; as autoridades acompanham a
  implantação da rede; e os eMSP, que vendem carregamentos em postos de vários OPC, prestam serviços
  de carregamento integrados.

Se só queres encontrar um posto e carregar, o que precisas está em [carregar na rua](/carregamento-publico/).

### CEAP: a porta europeia, sem dados próprios {#ceap}

O AFIR prevê também um Ponto de Acesso Comum Europeu (CEAP), alojado no
[Observatório Europeu dos Combustíveis Alternativos](https://alternative-fuels-observatory.ec.europa.eu)
(EAFO). É uma porta de entrada para descobrir os dados publicados em cada NAP nacional. Não guarda
dados: encaminha quem procura para a informação que está nos NAPs. A criação está prevista até 31 de
dezembro de 2026.

## O que um OPC tem de pôr no NAP {#o-que-os-opc-publicam}

Os OPC que operam postos públicos ou semipúblicos têm de disponibilizar dois tipos de dados, por API,
através do NAP nacional (AFIR, art. 20.º). A obrigação conta a partir de 14 de abril de 2025, para os
Estados-membros com os prazos aplicáveis.

- **Dados estáticos**: a localização do posto; o número de conectores; os lugares para pessoas com
  mobilidade reduzida; os contactos; o horário; o código do operador; os tipos de conector; o tipo de
  corrente (AC ou DC); a potência máxima do posto e do EVSE, o ponto de carregamento; e os tipos de
  veículo compatíveis.
- **Dados dinâmicos**: o estado operacional (em serviço ou avariado); a disponibilidade em tempo
  real; o preço ad hoc, o de quem carrega sem contrato; e se a eletricidade é 100 % renovável.

Quem publica pode ser o próprio OPC ou um intermediário, como uma plataforma de gestão de postos. A
responsabilidade é do OPC. Em Portugal, a MOBI.E publica no NAP o inventário estático e o estado
dinâmico, com preços.

### IDRO e IDACS: quem é quem nos dados {#idro-e-idacs}

O AFIR exige que cada Estado-membro nomeie uma Organização de Registo de Identificação (IDRO). A IDRO
gere os códigos únicos de identificação dos OPC e dos eMSP, os IDACS. Esses códigos entram nos dados
publicados no NAP e dizem, sem margem para dúvida, quem opera cada posto e quem presta serviços de
mobilidade.

A lista das IDRO de cada país e os códigos registados estão publicados em cada NAP nacional, ou em
registos associados. Em Portugal, esta função enquadra-se na DGEG e na estrutura da MOBI.E.

## Em Portugal, o NAP é do IMT-IP e os dados vêm da MOBI.E {#como-funciona-em-portugal}

O [portal do NAP português](https://nap-portugal.imt-ip.pt) é gerido pelo IMT-IP e serve os dados da
MOBI.E em dois endereços:

- **Inventário estático**: `https://pgm.mobie.pt/integration/nap/evChargingInfra`, com cerca de 190 MB,
  em XML DATEX II 3.3.
- **Estado dinâmico e preços**: `https://pgm.mobie.pt/integration/nap/evActualStatus`, com cerca de
  40 MB.

Por trás destes ficheiros, a MOBI.E tem dois papéis, e a lei tem dois modelos:

- **A MOBI.E é a EADME**, a Entidade Agregadora de Dados para a Mobilidade Elétrica, ao abrigo do DL
  93/2025, com regime transitório até 31-12-2027. Segundo a MOBI.E, a sua atividade como EADME é
  supervisionada pela AMT, a Autoridade da Mobilidade e dos Transportes.
- **A MOBI.E continua a ser a EGME**, a entidade gestora da mobilidade elétrica, até 31-12-2027. Gere a
  plataforma da rede e cobra a tarifa da EGME, fixada pela ERSE. Não é a TAR, a
  [tarifa de acesso às redes elétricas](/tarifas-de-acesso/).
- **Dois modelos de mercado convivem.** O DL 93/2025 trouxe um modelo novo, com contrato direto com o
  OPC ou com um eMSP. O DL 155/2026 prorrogou o período transitório até 31-12-2027 e mantém, até lá, o
  modelo antigo, em que um CEME vende a energia na rede MOBI.E.
- **Desde setembro de 2026**, segundo a MOBI.E, a área MOBI.DATA mostra a disponibilidade em tempo real
  dos postos de toda a rede pública. Inclui os OPC que não estavam ligados à MOBI.E, à medida que
  concluem a integração com a EADME.

## Enviar os dados à EADME: o quê, quando e como {#como-os-opc-enviam-os-dados}

A Portaria n.º 31/2026/1 manda a EADME fixar as regras técnicas. Já há uma: a Regra Técnica n.º
1/EADME/2026, aprovada e publicada a 18-05-2026, depois de consulta pública. Segundo a própria regra
(ponto 11), aplica-se 30 dias úteis depois da publicação.

- **Que dados**: os estáticos e os dinâmicos do art. 20.º do AFIR. O estado do EVSE junta num só campo
  o estado operacional e a disponibilidade. O preço ad hoc vai com todas as componentes (ponto 6).
- **Com que frequência**: os dados estáticos, até 24 horas depois de uma alteração; os dinâmicos, até
  um minuto depois (ponto 7).
- **Como, por DATEX II**: dois endereços em XML, sem autenticação, um para os dados estáticos e outro
  para os dinâmicos.
- **Como, por OCPI 2.2 ou 2.2.1**: no papel de OPC, com os módulos Versions, Credentials, Locations e
  Tariffs. Os dados estáticos que o OCPI não tem preenchem-se na plataforma da EADME, ou seguem em
  campos não normalizados definidos pela EADME (ponto 8 e anexo I).
- **Na transição**: se os teus postos estão na plataforma da MOBI.E, não tens de fazer nada durante o
  período transitório. A EADME converte para DATEX II o que já recebe por OCPP e OCPI. No fim do
  período, tens de escolher uma das duas formas acima (ponto 10).

:::aviso
**Dados em falha são uma infração.** Dados incompletos, errados ou fora da frequência são uma infração leve (DL 93/2025, art. 13.º, n.º 1, c), e art. 34.º, n.º 1, a)), lembra a regra no ponto 9. Se uma plataforma de gestão envia os dados por ti, a responsabilidade continua a ser tua.
:::

:::aviso
**A regra diz 2026, a lei diz 2027.** A regra técnica fala do fim do período transitório a 31-12-2026, porque foi escrita antes do DL 155/2026, que o prolongou até 31-12-2027. Se uma decisão tua depende desta data, confirma-a com a EADME.
:::

## Quem pode usar os dados, e onde estão as listas oficiais {#acesso-e-licenca}

Os endereços do NAP português são publicados com licenças de livre acesso. Os termos estão nas
páginas do NAP do IMT-IP.

- **O tarifário dos OPC** da MOBI.E é publicado em CSV, no sítio da MOBI.E.
- **A lista atualizada de OPC registados** está na DGEG. A dos CEME também, enquanto durar o regime
  transitório.
- **Para listas de NAPs, OPC ou eMSP de outros países**, a fonte autoritativa são os registos IDRO
  nacionais. Há também uma [lista de NAPs europeus para o carregamento](https://evnapdata.eu/naps).
- **Para o preço e o estado de um posto agora**, usa as ferramentas no fim da página: leem o NAP da
  MOBI.E.

## DATEX II: a língua comum dos NAPs {#datex-ii}

O DATEX II é a norma europeia (CEN/TS 16157) para trocar dados de tráfego e de mobilidade. No AFIR, é o
formato de referência para publicar nos NAPs os dados das infraestruturas de combustíveis
alternativos. É ele que torna esses dados interoperáveis entre Estados-membros.

### Dois conjuntos: o que fica e o que muda {#estrutura-de-dados}

Um NAP do AFIR publica, para cada posto, dois conjuntos de dados:

- **Inventário estático** (`evChargingInfra`, em Portugal): locais, pontos de carregamento (EVSE) e
  conectores, com identificadores, coordenadas, operador, potência, tipos de ficha, horário, contactos
  e acessibilidade. Muda raramente.
- **Estado dinâmico e preços** (`evActualStatus`, em Portugal): estado operacional, disponibilidade em
  tempo real e preço ad hoc, por ponto. Atualiza-se com frequência.

Em Portugal, os dois endereços da MOBI.E são XML DATEX II 3.3, com os namespaces
`energyInfrastructure`, `facilities`, `locationReferencing`, `locationExtension`, `commonExtension` e
`common`. Cada registo usa identificadores estáveis (site, EVSE, conector) e potência contínua
(`max_power_w`, `voltage` e `max_current`), não classes de potência.

As classes de potência do AFIR (anexo III) são as do reporte: até 22 kW é potência normal, acima disso
é alta potência. Cada país pode expor também outros formatos, como OCPI, GeoJSON ou CSV, mas o DATEX
II é o denominador comum.

### Como se lê um NAP {#como-se-le-um-nap}

- **Formato**: XML (DATEX II) ou, conforme o país, OCPI, GeoJSON, CSV ou JSON.
- **Acesso**: aberto, com chave ou com contrato formal, conforme o NAP.
- **Hierarquia típica**: site (o local) → EVSE (o ponto de carregamento) → conector.

A [documentação e os schemas da versão 3](https://datex2.eu) estão no sítio do DATEX II. Há também o
[portal DATEX@NAPs](https://datex2.naps.inqms.tamtamresearch.com/naps-browser/nap/index.html).

## Mitos e enganos {#mitos-e-enganos}

- **"Há um NAP europeu com os dados de todos os postos."** Não há. Cada Estado-membro opera o seu. O
  CEAP, previsto no AFIR, é uma porta de entrada para os NAPs nacionais e não guarda dados.
- **"O NAP é uma base de dados central."** É um ponto de acesso: agrega e disponibiliza o que os OPC
  lhe entregam.
- **"O NAP nasceu com o AFIR."** Já existia com a Diretiva ITS 2010/40/UE, para dados de mobilidade em
  geral. O AFIR estendeu-o ao carregamento elétrico (art. 20.º).
- **"Se a plataforma de gestão publica por mim, a responsabilidade é dela."** É do OPC, publique quem
  publicar (AFIR, art. 20.º).
- **"A tarifa da EGME é a TAR."** Não é. A tarifa da EGME é a que a MOBI.E cobra como gestora da
  plataforma, fixada pela ERSE. A TAR é a tarifa de acesso às redes elétricas.
- **"O período transitório acaba a 31-12-2026."** Era o que dizia a regra técnica da EADME, escrita
  antes do DL 155/2026. O prazo passou para 31-12-2027.
