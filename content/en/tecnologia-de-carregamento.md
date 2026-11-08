---
title: "From card to Plug & Charge: what runs behind the charger"
description: "Why your card works at another operator's charger, what OCPP and OCPI do, why Plug & Charge is slow to arrive and what a battery at the charger is for."
source: "tecnologia-de-carregamento"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "2bb814be6dbad3f03c92d772ceb03977a42e010384e2a24df6795cc0049efffa"
updated: "2026-11-08"
---

Charging with one company's card at another company's charger, one you have no contract with, is
roaming: behind the scenes, the two exchange the authorisation, the session data and the billing.
Underneath run two open protocols: OCPP connects the charger to the operator's system, OCPI connects
those systems to each other. Plug & Charge does away with the card, but only when the car, the charger
and whoever sells you the service all support it.

:::essencial
- **Roaming**: the OPC, which operates the charger, and the eMSP, which sells you the card or app, exchange the authorisation, the session data and the billing, directly or through a hub.
- **Plug & Charge**: you plug in and the session starts, authenticated by digital certificates (ISO 15118). If the car, the charger or the eMSP doesn't support it, you use the card or the app.
- **OCPP and OCPI**: OCPP connects each charger to the OPC's back office, OCPI connects back offices to each other. They don't compete, they complement each other.
:::

## Your card at another operator's charger: that's roaming {#roaming}

Roaming lets you charge with an eMSP's card or app at a charger run by an OPC you have no contract
with. The eMSP, the mobility service provider, sells you the card or app and bills you. The OPC, the
charge point operator, runs the chargers and the back office, the system that manages them. The two
exchange the authorisation, the session data and the billing. The same company can be both OPC and
eMSP.

**Ad hoc payment doesn't need roaming.** AFIR, Regulation (EU) 2023/1804, requires new or
renewed public chargers to accept it: you pay for that one charge
only, with no registration and no contract.

If you just want to charge and pay, what you need is in [charging on the road, by card, app or ad
hoc](/carregamento-publico/). What follows is for people who integrate, operate or study the network.

### Direct or through a hub {#direto-ou-atraves-de-um-hub}

Each OPC can connect to each eMSP directly (peer-to-peer) or through a **roaming hub**, which brings
many of them together in a single technical and contractual integration. The hubs you'll hear named:

| Hub | What it is | Protocols |
|---|---|---|
| Hubject (intercharge brand) | European hub | OICP, and OCPI too |
| Gireve | French hub | eMIP and OCPI |
| e-clearing.net | Hub with roots in the Netherlands and Germany | OCHP and OCPI |

Hubject also manages one of Plug & Charge's roots of trust. On top of the hubs sit managed roaming
platforms: they handle contracts, integration and settlement on behalf of OPCs and eMSPs.

How many chargers, partners or countries each one has, and what market share: those numbers change
fast and depend on who publishes them. If you need them, go to the source and check the date.

### In Portugal: from the MOBI.E platform to Mobi.Hub {#em-portugal}

Under the old regime, the platform of MOBI.E, Portugal's public charging network, connects the CEMEs,
the companies that sell you energy on the MOBI.E network, to the OPCs, and works as a national hub.
For the new regime, MOBI.E launched **Mobi.Hub** in October 2026: according to MOBI.E itself, it's a
roaming hub open to OPCs and eMSPs, whether or not they're connected to the old platform.

## Plug & Charge: you plug in and the session starts {#plug-charge}

With Plug & Charge, the car authenticates itself. You plug in and the session starts, with no card,
app or QR code. Authorisation and billing run behind the scenes, with digital certificates.

- **It only works if all three support it**: the car, the charger and the eMSP. If one doesn't, you
  use the card or the app.
- **Some cars accept several contract certificates**, from several eMSPs.
- **Which cars, chargers and eMSPs support it** is a list that keeps changing. Check with the specific
  operator.

### How it works: certificates and PKI {#como-funciona}

It's built on **ISO 15118**, the standard for communication between the car and the charger. ISO
15118-2 is the one installed today. ISO 15118-20 adds bidirectional charging (V2G) and TLS 1.3. [What
V2G is and where things stand](/carregar-em-casa/#v2l-v2h-e-v2g).

Identity is proved with a **PKI** (public key infrastructure): chains of X.509 certificates, signed by
certificate authorities, that prove who the car is and what the contract is.

- **The car holds two certificates**: a contract certificate, issued for the eMSP, and a provisioning
  certificate from the carmaker. When you plug in, it presents the contract certificate to the
  charger, which validates the chain up to a V2G root (V2G Root CA).
- **Four interlinked PKIs take part**: the OPC's, the certificate provisioning service's (CPS), the
  eMSP's and the carmaker's.
- **The contract certificate can be installed** at a charger, the first time, or through the
  carmaker's telematics.

### Why it isn't the norm yet {#porque-a-adocao-e-lenta}

Most sessions still use an RFID card or an app. Plug & Charge asks a lot of a lot of people:

- **Of the carmaker**: a security module in the car, certificate management through telematics and
  over-the-air software updates for new versions of ISO 15118.
- **Of everyone at once**: carmakers, OPCs, eMSPs and certificate authorities have to coordinate.
- **And there are several roots of trust**, which don't always recognise each other.

### AutoCharge: looks the same, isn't {#autocharge}

AutoCharge identifies the car by the identifier it sends to the charger, the EVCCID, often the MAC
address. It uses no certificates, which makes it simpler to get working. To the driver it looks just
like Plug & Charge. Only some OPCs offer it, and you have to turn it on in the app.

:::aviso
**AutoCharge is less secure.** Without certificates, any car that sends the same identifier is accepted. That's the trade-off you make when you turn it on in the app: more simplicity, less security.
:::

### Other ways to start a charge {#outras-formas-de-autenticar}

- **RFID or NFC card**, the most common.
- **App or QR code**, from the eMSP or the OPC.
- **Ad hoc payment** with a bank card.

### What the law says and who writes the rules {#normas-e-regras}

- **AFIR** (Regulation (EU) 2023/1804) requires interoperability and non-discriminatory access, and
  refers communication between the car and the charger to ISO 15118. [What AFIR requires of
  chargers](/afir/).
- **DL 93/2025, art. 6.º**, requires chargers installed or renewed to allow ad hoc and smart
  charging. The communication standards for bidirectional charging are AFIR's.
- **In Germany**, the application rule VDE-AR-E 2802-100-1 covers the management of ISO 15118
  certificates.
- **CharIN**, an association that promotes interoperability, publishes guides on the PKI.

## OCPP and OCPI: one talks to the charger, the other between back offices {#ocpp-e-ocpi}

They're two open protocols, and they complement each other. OCPP connects an OPC's back office to its
chargers. OCPI connects back offices to each other: the OPC's to the eMSPs' and to the hubs.

**Always state the version.** OCPP 1.6 or 2.0.1, ISO 15118-2 or -20: what holds for one may not hold
for the other. When someone tells you they support OCPP, ask which.

### OCPP, between the charger and the back office {#ocpp}

OCPP (Open Charge Point Protocol) is the open protocol between the charger and the OPC's central
management system, the CSMS, known as the back office. It's maintained by the Open Charge Alliance
(OCA).

- **Versions**: 1.6, the most installed; 2.0.1, also published as the IEC 63584 standard; and 2.1,
  which adds ISO 15118-20 and bidirectional charging.
- **What it does**: charger status, session authorisation, meter values, transactions, firmware
  updates, diagnostics and charging profiles (smart charging).
- **Why it matters**: without a common protocol, each charger maker would use its own, and the OPC
  would be locked in to one back-office supplier.

### OCPI, between back offices {#ocpi}

OCPI (Open Charge Point Interface) is the open protocol between back offices, from OPC to eMSP,
directly or through a hub. It's maintained by the EVRoaming Foundation, under a CC BY-ND 4.0 licence.

- **Versions**: 2.1.1, 2.2.1 and 2.3.0. Version 2.3.0 adds what AFIR asks for [charger
  data](/afir-nap/). There may already be a newer one: check with the EVRoaming Foundation.
- **What it does**: locations and real-time availability, authorisation tokens, sessions, CDRs (the
  charge detail records used for billing), tariffs, remote commands and smart charging.

### How they fit together {#como-se-juntam}

An OPC uses OCPP to manage its chargers and OCPI to connect to eMSPs and hubs. An example: an eMSP
sends a charging limit over OCPI to the OPC's back office, which passes it on to the charger over
OCPP.

## Batteries at the charger (BESS): more power than the grid gives {#bess}

A BESS (Battery Energy Storage System) is a fixed battery installed next to the charger. It charges
from the grid or from local renewable generation, and discharges into the chargers or into grid
services. With one, the charger delivers more power than the grid connection allows, without
upgrading the supply line.

### What it's for {#para-que-serve-um-bess}

- **Peak shaving.** Fast chargers draw power in peaks, high and unpredictable, and contracted power is
  paid for on those peaks. The BESS discharges at the peaks and lowers the power drawn from the grid.
  [How grid charges work when you operate a charger](/tarifas-de-acesso/).
- **Buying time.** It lets you install more chargers, or more powerful ones, without waiting for a
  grid upgrade, which can take months or years.
- **Supporting the grid.** It smooths out variations at the connection point and, depending on the
  market, can sell flexibility (frequency reserve, load shifting) or do price arbitrage.
- **Backup.** In some cases, it powers the charger during a grid outage.

How much it saves and how long it takes to pay back depends on the charging hub's usage profile, the
power tariffs and the grid services available in each country. Be wary of savings percentages or
payback periods quoted off the cuff. And to know whether a specific charger has a BESS, only the OPC
can confirm.

:::aviso
**An undersized BESS runs flat at the peaks** and stops cutting the power, just when it was needed. Sizing is a case-by-case study.
:::

## Myths and mistakes {#mitos-e-enganos}

- **"If my card has no agreement with that operator, I can't charge."** At a new or renewed public
  charger, you can: AFIR requires it to accept ad hoc payment, and that doesn't depend on roaming.
- **"OCPP and OCPI are alternatives."** They do different things. OCPP connects the charger to the
  back office, OCPI connects back offices to each other. An OPC uses both.
- **"With Plug & Charge, the card can stay at home."** Only if the car, the charger and the eMSP
  support it. Most sessions still use an RFID card or an app, so take it with you.
- **"AutoCharge is Plug & Charge by another name."** To the driver it looks the same, but AutoCharge
  uses no certificates. It recognises the car by its EVCCID and accepts any car that sends the same
  identifier.
- **"It supports OCPP, end of story."** The version is missing. 1.6 is the most installed; it's 2.1
  that adds ISO 15118-20 and bidirectional charging.
- **"A battery at the charger always pays for itself."** It depends on the usage profile, the power
  tariffs and the grid services in each country. And an undersized BESS runs flat at the peaks.
