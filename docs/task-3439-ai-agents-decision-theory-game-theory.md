# Decision Theory, Game Theory & Rational Choice

## Introduction

How should a rational agent make decisions under uncertainty? Decision theory and game theory provide the formal framework for understanding choice, strategy, and competition — and they're foundational to AI reasoning, economics, and political science.

## Decision Theory: The Science of Choice

### Normative Decision Theory

How *should* a rational agent decide? The standard model:

**Expected Utility Theory (EUT)**: A rational agent chooses the action that maximizes expected utility — the probability-weighted sum of utilities of possible outcomes.

Given a set of possible outcomes O, with probabilities P and utilities U, choose the action maximizing Σ P(o) × U(o).

**The axioms of rational choice**:
1. Completeness: The agent can compare any two outcomes
2. Transitivity: If A ≽ B and B ≽ C, then A ≽ C
3. Continuity: Certainty equivalents exist
4. Independence: If A ≽ B, then A with probability p ≽ B with probability p

Violations of these axioms reveal "irrational" behavior — but are they truly irrational, or is the theory too narrow?

### Descriptive Decision Theory

Actual human behavior deviates systematically from EUT. Amos Tversky and Daniel Kahneman's **Prospect Theory** showed:

- **Loss aversion**: Losses loom larger than equivalent gains (losses are ~2x more painful)
- **Reference points**: We frame outcomes relative to a status quo
- **Probability weighting**: We over-weight small probabilities, under-weight large ones
- **Framing effects**: The same objective choice is evaluated differently depending on framing

For AI: Building systems that model human users well requires accounting for these biases — not dismissing them as irrational.

### Challenges to Expected Utility

**The Allais Paradox**: Simple choices that violate the independence axiom. Real people prefer "guaranteed" options even when EUT says to gamble.

**Newcomb's Problem**: Two-boxers beat one-boxers by EUT logic, but one-boxers get more money. The problem is genuinely unresolved.

**The St. Petersburg Paradox**: A game with infinite expected value but finite rational value. Bernoulli's solution: diminishing marginal utility of money.

## Game Theory: Strategic Interaction

When multiple agents interact, decision theory becomes game theory.

### Basic Concepts

- **Zero-sum games**: One player's gain is another's loss (chess, poker)
- **Non-zero-sum games**: Mutual gains or mutual losses are possible
- **Nash Equilibrium**: No player can improve by unilaterally changing strategy
- **Pareto Efficiency**: No outcome can make someone better off without making someone worse

### Classic Games

**Prisoner's Dilemma**: The central puzzle of game theory. Two agents each have a dominant strategy (defect) that leads to a Pareto-inferior outcome (both cooperate would be better).

The resolution: **Reciprocal altruism**, **trigger strategies**, or **institutional enforcement** can sustain cooperation.

**The Tragedy of the Commons**: Garrett Hardin's insight: shared resources get depleted even when everyone would benefit from conservation. AI systems trained on common data resources face analogous collective action problems.

**Chicken**: Two cars drive toward each other; swerving is survival but shameful. Mutually exclusive — both swerve = survival, both straight = death, one swerves = one shame.

### Evolutionary Game Theory

Why do certain strategies persist? Evolutionary game theory applies game-theoretic reasoning to biological and cultural evolution:

- **Evolutionarily Stable Strategy (ESS)**: A strategy that, if adopted by a population, cannot be invaded by a mutant strategy
- **Replicator dynamics**: Strategies that outperform average spread; underperformers diminish

## Mechanism Design

Not just "how do players play?" but "how do we *design rules* so that rational self-interested agents produce desired outcomes?"

Key results:
- **Gibbard-Satterthwaite**: Under mild conditions, no voting system can be simultaneously strategy-proof, non-dictatorial, and have unlimited domain
- **Myerson's mechanism design**: The revelation principle — any mechanism can be converted to an incentive-compatible direct mechanism

### AI Applications

| Game Theory Concept | AI Application |
|--------------------|---------------|
| Nash equilibrium | Multi-agent AI systems |
| Mechanism design | Auction design, resource allocation |
| Contract theory | AI-human principal-agent relationships |
| Mechanism design | Incentivizing desired AI behavior |
| Signaling games | AI explanation and interpretability |

## Rational Choice AI

Building AI systems that make rational decisions requires:

1. **World models**: Accurate beliefs about the world
2. **Preference ordering**: A coherent utility function
3. **Reasoning under uncertainty**: Probabilistic reasoning
4. **Computational constraints**: Bounded rationality (Herbert Simon's insight: we satisfice, not optimize)

**Bounded Rationality**: Full rationality is computationally intractable for complex decisions. Herbert Simon's insight: humans and AI systems must use heuristics and satisficing strategies.

## Challenges

1. **The binding problem**: How can multiple AI agents commit to strategies when they can all defect?
2. **Counterfactual reasoning**: What would have happened if we chose differently?
3. **Preference aggregation**: How do we combine the preferences of multiple stakeholders?
4. **The alignment problem**: Whose utility function should an AI maximize?

## Resources

- Daniel Kahneman, *Thinking, Fast and Slow* (2011)
- Martin Osborne & Ariel Rubinstein, *A Course in Game Theory*
- Robert Aumann, *Game Theory* (collected papers)
- Herbert Simon, *Models of Bounded Rationality*
- Von Neumann & Morgenstern, *Theory of Games and Economic Behavior* (1944)
