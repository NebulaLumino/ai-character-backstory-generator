# Task 3402: Predictive Policing — Criminal Justice & Bail Reform

## Context
AI systems that predict criminal behavior, flight risk, and bail outcomes — and the civil rights implications of getting it wrong.

## Market Analysis

The predictive policing market is valued at $2.1B (2024), growing to $7.5B by 2030. However, it's deeply controversial. The Arnold Foundation has documented that algorithmic bail tools reduce pretrial detention by 40% without increasing recidivism — while biased tools increase racial disparities. Every state is now required to assess risk assessment tools for constitutional compliance under the 2022 EPA guidance.

Key players: Arnold Foundation (PSA/PSA-R), Equivant (COMPAS), Northpointe (Correctional Offender Management Profiling for Alternative Sanctions), and newer entrants like Audit AI and Fairly. The PSA (Public Safety Assessment) is now used in 40+ states and is the most validated tool with disparate impact testing.

The bail reform movement accelerated post-2020. Illinois eliminated cash bail entirely (2021). New Jersey reduced pretrial detention by 50% using algorithmic tools. Federal courts are now scrutinizing all algorithmic bail decisions under due process and equal protection standards.

## Technical Implementation

### Types of Predictive Systems

**1. Recidivism Prediction**
- Predicts likelihood of reoffending (general or violent)
- Input: criminal history, demographics, social factors
- Output: risk score (1-10 or Low/Medium/High)
- Controversy: COMPAS showed 2x false positive rate for Black defendants

**2. Flight Risk Assessment**
- Predicts failure to appear (FTA) for court dates
- Input: prior FTA history, ties to community, employment, family
- Arnold PSA: FTA rate is ~11% nationally; reduces to 6% with PSA-guided release
- Critical for bail reform — most people in jail haven't been convicted

**3. Pretrial Risk Assessment (PSA - Arnold Foundation)**
- Three scores: failure to appear, new criminal activity, new violent criminal activity
- Used in 40+ states, most heavily validated tool
- Benchmarked against racial disparities in outputs
- Open-source, free to use

### Core Algorithm Architecture
```
Defendant Profile → Risk Factor Extraction (ML model) → 
Score Calibration (calibrated probability) → Disparate Impact Check → 
Recommendation Output → Audit Trail
```

### Key Data Sources
- State criminal history databases (CHRI)
- Court records (new arrests, FTA history)
- Pretrial services intake interviews
- Jail booking data
- Some tools use social media/surveillance (ethically fraught)

### Tools & Techniques
- **Logistic regression + XGBoost**: Interpretable models preferred by courts
- **Fairlearn/AIF360**: Disparate impact measurement
- **SHAP**: Explain individual risk factor contributions to scores
- **LIME**: Local interpretability for courtroom testimony
- **PostgreSQL + DCF library**: Federal sentencing data

### Companies & Tools
- **Arnold Foundation PSA/PSA-R**: Gold standard, open-source, used in 40+ states
- **Equivant (Northpointe)**: COMPAS — most scrutinized, used in 40+ states
- **Equivant**: PSA 3.0 release in 2023 with improved calibration
- **Sapient Analytics**: Federal sentencing tools
- **Knight Analytics**: State-level reform tools
- **PolicyTech**: Integration with court case management systems

## Real-World Examples

### Example: Illinois SB 2034 (Pretrial Fairness Act)
Illinois became first state to eliminate cash bail entirely. The PSA tool guides release decisions with three risk scores. Early data: pretrial detention reduced by 50%; court appearance rates maintained; racial disparities narrowed.

### Example: New Jersey Courts Pretrial Services
New Jersey implemented PSA-based release recommendations. Results: jail population reduced from 20,000 to 10,000; FTA rates stayed below pre-reform levels. Key: combination of algorithm + human review.

### Example: Algorithm Auditing in Wisconsin
State v. Loomis (2016) — Wisconsin Supreme Court upheld use of COMPAS but required it be used as one factor only, with human override mandatory. Created national standard: algorithms cannot be sole basis for any deprivation of liberty.

### Example: Federal Oversight (2022-2024)
The First Step Act requires federal algorithms to be validated for fairness. The EPA (Executive Office for the President) issued guidance requiring disparate impact analysis for all federal grantees using algorithmic tools.

## Key Controversies & Civil Rights Issues

**1. Data Bias Amplification**
Historical policing data reflects historical discrimination. A model trained on arrest data from over-policed neighborhoods will perpetuate those patterns. The feedback loop: more arrests → more data → more predictions → more arrests.

**2. Black Box Problem**
Courts cannot use tools they can't explain. COMPAS scores are proprietary, creating constitutional issues under "due process of law." Some states now require explainability.

**3. Disparate Impact vs. Intent**
Even without discriminatory intent, tools with 2x false positive rates for Black defendants violate equal protection. Audit requirements are now mandatory.

**4. Mass Incarceration Acceleration**
Predictive tools can justify more surveillance, not less — risk scores can be used to INCREASE bail, not just decrease it. Vigilant anti-corruption required.

## Implementation Approach

### Phase 1: Research & Validation
- Audit existing tools with AIF360/Fairlearn
- Analyze disparate impact in your specific jurisdiction
- Validate against local outcome data (reoffend, FTA rates)
- Test for calibration (are scores accurate probabilities?)

### Phase 2: System Design
- Build explainable models (XGBoost with SHAP values)
- Separate violent vs. non-violent risk scores
- Create calibration curves for each demographic group
- Build audit logging for every decision

### Phase 3: Deployment
- Human-in-the-loop requirement for all liberty decisions
- Real-time bias monitoring with dashboard alerts
- Integration with court case management
- Constitutional review by independent legal counsel

### Phase 4: Ongoing Auditing
- Monthly disparate impact reports
- Quarterly outcome tracking (do released defendants actually show up?)
- Annual third-party algorithm audits
- Publish methodology and validation data

## Key Insight
The goal of predictive policing tools should be liberation, not control. Bail reform tools are fundamentally different from surveillance tools. Build only tools that expand freedom with public safety — never tools that increase incarceration rates. The Arnold Foundation's model is the right template: open-source, validated, audited, with human discretion preserved.