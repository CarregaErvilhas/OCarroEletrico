---
title: "Socket or wallbox: what the electrician has to get right"
description: "Dedicated circuit, breaker, RCD, sockets and which board feeds each space in a building: the DGEG technical guide's rules, so you know what to ask and check."
source: "instalacao-eletrica"
sourceCommit: "7e5bac3b6622e0bb1f1aa676e581bfd4658adc16"
sourceSha: "9aefd53ef7b01b68a1325bda3efd598f1f20c60d5e963c935e8edb2bc3597a34"
updated: "2026-11-08"
---

To charge at home or in your building's garage, the car needs a circuit of its own, with its own
circuit breaker and residual-current device, coming from the right board for the space. That's what
the Technical Guide from the DGEG, the energy authority, asks for: it explains how to apply the
RTIEBT, the technical rules for low-voltage electrical installations. The installer designs and does
the work; you get to know what to ask for and what to check.

:::essencial
- **One circuit per car**: dedicated, with cables of 2.5 mm² or more, a curve C or D circuit breaker and a residual-current device of 30 mA or less, at least type A, just for that connection point.
- **Wallbox with Type 2**: it also needs protection against fault currents with a DC component, unless the wallbox already has it built in.
- **In a building, the space decides the board**: if it's part of your unit, it's normally fed from the unit's main board; if it's a common space for your exclusive use, from the riser board or the common services board.
:::

## Before you call the electrician, answer four questions {#antes-de-chamar-o-eletricista}

Each answer changes what the installer will propose. Have them ready.

1. **Where is the space?** At a house, in a closed garage (boxe) in a building, marked on the floor
   of a shared garage, or in a shared charging area (a building, a company, a hotel).
2. **Is the space part of your unit (fração)?** It is if it's in the unit's description or has its
   own property register entry (artigo matricial). If it's a common space for your exclusive use, it
   isn't. That's what decides which board it can be fed from.
3. **Socket or wallbox, and for which car?** What matters is the on-board charger of the exact
   version.
4. **What contracted power do you have**, and is the contract single-phase or three-phase?

## The list to take to the electrician {#o-que-pedir-ao-eletricista}

Take it when you ask for a quote. It doesn't replace the design project or the installer: whoever
designs it, does it and confirms that a specific installation complies is the responsible technician
or the installation company (entidade instaladora). What's here is for knowing what to ask for and
what to check, not for doing the wiring yourself.

- **A dedicated circuit just for the car**, coming from the
  [right board for the space](/instalacao-eletrica/#de-que-quadro-se-alimenta).
- **Cable of 2.5 mm² or more**, rated for at least 16 A, with a voltage drop of up to 5 %.
- **Its own curve C or D circuit breaker and its own 30 mA residual-current device**, at least type
  A. If the wallbox doesn't have DC detection, a type B, or a type A or F with a DC detector.
- **A switch next to the socket**, or in the space's own board.
- **A fixed socket or wallbox**, between 0.5 m and 1.5 m from the floor, with the IP and IK ratings
  the location needs.
- **A surge protective device**, recommended.
- **Circuit and connection point labelled** with the space.
- **At the end, the paperwork**: the declaration of conformity or the statement of responsibility.
  [Who can install it and what paperwork to insist on](/carregar-em-casa/#quem-instala-e-que-papeis-pedir).

## The guide advises, the RTIEBT bind {#o-guia-e-as-rtiebt}

The rules come from two texts. The RTIEBT (Regras Técnicas das Instalações Elétricas de Baixa
Tensão, the low-voltage installation rules) are Portaria n.º 949-A/2006, and section 722, on
supplying electric vehicles, was added by Portaria n.º 252/2015. The DGEG's
[Technical Guide](https://www.dgeg.gov.pt/media/dzejui0r/guia-ve-ed-3-2023.pdf), 3rd edition, from
2023, written by the CTE 64 committee, interprets them.

What binds are the RTIEBT and the law. The guide is guidance: it says how to apply them and, on some
points, asks for more than section 722.

- **To read the RTIEBT**, use the
  [consolidated version in the Diário da República](https://diariodarepublica.pt/dr/legislacao-consolidada/portaria/2006-70055500),
  the official gazette, which already includes section 722, and not copies on other sites. That
  version has no legal value: what counts are the published ordinances (portarias).
- **The guide predates DL 93/2025.** Some legal references are
  [out of date](/instalacao-eletrica/#o-que-esta-desatualizado-no-guia), but the technical rules
  still stand.
- **A new guide is planned** (Portaria n.º 128/2026/1, art. 3.º, n.º 4). If the DGEG has already
  published a newer edition, that's the one that counts, and what's here may have changed.

The values that follow (cable sizes, currents, heights, IP and IK codes) are rules from the guide,
not estimates. In brackets is the section they come from: the guide's, as in (guide, 3.1.5), or the
RTIEBT's, as in (RTIEBT, 803.6.4).

## Modes 1 to 4: how the car connects {#modos-de-carga}

The mode says how the car connects to the installation (guide, 2.1.8). Modes 1 to 3 charge on
alternating current, through the car's on-board charger; mode 4, on direct current.

| Mode | How it connects | Notes |
|---|---|---|
| 1 | Standard socket, up to 16 A, no protection in the cable | AC. Only phase, neutral and earth. |
| 2 | Standard socket, up to 32 A, with a control box in the cable | AC. The box has a pilot function and residual-current protection. It's the cable that comes with many cars. |
| 3 | Fixed charger (wallbox), permanently connected to the installation | AC, Type 2 socket or cable. The pilot function runs to the charger. |
| 4 | External charger supplying direct current | DC charger, always with the cable attached to it. |

The guide calls SAVE (sistema de alimentação de veículos elétricos) what many standards call EVSE:
the cable, the plugs, the sockets and the charger (guide, 2.2.22).

:::aviso
**No extension leads and no second cable** between the car and the socket or charger. Adapters only if they're made for charging, marked as such and approved by the makers of the car and of the equipment, and never to switch from one mode to another (guide, 2.2.1 and 2.2.2).
:::

## The circuit: one per car, and only for it {#o-circuito}

The circuit only feeds the connection point and its auxiliary loads, and shouldn't be affected by a
fault on other circuits (guide, 3.1.5).

- **Cables of 2.5 mm² or more**, sized for at least 16 A (guide, 3.1.5 and 4.3).
- **Voltage drop of up to 5 %** between the origin of the installation and the connection point
  (guide, 3.1.5).
- **Its own circuit breaker** on each final circuit, curve C or D, chosen for the type of load (guide,
  4.3 and 5.1.2.2). The protection can't reset automatically (guide, 4.2).
- **Simultaneity factor 1**: each point counts as if it were always at maximum current. It can only be
  lower on a circuit with several points, and only if there's a load control system (guide, 3.1.3).
- **Surge protective device**: the guide recommends one, near the origin of the installation (guide,
  4.4 and 5.1.2.3).
- **Don't know yet which car is coming?** The circuit can end in a junction box, ready for a socket or
  a charger to be connected later (guide, 3.1.6).
- **Earthing system**: as a rule, TT. If the network is TN, the final circuit must be TN-S, with no
  PEN conductor (guide, 3.1.4).

### How much power each breaker gives {#potencia-por-disjuntor}

The maximum power of each circuit depends on the breaker (guide, 3.1.2, table 2):

| Breaker | Single-phase, 230 V | Three-phase, 230/400 V |
|---|---|---|
| 10 A | 2.3 kVA | — |
| 16 A | 3.68 kVA | 11.1 kVA |
| 20 A | 4.6 kVA | 13.9 kVA |
| 25 A | 5.75 kVA | 17.3 kVA |
| 32 A | 7.36 kVA | 22.2 kVA |
| 40 A | 9.2 kVA | 27.7 kVA |

Your contracted power needs headroom above the circuit's. The guide gives an example (3.1.2): to
charge at 3.68 kVA, even with nothing else on, the minimum contracted power step would be 4.6 kVA,
that is, 20 A at 230 V. The steps and what they cost come from your electricity contract.

## The residual-current device: one per point, 30 mA or less {#o-diferencial}

Each connection point has its own residual-current device (RCD, in Portuguese DR), at least type A,
of 30 mA or less, that cuts all live conductors, including neutral (guide, 5.1.2.1.1).

A charger with a Type 2 socket or cable (EN 62196) also needs protection against fault currents with a
DC component, unless the charger itself already has it. Any one of three will do (guide, 5.1.2.1.1):

- a type B RCD;
- a type A with a DC detector (IEC 62955);
- a type F with a DC detector (IEC 62955).

:::aviso
**Check the wallbox's data sheet before choosing the RCD.** If DC detection is already built into the charger, its own RCD is enough, at least type A and 30 mA or less. If it isn't, you need one of the three options above.
:::

- **Don't know yet what will charge there?** A type A, a type A or F with a detector, or a type B can
  go in. When the charger is installed, the installer has to confirm the RCD is suitable (guide,
  5.1.2.1.1, note 1).
- **The guide asks for more than the RTIEBT.** It's stricter than the text of section 722, because
  international standards changed after 2015 (guide, 5.1.2.1.1, note 2). Follow the guide.
- **Selectivity.** There should be selectivity between this RCD and those upstream, so a fault in the
  car doesn't cut power to the whole house (guide, 5.1.2.1.1).

## Sockets and plugs: which, where and at what height {#tomadas-e-fichas}

The guide says which socket or plug goes with each mode (guide, 5.1.2.5.1 and table 3):

| Socket or plug | Standard | For which mode | Rule |
|---|---|---|---|
| Domestic socket (Schuko) | NP 1260 | 1 or 2 | Up to 10 A of charging current, unless factory-marked for charging vehicles. |
| Industrial CEE socket | EN 60309 | 1 or 2 | In a place open to the public, only with shutters or equivalent protection. |
| Type 2 | EN 62196-2 | 3 | Only on a charger (wallbox), which manages charging with the car. |
| CCS (Combo 2) and CHAdeMO | EN 62196-3 | 4 | Cable attached to the DC charger. |

- **Domestic sockets are for installations that already exist.** That's the only place the guide
  recommends them. In a renovation, a socket made for charging goes in (guide, 5.1.2.5.1).
- **Fixed, close and at the right height.** Sockets are fixed to a wall or in a board, never loose, as
  close as possible to the space, with the bottom edge between **0.5 m and 1.5 m** from the floor
  (guide, 5.1.2.5.1).
- **One socket, one car.** Each socket or plug feeds only one car (guide, 5.1.2.5.1).
- **A switch next to the socket.** There has to be a switch or other device that cuts the circuit at
  full load. The plug doesn't count as a way to cut it (guide, 3.1.6 and 4.5). Where the cut-off is in
  the board, the socket carries the sign "Desligar o interruptor antes de retirar a ficha" (switch
  off before unplugging) (guide, figure 5).
- **Type 2 without a charger, no.** A loose Type 2 socket, without a charger, isn't used: without a
  charger, the car only charges in mode 1 or 2 (guide, figure 5, note).
- **Everything labelled.** Each connection point is labelled with the space it belongs to, and the
  circuit in the board has the same label (guide, 3.1.6). The equipment is marked, for example with
  "VE" (guide, 5.1.1).

## Which board feeds the space {#de-que-quadro-se-alimenta}

The guide has standard layouts for each case, in figures 6 to 19 (guide, 3.1.1 and table 1). Who is
responsible for the charger in each case is another matter, covered in
[charging at home](/carregar-em-casa/#de-que-quadro-sai-a-eletricidade).

### House: from the home's installation {#moradia}

At a house, the space is fed from the home's installation, with its own supply line (ramal), with or
without a closed garage (guide, figures 8 and 9).

### Building: part of your unit, or just for your exclusive use? {#predio-lugar-de-uso-exclusivo}

For a space for exclusive use, the layout depends on where the power comes from and on whether the
space is a closed garage or a space marked on the floor (guide, 3.1.1, point b2):

| Origin | Closed garage (boxe) | Space marked on the floor |
|---|---|---|
| The unit's main board | figure 10 | figure 10A |
| Riser board, with the space's own main board | figure 11 | figure 11A |
| Common services board | figure 12 | figure 13 |

- **A space that's part of the unit** (it's in the unit's description): as a rule, it's fed from the
  unit's main board (RTIEBT, 803.6.4). In an existing building, if that isn't possible, it can be fed
  from the riser board (quadro de colunas) or the common services board (guide, 2.6.3, note 2, and
  3.1.1, note 5).
- **A common space for exclusive use** (for example, a space in the shared garage assigned to the unit
  that isn't part of its description): it can't be fed from the unit's main board (guide, 2.6.4, note
  2). That leaves the riser board or the common services board.
- **Common services, only as a last resort.** The guide recommends these solutions only when the
  others aren't technically or economically viable. And it always requires, on top of the common
  services meter, individual metering of each point (guide, 3.1.1, footnote 2, and part 7, note 1).
  On a space with no closed garage and no authentication of whoever charges, access to the socket or
  charger must be controlled (guide, figure 13).
- **The DGEG prefers the riser board.** In a 2024 clarification, it says that feeding from the riser
  board answers the limitations of feeding from common services. If you're torn between the two,
  that's the solution the DGEG prefers.

To separate the car's consumption with a meter of its own, see
[when a sub-CPE pays off](/sub-cpe/).

### Shared charging area {#zona-de-carregamento-partilhada}

A dedicated area in a car park (a building, a company, a hotel) with access only for owners or
customers has three options. It's fed from a separate installation with its own supply line, from the
riser board or from the common services board (guide, 3.1.1, point c, and figures 14 to 19). Without authentication of
whoever charges, the guide recommends controlling access to the socket or charger, to prevent misuse
(guide, figure 5).

### Where the cables run {#por-onde-passam-os-cabos}

- **Only through common areas and the unit's own spaces.** The circuit for a space fed from the unit
  never goes through another owner's closed garage or space (guide, 3.1.5).
- **A space marked on the floor gets its own board.** The circuit comes from a board for that space,
  which only opens with a key or a tool, and next to the access there's a main switch for all of that
  space's circuits (guide, 3.1.5).
- **Cables with a name.** They're marked or labelled with the home and the space they connect, so
  everyone knows whose they are during a repair (guide, 3.1.5).
- **In the riser duct, under conditions.** It's where the meter cables run up. The circuits for the
  homes' annexes can run there if: the duct has spare room for them; the cables are labelled and kept
  apart from the riser's, without getting in the way of maintenance; and they're at least 10 cm from
  the riser board and the riser boxes, and 5 cm from the meters. No equipment of any kind goes in the
  duct (RTIEBT, 803.2.3.2.3).
- **Not through the lift shaft.** Nor through ducts or pipes of other installations. That's the DGEG's
  position (FAQ 2.1.17), citing section 803.4.1 of the RTIEBT. That section's text only says the
  risers sit in common areas, somewhere easy to reach: the ban is the DGEG's reading of it.

### Emergency cut-off {#corte-de-emergencia}

On a floor with spaces marked on the floor fed from the homes' boards, there has to be a fail-safe
system, on the floor's main board, that cuts all those supplies at once. It's labelled as the
emergency cut-off (guide, 4.5.1).

That cut-off breaks all live conductors, including neutral. Plugs and sockets never serve as an
emergency cut-off (guide, 4.5.1).

## The power for a car park: how many spaces, and how much each {#potencia-no-parque-de-um-predio}

In a building's car park, each connection point counts for at least **3680 VA**, or its own power if
that's higher (guide, 3). The minimum number of spaces to plan for is rounded up (guide, 3):

- **residential building**: N = 0.8 + 0.2 × n, where n is the number of spaces in the car park, not
  counting those already fed from the units;
- **other car parks with a dedicated area**: N = 0.9 + 0.1 × n. In a car park with more than 400
  spaces, N can be capped at 41.

The rest of the rules:

- **Ready, not built.** The installation doesn't have to be built for every space, but it has to be
  ready to connect each one "easily": cable trays or surface cables with clips, without cutting into
  walls (guide, 3, note 3).
- **Beyond what was sized, load control.** When the points or the power go beyond what was sized, a
  load control system is needed, which switches loads off or, in modes 3 and 4, lowers the charging
  current (guide, 3).
- **Car parks that aren't residential**: one connection point from the start is enough. The guide
  recommends dedicating half the minimum power to charging from the outset (guide, 3, note 4).

What the law requires of new buildings is in [charging at home](/carregar-em-casa/#predios-novos).

## Inside and out: water, dust and knocks {#dentro-e-fora}

The equipment has to stand up to where it's installed (guide, 5.2.1 and 5.3.1, tables 4 and 5):

| Where | Water | Dust | Mechanical impact |
|---|---|---|---|
| Indoor garage in a building | IPX1 or IPX2 | IP4X | IK08 with protection from the car, IK10 without it (between 0.9 and 2 m); IK07 inside a closed garage |
| Outdoors | IPX4 or more, depending on exposure | IP4X | IK08 with protection, IK10 without it (up to 2.5 m) |

- **Outdoors, from –25 °C to +40 °C.** The equipment has to withstand that range. At a house, the
  impact protection of outdoor equipment can be lower, but not below the indoor level (guide, table 5).
- **Locked.** Boards and chargers with accessible live parts close with a key or a tool and, with the
  door open, keep at least IPXXB or IP2X (guide, 4.1).
- **A light that shows there's power.** Indoors, the guide recommends a voltage indicator lamp on each
  charging circuit (guide, 5.2.2).

## And the car powering the house? {#carro-a-alimentar-a-casa}

In modes 1 and 2, the car feeding power into the installation is prohibited. In mode 3, the charger
has to prevent it happening by accident. In 2023, the rules for the car deliberately powering the
house were still being studied at CENELEC (guide, 5.1.2.6).
[Where V2H stands today](/carregar-em-casa/#v2l-v2h-e-v2g).

## Chargers open to the public: earthing and voltage {#postos-acessiveis-ao-publico}

This is for OPCs, the charge point operators, and for designers. Someone charging at home rarely
needs it.

- **Earthing.** Earth resistance can't allow touch voltages above 25 V, at any time of year. Chargers
  fed from the grid have their own earth electrodes (guide, 5.3.2).
- **Copper earth conductors**: bare, 25 mm² or more; insulated (0.6/1 kV, green/yellow, black sheath),
  16 mm² or more (guide, 5.3.2).
- **Power only to charge.** On a public charger, the socket only goes live after whoever is charging
  authenticates (modes 1 and 2) or the charger detects the car (modes 3 and 4) (guide, 3.1.6).

## What the RTIEBT say and the guide doesn't repeat {#o-que-dizem-as-rtiebt}

Section 722 of the RTIEBT (Portaria n.º 252/2015) is the rule; the guide applies it and, on some
points, is stricter. This is what section 722 says that the guide doesn't repeat, or says
differently:

- **Motorbikes too.** For the RTIEBT, an electric vehicle includes motorcycles, mopeds, tricycles,
  quadricycles and hybrids that charge from the grid (722.3.1). The circuit rules apply to a socket for
  charging a motorbike.
- **Plug locking.** In modes 3 and 4, an electrical or mechanical system prevents plugging in or
  unplugging while the socket or connector is live (722.55.101.4).
- **RCD.** Section 722 asks for at least type A and, on a three-phase supply whose load isn't known,
  protection against currents with a DC component, for example a type B (722.531.2.101). The guide
  goes further and asks for that protection on any charger with Type 2, unless the charger has it
  ([see the residual-current device](/instalacao-eletrica/#o-diferencial)).
- **Mechanical impact.** In public areas and car parks, equipment is protected against medium impacts
  (AG2): by its location, by mechanical protection, or by an IK07 code or higher (722.512.2.103). The
  guide asks for IK08 or IK10 in buildings' indoor garages and outdoors.
- **Outdoors.** IPX4 and IP4X at least (722.512.2.101 and 722.512.2.102).
- **Emergency cut-off**, where required: it cuts at full load and cuts all live conductors, including
  neutral (722.536.4.101).
- **Sockets.** EN 60309 or EN 62196, and also NP 1260 domestic sockets up to 16 A (722.55.101.1). The
  guide limits the Schuko to 10 A of charging current, unless it's marked for charging.

Of the general rules for buildings, these matter most for charging in a building:

- **Annexes of homes** (garage, closed garage, space) reached only through common areas: they're fed
  from the home's main board, by their own circuits that only run through common areas and that
  home's own spaces. Next to the annex's access there's a cut-off for all conductors (803.6.4). That's
  where the DGEG's "a partir do quadro de entrada da fração" (from the unit's main board) comes from.
- **Common services circuits**: run only through common areas (803.6.3).
- **Minimum power for a home**, for sizing the installation: 3.45 kVA (one room), 6.90 kVA (two to
  six) or 10.35 kVA (more than six), single-phase (801.5.2.2). With a car charging from the unit, more
  than these minimums may be needed (guide, 3.1.2).

## What's out of date in the guide {#o-que-esta-desatualizado-no-guia}

The guide is from September 2023 and cites the 2010 regime. When you come across these passages, the
rule today is different:

- **It cites DL 39/2010 and DL 90/2014.** They were revoked by DL 93/2025 from 19 August 2025: they're
  the rules of the previous regime.
- **It says OPCs' chargers are inspected every four years** (DL 90/2014). Today it's every five years,
  by an EIIEL, an electrical installations inspection body (DL 93/2025, art. 16.º).
- **It cites Portarias n.º 220/2016 and 221/2016 and Directive 2014/94/EU.** The directive was
  replaced by AFIR (Regulation (EU) 2023/1804). The ordinances under DL 93/2025 are in
  [the guide to AFIR and the new Portuguese regime](/afir/).
- **It suggests marking equipment with the model in the annex to DL 39/2010.** The letters "VE" or
  equivalent are enough.
- **The DGEG's 2024 clarification cites art. 29.º of DL 39/2010**, on installation in existing
  buildings. Today the condominium rule is in art. 23.º of DL 93/2025:
  [what the condominium (condomínio) can and can't do](/carregar-em-casa/#num-predio).

## Myths and mistakes {#mitos-e-enganos}

- **"A type A RCD is enough for any wallbox."** It isn't. On a charger with a Type 2 socket or cable,
  the guide also asks for protection against currents with a DC component: a type B, or a type A or F
  with a detector. It only waives it if the charger itself already has it (guide, 5.1.2.1.1).
- **"The RCD already in the board will do."** Each connection point has to have its own, of 30 mA or
  less. And there should be selectivity with those upstream, so a fault in the car doesn't cut power to
  the whole house (guide, 5.1.2.1.1).
- **"A Type 2 socket on the wall works as a wallbox."** It doesn't. Without a charger, the car only
  charges in mode 1 or 2, and a loose Type 2 socket isn't used (guide, figure 5, note).
- **"To switch off, you pull the plug."** The plug isn't a way to cut the circuit. Next to the socket
  there has to be a switch that cuts at full load (guide, 3.1.6 and 4.5), and plugs and sockets never
  serve as an emergency cut-off (guide, 4.5.1).
- **"These rules are only for cars."** They aren't: for the RTIEBT, a motorbike that charges from the
  grid is an electric vehicle too (722.3.1).
