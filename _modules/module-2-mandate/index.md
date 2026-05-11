---
title: "Module 2: Mandate"
has_children: true
nav_order: 2
permalink: /modules/module-2-mandate/
---

# Module 2: Mandate — From Theory to Law: California's Forced Sterilization Program

**Sessions 4–6** · **HCE concepts: Classification, Representation**

## What this module covers

Between 1909 and 1952, California forcibly sterilized over 20,000 people using standardized recommendation forms descended directly from Galton's measurement apparatus. The forms *did not include a race field*, so researchers had to invent a racial category after the fact, using Spanish surnames as a proxy.

The module introduces conditional probability, rate ratios, and the chi-squared test, including the **Pearson inversion**, in which students use Karl Pearson's own test (invented in 1900 to argue for racial hierarchies) to measure the racial harm of a eugenic policy. The module also introduces the distinction between a *measurement* and a *diagnosis*.

## Learning Objectives

By the end of this module, students will be able to:

1. Explain how eugenic theory crossed the Atlantic and became law in California through the Human Betterment Foundation, Charles Davenport, and the 1909 sterilization statute.
2. Read published summary statistics from a peer-reviewed public-health paper and reconstruct the comparisons it reports.
3. Compute and interpret **conditional probabilities**: P(sterilized | Latina) read aloud as "the probability of being sterilized given that you were Latina."
4. Compute and interpret a **rate ratio** (relative risk) and explain in plain English what a rate ratio of 1.59 means.
5. Apply Karl Pearson's **chi-squared test of independence** using `scipy.stats.chi2_contingency` and read the p-value correctly.
6. Distinguish *statistical significance* (was the pattern probably not chance?) from *effect size* (how big is the pattern?).
7. Reason about **proxy variables** (Spanish surname as a stand-in for Latina) and run a sensitivity analysis to see how categorization choices move a conclusion.
8. Distinguish a **measurement** (a reading from a calibrated instrument) from a **diagnosis** (a judgment recorded as data).
9. Explain what aggregate state data *reveals* and what it structurally *cannot show* about individual human lives, and why that matters for Module 3.

## Get started

- **For teachers** → [Lecture Guide](./lecture-guide/)
- **For students** → [Notebook](./notebook/)
- **Data Audit** → [Audit prompt and rubric](./data-audit/)

## Required readings

- Novak et al., ["Disproportionate Sterilization of Latinos Under California's Eugenic Sterilization Program, 1920–1945"](https://pmc.ncbi.nlm.nih.gov/articles/PMC5888070/), *AJPH* 2018
- Stern et al., ["California's Sterilization Survivors: An Estimate and Call for Redress"](https://pubmed.ncbi.nlm.nih.gov/27854540/), *AJPH* 2017

*Recommended:* Whatcott, [*Menace to the Future*, Prologue + Intro](https://dukeupress.edu/menace-to-the-future); HCE Toolkit — [Classification, Representation](https://data104.org/hce/)

## Inversion moment

**The proxy sweep.** Researchers identified Latina sterilization victims by Spanish surname, a decision made decades after the data was collected. Students vary the classification error rate of the proxy and watch the racial disparity estimate shift. The 1.59× disparity stays above 1.0 even at aggressive misclassification rates, but the precise number moves. Any reported figure depends on a categorization choice that is itself a research artifact.

## Data Audit #2

Applied to the sterilization dataset, with an explicit **cross-module synthesis** component: students compare the Galton dataset (Module 1) to the sterilization dataset (Module 2) under Classification and Representation. This is the course's single required piece of written cross-module synthesis, and it lives inside the audit rather than as a separate essay.
