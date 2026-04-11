# Philosophy of Science & Theory Confirmation

## Introduction

When we say a scientific theory is "confirmed," what do we mean? And how does AI learn from data in ways that mirror (or diverge from) scientific reasoning? Philosophy of science offers the conceptual toolkit to answer these questions.

## The Problem of Induction

David Hume (1711–1776) identified a foundational problem: no finite set of observations can logically entail a universal generalization. Seeing one million white swans doesn't *prove* all swans are white.

This is the **problem of induction** — and it's central to understanding both scientific methodology and machine learning.

## Key Philosophers and Their Contributions

### Karl Popper (1902–1994): Falsificationism

Popper proposed that science doesn't confirm theories — it *fails to refute* them. A theory is scientific only if it's falsifiable.

**Implication for AI**: Overfitting to training data is the ML equivalent of pseudoscience — fitting noise rather than discovering signal. Good generalization = surviving diverse falsification attempts.

### Thomas Kuhn (1922–1996): Paradigms and Revolutions

Science doesn't progress smoothly. Instead, it alternates between periods of **normal science** (puzzle-solving within a paradigm) and **scientific revolutions** (paradigm shifts). Copernicus → Newton → Einstein.

**Implication for AI**: The "AI paradigm shifts" (perceptrons → deep learning → transformers → diffusion) mirror Kuhnian revolutions.

### Imre Lakatos: Research Programmes

Theories don't exist in isolation — they come in "research programmes" with a hard core of protected beliefs and a protective belt of auxiliary hypotheses. Progress = programmes that predict novel facts.

### Bayesian Confirmation Theory

Modern philosophy of science has largely embraced Bayesianism: a theory T is confirmed by evidence E in proportion to how much E would increase our credence in T.

> P(T|E) = P(E|T) × P(T) / P(E)

This is remarkably close to how modern AI systems update beliefs — and how they *should* reason under uncertainty.

## Theory Confirmation in the Age of AI

AI systems face the confirmation problem acutely:

1. **Overfitting**: ML models that "confirm" their training data too precisely
2. **Underdetermination**: Many models fit the same data; which one is "true"?
3. **Novelty detection**: Scientific progress requires predicting *new* phenomena

## The No Free Lunch Theorem

Wolpert and Macready's No Free Lunch theorem states that no learning algorithm is universally better than any other when averaged over all possible problems. This is a formal version of Hume's problem of induction applied to ML.

## Falsification in ML: Cross-Validation

Just as Popper demanded falsifiability, ML practice demands out-of-sample testing:

| Method | Popperian Parallel |
|--------|-------------------|
| Training set | Preliminary experiments |
| Validation set | Attempted falsifications |
| Test set | Final critical test |
| Regularization | Protecting core beliefs from ad-hoc modifications |

## Challenges for AI Science

1. **Black-box models**: Deep learning is notoriously uninterpretable — can we confirm what they've learned?
2. **Extrapolation vs. interpolation**: Models that work in-distribution may fail out-of-distribution
3. **Statistical vs. causal**: Correlation is not confirmation of causation — but how do we distinguish?

## Tools & Concepts

| Concept | Description |
|---------|-------------|
| Popperian Falsification | Science proceeds by failed refutations |
| Bayesian Confirmation | Evidence updates credence via Bayes' theorem |
| Inference to the Best Explanation | We accept the explanation that best unifies phenomena |
| Occam's Razor | Prefer simpler theories that explain equally well |
| Novel Prediction | A theory is strong if it predicts surprising new facts |

## The Future: AI as Scientist

Systems like **Berkeley's AI scientist**, **GNoTOMY**, and **AlphaFold** suggest AI can participate in scientific discovery. The question is whether current systems can go beyond curve-fitting to genuine theory formation.

## Resources

- Carl Hempel, *Philosophy of Natural Science*
- Bas van Fraassen, *The Scientific Image*
- Earman & Salmon, *Introduction to Philosophy of Science*
- The Stanford Encyclopedia of Philosophy (plato.stanford.edu) — Philosophy of Science entries
