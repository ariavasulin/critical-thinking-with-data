---
title: Lecture Guide
parent: "Module 1: Measure"
nav_order: 1
permalink: /modules/module-1-measure/lecture-guide/
---

# Lecture Guide — Module 1: Measure

Module 1 opens the course arc by asking a deceptively simple question: **where did the statistical tools we use every day actually come from — and what were they built to do?** Students work with Galton's original 1886 height dataset, learn correlation and regression, and discover that the math itself undermined its inventor's eugenic thesis through regression to the mean.

This guide covers three ~50-minute sessions (Hook → Core → Close) and includes narrative beats, board work, facilitation prompts, misconception watchlist, and the formal Data Audit #1 protocol.

## Module arc at a glance

- **Session 1 (Hook + Setup):** London 1884; who paid three pence to be measured; introduce Classification and Performativity.
- **Session 2 (Core Technical):** EDA, correlation, regression, and the discovery of regression to the mean.
- **Session 3 (Close):** The 1.08 transmutation toggle; formal Data Audit #1 using Classification and Performativity.

## Learning goals

By the end of Module 1, students should be able to:

1. Explain the historical origins of correlation, regression, and the standard deviation, and connect them to the eugenics movement.
2. Load a dataset and produce basic descriptive statistics (mean, median, standard deviation) using Python.
3. Identify sampling bias in a dataset and explain what populations are over- or under-represented.
4. Interpret a correlation coefficient and distinguish correlation from causation.
5. Define "regression to the mean" and explain why it mattered — and why it quietly demolished Galton's eugenic thesis.
6. Describe Galton's "transmutation" of female heights by 1.08 and explain why it is both methodologically and ethically problematic.
7. Produce a short, evidence-based critique using the HCE concepts of Classification and Performativity.

## Session 1 — Hook + Setup (London, 1884)

### Session objective

Students understand who Galton was, what he was trying to prove, and why the identity of the people who paid three pence to be measured matters for every conclusion drawn from their data.

### Suggested flow (~50 min)

- **Hook (8 min):** Display the first five rows of the Galton dataset with no context. Ask: "What can you learn from these four columns? What can you *not* learn?"
- **Context mini-lecture (12 min):** Francis Galton, the International Health Exhibition, the coining of "eugenics" (1883), and the Anthropometric Laboratory as a class- and race-bounded convenience sample.
- **Close reading in pairs (15 min):** Students examine the `.describe()` output and gender breakdown. Prompt: "The father height range is 62″–78.5″. Modern US adult males range roughly 59″–80″. What does the narrow range tell us about who showed up?"
- **Whole-class synthesis (10 min):** Build class definitions of **Classification** (who set the categories? what's counted?) and **Performativity** (does the measurement change what it claims to describe?).
- **Exit ticket (5 min):** "One thing this dataset cannot tell us about the people it contains is ___ because ___."

### Board plan

- Left: **Key terms** — Classification, Performativity, convenience sample, sampling bias.
- Center: **Prompt** — "Who paid three pence? Who didn't? Why does it matter?"
- Right: **Tension statement** — "The math works. The sample doesn't represent the world. Both are true."

### Facilitation moves

- If students say "it's just height data," redirect: "Whose heights? Collected for what purpose? What was Galton hoping to prove?"
- If students focus on the numbers only, ask: "What populations are structurally absent from this dataset?"
- Resist resolving the tension between useful math and biased origins — that tension is the pedagogical engine of the entire course.

### Misconception watchlist

- "Old data is automatically bad data."
  The data is real and the math works; the problem is what it cannot represent.
- "Bias means the numbers are wrong."
  The numbers are accurate for the sample — the bias is in who the sample includes.
- "If the math works, the origins don't matter."
  Module 1 exists to show that origins shape what conclusions are possible.

### Homework

- Read assigned selections from Clayton, *Bernoulli's Fallacy*, Ch. 3, and identify one sentence that connects to sampling bias in the Galton dataset.

## Session 2 — Core Technical (Correlation, Regression, Regression to the Mean)

### Session objective

Students compute correlation and regression on the Galton dataset and discover regression to the mean — the finding that quietly undermined Galton's eugenic thesis.

### Suggested flow (~50 min)

- **Do now (5 min):** Predict: "If a father is 6 inches taller than average, how much taller than average do you expect his son to be?" Write down a number.
- **Notebook build (25 min):** Step-by-step through EDA, correlation heatmap, scatter plots with regression lines (child vs. father, child vs. mother, child vs. mid-parent height).
- **Discovery moment (10 min):** Students compare their prediction to the regression slope. The slope is less than 1 — tall parents produce children who are tall but *less extreme*. Walk through regression to the mean with the worked example in the notebook.
- **Pair discussion (8 min):** "If traits always regress toward the mean, can selective breeding produce a permanently 'superior' population? What does the math say about Galton's own argument?"
- **Wrap (2 min):** Name one finding from today that surprised you and one question it raises for Session 3.

### Board plan

- Left: **Technical checkpoints** — `.describe()`, `.corr()`, scatter + regression line, slope interpretation.
- Center: **Discovery prompt** — "The slope is less than 1. What does that mean for Galton's thesis?"
- Right: **Claim template** — "Regression to the mean shows that ___, which undermines the eugenic claim that ___."

### Facilitation moves

- When students see the correlation, ask: "Correlation tells us *that* two things move together. Does it tell us *why*?"
- After the regression slope, ask: "If Galton's thesis were correct, what slope would you expect? What slope did he get?"
- Encourage students to articulate the irony: the inventor of regression analysis was undone by regression to the mean.

### Misconception watchlist

- "Correlation means causation."
  This is the single most important distinction in the module. Name it explicitly and repeatedly.
- "Regression to the mean is about decline."
  It's about statistical reversion, not biological degeneration. Galton's own word ("mediocrity") was misleading.
- "If the slope is positive, Galton was right."
  The slope is positive *and* less than 1. Both facts matter. Height is heritable *and* regresses.

### Homework

- Read Gorroochurn (2016) and identify the passage where Galton changes his terminology from "reversion" to "regression." Why did the name change matter?

## Session 3 — Close (The 1.08 Toggle + Data Audit #1)

### Session objective

Students examine Galton's transmutation of female heights, toggle the 1.08 multiplier on and off, observe the regression line shift, and complete Data Audit #1 using Classification and Performativity.

### Suggested flow (~50 min)

- **Launch (5 min):** Recap regression to the mean. Introduce the problem: "Galton wanted one regression line for the whole population. But male and female height distributions are different. What did he do?"
- **Notebook exploration (15 min):** Students run the transmutation section — multiplying female heights by 1.08 and observing the scatter plot with and without the multiplier. Side-by-side display.
- **Discussion (12 min):** "The line moved. The world didn't change. A methodological choice moved it." Students articulate what the 1.08 factor assumes about female bodies and why treating it as a neutral correction is problematic.
- **Data Audit writing (15 min):** Formal two-question protocol (Classification and Performativity) applied to the Galton dataset. This is the first audit and is scaffolded with vocabulary definitions and a worked example.
- **Closing reflection (3 min):** "When data is collected to justify control over people's bodies, what responsibility do analysts have when they use that data decades later?" (This question bridges directly to Module 2.)

### Board plan

- Left: **Deliverables** — completed notebook through transmutation, 2-question audit.
- Center: **Inversion prompt** — "Same data, different multiplier, different line. What changed?"
- Right: **Quality bar** — each audit response cites concrete notebook evidence (a number, a chart, a code step).

### Facilitation moves

- If students say 1.08 is "just a correction factor," ask: "Correction toward what? Whose height is the standard?"
- When students write audit responses, push beyond labels: "You named a classification. Now name what it makes invisible."
- Use one anonymized exemplar response to calibrate expectations before submission.

### Misconception watchlist

- "The 1.08 multiplier is a standard scientific adjustment."
  It is a methodological choice that encodes an assumption about whose body is the default.
- "Performativity is just about language."
  In this module, a numeric transformation *performs* a claim about gender equivalence.
- "The audit is opinion."
  Audit claims must cite specific data, charts, or code output.

## Data Audit #1 implementation notes

- This is the first audit. Scaffold it: provide the vocabulary definitions for Classification and Performativity on the prompt sheet, and include one worked example response.
- Require students to cite at least one specific number, chart, or code output from their notebook in each response.
- Suggested scoring: 1-4 per question, aligned to concept accuracy + evidence specificity.
- Two questions only (Classification and Performativity) — keep the bar achievable so students build confidence for Audit #2.

## Materials and prep checklist

- Projector-ready display of the raw Galton dataset (first 5 rows, no context).
- Module 1 notebook pre-run through all cells once for sanity checks; ensure `figures/` directory images are generated.
- Side-by-side display template for transmutation on/off comparison.
- Printed or digital Data Audit #1 prompt, rubric, and worked example.
- Timer for pair discussions and quick transitions.

## Required readings

- Aubrey Clayton, [*"How Eugenics Shaped Statistics"*](./extra/reading1_guide/)
- Greenwood, C. J., Bhavnani, R., & Harmon, K., [*"Teaching the Difficult Past of Statistics"*](./extra/reading2_guide/)

*Recommended:* James Hanley, "'Transmuting' Women into Men"; HCE Toolkit — [Performativity](https://data104.org/hce/).
