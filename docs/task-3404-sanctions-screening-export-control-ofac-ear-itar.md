# Task 3404: Sanctions Screening & Export Control — OFAC, EAR, ITAR

## Context
AI systems that screen individuals and entities against sanctions lists, detect export control violations, and ensure compliance with OFAC, BIS (EAR), and State Department (ITAR) regulations.

## Market Analysis

Global sanctions activity exploded post-2022: OFAC added 3,500+ new designations in 2022-2023, EU added 2,000+, UK added 800+. The total cost of sanctions compliance for financial institutions is estimated at $20B annually. False positive rates in manual screening run 60-80%, creating massive compliance bottlenecks. The US Treasury's FinCEN estimates $2.6T in money laundering annually — sanctions screening is the front line.

The export control regime (EAR/ITAR) governs dual-use technologies. BIS's Entity List now has 6,000+ entries. Violations carry fines up to $20M per incident or twice the transaction value. Criminal penalties include up to 20 years imprisonment. Russia sanctions enforcement (post-2022 Ukraine invasion) has become the largest in US history.

Key players: Dow Jones (Factiva/IDN screening), LexisNexis (Nexis screening), Refinitiv (World-Check, 300M+ screened entities), ComplyAdvantage (AI-powered, 2M+ sanctions hits), Oracle Financial Services (FCCM), AML Dynamics. The legacy players (World-Check, Dow Jones) are being disrupted by AI-native screening tools with better false positive rates.

## Technical Implementation

### Sanctions Screening Architecture
```
Transaction/Party → Name Matching Engine → 
Entity Resolution → List Cross-reference → 
Risk Scoring → Alert Triage → 
Investigator Review → Disposition Logging
```

**Name Matching (Critical)**:
- Soundex, Metaphone, and Levenshtein distance for phonetic matching
- Generative AI for synonym and language-variant matching (e.g., "Kremlin" vs "Роском")
- ML classifiers trained on true positive/negative matches
- Handles: transliteration variations, incomplete names, name order changes, shell company names

**Entity Resolution**:
- Know Your Customer (KYC) data matched against sanctions lists
- Fuzzy matching with confidence scores
- Geographic risk scoring
- Ownership structure analysis (for sanctioned oligarchs' companies)

### OFAC SDN List Structure
- **SDN (Specially Designated Nationals)**: Blocked assets, no transactions
- **Consolidated Sanctions List**: 35,000+ entries (individuals, entities, vessels)
- **Sectoral Sanctions Identifications (SSI)**: Russian finance, energy, defense sectors
- **Foreign Sanctions Evaders (FSE)**: Proliferators and evaders
- **Palestinian Legislative Council (PLC)**: Hamas affiliates

### EAR (Export Administration Regulations)
- **CCL (Commerce Control List)**: 10 categories (nuclear, missile tech, etc.)
- **EAR99**: Items not on CCL but still subject to anti-terrorism controls
- **Entity List**: Foreign parties requiring license for specific exports
- **Denied Persons List**: Prohibited from receiving exports
- **Unverified List**: BIS cannot confirm reliability of end user

### ITAR (International Traffic in Arms Regulations)
- **USML (U.S. Munitions List)**: 21 categories of defense articles
- **DDTC (Directorate of Defense Trade Controls)**: Licenses for defense exports
- **Technical Data controls**: Even emails about ITAR-tech require classification

### AI Techniques Used
1. **NLP for regulatory text analysis**: Parse OFAC guidance, BIS regulations, statutory changes
2. **Graph neural networks**: Map corporate ownership structures for sanctions evasion
3. **Anomaly detection**: Flag unusual transaction patterns indicating sanctions evasion
4. **Generative AI**: First-pass legal review of compliance flags

### Tools & Platforms
- **ComplyAdvantage**: AI screening with 99.7% match accuracy, 85% fewer false positives
- **Refinitiv World-Check**: 300M+ entities, 1,000+ sanctions lists
- **LexisNexis Nexis**: 40,000+ news sources for adverse media screening
- **Oracle FCCM**: Enterprise financial crime and compliance
- **Quantexa**: Entity resolution and graph analytics for sanctions
- **AML Analytics**: Machine learning for transaction monitoring

## Real-World Examples

### Example: Russian Oligarch Asset Freezing
Post-2022 sanctions froze $300B+ in Russian central bank assets. Banks used AI to:
- Screen all existing customers against expanded Russian sanctions list
- Identify shell companies owned by sanctioned oligarchs
- Map ownership chains across 50+ jurisdictions
- Flag new accounts opened by proxies within 48 hours of designation

### Example: Dual-Use Export Control (China Entity List)
A semiconductor equipment manufacturer must check all customers:
- Is the customer on Entity List? (requires license, likely denied)
- Is the customer a "military end user"? (MEU check)
- Is the item on CCL with China as a destination? (license required)
- AI system automates this check across 10,000+ orders daily

### Example: Maritime Sanctions Evasion
Russian oil tankers use "ship-to-ship transfers" and "ghost fleet" vessel spoofing to evade sanctions. AI combines:
- AIS (Automatic Identification System) data
- Satellite imagery (SAR/Radar) for dark vessel detection
- Port authority data for ship matching
- Financial transaction analysis for payment trails

### Example: Financial Institution Screening (600M Transactions/Day)
A large bank processes 600M transactions daily. AI screening:
- Hardware-accelerated name matching (FPGA/ASIC)
- Real-time KYC/AML checks against sanctions lists
- Graph analysis for counter-party risk
- False positive rate reduced from 70% to 12% with AI

## Implementation Approach

### Phase 1: Core Screening Engine
- Deploy name matching engine with ML classifiers
- Build entity resolution pipeline
- Integrate all sanctioned party lists (OFAC, UN, EU, UK, BIS)
- Real-time transaction screening with sub-100ms latency

### Phase 2: Export Control Module
- CCL/CCAT classification engine
- Entity List, Denied Persons screening
- License determination workflow
- Technical data control classification

### Phase 3: Advanced Analytics
- Corporate ownership graph for UBO (Ultimate Beneficial Owner) analysis
- Adverse media screening (KPress, Factiva integration)
- Transaction pattern anomaly detection
- Real-time regulatory change monitoring and alert system

### Phase 4: Enterprise Integration
- SWIFT/FIS messaging integration
- Core banking system integration
- ERP (SAP/Oracle) integration for export control
- Board-level compliance dashboards

## Key Insight
Sanctions compliance is a data quality and speed problem, not a legal knowledge problem. The legal framework is clear — the execution is everything. The competitive moat is in the name matching accuracy and entity resolution graph. A system that catches 99% of true positives with 5% false positives beats a legal expert who reviews slowly. Build for speed, precision, and audit trail — every decision must be defensible to regulators 10 years later.