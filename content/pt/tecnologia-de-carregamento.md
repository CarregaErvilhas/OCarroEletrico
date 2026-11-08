---
title: "Do cartão ao Plug & Charge: o que corre por trás do posto"
description: "Porque o teu cartão funciona no posto de outro operador, o que fazem o OCPP e o OCPI, porque o Plug & Charge tarda e para que serve uma bateria no posto."
source: "tecnologia-de-carregamento"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "2bb814be6dbad3f03c92d772ceb03977a42e010384e2a24df6795cc0049efffa"
updated: "2026-11-08"
---

Carregar com o cartão de uma empresa no posto de outra, com quem não tens contrato, é roaming: as
duas trocam por trás a autorização, os dados da sessão e a faturação. Por baixo correm dois
protocolos abertos: o OCPP liga o posto ao sistema do operador, o OCPI liga esses sistemas entre si.
O Plug & Charge dispensa o cartão, mas só quando o carro, o posto e quem te vende o serviço o
suportam.

:::essencial
- **Roaming**: o OPC, que opera o posto, e o eMSP, que te vende o cartão ou a app, trocam entre si a autorização, os dados da sessão e a faturação, diretamente ou através de um hub.
- **Plug & Charge**: ligas o cabo e a sessão começa, autenticada por certificados digitais (ISO 15118). Se o carro, o posto ou o eMSP não o suportam, usas o cartão ou a app.
- **OCPP e OCPI**: o OCPP liga cada posto ao backoffice do OPC, o OCPI liga backoffices entre si. Não competem, completam-se.
:::

## O teu cartão no posto de outro operador: é o roaming {#roaming}

O roaming deixa-te carregar com o cartão ou a app de um eMSP num posto de um OPC com quem não tens
contrato. O eMSP, o prestador de serviços de mobilidade, vende-te o cartão ou a app e fatura-te. O
OPC opera os postos e o backoffice, o sistema que os gere. Os dois trocam entre si a autorização, os
dados da sessão e a faturação. A mesma empresa pode ser OPC e eMSP.

**O pagamento ad hoc não precisa de roaming.** O AFIR, o Regulamento (UE) 2023/1804, obriga os
postos públicos novos ou renovados a aceitá-lo: pagas só aquele carregamento,
sem registo nem contrato.

Se só queres carregar e pagar, o que precisas está em [carregar na rua, com cartão, app ou ad
hoc](/carregamento-publico/). O que se segue é para quem integra, opera ou estuda a rede.

### Direto ou através de um hub {#direto-ou-atraves-de-um-hub}

Cada OPC pode ligar-se a cada eMSP diretamente (peer-to-peer) ou através de um **hub de roaming**,
que junta muitos numa só integração técnica e contratual. Os hubs que vais ouvir nomear:

| Hub | O que é | Protocolos |
|---|---|---|
| Hubject (marca intercharge) | Hub europeu | OICP, e também OCPI |
| Gireve | Hub francês | eMIP e OCPI |
| e-clearing.net | Hub com origem nos Países Baixos e na Alemanha | OCHP e OCPI |

A Hubject gere também uma das raízes de confiança do Plug & Charge. Por cima dos hubs há plataformas
de roaming gerido: tratam dos contratos, da integração e da liquidação por conta de OPC e eMSP.

Quantos postos, parceiros ou países tem cada um, e que quota de mercado: esses números mudam depressa
e dependem de quem os publica. Se precisares deles, vai à fonte e vê a data.

### Em Portugal: da plataforma MOBI.E ao Mobi.Hub {#em-portugal}

No regime antigo, a plataforma da MOBI.E liga os CEME, quem te vende a energia na rede MOBI.E, aos
OPC, e funciona como hub nacional. Para o novo regime, a MOBI.E lançou em outubro de 2026 o
**Mobi.Hub**: segundo a própria MOBI.E, é um hub de roaming aberto a OPC e eMSP, estejam ou não
ligados à plataforma antiga.

## Plug & Charge: ligas o cabo e a sessão começa {#plug-charge}

Com Plug & Charge, o carro autentica-se sozinho. Ligas o cabo e a sessão começa, sem cartão, app nem
QR code. A autorização e a faturação correm por trás, com certificados digitais.

- **Só funciona se os três o suportarem**: o carro, o posto e o eMSP. Se um falhar, usas o cartão ou
  a app.
- **Alguns carros aceitam vários certificados de contrato**, de vários eMSP.
- **Que carros, postos e eMSP o suportam** é uma lista que muda. Confirma com o operador concreto.

### Como funciona: certificados e PKI {#como-funciona}

Assenta na **ISO 15118**, a norma da comunicação entre o carro e o posto. A ISO 15118-2 é a que está
instalada. A ISO 15118-20 acrescenta o carregamento bidirecional (V2G) e TLS 1.3. [O que é o V2G e
onde estamos](/carregar-em-casa/#v2l-v2h-e-v2g).

A identidade prova-se com uma **PKI** (infraestrutura de chave pública): cadeias de certificados
X.509, assinadas por autoridades de certificação, que provam quem é o carro e qual é o contrato.

- **O carro guarda dois certificados**: um de contrato, emitido para o eMSP, e um de
  aprovisionamento, do fabricante do carro. Ao ligar, apresenta o de contrato ao posto, que valida a
  cadeia até uma raiz V2G (V2G Root CA).
- **Participam quatro PKI ligadas entre si**: a do OPC, a do serviço de aprovisionamento de
  certificados (CPS), a do eMSP e a do fabricante do carro.
- **O certificado de contrato pode ser instalado** num posto, na primeira vez, ou pela telemática do
  fabricante.

### Porque ainda não é a regra {#porque-a-adocao-e-lenta}

A maioria das sessões ainda usa cartão RFID ou app. O Plug & Charge pede muito a muita gente:

- **Ao fabricante do carro**: um módulo de segurança no carro, a gestão dos certificados pela
  telemática e atualizações de software à distância para as novas versões da ISO 15118.
- **A todos ao mesmo tempo**: fabricantes, OPC, eMSP e autoridades de certificação têm de se
  coordenar.
- **E há várias raízes de confiança**, que nem sempre se reconhecem entre si.

### AutoCharge: parece igual, não é {#autocharge}

O AutoCharge identifica o carro pelo identificador que este envia ao posto, o EVCCID, muitas vezes o
endereço MAC. Não usa certificados, e por isso é mais simples de pôr a funcionar. Para o condutor
parece igual ao Plug & Charge. Só alguns OPC o oferecem, e é preciso ativá-lo na app.

:::aviso
**O AutoCharge é menos seguro.** Sem certificados, qualquer carro que envie o mesmo identificador é aceite. É essa a troca que fazes ao ativá-lo na app: mais simplicidade, menos segurança.
:::

### Outras formas de começar a carga {#outras-formas-de-autenticar}

- **Cartão RFID ou NFC**, a mais comum.
- **App ou QR code**, do eMSP ou do OPC.
- **Pagamento ad hoc** com cartão bancário.

### O que diz a lei e quem escreve as regras {#normas-e-regras}

- **O AFIR** (Regulamento (UE) 2023/1804) exige interoperabilidade e acesso não discriminatório, e
  remete a comunicação entre o carro e o posto para a ISO 15118. [O que o AFIR exige aos
  postos](/afir/).
- **O DL 93/2025, art. 6.º**, obriga os postos instalados ou renovados a permitir o carregamento ad
  hoc e inteligente. As normas de comunicação para o bidirecional são as do AFIR.
- **Na Alemanha**, a regra de aplicação VDE-AR-E 2802-100-1 trata da gestão dos certificados da ISO
  15118.
- **A CharIN**, uma associação que promove a interoperabilidade, publica guias sobre a PKI.

## OCPP e OCPI: um fala com o posto, o outro entre backoffices {#ocpp-e-ocpi}

São dois protocolos abertos e completam-se. O OCPP liga o backoffice de um OPC aos seus postos. O
OCPI liga backoffices entre si: o do OPC aos dos eMSP e aos hubs.

**Diz sempre a versão.** OCPP 1.6 ou 2.0.1, ISO 15118-2 ou -20: o que vale para uma pode não valer
para a outra. Quando alguém te disser que suporta OCPP, pergunta qual.

### OCPP, entre o posto e o backoffice {#ocpp}

O OCPP (Open Charge Point Protocol) é o protocolo aberto entre o posto e o sistema de gestão central
do OPC, o CSMS, a que se chama backoffice. Mantém-no a Open Charge Alliance (OCA).

- **Versões**: a 1.6, a mais instalada; a 2.0.1, publicada também como norma IEC 63584; e a 2.1, que
  acrescenta a ISO 15118-20 e o carregamento bidirecional.
- **O que faz**: estado do posto, autorização das sessões, valores de medição, transações,
  atualização de firmware, diagnóstico e perfis de carga (carregamento inteligente).
- **Porque importa**: sem um protocolo comum, cada fabricante de postos usaria o seu, e o OPC ficava
  preso a um fornecedor de backoffice.

### OCPI, entre backoffices {#ocpi}

O OCPI (Open Charge Point Interface) é o protocolo aberto entre backoffices, do OPC para o eMSP,
diretamente ou através de um hub. Mantém-no a EVRoaming Foundation, sob licença CC BY-ND 4.0.

- **Versões**: 2.1.1, 2.2.1 e 2.3.0. A 2.3.0 acrescenta o que o AFIR pede para [os dados dos
  postos](/afir-nap/). Pode já haver uma mais recente: confirma na EVRoaming Foundation.
- **O que faz**: localizações e disponibilidade em tempo real, tokens de autorização, sessões, CDR
  (os registos de carregamento para faturar), tarifas, comandos remotos e carregamento inteligente.

### Como se juntam {#como-se-juntam}

Um OPC usa o OCPP para gerir os seus postos e o OCPI para se ligar a eMSP e a hubs. Um exemplo: um
eMSP envia por OCPI um limite de carga ao backoffice do OPC, e este passa-o ao posto por OCPP.

## Baterias no posto (BESS): mais potência do que a rede dá {#bess}

Um BESS (Battery Energy Storage System) é uma bateria fixa instalada junto do posto. Carrega da rede
ou de produção renovável local, e descarrega para os carregadores ou para serviços de rede. Com ele,
o posto entrega mais potência do que a ligação à rede permite, sem reforçar o ramal.

### Para que serve {#para-que-serve-um-bess}

- **Cortar picos (peak shaving).** Os postos rápidos puxam potência aos picos, altos e
  imprevisíveis, e a potência contratada paga-se por esses picos. O BESS descarrega nos picos e baixa
  a potência pedida à rede. [Como se paga a rede quando se opera um posto](/tarifas-de-acesso/).
- **Ganhar tempo.** Dá para instalar mais carregadores, ou mais potentes, sem esperar por um reforço
  da rede, que pode levar meses ou anos.
- **Apoiar a rede.** Amortece variações no ponto de ligação e, conforme o mercado, pode vender
  flexibilidade (reserva de frequência, deslocação de consumo) ou fazer arbitragem de preços.
- **Reserva.** Em alguns casos, alimenta o posto durante uma falha da rede.

Quanto poupa e em quanto tempo se paga depende do perfil de uso do hub de carregamento, das tarifas
de potência e dos serviços de rede de cada país. Desconfia de percentagens de poupança ou de prazos
de retorno dados de cor. E para saber se um posto concreto tem BESS, só o OPC confirma.

:::aviso
**Um BESS subdimensionado esgota-se nos picos** e deixa de cortar a potência, justamente quando fazia falta. O dimensionamento é um estudo de cada caso.
:::

## Mitos e enganos {#mitos-e-enganos}

- **"Se o meu cartão não tem acordo com aquele operador, não carrego."** Num posto público novo ou
  renovado, carregas na mesma: o AFIR obriga-o a aceitar pagamento ad hoc, e isso não depende do
  roaming.
- **"OCPP e OCPI são alternativas."** Fazem coisas diferentes. O OCPP liga o posto ao backoffice, o
  OCPI liga backoffices entre si. Um OPC usa os dois.
- **"Com Plug & Charge, o cartão fica em casa."** Só se o carro, o posto e o eMSP o suportarem. A
  maioria das sessões ainda se faz com cartão RFID ou app, por isso leva-o.
- **"AutoCharge é Plug & Charge com outro nome."** Para o condutor parece igual, mas o AutoCharge não
  usa certificados. Reconhece o carro pelo EVCCID e aceita qualquer carro que envie o mesmo
  identificador.
- **"Suporta OCPP, está tudo dito."** Falta a versão. A 1.6 é a mais instalada; é a 2.1 que
  acrescenta a ISO 15118-20 e o carregamento bidirecional.
- **"Uma bateria no posto paga-se sempre."** Depende do perfil de uso, das tarifas de potência e dos
  serviços de rede de cada país. E um BESS subdimensionado esgota-se nos picos.
