# Carbon Capture & Direct Air Capture: A Research Memo

## Overview

Carbon capture technology refers to a suite of methods designed to prevent carbon dioxide (CO₂) from entering the atmosphere, or to remove CO₂ that is already present. The field encompasses point-source capture (capturing emissions from industrial facilities like cement plants and steel mills) and direct air capture (DAC), which pulls CO₂ directly from ambient air. This memo focuses on the technological landscape, economic realities, and emerging innovations in carbon capture, with particular emphasis on Direct Air Capture as one of the most transformative—and controversial—approaches to climate remediation.

### The Scale of the Challenge

The Intergovernmental Panel on Climate Change (IPCC) indicates that limiting global warming to 1.5°C requires removing between 100 million and 1 billion tonnes of CO₂ annually by 2050, rising to billions of tonnes per year by century's end. Currently, global carbon capture capacity stands at approximately 50 million tonnes per year across all operating facilities—a tiny fraction of what's needed. The gap between current capacity and required capacity represents both a monumental engineering challenge and a multi-trillion dollar market opportunity.

### How Carbon Capture Works

**Point-Source Capture** captures CO₂ from emission streams at industrial facilities before it enters the atmosphere. This is typically done via:
- **Pre-combustion capture**: Converting fuel into a mixture of hydrogen and CO₂ before combustion, then separating the CO₂
- **Post-combustion capture**: Using solvents (typically amines) to absorb CO₂ from flue gas streams
- **Oxy-fuel combustion**: Burning fuel in pure oxygen to produce a stream of CO₂ and water vapor that's easier to capture

**Direct Air Capture (DAC)** is fundamentally different—it pulls ambient air across a sorbent material that binds CO₂, then releases it as a concentrated stream for sequestration or use. The two primary DAC approaches are:

1. **Liquid-based DAC**: Air contacts a liquid solvent (typically potassium hydroxide) that absorbs CO₂. The solution is then heated to release pure CO₂ while the solvent is regenerated.

2. **Solid sorbent DAC**: Air passes through a solid material (often amine-functionalized sorbents) that captures CO₂. Temperature or pressure swings release the CO₂, regenerating the sorbent.

### Major DAC Operators

As of early 2026, several companies operate DAC facilities:

- **Climeworks** (Switzerland): Operates the world's largest DAC plant, Mammoth (in Iceland), with capacity of 36,000 tonnes CO₂/year. Their plants use solid sorbent technology powered by renewable geothermal energy.

- **Carbon Engineering** (now part of 1PointFive, backed by Occidental): Operating a DAC plant in Texas using liquid solvent technology, with plans for larger facilities.

- **Global Thermostat** (Georgia Tech spinoff): Demonstrated solid sorbent DAC at pilot scale.

- **Verdox** (founded by MIT researchers): Developing electrochemical DAC systems.

### Economic Considerations

The cost of DAC remains the central challenge. As of 2025-2026, costs range from $250-$600 per tonne of CO₂ for first-generation plants, though Climeworks has stated a target of reaching $200-300/tonne by 2030 and eventually sub-$100/tonne with learning curves and scale. For comparison, the EU Emissions Trading System (ETS) carbon price was approximately €70-80/tonne in early 2026—meaning DAC is currently 3-8x more expensive than purchasing carbon allowances.

However, costs are falling rapidly. The learning rate for DAC has historically been around 15-20% cost reduction per doubling of capacity, similar to solar photovoltaics' early trajectory. If this holds, DAC could become cost-competitive with carbon prices by the mid-to-late 2030s. Government support is critical: the US Inflation Reduction Act provides up to $180/tonne in tax credits for carbon capture and DAC, significantly improving project economics.

## AI Applications in Carbon Capture

### Monitoring and Verification

Machine learning plays an increasingly important role in monitoring geological CO₂ storage sites. AI models analyze seismic data, wellbore measurements, and surface deformation data to detect potential CO₂ leakage in real time, providing the verification framework that carbon markets require.

### Materials Discovery

The discovery of better sorbent materials is fundamental to reducing DAC costs. AI-driven approaches are transforming this search:

- **Density Functional Theory (DFT) calculations** combined with machine learning can screen thousands of potential sorbent materials computationally before experimental synthesis
- **Generative models** can propose novel amine structures or MOF (Metal-Organic Framework) designs optimized for CO₂ binding strength, selectivity, and regeneration energy
- **High-throughput molecular dynamics** using neural network potentials can model sorbent-CO₂ interactions at scales impossible for ab initio methods

Google's DeepMind has applied similar approaches to protein structure prediction (AlphaFold), and the same paradigm is being applied to materials science through initiatives like the Materials Project and the DiscoverE project.

### Process Optimization

DAC plants are complex chemical engineering systems with many interdependent variables. Reinforcement learning and neural network-based process control can optimize:

- Energy consumption vs. CO₂ capture rate tradeoffs
- Sorbent regeneration temperature profiles
- Fan speed and airflow for optimal contact time
- Regeneration cycle timing

Carbon Engineering and Climeworks both use advanced process control systems, and AI optimization can improve efficiency by 10-20% compared to rule-based control.

### Carbon Market Intelligence

AI tools analyze carbon market data, policy developments, and project-specific information to help operators and investors make decisions about carbon credit purchases, DAC investment, and market positioning. Natural language processing models analyze regulatory filings, news, and scientific literature to predict policy changes that affect carbon prices.

## Tools & Methods

### Geological Storage Assessment

CO₂ storage requires suitable geological formations—typically deep saline aquifers, depleted oil and gas reservoirs, or basalt formations. AI tools analyze:

- 3D seismic interpretations with neural networks to map formation properties
- Well log data to identify permeable zones
- Geomechanical models to predict cap rock integrity
- Transport simulations to track CO₂ plume migration

### Life Cycle Assessment (LCA)

AI-accelerated LCA tools can model the full greenhouse gas implications of DAC systems, including energy consumption, materials manufacturing, water use, and land requirements. This is essential for verifying that DAC actually removes more CO₂ than it emits.

### Satellite Monitoring

Satellite-based InSAR (Interferometric Synthetic Aperture Radar) can detect ground surface movement at sub-millimeter precision, allowing AI systems to monitor CO₂ injection-induced uplift or subsidence. This provides verification for carbon credit programs.

## Challenges

### Energy Requirements

DAC is fundamentally an energy-intensive process. The thermodynamic minimum energy to separate CO₂ from air is approximately 20 kJ/mol CO₂ (~200 kWh/tonne). Current plants use 1,500-2,500 kWh/tonne, meaning significant improvement is possible through better technology. If DAC is powered by fossil fuels, it could actually increase net CO₂ emissions.

### Water Consumption

Liquid solvent DAC systems can consume significant amounts of water through evaporation, particularly in arid climates. This creates tension between DAC deployment and water scarcity, especially as climate change increases drought frequency in many regions.

### Land Use

Large-scale DAC requires substantial land. At $300/tonne and 2,000 kWh/tonne of energy input, a 1 million tonne/year DAC facility requires roughly 100 MW of continuous power (if electrical) and significant infrastructure. If powered by solar, land requirements are approximately 5-10 acres per MW, making a large DAC facility occupy 500-1,000 acres.

### Carbon Accounting

Verifying that captured CO₂ is permanently stored is essential for carbon credits. Subsurface storage requires monitoring over decades to centuries—a timeframe that exceeds most carbon credit instruments' verification periods.

## Ethics

### Permanence and Intergenerational Responsibility

Captured CO₂ in geological storage may leak over millennia. Is it ethical to sell carbon credits today for storage that must be verified over centuries? The concept of "permanent" carbon sequestration is philosophically problematic when human institutions rarely persist that long.

### Greenwashing Concerns

Some critics argue that heavy investment in DAC creates a "moral hazard"—allowing governments and corporations to delay emissions reductions while relying on future carbon removal. This is a legitimate concern: if organizations invest in removal rather than reduction, total atmospheric CO₂ may continue rising even as removal capacity scales.

### Resource Allocation

The capital invested in DAC could alternatively fund renewable energy, energy efficiency, forest conservation, or community adaptation. Some critics argue that in a world of limited capital, DAC represents a distraction from preventing emissions in the first place. The ethics of spending billions on technological carbon removal versus emissions prevention remains vigorously debated.

### Equity and Access

DAC facilities are currently concentrated in wealthy countries (Switzerland, Iceland, USA). The technology could widen the gap between wealthy nations that can afford carbon removal and vulnerable communities already experiencing climate impacts. Additionally, the CO₂ stored may be sourced from global emissions, creating complex ownership and benefit-sharing questions.

## Future Directions

### Next-Generation Sorbents

Research into advanced materials continues to push the boundaries of what DAC can achieve:

- **Metal-Organic Frameworks (MOFs)**: Tunable crystalline materials with extremely high surface areas and selective CO₂ binding
- **Solid amine sorbents**: Immobilized amines on porous supports that combine high capacity with low regeneration energy
- **Electrochemical capture**: Using electrical fields to drive CO₂ capture, potentially powered by low-cost renewable electricity

### Ocean-Based Carbon Removal

Complementing DAC, ocean-based approaches aim to enhance the ocean's natural carbon sink:

- **Ocean alkalinity enhancement**: Adding alkaline minerals (like silicate or limestone) to seawater to increase CO₂ dissolution
- **Seaweed cultivation**: Growing kelp forests that sink carbon to the deep ocean when they die
- **Electrolysis-enhanced weathering**: Using electrical current to transform seawater chemistry and increase CO₂ absorption

These approaches could be significantly cheaper than DAC due to the ocean's massive capacity as a carbon sink, but monitoring and verification challenges are considerable.

### Carbon Use vs. Storage

An active debate exists around whether captured CO₂ should be stored geologically or used as a feedstock:

- **Carbon-negative fuels**: Using captured CO₂ to produce synthetic fuels (via hydrogen from renewable electrolysis), creating a carbon-neutral fuel cycle
- **Concrete curing**: CO₂ can be permanently mineralized into concrete, replacing Portland cement (which accounts for ~8% of global emissions)
- **Carbonated materials**: Using CO₂ in the production of building materials

Carbon use can provide revenue streams that improve project economics, but critics argue that "use" can imply "emissions eventually occur" unless the carbon is durably locked away.

### Policy and Scale

The future of carbon capture depends heavily on policy support:

- The US 45Q tax credit (enhanced under the IRA) provides substantial incentives for carbon capture and storage
- The EU Carbon Border Adjustment Mechanism (CBAM) creates market pressure for low-carbon industrial processes
- Article 6 of the Paris Agreement establishes frameworks for international carbon market cooperation

The scale-up required is unprecedented. The IEA estimates that reaching net-zero by 2050 requires approximately 60 DAC plants coming online every year from now until 2050—each requiring $500M-$1B in capital investment. This is a multi-trillion dollar mobilization comparable to historical infrastructure buildouts.

The science is clear: carbon capture and especially DAC represent necessary components of a portfolio approach to climate change. The economics are improving rapidly, but the gap between current capacity and need remains enormous. The ethical complexities require careful governance. Yet without technological carbon removal at scale, the world's path to net-zero becomes significantly narrower.