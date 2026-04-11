# Task 3401: Legal Reasoning — Case-Based Precedent Mapping

## Context
AI that maps legal precedents by analyzing case relationships, outcome patterns, and judicial reasoning chains.

## Market Analysis

The legal AI market is valued at $3.2B (2024) and projected to reach $10.8B by 2030 (CAGR 22.3%). Legal research automation is the fastest-growing segment, with firms spending $21B annually on research. Westlaw and LexisNexis dominate with 60%+ market share, but both are showing age — their AI features are bolted-on rather than原生 AI-native. Startups like CaseText (acquired by Thomson Reuters for $650M), Equivio, and Kira Systems are capturing the premium law firm market.

Case-based precedent mapping is particularly underserved. Most tools show you a single case; the real power is in tracing how a line of cases evolved across decades. Associates spend 6-12 hours per case on this research — AI can compress that to minutes.

## Technical Implementation

### Core Architecture
```
Query → Case Retrieval (vector search) → Relationship Graph Builder → 
Outcome Classifier → Precedent Strength Scorer → Visualization Layer
```

### Data Sources
- **CourtListener API** (free, CC0 case law) — 10M+ opinions
- **Westlaw/Lexis API** (paid, premium) — authoritative citations
- **Google Scholar** (scraping risk) — historical cases
- **State court databases** (individual state APIs)

### Key AI Techniques
1. **Embedding-based retrieval**: Fine-tune legal BERT models (e.g., Lawinstruct, MultiLegalBERT) on case embeddings for similarity search
2. **Outcome classification**: Binary (win/loss) and multi-class (affirmed/reversed/remanded) classifiers trained on labeled outcomes
3. **Legal relationship extraction**: NER for parties, judges, statutes cited; coreference resolution for case references
4. **Reasoning chain extraction**:链式推理 for how courts distinguished/followed prior cases
5. **Precedent strength scoring**: Based on jurisdiction, court level, subsequent treatment, citations received

### Tools & Libraries
- **LangChain/LlamaIndex**: RAG pipelines for case retrieval
- **NetworkX**: Relationship graph construction
- **spaCy**: Legal NER and relationship extraction
- **Plotly/D3.js**: Interactive precedent visualization
- **Neo4j**: Graph database for storing case relationships

### Specific Companies
- **CaseText (CaseMatrix AI)**: Real-time case analysis, $400/user/month
- **Reed Group**: Labor and employment law precedents
- **Lexis+**: AI-assisted legal research with "Shepard's" citation analysis
- **Westlaw Edge**: "KeyCite" AI for negative treatment detection
- **Given** (YC-backed): Contract reasoning AI
- **Harvey AI**: General legal AI for AmLaw 100 firms

## Real-World Examples

### Example: Personal Injury Case Research
A personal injury attorney needs to establish "proximate cause" precedent in California. The AI:
1. Queries court databases for "proximate cause" + "California" + "personal injury"
2. Returns 200+ cases, clustered by outcome (plaintiff win vs. defendant win)
3. Maps the strongest cases into a reasoning chain: 2010 landmark → 2015 CA Supreme Court extension → 2022 appellate limitation
4. Surfaces distinguishing cases that cut against the theory
5. Generates a memo with live case citations and strategic notes

### Example: Contract Dispute Precedent
In a breach of contract case, the AI maps how courts interpreted "material breach" across 50 years — showing a trend toward stricter standards in commercial contracts post-2008 financial crisis.

### Example: Constitutional Law Evolution
Tracking how courts have interpreted the Commerce Clause across 200+ Supreme Court cases, identifying cyclical patterns and current trajectory.

## Implementation Approach

### Phase 1: Foundation (Week 1-2)
- Set up CourtListener API integration
- Deploy vector database (Weaviate or Qdrant)
- Build basic case search with TF-IDF and embedding hybrid
- Simple outcome classifier (label existing case data)

### Phase 2: Graph Engine (Week 3-4)
- Build citation graph using Casey (CourtListener's graph database)
- Implement relationship extraction (cited by → cited by → treatment relationships)
- Visualize with D3.js force-directed graph
- Precedent strength algorithm based on Citation network analysis

### Phase 3: Intelligence Layer (Week 5-6)
- Fine-tune legal embedding model on practice-area-specific data
- Chain-of-thought reasoning for distinguishing analysis
- Auto-generate research memos with live citations
- Alert system for new cases affecting existing precedents

### Phase 4: Production
- Multi-jurisdiction support
- Real-time case alerts (docket tracking integration)
- Client portal with case status visualization
- Integration with Clio, Practice Management software

## Key Insight
The moat isn't the AI — it's the relationship graph. Anyone can build a case search. The defensible advantage is the provenance chain: knowing not just what cases say, but how they relate to each other over time, which courts are citing which precedents, and where the doctrine is heading. Build the graph first, layer intelligence on top.