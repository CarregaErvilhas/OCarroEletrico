---
title: "A contract just for the car: when a sub-CPE pays off"
description: "A sub-CPE gives a charger its own meter, code and contract, with no second connection. It's optional. Who asks, how, what it costs, what changes in a building."
source: "sub-cpe"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "184a1f4994c6fd4a93d4414ede84b53d0415576c073735c46b148c0e16b95ae3"
updated: "2026-11-08"
---

A sub-CPE is a meter with its own code and electricity contract for a charger, inside the
installation that's already there: the house, the apartment building, the company. It's optional,
and it pays off when you want to choose the charger's supplier and power and get a separate bill. If
all you want is to split the bill with the condominium (condomínio), an agreement between the parties
is enough, and it's often the simplest way.

:::essencial
- **It's optional**: it isn't required to charge at home or in a building, and it won't become so in 2027.
- **It's requested by whoever has the charger (the DPC) or runs it (the OPC)**, with written authorisation from the installation's account holder, which in a building is, as a rule, the condominium.
- **In a building with chargers on MOBI.E**, a sub-CPE forces every charger in that installation off the platform, not just yours.
:::

## A delivery point inside another {#o-que-e}

The official name is **internal delivery point** (ponto de entrega interno): a metering and supply
point inside an installation that's already connected to the grid, with its own meter, its own code
and its own electricity contract (DL 93/2025, art. 24.º, n.º 3; Regulamento n.º 7/2026, art. 4.º, n.º
2, alínea n)). The code the distribution grid operator (ORD) gives it is the sub-CPE, from CPE (código
de ponto de entrega), the code that identifies an installation on the grid. That's what ERSE, the energy regulator, and the grid operators call it, and it's
the name you'll find on the paperwork.

- **It sits inside the existing installation**, downstream of its meter. The physical connection to
  the grid is still just one, the main CPE's.
- **It's for separating consumption**, in this case the chargers', when the installation isn't only
  for electric mobility: a house, a building, a company, a shopping centre.
- **What you gain is contractual independence**: choosing the charger's supplier, contracted power,
  cycle and tariff option, without mixing them with the house's or the condominium's.

It came with the new electric mobility regime, to give free choice of supplier to the OPC or DPC
feeding chargers from someone else's installation. The rules have been in force since 6 July 2026:
Regulamento n.º 8/2026 and chapter II of title III of Regulamento n.º 7/2026 were published on 6
January 2026 and took effect six months later.

## Not a second connection, and no extra power {#o-que-nao-e}

- **It isn't a second service line.** Anyone who wants an independent grid connection asks the ORD
  for a new CPE, with building work and power requested from the grid. That's something else, more
  expensive and slower.
- **It doesn't give more power.** A sub-CPE can't have a power level above that of the installation
  it sits in (Regulamento n.º 7/2026, art. 99.º). If the main connection has no spare power, the way
  forward is an upgrade, not a sub-CPE.
- **It isn't the virtual CPE.** That's the code the ORD uses to aggregate electric mobility
  consumption in the EGME model, the EGME being the body that runs the MOBI.E platform (Regulamento
  n.º 7/2026, art. 4.º, n.º 2, alínea g)). It has no meter or contract of its own, and doesn't split
  bills.
- **It isn't a MOBI.E meter, nor a CEME's**, the company that sells you energy on the network by card
  or app. The sub-CPE's meter is the same kind of equipment as the grid connection's, and its data go
  into the electricity sector's billing.
- **It doesn't work in provisional or temporary installations**, like the supply to a building site
  (Commercial Relations Regulation, Regulamento de Relações Comerciais or RRC, art. 131.º, n.º 4).

## Three ways to separate the car's bill {#tres-modelos}

First find out which model your charger is on, because the rules change with it. According to ERSE,
in its report on Public Consultation n.º 135, the choice belongs to the installation's account holder.

1. **Charger connected to MOBI.E.** Charging goes through the platform and a CEME's card. It's the
   previous regime's model, kept until 31 December 2027 (DL 93/2025, art. 44.º, as amended by DL
   155/2026). It only exists while the transition period lasts.
2. **Agreed model** (modelo acordado). The consumption stays on the main installation's contract and
   the parties settle the cost between themselves, often using the charger's own meter. No new
   electricity contract, no ORD involvement. It's what many condominiums and companies do today.
3. **Sub-CPE.** An ORD meter, its own supply contract and its own bill.

The big difference is who pays whom. In the agreed model, the money for the energy passes from one
person to another by private agreement. With a sub-CPE, there are two customers of the electricity
sector, each with their own supplier. ERSE treats the sub-CPE as an option, not a mandatory
replacement for the agreed model.

### When it pays off, and when an agreement is enough {#quando-compensa}

- **It pays off when you want a contract just for the charger**: your supplier, your power, your
  cycle and your tariff option, with a separate bill. A company that installs its own wallbox at an
  employee's home is that charger's DPC, and can request the sub-CPE in its own name so the
  electricity bill is in its name. How that works is in [charging company cars](/empresas-e-frotas/).
- **An agreement is enough when you only want to split the bill**, within a household or a building.
  The agreed model is still valid, and it's often the simplest solution.
- **It doesn't fix a lack of power.** That takes an upgrade.
- **In a building with chargers on MOBI.E, it weighs more.** A sub-CPE forces all of them off the
  platform, as explained [under the building section](/sub-cpe/#no-condominio).

## Who asks, and who has to say yes {#quem-pede}

You don't ask as an owner in the building: the request belongs to the charger's OPC or DPC (Guia de Medição, Leitura e Disponibilização de Dados, ERSE's metering and
data guide, or GMLDD, art. 11.º-A, n.º 1). If the wallbox is yours, you're its DPC and you can be
the one who asks.

- **With express authorisation from the account holder** of the installation connected to the public
  grid (n.º 2). In a house, that's whoever holds the contract. In a building it's, as a rule, the
  condominium, through the common services contract. In a company, it's whoever holds the electricity
  contract.
- **Right after the main meter.** The internal meter goes immediately downstream of the meter of the
  installation the charger connects to, and can't be in series with other internal meters already
  there (n.º 3). In a building, this is decided by the wiring diagram, not by conversation: first
  check [which board the charger is fed from](/carregar-em-casa/#de-que-quadro-sai-a-eletricidade).
- **The ORD has to get in.** It needs access to the inside of the installation to fit and read the
  meter (n.º 7).

If there's a dispute with the condominium or the installation's account holder, get legal support.

## How to ask for one, in eight steps {#como-se-pede}

The process runs at the ORD, but whoever asks is the one who drives it. Follow this order.

1. **Check that it fits.** The installation is permanent, isn't only for electric mobility, and has
   a charger. The internal meter goes downstream of the main one, not in series.
2. **Get written authorisation** from the account holder of the grid-connected installation. Without
   it, the request goes nowhere.
3. **Submit the request to the ORD**, on its online portal or at a service point. At E-REDES, the grid
   operator, it's called a submetering request (pedido de submedição, PSUB). The documents come
   right after this list.
4. **Pay the regulated price** for the request and the meter. According to E-REDES, it's calculated
   from the voltage level of the secondary installation.
5. **The ORD creates the sub-CPE and fits the meter**, within two months of the request at most, as
   long as it has access to the installation (GMLDD, art. 11.º-A, n.º 7). According to E-REDES, the
   secondary installation gets a new code.
6. **Certify the installation** with the DGEG, the energy authority, or a certification body. It's
   mandatory, and it's up to you.
7. **Sign a supply contract** with the supplier the sub-CPE's holder chooses. The contract stays at
   the same voltage level as the main installation.
8. **Up and running**: readings every quarter of an hour, data for each contract holder and a
   separate bill for the sub-CPE.

Two months is the only deadline the law sets, and it's only for the meter. From step 3 to step 6, not
everything is the ORD's: adapting the installation and certifying it are up to whoever asks, and
they're usually what holds things up. The contract with the supplier runs separately too.

### What to bring to the request {#documentos}

According to E-REDES's submetering conditions, the usual paperwork is:

- identification of whoever is asking, and the main installation's CPE;
- the maximum power wanted and the voltage level of the submetering connection;
- the installation's single-line diagram;
- the main installation holder's statement authorising the internal delivery point;
- photos of where the meter will go.

Above 41.4 kVA, add a technical description of the equipment, including the remote-controlled
cut-off. This is E-REDES's practice and paperwork, not law, and it can change.

## What it costs: the meter has a regulated price, the rest is a quote {#quanto-custa}

There are three parts: the meter, the work and the energy. Nobody should quote you the meter's price
from memory: it's regulated, approved every year and depends on the voltage level.

- **The meter** has a regulated price per unit, approved every year by ERSE, covering purchase,
  installation, operation and maintenance. The ORDs propose the amount by 15 September. Without a
  proposal, the self-consumption price for generation or storage equipment applies (Regulamento n.º
  7/2026, art. 100.º). Ask the ORD for the figure at your voltage level.
- **The work**: adapting the installation, certification, the certified technician and, if needed,
  the cut-off equipment. Each case gets its own quote.
- **At E-REDES**, according to E-REDES itself, the metering equipment becomes the property of whoever
  asked and is renewed after ten years. During that time, maintenance is E-REDES's. It's each
  operator's own practice: check with the ORD in your area.
- **The energy** is paid at the sub-CPE contract's price, plus the grid access tariffs (tarifas de
  acesso às redes, TAR). As anywhere in the electricity sector, it isn't just the kWh: the power
  charge counts too. The internal point pays every TAR component except reactive energy (Regulamento
  n.º 7/2026, art. 99.º). The detail is in [grid access tariffs](/tarifas-de-acesso/).

### You don't pay for the energy twice {#sem-duplicar}

The charger's energy is no longer billed on the main contract and moves to the sub-CPE's. The ORD
works out the main installation's consumption by difference, at what's called the virtual metering
point (Regulamento n.º 7/2026, art. 98.º). What's new is a fixed charge on the sub-CPE's bill. On the
other hand, the main installation's contracted power can go down, if the consumption left there drops
to a lower power level.

## In a building: who signs, and what changes for the neighbours {#no-condominio}

- **The management authorises it.** The main contract's holder is, as a rule, the condominium,
  through the common services contract. The building's management signs the authorisation, and the
  owners' meeting should agree, because the sub-CPE creates a new meter inside a shared installation.
  As for the majority needed, ask the management. If there's a dispute, get legal support.
- **It doesn't replace the notice to install the charger.** A sub-CPE doesn't do away with the prior
  notice to the management to install the charger in the parking space (DL 93/2025, art. 23.º).
  They're two separate procedures: one is the right to install the charger, the other is separating
  the consumption. The first is covered in [how to notify the building](/carregar-em-casa/#comunicacao-previa).
- **A building can have several sub-CPEs**, one per charger or one per group of chargers, as long as
  each meets the technical conditions. What can't happen is an internal meter in series with another.
- **The agreement still works.** If the condominium doesn't want to touch the common services
  contract, the agreed model is still valid, and it's often the simplest solution. ERSE says
  explicitly that joining the sub-CPE scheme is optional.

:::aviso
**Chargers on MOBI.E in the building? They all come off.** A sub-CPE forces every charger in the installation off the EGME's platform, not just the requester's (Regulamento n.º 7/2026, art. 101.º, n.º 2). In a building where several owners are on MOBI.E, this affects the neighbours.
:::

At the end of the transition period, on 31 December 2027, every charger comes off the platform anyway
(Regulamento n.º 7/2026, art. 101.º, n.º 4, and DL 93/2025, art. 44.º, as amended by DL 155/2026). A
charger connected to MOBI.E is the previous regime's model, and it only lasts until then. How it
works until that date is in [on MOBI.E or not](/carregar-em-casa/#ligado-a-mobi-e-ou-nao).

## Bills, data and solar panels {#faturacao-dados-e-autoconsumo}

- **Grid access tariffs**: a sub-CPE pays the same prices as any delivery point, except for reactive
  energy, which isn't measured at the internal point (Regulamento n.º 7/2026, art. 99.º; GMLDD, art.
  97.º-A, n.º 8). The voltage level and type of supply are those of the installation the sub-CPE sits
  in.
- **Power in BTN** (normal low voltage, baixa tensão normal): the sub-CPE's power level can't be
  higher than that of the installation it sits in. And the main installation's contracted power can't
  be lower than the highest power level among its internal points (Regulamento n.º 7/2026, art.
  98.º).
- **Data**: balances are per quarter of an hour. The ORD gives the main contract's holder the data of
  the connection point and of the virtual metering point and, on request, those of each internal
  point. To each sub-CPE's holder, it gives the data of their own meter (GMLDD, art. 97.º-A, n.ºs 5 e
  6).
- **Quality of service**: the internal point doesn't count as a delivery point for continuity of
  service compensation. The compensation limit is calculated on the annual consumption of the grid
  connection point, without subtracting the internal consumption (Quality of Service Regulation,
  Regulamento de Qualidade de Serviço, art. 2.º, alínea kk), and art. 102.º, n.º 5).
- **Self-consumption**: internal points can take part in self-consumption like any delivery point
  (Self-Consumption Regulation, Regulamento do Autoconsumo, art. 7.º). Whatever is fed in at the
  internal point counts as feeding into the grid (GMLDD, art. 97.º-A, n.º 4). During the transition
  period, chargers connected to MOBI.E remain excluded from self-consumption (GMLDD, art. 128.º-A).
- **Outages**: the sub-CPE depends on the main CPE. An interruption on the main one also cuts the
  charger, and the sub-CPE has no power of its own beyond what the main connection can deliver.

### A debt on the sub-CPE can reach the common services {#falta-de-pagamento}

If the sub-CPE's bills go unpaid, the interruption rules of the Commercial Relations Regulation
apply, as at any delivery point. So the ORD must be able to cut off the internal point, preferably
remotely.

Installations that already existed when the regulation came into force have up to **12 months** to
adapt to this, and the responsibility lies with the sub-CPE's holder. There's no clear deadline: the
article only takes effect from 6 July 2026 and how to count isn't defined. Check with the ORD.

:::aviso
**Within that period, the charger's debt can cut off the main installation.** If the ORD can't cut off the internal point for reasons attributable to the customer, it can cut off the main installation, with the regulatory prior notice. In a building, that means a sub-CPE debt can affect the common services. Without adapting in time, the installation can no longer have an internal delivery point (Regulamento n.º 7/2026, art. 103.º).
:::

## Myths and mistakes {#mitos-e-enganos}

- **"I'll get a sub-CPE to have more power at the charger."** It doesn't work that way. Power is still
  limited by the main connection (Regulamento n.º 7/2026, art. 99.º). More power takes an upgrade.
- **"The sub-CPE is the MOBI.E meter."** It isn't. It's a delivery point of the electricity sector,
  with its own CPE.
- **"From 2027, a sub-CPE is mandatory."** It isn't. ERSE frames it as an option. What ends on 31
  December 2027 is the transition period of the EGME model.
- **"The charger's own meter is enough to split the bills."** It depends on what you want to split.
  To share the cost within a household or a building, the agreed model is enough. To have an
  electricity contract of its own, you need the sub-CPE.
- **"An owner asks E-REDES for the sub-CPE in their own name."** No. The request comes from the OPC or
  the DPC, with authorisation from the installation's account holder, which in a building is the
  condominium (GMLDD, art. 11.º-A, n.ºs 1 e 2). If the wallbox is yours, you ask as its DPC.
