# Scientific Figure & Infographic Generation: When Data Meets Design

## The Communication Crisis in Science

A 2024 survey by *Nature* found that 73% of researchers consider figure preparation a significant time burden, with senior researchers spending an average of 12 hours per figure on complex visualizations. The same survey found that papers with well-designed figures received 47% more citations than papers with equivalent content but poorly formatted figures—a finding consistent with the "aesthetic-usability effect" from cognitive psychology, where perceived quality of visual presentation influences perceived quality of the underlying research.

The problem is structural: most scientists receive no formal training in visual communication, yet are expected to produce publication-quality figures for journals that enforce increasingly strict formatting standards. The result is a proliferation of default Excel charts, clip-art-adorned presentations, and information-dense figures that obscure rather than illuminate.

The market has responded with a new generation of tools that blend scientific rigor with contemporary design sensibility. BioRender, the Toronto-based startup, became the defining company of this space after raising $210 million in a 2024 Series B, reaching a valuation of $1.3 billion. Their growth—200,000 scientists and pharmaceutical researchers as customers as of early 2025—testifies to massive latent demand for better scientific visualization.

## The Figure Generation Landscape

**BioRender** dominates scientific illustration in biology, biochemistry, and biomedical research. Their pre-made icon library now exceeds 50,000 scientifically accurate illustrations across 30 fields, all in a consistent style that is immediately recognizable as BioRender's aesthetic. The subscription model (starting at $15/month for academics) is justified by the time savings: a diagram that takes 4 hours in Adobe Illustrator takes 20-30 minutes in BioRender. Their partnership with *Nature* and *Cell* to embed direct BioRender export into journal submission portals was strategically decisive. The weakness is that BioRender is essentially a specialized illustration tool—limited to pre-defined scientific pathways, cell types, and molecular structures, with limited flexibility for novel visualizations.

**Sci图 (Scifig)** developed by a team at Tsinghua University, has become the primary competitor in the Chinese research market. Their integration with China National Knowledge Infrastructure (CNKI) and Chinese journal submission systems gives them structural advantages in domestic markets.

**Matplotlib, Seaborn, and the Python Visualization Ecosystem** remain the dominant tools for data visualization in science. The publication-quality figures in most machine learning, physics, and computational biology papers are generated with matplotlib or seaborn. The advantage is total flexibility and reproducibility—figures are defined by code, so the exact visualization can be regenerated. The disadvantage is that matplotlib requires substantial Python expertise and design sensibility that most bench scientists don't have.

**Observable Plot** (from the maker of D3.js) has emerged as the preferred tool for exploratory data visualization in data science contexts. Its grammar-of-graphics approach allows rapid iteration on figure concepts, and the Observable framework enables interactive figures that can be embedded directly in Jupyter notebooks.

## AI-Assisted Figure Generation: The New Frontier

The emergence of multimodal AI models has created a new category: tools that generate figures from natural language descriptions of the visualization needed. The most mature in this category:

**Tableau's Ask Data** feature allows natural language queries that generate corresponding visualizations—"show me revenue by region for Q3" generates a bar chart. Not scientific-figure grade, but useful for business analytics contexts.

**Penrose** (from MIT CSAIL) is the most intellectually ambitious project in this space: a system that converts natural language descriptions of mathematical diagrams into precise vector graphics. Describe "a triangle with altitude from vertex A intersecting side BC at a right angle" and Penrose generates a mathematically correct diagram. The underlying symbolic system prevents the output from being visually wrong in ways that plague hand-drawn figures (wrong angles, inconsistent labels, non-Euclidean features). Penrose is open source and has been integrated into several journal tools.

**Researchify** (a Y Combinator 2024 startup) takes a different approach: feed it a paper's text and it generates an infographic summary of key findings, optimized for Twitter and LinkedIn distribution. The output is in newsletter-friendly formats and is increasingly used by labs for science communication. A 2024 *PLOS ONE* study found that papers promoted via AI-generated infographics on social media had 2.3x higher Altmetric scores than unpromoted papers.

## Scientific Infographics for Public Communication

The demand for science infographics has grown substantially with increased emphasis on public science communication and science media. This is a different genre from publication figures—it's closer to journalism or design than to technical documentation.

**Adobe Illustrator with scientific icon libraries** remains the professional standard for complex infographics. The Science Fig bundle (a collection of scientific icon packs for Adobe Illustrator) has become standard equipment for science communicators at major research institutions.

**Canva's Scientific Template Library** has democratized basic scientific infographics. The 2025 integration of AI-assisted design features ("describe the infographic you want") has made Canva a viable option for labs without dedicated designers. The limitation is that Canva's scientific accuracy is not guaranteed—icon libraries are not peer-reviewed for scientific correctness.

**Piktochart** is purpose-built for infographic and data visualization, with templates designed specifically for research communication. Their "research summary" template has been adopted by several UK research councils as the standard format for grant lay summaries.

## Interactive Figures and the Web-Publication Shift

Journals are increasingly accepting—or requiring—interactive figures that allow readers to explore data. This shifts the technical requirements significantly: from static image generation to embedded web components.

**Plotly's** Python and R libraries generate interactive figures that can be embedded directly in HTML, including mouse-over tooltips, zoom, and pan. *Nature Methods* and *PLOS Computational Biology* now accept Plotly HTML outputs as supplementary materials.

**D3.js** remains the gold standard for custom interactive visualizations but requires substantial JavaScript expertise. The **Observable** notebook environment, created by D3 creator Mike Bostock, provides a lower-friction entry point: write JavaScript in a notebook-style interface and see results immediately.

**Bokeh** (from NumFOCUS) generates interactive web visualizations in Python without requiring JavaScript knowledge. Its server-based architecture allows for live data updating, making it suitable for dashboard-style visualizations.

## Implementation: A Lab Figure Production Workflow

For a research group wanting to professionalize their figure production:

**Tier 1: Reproducible data figures.** Use matplotlib with a shared style file (defining font, color palette, DPI settings, axis formatting) that enforces visual consistency across all papers. A well-designed matplotlibrc file that matches your target journal's figure requirements eliminates most reformatting effort. Seaborn adds statistical visualization primitives on top of matplotlib with sensible defaults.

**Tier 2: Scientific illustration.** BioRender for biology and biomedical process diagrams; Adobe Illustrator for custom or physics/chemistry illustrations. Train at least one lab member to proficiency in one tool and have them maintain a shared icon/element library that can be reused across figures.

**Tier 3: AI-assisted infographic generation.** Researchify or Canva for science communication deliverables; Penrose for mathematical diagrams. Integrate these as supplements to, not replacements for, publication-quality static figures.

The key discipline is establishing figure templates before data collection begins. Generating figures from pre-existing template codeforces visualization decisions to be made once, transparently, with full team input—rather than retrofitted to whatever the data happened to show. This also improves reproducibility: figures generated from template code have exact parameters that can be reported as part of the methods.
