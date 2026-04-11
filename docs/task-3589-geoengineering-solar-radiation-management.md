# Geoengineering & Solar Radiation Management: A Research Memo

## Overview

Solar geoengineering (also called Solar Radiation Modification or SRM) refers to a suite of proposed technologies that would reflect a small fraction of incoming sunlight back into space, reducing global temperatures and potentially counteracting some effects of anthropogenic climate change. Unlike emissions reduction or carbon removal, geoengineering does not address the root cause of climate change (excess atmospheric CO₂) but instead attempts to mask its symptoms.

This memo examines the scientific basis for solar geoengineering, the state of research, the profound ethical debates surrounding it, and AI's emerging role in this highly controversial field.

## The Science of Solar Geoengineering

### The Basic Principle

The Earth's energy balance is governed by incoming solar radiation (shortwave, ~340 W/m² at top of atmosphere) and outgoing terrestrial radiation (longwave, infrared). Adding CO₂ to the atmosphere traps more longwave radiation, warming the surface. SRM works by increasing planetary albedo (reflectivity), reducing the amount of absorbed solar energy and thereby counteracting greenhouse warming.

The basic physics is straightforward: if we can reflect ~1-2% of incoming sunlight back to space, we could offset the warming effect of a doubling of CO₂ (~3.7 W/m² radiative forcing). This is equivalent to roughly 1-2% of total solar input, or ~3-7 W/m² of reflective forcing.

### Approaches to SRM

**Stratospheric Aerosol Injection (SAI)**

The most researched approach involves injecting reflective aerosols (sulfate particles, or other particulates) into the stratosphere (20-25 km altitude). This mimics the cooling effect of major volcanic eruptions—the 1991 Mount Pinatubo eruption injected approximately 20 Mt of SO₂ into the stratosphere, creating a global cooling of ~0.5°C that lasted 2-3 years.

For continuous SRM, continuous injection would be required: modeling suggests 1-5 Mt SO₂/year to offset 1°C of warming. This would need to be delivered by high-altitude aircraft (capable of flying at 20+ km altitude) in a coordinated, global program.

The aerosols would need to be replenished continuously (residence time of stratospheric aerosols is 1-3 years), meaning any cessation of injection would lead to rapid warming as the aerosols settle out—creating what critics call a "termination shock."

**Marine Cloud Brightening (MCB)**

This approach involves seeding marine low-level clouds with sea-salt particles to increase their reflectivity. Sea-salt particles are hygroscopic (water-attracting), increasing droplet size and cloud albedo. The concept is that bright, reflective ship tracks (visible in satellite imagery as lines of brighter clouds behind ships) demonstrate the feasibility of cloud brightening.

Marine cloud brightening could be implemented at regional scale using a fleet of autonomous vessels equipped with seawater atomizers, targeting cloud decks over vulnerable ocean regions (e.g., Arctic to slow sea ice loss, tropical oceans to reduce hurricane intensity).

**Cirrus Cloud Thinning**

High-altitude cirrus clouds actually warm the planet (by trapping outgoing infrared radiation) rather than cooling it. Thinning these clouds—removing the most insulating ones—could reduce the greenhouse effect. This is more speculative and technically challenging than stratospheric injection or marine cloud brightening.

**Surface Albedo Modification**

Reflective surfaces (white roofs, reflective pavements, desert reflectors) and ocean albedo modification (foam or bubble generation) are surface-level approaches that could contribute but have limited global scalability.

## The Climate Modeling Challenge

### Model Dependence

The climate effects of SRM are highly model-dependent. Different climate models produce different results for:

- **Temperature response**: How much cooling per W/m² of SRM?
- **Precipitation effects**: Will SRM reduce monsoon rainfall? Regional models suggest significant precipitation changes, especially in the tropics
- **Ozone effects**: Stratospheric aerosol injection could affect stratospheric ozone chemistry, potentially delaying ozone recovery
- **Termination shock**: How rapidly would temperatures return if injection stopped?

The range of model estimates for key SRM parameters is large enough that field deployment decisions cannot be made based on current modeling alone.

### Regional Heterogeneity

SRM does not uniformly reduce temperatures. Modeling shows significant regional variation:

- **Polar amplification**: SAI tends to produce stronger cooling at high latitudes than at the equator
- **Monsoon disruption**: SRM could reduce monsoon rainfall in South Asia, Sub-Saharan Africa, and other regions that depend on seasonal rainfall
- **Uneven cooling**: Different regions would cool by different amounts, creating a patchwork of climate responses

This heterogeneity is the core ethical problem: SRM benefits some regions at the expense of others, creating winners and losers even as it addresses the global temperature rise.

### The "Free Rider" Problem

Any country could, in theory, unilaterally deploy SRM without international agreement. A single nation (or even a private actor) with sufficient resources could attempt geoengineering, affecting the entire planet's climate. This creates a "free rider" problem: some nations might choose to deploy SRM based on their own interests, without the consent of affected populations elsewhere.

## AI Applications in Geoengineering Research

### Climate Model Emulation

SRM research requires running thousands of model simulations with varying injection rates, injection locations, aerosol types, and background climate conditions. AI-based climate model emulators can:

- **Fast-forward simulations**: Neural network emulators can predict the climate response to arbitrary SRM scenarios in milliseconds vs. hours for full GCM runs, enabling rapid exploration of parameter space
- **Uncertainty quantification**: Bayesian neural networks that produce probabilistic outputs, giving decision-makers a sense of the uncertainty range
- **Out-of-sample testing**: Evaluating emulators on held-out simulation results to validate their accuracy

This approach is particularly valuable given that state-of-the-art GCM simulations of SRM scenarios require enormous computational resources that are not available at scale.

### Observational Data Analysis

AI is being applied to detect and interpret signals of SRM in observational data:

- **Volcanic analog studies**: Using the 1991 Pinatubo eruption as a natural experiment to validate climate model predictions of aerosol injection effects
- **Atmospheric detection**: ML systems that could detect unauthorized stratospheric aerosol injection from atmospheric monitoring data
- **Effect attribution**: Distinguishing SRM effects from natural climate variability and other forcing agents

### Governance and Risk Modeling

AI models are being used to explore the governance implications of SRM:

- **Game-theoretic analysis**: Modeling how different nations might behave in a world with and without SRM, identifying cooperation and conflict scenarios
- **Decision frameworks**: Multi-criteria decision analysis that weighs temperature benefits against precipitation risks, termination shock, and governance challenges

## Tools and Methods

### Global Climate Models (GCMs)

The standard tool for SRM assessment is a climate model, typically at CMIP-class resolution (100 km horizontal grid). Key modeling centers include:

- **NCAR CESM**: Has performed the most comprehensive SAI simulations
- **UK Met Office UM**: Used for UK-funded SRM research
- **EC-Earth, GFDL**: Other major modeling centers

### Earth System Models (ESMs)

More comprehensive ESMs that include atmospheric chemistry, ocean biogeochemistry, and ecosystem dynamics are needed for long-term SRM assessments. These are computationally expensive and limited in number.

### Integrated Assessment Models (IAMs)

IAMs combine climate models, economic models, and emissions scenarios to provide policy-relevant analysis. They can evaluate the cost-effectiveness of SRM relative to mitigation and adaptation.

## Challenges

### Termination Shock

If SRM were deployed and then stopped—whether due to political decision, conflict, or technical failure—the climate would rapidly revert to the pre-SRM warming trajectory. For a world that had grown accustomed to lower temperatures, the "termination shock" could be catastrophic, especially for agriculture and ecosystems adapted to the SRM-altered climate. This is the single greatest risk of SRM.

### Governance Vacuum

There is currently no international legal framework governing SRM. The London Protocol (2008 amendment) prohibits ocean fertilization, but has no provisions for marine cloud brightening. The UN Environment Programme has published SRM governance principles, but these are non-binding. The absence of governance frameworks is a serious barrier to responsible research and potentially a trigger for unilateral action.

### Irreversibility and Path Dependence

Unlike emissions reductions (which can be reversed by emitting less), SRM creates a path-dependent situation: once deployed, it is difficult to stop without termination shock. This irreversibility means the decision to begin SRM is a profound one that locks in future commitments.

### Unknown unknowns

The scientific understanding of SRM is incomplete. There may be effects—on ozone, on ecosystems, on ocean circulation—that are not yet modeled or understood. The absence of empirical data at scale (we have only one planetary experiment to observe: volcanic eruptions) means SRM carries genuine unknowns that cannot be quantified.

## Ethics

### Who Decides?

SRM is a planetary intervention that affects every person on Earth, yet there is no mechanism for global consent. The governance question—who decides, who pays, who benefits, who bears the risks—is fundamentally political.

Some propose a global treaty analogous to the Outer Space Treaty; others argue for a broader "geoengineering governance convention." International organizations like the UN Environment Programme, the World Academy of Sciences, and the IPCC are all engaged in building frameworks, but none have binding authority.

### Moral Hazard

The strongest ethical objection to SRM is that it creates a moral hazard—the temptation to rely on technological intervention rather than reducing emissions. If SRM appears to work, will governments and corporations reduce their mitigation efforts?

The empirical evidence from climate policy suggests this is a real risk: the existence of CDR technologies reduces urgency to cut emissions; the existence of SRM could reduce urgency even more dramatically, since it offers faster, cheaper temperature reduction than emissions cuts.

However, moral hazard cuts both ways: if SRM reduces the perceived urgency of action, it delays mitigation. But if SRM prevents the worst climate impacts, it buys time for adaptation and mitigation. The moral hazard argument alone should not preclude research.

### Intergenerational Responsibility

SRM imposes risks and decisions on future generations without their consent. If current generations deploy SRM and then stop (or if a termination shock occurs), future generations inherit both the warming and potentially the ecological disruptions of SRM.

### Environmental Justice

SRM's regional heterogeneity creates environmental justice concerns. Who bears the risk of monsoon disruption? Who gains from Arctic cooling? These questions require engagement with affected communities, not just technical assessments by researchers in wealthy nations.

### The Butterfly Effect

There is something philosophically troubling about deliberately manipulating the planet's climate. Even setting aside practical concerns, the act of deliberately modifying the Earth's energy balance raises questions about humanity's relationship with the natural world and the limits of technological intervention.

## The State of Research: A Controlled Field

### Current Research Programs

SRM research is constrained by the "governance gap" and by research funding challenges:

- **SCoPEx**: Harvard's Stratospheric Cloud Observation Project—a balloon-based program to gather data on stratospheric conditions—has been paused pending governance framework development
- **SilverLining** (US): A private research organization funding SAI research
- **EU-funded projects**: Several EU research programs have funded SRM modeling and assessment

The field has coalesced around the principle that SRM research should be conducted within governance frameworks and with international transparency, distinguishing responsible research from irresponsible experimentation.

### The Case for Outdoor Experimentation

To validate models and gather empirical data, some researchers argue that carefully bounded outdoor experiments—testing marine cloud brightening at small scale, or balloon-based stratospheric sampling—are necessary and ethically justified if conducted transparently with international oversight.

Critics argue that any outdoor experimentation—even small-scale—could provide cover for military or commercial deployment and lowers the threshold for full-scale SRM.

## Future Directions

### Machine Learning for SRM Prediction

Better climate models, accelerated by ML, are the primary scientific frontier for SRM research. Specifically, reducing uncertainty in regional precipitation effects is essential before any deployment consideration.

### Geoengineering + Carbon Removal Synergies

SRM alone does not address ocean acidification, sea level rise (except through temperature moderation), or the long-term trajectory of CO₂-driven warming if emissions continue. The most defensible position combines SRM (to buy time) with aggressive carbon removal (to address root cause).

### International Governance Development

The development of robust, inclusive international governance frameworks for SRM—perhaps under the UNFCCC or a dedicated convention—is essential before field deployment. The 2024 UNEP report on SRM governance outlines a path toward this framework.

The geoengineering debate is ultimately a debate about risk management in a world of irreducible uncertainty. Reducing greenhouse gas emissions remains the only permanent solution to climate change. But the possibility that emissions reduction may be insufficient or too slow—combined with the growing evidence of climate impacts—makes SRM research a necessary, if deeply troubling, component of the climate action toolkit.