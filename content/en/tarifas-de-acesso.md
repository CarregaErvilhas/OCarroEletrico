---
title: "Access tariffs: an unused charger still pays for the grid"
description: "On MOBI.E, the TAR ME charges per kWh only. Off it, and for everyone from 2028, power enters the bill. What changes for operators and how to cut the cost."
source: "tarifas-de-acesso"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "1ac5aec1a0ebd9b0b891e75398b66be8912bb3ad5e5285d617804a379f7bac5f"
updated: "2026-11-08"
---

At MOBI.E chargers, the grid access tariff (TAR, tarifa de acesso às redes) is charged per kWh only,
and the driver pays it, until 31 December 2027. Off MOBI.E, and for everyone from 1 January 2028, the
OPC (the charge point operator) pays the normal TAR, which has power terms. A fast charger with little
use ends up paying for the grid even on days when nobody charges.

:::essencial
- **On MOBI.E**, the TAR ME has per-kWh prices only: a charger that's hardly used doesn't pay for the power it has.
- **On BTE and MT, off MOBI.E**, a single quarter of an hour at full power sets the contracted power for the next 12 months.
- **The grid's fixed cost moves from the driver to the OPC**, who has to recover it in the price: with few charging sessions, that's a lot per kWh.
:::

## Before you do the maths, answer five questions {#antes-de-fazer-contas}

The answers tell you which TAR your charger pays and what pushes it up.

1. **Is the charger connected to MOBI.E?** And if so, will it leave before the end of the transition period?
2. **What voltage level is it connected at?** BTN (normal low voltage, up to 41.4 kVA), BTE (low voltage above 41.4 kVA) or MT (medium voltage, with its own transformer substation).
3. **What power do the chargers have**, and is there power management or a battery (BESS)?
4. **How many kWh do you sell a month, and at what times?** Consumption in peak hours weighs heavily.
5. **Does the charger have a connection of its own**, or is it in an installation with other loads (a shop, a condominium, a company), perhaps with a sub-CPE?

## What the TAR is, and what it isn't {#o-que-e-a-tar}

The grid access tariff pays for the use of the transmission and distribution grids and for energy
policy costs (CIEG). ERSE, the energy regulator, sets it every year, in December, for the following
year and by voltage level (Regulamento Tarifário, the Tariff Regulation). The ORD, which runs the
distribution grid, bills it to the electricity supplier (comercializador), who passes it on in the
customer's bill.

**The TAR is only the grid part.** On top of it, the OPC pays for the energy, the supplier's margin and
taxes. And since prices change every year, always check which year the price you're working with is
from.

It has up to four terms, depending on the voltage level (Regulamento Tarifário, arts. 44.º, 45.º, 52.º
e 54.º):

| Term | BTN | BTE and MT |
|---|---|---|
| Contracted power (per day) | The tier (escalão) chosen in the contract | **The maximum power drawn over the last 12 months**, including the billing month |
| Peak-hours power (per kW and per day) | None | Energy in peak hours divided by the peak hours in the period |
| Active energy (per kWh, per time period) | Yes | Yes |
| Reactive energy | No | Yes |

On BTE there are no tiers: you can contract any power above 41.4 kVA. But the contracted power can't
exceed the connection's requested power (potência requisitada), according to the E-REDES connections
manual.

### The quarter of an hour that rules {#potencia-tomada}

On BTE and MT, what you pay as contracted power is the maximum power drawn. And power drawn
(potência tomada) is the highest average active power in any uninterrupted 15-minute period (Regulamento Tarifário, art.
44.º). What counts is the average over those 15 minutes, not the instantaneous peak: a short session
weighs what it drew, on average, in that quarter of an hour.

:::aviso
**One quarter of an hour stays on the bill for a year.** On BTE and MT, a single 15-minute period at full power in a month sets the contracted power for the next 12 months.
:::

### Peak hours: few and expensive {#horas-de-ponta}

On the mainland's weekly cycle, peak hours are 5 h per working day in winter time and 3 h in summer
time, with no peak at weekends. On the daily cycle they're 4 h a day, every day (Regulamento
Tarifário, Quadro 8). The price per kW of peak-hours power is much higher than that of contracted
power.

## On MOBI.E: the grid is paid per kWh {#na-mobi-e}

At chargers connected to MOBI.E, Portugal's public charging network, the energy for charging pays a
TAR of its own, the electric mobility TAR (TAR ME). It has **per-kWh prices only**, as a two-period or
three-period option, with no contracted power and no peak-hours power (Regulamento Tarifário, arts.
57.º e 58.º).

- **How it gets to per kWh.** ERSE converts the power prices of the BTN TAR into per-kWh prices, per
  time period, based on the consumption profile of the electric mobility network. The reason,
  according to ERSE: the load, the cars, varies in time and space.
- **There are four variants**, depending on the voltage level of the charger's connection: BT, MT, AT
  and MAT. All start from the BTN TAR, and the higher-voltage ones take out the use of grids they
  don't use.
- **Who bills whom.** The ORD bills the TAR ME to the supplier that supplies the CEME (Regulamento n.º
  7/2026, art. 10.º). The CEME, the company that sells energy to the driver on MOBI.E, passes it on in
  the driver's invoice, separately from the OPC's tariff.

**What this gives the OPC:** the fixed grid cost of a MOBI.E charger is paid by the driver, per kWh. A
fast charger that's hardly used doesn't pay for the power it has. There's only a grid cost when there
are charging sessions.

### It has an end date, and no successor in sight {#tem-prazo}

The TAR ME only applies during the transition period, which DL 155/2026 extended to 31 December 2027.
And only to CEME deliveries at chargers that stay connected to MOBI.E, according to ERSE. DL 93/2025
doesn't provide for a TAR of its own for chargers off MOBI.E, and as of 6 November 2026 we found no
ERSE proposal to that effect.

## Off MOBI.E: power enters the bill {#fora-da-mobi-e}

Off MOBI.E, the OPC buys the charger's electricity from a supplier, like any consumer installation (DL
93/2025, art. 9.º), and pays the normal TAR for its voltage level. That's already the case today for
anyone who takes their charger off MOBI.E. From 1 January 2028, it's the case for everyone.

**On BTN**, for AC chargers up to 41.4 kVA in total, the power term is the one for the chosen tier.
It's a known fixed cost, and you lower it by changing tier.

**On BTE and MT**, for DC chargers and car parks with many chargers, both power terms come in:

- **Contracted power**: the highest quarter of an hour of the last 12 months. A 150 kW charger that
  once reaches 150 kW as a 15-minute average pays for 150 kW a day for a year, sessions or not.
- **Peak-hours power**: each kWh sold in those hours weighs heavily, because the price per kW is
  several times that of contracted power.

The result: the grid's fixed cost moves from the driver, who paid it per kWh, to the OPC, who pays it
per kW. The OPC has to recover it in the price it charges. At a charger with few sessions, that's a
lot per kWh.

## And the driver? Always pays, only where changes {#e-o-condutor}

The TAR isn't just a matter for those who run or own chargers: it always ends up in the price of charging. On
MOBI.E, it comes on the CEME's invoice, separately from the OPC's tariff. Off MOBI.E, you don't pay it
separately: it's inside the price of the OPC or the eMSP, the company that sells you charging by card
or app at chargers from several OPCs. And at a charger with few sessions, after 2027, the grid's fixed
cost has to fit into the price of each kWh.

How you pay for charging at a public charger is in [charging on the road](/carregamento-publico/).

## The maths for a little-used charger {#a-conta}

To see how much the normal TAR weighs at a charger on BTE or MT, do the maths for a month of 30 days,
with that year's prices:

1. **Fixed term** = contracted power (kW) × contracted power price × 30.
2. **Peak-hours power** = (kWh in peak hours ÷ peak hours in the month) × peak-hours power price × 30.
3. **Energy** = kWh in each period × active energy price for that period.
4. **Grid cost per kWh** = the sum of the three ÷ kWh sold in the month.

On MOBI.E, the maths is shorter: kWh in each period × TAR ME price for that period.

The fixed term doesn't depend on kWh. Hence the rule: **below a certain monthly consumption, the
normal TAR costs more per kWh than the TAR ME, and the less use, the worse**. Above that consumption,
the normal TAR can even come out cheaper, because active energy on BTE and MT costs less per kWh than
the TAR ME.

This year's TAR prices, published by ERSE, and a worked example with them for a rapid charger, each
with its source and the date it was checked:

{{factos kind=mercado series=tar}}

The maths is an estimate, and it's only as good as its assumptions: the peak power, the kWh per
month and the share of consumption in peak hours. The real figure depends on the cycle, the tariff
option and the supplier. And it doesn't tell you whether to invest: it shows what weighs and what
changes it. To do it with your own numbers, use the tools at the end of the page.

### Who feels the change most {#quem-mais-sente-a-mudanca}

- **Fast chargers in places with little passing traffic.**
- **Municipal or coverage networks**, installed to meet targets rather than demand.
- **Car parks with many chargers on a single BTE or MT connection**, which are rarely all in use.

## Six ways to cut the cost {#formas-de-baixar-o-custo}

Each one works on a different part of the bill. Which one pays off depends on the charger, its use and
its connection.

- **Limit power with load management** (OCPP, smart charging). What counts is the 15-minute average
  at the connection. So limiting the car park's total lowers the contracted power for the next 12
  months.
- **Shave the peaks with a battery (BESS).** The battery supplies the peaks and the grid sees a lower
  power.
- **Stay out of peak hours.** Higher prices or limited power in those hours lower the peak-hours
  power.
- **Stay on MOBI.E until the end of the transition period**, on 31 December 2027, while the TAR ME
  exists.
- **Join the charger to an installation with other loads**, a supermarket, for example. The fixed term
  is shared, but the charger's peak adds to the installation's, and the power drawn is the total's.
- **On BTN, choose the tier by actual use**, not by the chargers' maximum power.

How load management, OCPP and stationary batteries work is in [charging
technology](/tecnologia-de-carregamento/).

:::aviso
**Lowering the power in the contract, on its own, doesn't help.** Moving to a lower tier or a lower power without limiting the chargers' power achieves nothing. On BTE and MT, the contracted power goes back up with the first peak.
:::

## Sub-CPE: the power term follows it {#sub-cpe}

A sub-CPE is an internal delivery point, with its own code, inside an installation already connected
to the grid. It doesn't escape the power term.

- **It pays every term of the TAR**, except reactive energy, at the voltage level of the installation
  it sits in (Regulamento n.º 7/2026, art. 99.º).
- **On BTE and MT**, the contracted power is the maximum power drawn measured at the internal point.
  **On BTN**, it's the tier contracted with the sub-CPE's supplier, which can't be higher than the
  main installation's.
- **The main installation pays the TAR on consumption by difference**, the so-called virtual metering
  point. On BTN, the main installation sits on the tier equal to or just above the maximum power drawn
  at that virtual point over the last 12 months (art. 98.º).

[Who asks for a sub-CPE, how, and what it costs](/sub-cpe/).

## Myths and mistakes {#mitos-e-enganos}

- **"The TAR ME ends at the end of 2026."** No. ERSE's 2025 documents talk of a transition period until
  31 December 2026, but DL 155/2026 extended it to 31 December 2027.
- **"A sub-CPE only pays for energy and peak-hours power."** That was ERSE's 2025 proposal. The
  approved text didn't end up that way: the internal point pays every term of the TAR, except reactive
  energy (Regulamento n.º 7/2026, art. 99.º).
- **"The TAR is what the charger's electricity costs."** It's only the grid part. Add the energy, the
  supplier's margin and taxes.
- **"A short session at 150 kW sets 150 kW for the year."** What counts is the 15-minute average, not
  the instantaneous peak (Regulamento Tarifário, art. 44.º). A full quarter of an hour at full power,
  though, is enough.
- **"I lower my contracted power and pay less."** Only if you also limit the chargers' power. On BTE
  and MT, the first peak pushes it back up.
- **"After 2027 there'll be a TAR of its own for chargers off MOBI.E."** DL 93/2025 doesn't provide for
  one, and as of 6 November 2026 we found no ERSE proposal to that effect. If someone tells you about
  one, ask for the source.
- **"The driver always pays the TAR separately."** Only on MOBI.E, on the CEME's invoice. Off it, it's
  inside the price of the OPC or the eMSP.
