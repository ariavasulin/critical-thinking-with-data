---
title: Lecture Guide
parent: "Module 2: Mandate"
nav_order: 1
permalink: /modules/module-2-mandate/lecture-guide/
---

# Lecture Guide — Module 2: Mandate

Module 2 turns the course from theory to history. The question shifts from "Where did these tools come from?" to **"What happened when eugenic theory became law?"** Students work with data from California's forced sterilization program (1909–1952), using statistical tools the eugenicists themselves built (conditional probability, rate ratios, Karl Pearson's chi-squared test) to measure the disparities those tools were meant to justify.

This guide covers three ~50-minute sessions (Hook → Core → Close) and includes narrative beats, board work, facilitation prompts, misconception watchlist, and the formal Data Audit #2 protocol.

## Module arc at a glance

- **Session 4 (Hook + Setup):** From theory to law; California's sterilization statute; introduce Representation.
- **Session 5 (Core Technical):** Conditional probability, rate ratios, chi-squared test; the Pearson inversion.
- **Session 6 (Close):** The proxy problem (sensitivity analysis); diagnosis vs. measurement; Data Audit #2 with cross-module synthesis.

## Learning goals

By the end of Module 2, students should be able to:

1. Explain how eugenic theory crossed the Atlantic and became law in California.
2. Compute and interpret conditional probabilities and rate ratios from published summary statistics.
3. Apply the chi-squared test using `scipy.stats.chi2_contingency` and read the p-value correctly.
4. Distinguish statistical significance from effect size.
5. Reason about proxy variables (Spanish surname → Latina) and run a sensitivity analysis.
6. Distinguish a measurement (a reading from a calibrated instrument) from a diagnosis (a judgment recorded as data).
7. Produce a short, evidence-based critique using the HCE concepts of Classification and Representation, with explicit cross-module comparison to Module 1.

## Session 4 — Hook + Setup (From Theory to Law)

### Session objective

Students understand how Galton's ideas traveled from a London exhibition booth to a California statute that authorized the forced sterilization of over 20,000 people, and why the records of those sterilizations are both essential to use and badly incomplete.

### Suggested flow (~50 min)

- **Hook (8 min):** Display the redacted sterilization recommendation form image from the notebook. Ask: "What kind of data does this form produce? What can it tell us? What can it never tell us?"
- **Context mini-lecture (12 min):** Galton → Davenport → the Human Betterment Foundation → California's 1909 statute. Emphasize the direct line from Module 1's "theory" to Module 2's "law." Show the Sonoma State Home photograph and Popenoe (1931) image for historical grounding.
- **Data discovery in pairs (15 min):** Students load the Stern and Novak datasets and examine their structure. Prompt: "These datasets were reconstructed by historians from institutional records decades after the sterilizations occurred. What does that mean for what the data can and cannot show?"
- **Whole-class synthesis (10 min):** Build class definition of **Representation** (how does data stand in for people?). Revisit **Classification** from Module 1; note that the sterilization forms did *not* include a race field.
- **Exit ticket (5 min):** "One thing this dataset structurally cannot show about the people it documents is ___ because ___."

### Board plan

- Left: **Key terms** — Representation, Classification (review), proxy variable, institutional record.
- Center: **Prompt** — "What does a standardized form make visible? What does it erase?"
- Right: **Tension statement** — "We have to read these records to know what happened. The same system that did the harm wrote them."

### Facilitation moves

- If students are uncomfortable with the content, name it directly: "This is difficult material. The discomfort is appropriate. Our job is to be precise, not detached."
- If students treat the data as abstract, redirect: "Approximately 831 survivors of this program were still alive in 2016. These are not historical abstractions."
- If students focus only on the numbers, ask: "Who filled out this form? Who authorized it? Who was the person on the other side of it?"

### Misconception watchlist

- "This couldn't happen today."
  Reproductive coercion in institutional settings has been documented as recently as the 2010s. The structural pattern persists.
- "The data is too old to matter."
  The data documents harm to real people, many of whose families are alive. Historical data analysis is an ethical act.
- "If it was legal, it was legitimate."
  Legality and legitimacy are not the same. The entire module is about what happens when unjust power is formalized in law.

### Homework

- Read Novak et al. (2018) abstract and methods section. Identify: (a) the primary finding, (b) the proxy variable used for race, and (c) one limitation the authors name.

## Session 5 — Core Technical (Conditional Probability, Rate Ratios, Chi-Squared)

### Session objective

Students compute conditional probabilities and rate ratios from the sterilization data, then apply Karl Pearson's own chi-squared test to quantify racial disparities in sterilization rates. They use the tools of eugenics to measure what eugenic policy actually did.

### Suggested flow (~50 min)

- **Do now (5 min):** Define in your own words: "What is a conditional probability? Give an everyday example."
- **Notebook build (25 min):** Step-by-step through conditional probability (`P(sterilized | Latina)` vs. `P(sterilized | non-Latina)`), rate ratio computation, and chi-squared test with `scipy.stats.chi2_contingency`. Students produce the contingency table and interpret the p-value.
- **Pearson inversion moment (10 min):** Name the irony explicitly: "Karl Pearson built the chi-squared test in 1900 to argue for racial hierarchies. You just used his test to measure the racial harm of a eugenic policy. The math is the same tool either way; what changes is who's using it and what they're using it to show."
- **Pair discussion (8 min):** "The rate ratio is 1.59×. Is that number *statistically significant* (the chi-squared test says yes)? Is it *large*? These are different questions. What's the difference between significance and effect size?"
- **Wrap (2 min):** "Name one thing the chi-squared test can tell you and one thing it cannot."

### Board plan

- Left: **Technical checkpoints** — conditional probability formula, rate ratio computation, contingency table, chi-squared output (χ², p-value).
- Center: **Inversion prompt** — "Pearson's test, built for eugenics, now measures eugenic harm."
- Right: **Claim template** — "The rate ratio of ___ means that ___, and the p-value of ___ means that ___."

### Facilitation moves

- When students compute the rate ratio, ask: "What does 1.59× mean in plain English? If you were explaining this to someone who has never taken a statistics course, what would you say?"
- When students see the p-value, ask: "Does this tell us *why* the disparity exists? Or only that it is unlikely to be chance?"
- Push students to distinguish between what the test proves and what it does not: statistical significance is not moral significance, and effect size is not the same as lived impact.

### Misconception watchlist

- "A small p-value means the effect is large."
  A small p-value means the pattern is unlikely to be chance. The rate ratio tells you the size.
- "The chi-squared test proves discrimination."
  The test detects a non-random association. Proving discrimination requires argument, not just a number.
- "If the numbers are right, the analysis is neutral."
  Every analytic choice (which category to use, which proxy to trust, which time period to examine) shapes the conclusion.

### Homework

- Draft a one-paragraph explanation of the Pearson inversion for a reader who knows what a chi-squared test is but doesn't know its history.

## Session 6 — Close (Proxy Problem + Diagnosis vs. Measurement + Data Audit #2)

### Session objective

Students run a sensitivity analysis on the Spanish-surname proxy variable, distinguish measurements from diagnoses, and complete Data Audit #2 with an explicit cross-module synthesis comparing the Galton dataset (Module 1) to the sterilization dataset (Module 2).

### Suggested flow (~50 min)

- **Launch (5 min):** Recap the rate ratio. Introduce the proxy problem: "Researchers identified Latina victims by Spanish surname. That was a choice made decades after the data was collected. How sensitive is the 1.59× finding to that choice?"
- **Sensitivity analysis (12 min):** Students vary the false-positive rate of the surname proxy and observe how the rate ratio shifts. Key takeaway: the disparity stays above 1.0 even at aggressive misclassification rates (that's robustness), but the precise number moves.
- **Diagnosis vs. measurement (8 min):** Students examine the top-10 diagnoses in the dataset (e.g., "feebleminded," "moron"). Ask: "Is 'feebleminded' a measurement like height, or a judgment written onto a form? What kind of data does a diagnosis produce, compared to the height data in Module 1?"
- **Bridge to Module 3 (5 min):** Read the closing passage of the notebook: "Those are aggregate counts. Things aggregate counts cannot show: a single face..." Ask: "If you wanted to show the people the counts can't, how would you do it with data?" (This bridges to Du Bois.)
- **Data Audit writing (17 min):** Formal three-question protocol: Classification (applied to sterilization data), Representation (applied to sterilization data), and a cross-module synthesis paragraph comparing Module 1 and Module 2 under Classification and Representation.
- **Closing reflection (3 min):** "What does this data reveal? What does it structurally conceal? Why does the gap matter?"

### Board plan

- Left: **Deliverables** — completed notebook through sensitivity analysis, 3-part audit.
- Center: **Feedback stems** — "The proxy matters because ___." / "A diagnosis differs from a measurement because ___."
- Right: **Quality bar** — each audit response cites concrete notebook evidence; the synthesis paragraph explicitly compares Modules 1 and 2.

### Facilitation moves

- During the sensitivity analysis, ask: "Does the uncertainty in the proxy mean we shouldn't use it? Or does it mean we should report the range?"
- When discussing diagnoses, push students to name the power asymmetry: "Who wrote the diagnosis? Did the person diagnosed have any say?"
- During audit writing, require students to use evidence from *both* modules in the synthesis paragraph.

### Misconception watchlist

- "If the proxy is imperfect, the finding is invalid."
  An imperfect proxy means you have a range to report, not nothing to report. The sensitivity analysis tells you how wide that range is; it doesn't tell you to throw the evidence out.
- "A diagnosis is a fact."
  A diagnosis is a judgment made by a person in a position of power, recorded on a form. It reflects the diagnostic categories available at the time, not an objective truth.
- "Aggregate data tells the whole story."
  Aggregate counts reveal patterns. They cannot show individual experience, resistance, or survival. Both levels of analysis matter.

## Data Audit #2 implementation notes

- This is the second audit. Remove the worked example from the prompt; students should now apply the concepts independently.
- Three parts: Classification (sterilization data), Representation (sterilization data), and a cross-module synthesis paragraph comparing the Galton dataset (Module 1) to the sterilization dataset (Module 2) under Classification and Representation.
- The synthesis paragraph is the course's single required piece of written cross-module comparison. It should be 5–8 sentences.
- Require students to cite evidence from both modules in the synthesis.
- Suggested scoring: 1-4 per question (two questions + one synthesis), aligned to concept accuracy + evidence specificity + comparative precision.

## Materials and prep checklist

- Projector-ready images: sterilization recommendation form, Sonoma State Home, Popenoe (1931), Carrillo (AB 1764 author).
- Module 2 notebook pre-run through all cells once for sanity checks.
- Printed or digital Data Audit #2 prompt and rubric.
- Content note for students: distribute at beginning of Session 4, as specified in the notebook.
- Timer for pair discussions and audit writing.

## Required readings

- Novak et al., ["Disproportionate Sterilization of Latinos Under California's Eugenic Sterilization Program, 1920–1945"](https://doi.org/10.2105/AJPH.2018.304369), *AJPH* 2018
- Stern et al., ["California's Sterilization Survivors: An Estimate and Call for Redress"](https://doi.org/10.2105/AJPH.2016.303489), *AJPH* 2017

*Recommended:* Whatcott, *Menace to the Future*, Prologue + Intro; HCE Toolkit — [Classification, Representation](https://data104.org/hce/).
