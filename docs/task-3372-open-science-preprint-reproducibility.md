# Open Science, Preprints & Reproducibility: The Infrastructure Behind Transparent Research

## The Reproducibility Crisis Nobody Fixed

The 2016 "Reproducibility Project" from the Center for Open Science remains the defining study of the reproducibility problem in academia. Researchers attempted to replicate 100 studies published in three top psychology journals, using original materials and protocols. Only 36% replicated successfully. A 2022 follow-up in *Nature* found similar patterns in cancer biology, where only 26% of landmark studies replicated in rigorous independent trials. The problem isn't that scientists are dishonest—it's that the system incentives speed of publication over verifiability, and that most published findings represent cherry-picked best results from multiple analytical pathways.

The open science movement emerged from this crisis with a practical mission: make research artifacts—data, code, protocols, and pre-registration documents—permanently accessible alongside publications. The movement has matured from idealistic advocacy to serious infrastructure development, with real deployment challenges that illuminate what institutional open science actually looks like.

## Preprints: The Publication Pipeline Gets Disrupted

Preprints—manuscripts posted publicly before formal peer review—represent the most visible and contested innovation in scientific publishing. The arXiv preprint server, launched in 1991 by Paul Ginsparg at Los Alamos, has been central to physics for decades. In 2023, arXiv passed 2 million submissions and serves roughly 8 million downloads per month. bioRxiv, the biology equivalent launched in 2013, surpassed 200,000 preprints in 2024. medRxiv, covering health sciences, has grown to over 150,000 since its 2019 launch.

The COVID-19 pandemic proved the preprint model in the most stressful possible test case. The WHO and CEPI used preprints as early-warning signals, with some preprint analyses influencing policy before formal peer review. The now-infamous *The Lancet* retraction of the Surgisphere hydroxychloroquine paper—which would have been a preprint in many fields—illustrated both the value (rapid sharing) and danger (insufficient vetting) of the model. The post-pandemic recalibration led to medRxiv adopting mandatory statistical review and a more explicit "preprint, not final" labeling system.

China launched the ChinaXiv preprint server in 2016, which as of 2025 processes about 40,000 preprints annually, predominantly in Mandarin. India has invested in OPENS, and the European Research Council has funded preprint infrastructure through the OPER.pre repository. AfricaXiv, launched in 2018, is attempting to address the significant structural barriers to preprint adoption in African research communities.

The business model question for preprint servers remains unresolved. arXiv runs on roughly $3.5 million annually, primarily funded by Cornell University and a consortium of other research institutions—a remarkable bargain for serving the entire global physics community. bioRxiv is funded by the Cold Spring Harbor Laboratory. The economics work because preprint servers have essentially zero peer review costs and minimal editorial infrastructure. The challenge is that this model scales poorly if servers try to add quality signals, overlays, or community features.

## Reproducibility Infrastructure: What Actually Exists

**OSF (Open Science Framework)** from the Center for Open Science is the backbone infrastructure for open science practices. It's a free, open-source platform for registering studies, storing data, linking to preprints, and managing collaborators. As of early 2026, OSF hosts over 5 million projects and has been used in pre-registration for studies published in every major journal. The pre-registration feature is its most transformative component: researchers formally declare their analysis plan before data collection, then commit to following that plan exactly. This eliminates the HARKing (Hypothesizing After Results are Known) problem, where researchers reverse-engineer hypotheses from observed results and present them as a priori predictions.

**Code Ocean** and **Gigantum** offer "computational notebooks in the cloud"—environments where anyone can run the exact code used to generate a paper's results. Code Ocean'sCapsule system packages data, code, computational environment, and results into a reusable unit that journals like *Nature Methods* and *PLOS Computational Biology* now recommend or require for publication. The practical value is enormous: a reviewer or reader can execute the exact code, observe the exact intermediate outputs, and verify the chain from raw data to published conclusion.

**Whole Tale** (from the DataVerse network at Harvard) goes further, treating the entire research article as a computational object. The tale (reproducible research object) can be executed, modified, and re-published. It integrates with repositories like Dryad and Zenodo for data archival.

**Protocols.io** has built a parallel infrastructure for methodological transparency. Their platform hosts over 200,000 research protocols, with version control and community annotation. Unlike methods sections in papers—which are compressed and often omit critical procedural details—protocols.io protocols are step-by-step executable documents. The platform's integration with *Nature Protocols* means protocols can be simultaneously a community resource and citable scholarly objects. Lab managers at pharmaceutical companies like Roche and Novartis have started using it internally for SOP development, which represents an interesting commercial adoption.

## Preregistration and the Analysis Plan Revolution

Preregistration is the single practice most associated with improving reproducibility. The AsPredicted template, developed by Brian Nosek and colleagues, is the simplest approach: a one-page form declaring hypotheses, sample size, exclusion criteria, and analysis plan. The AsPredicted website has facilitated over 700,000 registrations since 2012. The commitment to following the registered plan, even if results are embarrassing or null, is what produces trustworthy science.

The tension is that preregistration is professionally risky. Null results are harder to publish, and committing to an analysis plan in advance means you can't hunt for post-hoc significance. The *Journal of the American Medical Association* published research in 2023 showing that mandatory preregistration at submission led to a 32% increase in null findings being published—good for science, painful for researchers who invested years in studies that "failed."

Registered Reports, a publishing format pioneered by Cortex and now offered by over 300 journals (including *Nature Communications*, *PLOS Biology*, and most APA journals), solves the publication incentive problem by committing to publish the study before data is collected. Reviewers approve the protocol, and the journal commits to publishing results regardless of outcome. The format has shown dramatic effects: the replication rate for Registered Reports is approximately 85%, compared to 36% for conventional studies.

## Licensing and Attribution: The Unsolved Economics

A major infrastructure gap that doesn't get discussed enough is licensing for research artifacts. When a researcher shares their data and code alongside their paper, what license governs re-use? The dominant licenses in open science are increasingly CC-BY (attribution required) and CC0 (public domain), but neither maps cleanly onto the actual norms of scientific attribution, where蹭 authorship without contribution is a professional violation.

The Grotthuss Protocol, developed by the Open Science MOOC community, proposes a "minimal reuse license" that requires attribution and a link back to the original study, but otherwise permits re-analysis, reproduction, and building upon the work. The practical adoption of these licenses remains low because most researchers never think about licensing when sharing artifacts, and institutional repositories default to "all rights reserved."

## Practical Implementation: Setting Up a Lab's Open Science Workflow

For a research group adopting open science practices, the minimum viable infrastructure consists of:

1. **OSF private dashboard** for managing active projects with embargo features (keep data private until publication)
2. **GitHub/GitLab repository** for code, with Zenodo integration for DOI minting on releases  
3. **Protocols.io workspace** for lab SOPs and method development
4. **Preregistration template** (AsPredicted or OSF Prereg) as the default starting point for new studies

The cultural shift is harder than the technical setup. Lab managers implementing this workflow report that getting graduate students to consistently preregister studies takes 6-12 months of habit formation. The most effective approach is making the preregistration document the collaborative working document from day one—using it to plan the study together rather than as a bureaucratic exercise after the fact.

Open science infrastructure is maturing rapidly, but the last-mile problem remains human: researchers trained in traditional publishing norms need active mentorship to internalize that open practices aren't just good ethics—they produce better science. The reproducibility crisis created the conditions for change; the infrastructure now exists to act on that learning.
