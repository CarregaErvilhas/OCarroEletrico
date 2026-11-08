---
title: "The NAP: what data chargers must publish, and how it gets there"
description: "The National Access Point, plainly: what AFIR requires charge point operators to publish, how data reaches the EADME and how to read Portugal's NAP."
source: "afir-nap"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "5079bf9a60c10d09236b4277ec4cbe3405fb494800b0539dd1ee494edca02701"
updated: "2026-11-08"
---

Every Member State has a National Access Point (NAP), where charger data is published: where the
chargers are, which plugs they have, whether they're free and what they cost. AFIR requires charge
point operators (OPC, operador de pontos de carregamento), who run public and semi-public chargers,
to put that data there. In Portugal, the NAP is managed by IMT-IP and fed by MOBI.E, which collects
the operators' data as the EADME.

:::essencial
- **The NAP is an access point, not a central database**: each country has its own, and operators hand it the static and dynamic data of each charger (AFIR, art. 20.º).
- **In Portugal, the data goes through MOBI.E**: as the EADME, it collects it from operators and publishes it on IMT-IP's NAP, in DATEX II 3.3, with status and prices.
- **If you're an operator**: static data within 24 hours of a change, dynamic data within one minute, via DATEX II or OCPI. With your chargers on the MOBI.E platform, you have nothing to do until the transitional period ends.
:::

## Europe says publish, Portugal organises, MOBI.E runs it {#tres-camadas}

Regulation (EU) 2023/1804, AFIR, applies directly in every Member State. Art. 20.º requires charger
data to be published on a National Access Point.

Every rule about the NAP comes from one of three layers:

- **The European obligation**: AFIR.
- **Portuguese law**: DL 93/2025 and DL 155/2026.
- **How the NAP is actually run**: MOBI.E and IMT-IP.

AFIR sets minimum power per TEN-T network node and deployment deadlines. For exact deadlines,
distances and power levels, always go to the official version: the
[text of AFIR](https://eur-lex.europa.eu/eli/reg/2023/1804/oj) and the decree-laws. The rest of the
regulation, and how it applies in Portugal, is in
[what AFIR requires of the charging network](/afir/).

## What a NAP is, and what it isn't {#o-que-e-um-nap}

A National Access Point is each Member State's central platform for publishing data on alternative
fuels infrastructure, including charging points. The idea didn't start with AFIR. It already existed
under the ITS Directive 2010/40/UE and its delegated regulations (MMTIS, RTTI, SRTI, SSTP), for
mobility data in general. AFIR extended it to alternative fuels, above all to electric charging
(art. 20.º).

- **Each country has its own.** There is no single European NAP.
- **It's an access point, not a centralised database.** It aggregates and makes available the data
  that operators, and other bodies, hand it.
- **It serves three purposes**: drivers find available chargers; authorities monitor how the network
  is being rolled out; and eMSPs, which sell charging at chargers from many operators, offer
  integrated charging services.

If you only want to find a charger and plug in, what you need is in
[charging on the road](/carregamento-publico/).

### CEAP: the European gateway, with no data of its own {#ceap}

AFIR also provides for a Common European Access Point (CEAP), hosted by the
[European Alternative Fuels Observatory](https://alternative-fuels-observatory.ec.europa.eu) (EAFO).
It's a gateway for discovering the data published on each national NAP. It stores no data: it points
whoever is looking to the information held on the NAPs. It is due to be set up by 31 December 2026.

## What an operator has to put on the NAP {#o-que-os-opc-publicam}

Operators running public or semi-public chargers must make two kinds of data available, via API,
through the national NAP (AFIR, art. 20.º). The obligation applies from 14 April 2025, for the
Member States with the applicable deadlines.

- **Static data**: the charger's location; the number of connectors; spaces for people with reduced
  mobility; contact details; opening hours; the operator code; connector types; current type (AC or
  DC); the maximum power of the charger and of the EVSE, the charging point; and compatible vehicle
  types.
- **Dynamic data**: operational status (in service or out of order); real-time availability; the ad
  hoc price, the one paid by someone charging without a contract; and whether the electricity is
  100 % renewable.

The publishing can be done by the operator itself or by an intermediary, such as a charger
management platform. The responsibility is the operator's. In Portugal, MOBI.E publishes the static
inventory and the dynamic status, with prices, on the NAP.

### IDRO and IDACS: who's who in the data {#idro-e-idacs}

AFIR requires each Member State to appoint an ID Registration Organisation (IDRO). The IDRO manages
the unique identification codes of operators and eMSPs, the IDACS. These codes go into the data
published on the NAP and say, with no room for doubt, who runs each charger and who provides
mobility services.

The list of IDROs for each country and the registered codes are published on each national NAP, or
in associated registers. In Portugal, this function sits with the DGEG, the energy authority, and
within the MOBI.E structure.

## In Portugal, the NAP is IMT-IP's and the data comes from MOBI.E {#como-funciona-em-portugal}

The [Portuguese NAP portal](https://nap-portugal.imt-ip.pt) is managed by IMT-IP and serves MOBI.E's
data at two addresses:

- **Static inventory**: `https://pgm.mobie.pt/integration/nap/evChargingInfra`, about 190 MB, in
  DATEX II 3.3 XML.
- **Dynamic status and prices**: `https://pgm.mobie.pt/integration/nap/evActualStatus`, about 40 MB.

Behind these files, MOBI.E has two roles, and the law has two models:

- **MOBI.E is the EADME**, the electric mobility data aggregator (Entidade Agregadora de Dados para a
  Mobilidade Elétrica), under DL 93/2025, with a transitional regime until 31 December 2027.
  According to MOBI.E, its work as the EADME is supervised by the AMT, the mobility and transport
  authority (Autoridade da Mobilidade e dos Transportes).
- **MOBI.E is still the EGME**, the electric mobility managing body, until 31 December 2027. It
  manages the network platform and charges the EGME tariff, set by ERSE, the energy regulator. That
  isn't the TAR, the [access tariff for the electricity grids](/tarifas-de-acesso/).
- **Two market models live side by side.** DL 93/2025 brought a new model, with a direct contract
  with the operator or with an eMSP. DL 155/2026 extended the transitional period to 31 December 2027
  and, until then, keeps the old model, in which a CEME (electricity retailer for electric mobility)
  sells the energy on the MOBI.E network.
- **Since September 2026**, according to MOBI.E, its MOBI.DATA area shows real-time availability for
  chargers across the whole public network. That includes operators that weren't connected to
  MOBI.E, as they finish integrating with the EADME.

## Sending data to the EADME: what, when and how {#como-os-opc-enviam-os-dados}

Portaria n.º 31/2026/1 tells the EADME to set the technical rules. There's already one: Technical Rule n.º
1/EADME/2026 (Regra Técnica), approved and published on 18 May 2026, after public consultation.
According to the rule itself (point 11), it applies 30 working days after publication.

- **What data**: the static and dynamic data of AFIR art. 20.º. The EVSE status combines
  operational status and availability in a single field. The ad hoc price comes with all its
  components (point 6).
- **How often**: static data within 24 hours of a change; dynamic data within one minute (point 7).
- **How, via DATEX II**: two XML addresses with no authentication, one for static data and one for
  dynamic data.
- **How, via OCPI 2.2 or 2.2.1**: in the operator role, with the Versions, Credentials, Locations and
  Tariffs modules. Static data that OCPI doesn't have is filled in on the EADME platform, or sent in
  non-standard fields defined by the EADME (point 8 and annex I).
- **During the transition**: if your chargers are on the MOBI.E platform, you don't have to do
  anything during the transitional period. The EADME converts to DATEX II what it already receives
  via OCPP and OCPI. When the period ends, you have to choose one of the two methods above (point 10).

:::aviso
**Faulty data is an offence.** Incomplete, wrong or late data is a minor offence (DL 93/2025, art. 13.º, n.º 1, c), and art. 34.º, n.º 1, a)), as the rule points out in point 9. If a management platform sends the data for you, the responsibility is still yours.
:::

:::aviso
**The rule says 2026, the law says 2027.** The technical rule puts the end of the transitional period on 31 December 2026, because it was written before DL 155/2026, which extended it to 31 December 2027. If a decision of yours depends on this date, confirm it with the EADME.
:::

## Who can use the data, and where the official lists are {#acesso-e-licenca}

The Portuguese NAP's addresses are published under open-access licences. The terms are on IMT-IP's
NAP pages.

- **Operators' tariffs** on MOBI.E are published as CSV on the MOBI.E website.
- **The up-to-date list of registered operators** is at the DGEG. So is the list of CEMEs, while the
  transitional regime lasts.
- **For lists of NAPs, operators or eMSPs in other countries**, the authoritative source is the
  national IDRO registers. There is also a
  [list of European NAPs for charging](https://evnapdata.eu/naps).
- **For a charger's price and status right now**, use the tools at the end of the page: they read
  MOBI.E's NAP.

## DATEX II: the common language of NAPs {#datex-ii}

DATEX II is the European standard (CEN/TS 16157) for exchanging traffic and mobility data. Under AFIR,
it's the reference format for publishing alternative fuels infrastructure data on NAPs. It's what
makes that data interoperable between Member States.

### Two datasets: what stays put and what changes {#estrutura-de-dados}

An AFIR NAP publishes two datasets for each charger:

- **Static inventory** (`evChargingInfra`, in Portugal): sites, charging points (EVSE) and
  connectors, with identifiers, coordinates, operator, power, plug types, opening hours, contacts and
  accessibility. It rarely changes.
- **Dynamic status and prices** (`evActualStatus`, in Portugal): operational status, real-time
  availability and ad hoc price, per point. It's updated often.

In Portugal, MOBI.E's two addresses are DATEX II 3.3 XML, with the namespaces
`energyInfrastructure`, `facilities`, `locationReferencing`, `locationExtension`, `commonExtension`
and `common`. Each record uses stable identifiers (site, EVSE, connector) and continuous power
(`max_power_w`, `voltage` and `max_current`), not power classes.

AFIR's power classes (annex III) are the ones used for reporting: up to 22 kW is normal power, above
that is high power. Each country may also expose other formats, such as OCPI, GeoJSON or CSV, but
DATEX II is the common denominator.

### How to read a NAP {#como-se-le-um-nap}

- **Format**: XML (DATEX II) or, depending on the country, OCPI, GeoJSON, CSV or JSON.
- **Access**: open, with a key, or under a formal contract, depending on the NAP.
- **Typical hierarchy**: site (the location) → EVSE (the charging point) → connector.

The [documentation and schemas for version 3](https://datex2.eu) are on the DATEX II website. There is also the
[DATEX@NAPs portal](https://datex2.naps.inqms.tamtamresearch.com/naps-browser/nap/index.html).

## Myths and mistakes {#mitos-e-enganos}

- **"There's one European NAP with the data for every charger."** There isn't. Each Member State runs
  its own. The CEAP, provided for in AFIR, is a gateway to the national NAPs and stores no data.
- **"The NAP is a central database."** It's an access point: it aggregates and makes available what
  operators hand it.
- **"The NAP was born with AFIR."** It already existed under the ITS Directive 2010/40/UE, for
  mobility data in general. AFIR extended it to electric charging (art. 20.º).
- **"If the management platform publishes for me, the responsibility is theirs."** It's the
  operator's, whoever does the publishing (AFIR, art. 20.º).
- **"The EGME tariff is the TAR."** It isn't. The EGME tariff is the one MOBI.E charges as the
  platform's manager, set by ERSE. The TAR is the access tariff for the electricity grids.
- **"The transitional period ends on 31 December 2026."** That's what the EADME's technical rule
  said, written before DL 155/2026. The deadline moved to 31 December 2027.
