---
title: Pedagogy
nav_order: 3
permalink: /pedagogy/
---

# Pedagogy

## HCE Toolkit

The course adopts the Human Contexts and Ethics Toolkit developed at UC Berkeley (see [data104.org/hce](https://data104.org/hce/)), which provides a shared theoretical vocabulary for Data C104 (Human Contexts and Ethics of Data) and Data C4AC (Data and Justice). Because this curriculum is designed to prepare students for those college-level courses, we adopt the HCE concepts directly (introduced at a high-school-appropriate level) rather than inventing new frameworks.

Four HCE concepts structure the three-module arc. Each is introduced in its own module and returns in later modules in new technical contexts. This recurrence is the curriculum's bridging mechanism: students see the same concept operate differently across cases, and the differences are what teach.

| HCE Concept | Definition (from the HCE Toolkit) | Introduced in | Returns in |
|---|---|---|---|
| **Classification** | "Implicit and explicit social organization of beings and knowledge into discrete categories." | Module 1 (Galton's gender binary, class sampling) | Module 2 (Spanish-surname proxy; diagnostic categories) |
| **Performativity** | "The way that actions that describe the world can shape and even bring into being the very phenomena they set out to describe." | Module 1 (the 1.08 transmutation, regression to mean) | Module 2 (eugenic measurement made sterilization policy thinkable) |
| **Representation** | "The way in which one thing is made to 'stand for' another." | Module 2 (aggregate statistics standing for 20,000 individuals) | Module 3 (Du Bois's plates as community self-representation) |
| **Agency** | "The ability or capacity to act or exert power." | Module 3 (Du Bois's "insider citizen researchers") | Data Audits (students producing their own analytic framings) |
| **Narratives** | "Stories in time that express and explain things that matter to people." | *Not a core focus in this course* | *Not a core focus in this course* |
| **Vulnerability** | "Disproportionate susceptibility to harm." | *Not a core focus in this course* | *Not a core focus in this course* |
| **Power** | "The influence or control over the behavior of people or systems." | *Not a core focus in this course* | *Not a core focus in this course* |
| **Identity/Positionality** | "The social and political context that creates one's identity." | *Not a core focus in this course* | *Not a core focus in this course* |
| **Co-production** | "The simultaneous and reciprocal shaping of science/technology and society." | *Not a core focus in this course* | *Not a core focus in this course* |
| **Labor** | "The human effort, both visible and invisible, required to produce technologies." | *Not a core focus in this course* | *Not a core focus in this course* |
| **Sociotechnical Systems** | "The entangled material and social components of any system." | *Not a core focus in this course* | *Not a core focus in this course* |

These additional HCE concepts appear as secondary lenses throughout the modules, but the core four (Classification, Performativity, Representation, Agency) are the only ones assessed in the recurring data audits.

---

## The Data Audit (recurring assessment)

Every module ends with a Data Audit, the same structured four-question response, applied to the dataset the module worked with. The audit is the course's single most important habit and happens three times (end of Modules 1, 2, and 3).

For every dataset, students write 2–4 sentences with specific evidence from the notebook answering:

1. **Classification**: What categories does this data use? Who decided them? What gets counted, and what is absent or invisible?
2. **Performativity**: What does this data set out to describe? What does it bring into being through the act of describing?
3. **Representation**: How does this data "stand for" the people in it? Whose work went into the representation? What does the representation do that the people couldn't?
4. **Agency**: Who produced this data? Whose agency does it amplify, and whose does it constrain?

**Rubric:** Each question is scored 1–4 based on (a) whether the student cited specific evidence from their own notebook output and (b) whether the response engages the HCE concept as defined, not in a generic way. A full rubric is included with the audit prompt.

The audit is first introduced as *vocabulary* in Module 1 (Classification, Performativity), expanded in Module 2 (Representation), and formalized as a four-question protocol in Module 3. By the end of the course, students have completed the audit three times, once per module.

---

## Technical Skills Progression

Technical skills accumulate across the three modules. No skill is taught twice; skills introduced earlier are invoked by name in later modules and extended.

| Skill | Module 1 (Galton) | Module 2 (Sterilization) | Module 3 (Du Bois) |
|---|---|---|---|
| Python / Jupyter basics |  Introduced (M1-S1) |  |  |
| pandas DataFrames | Introduced | ↩ Invoked | ↩ Invoked |
| Descriptive statistics | Introduced | ↩ Invoked |  |
| Histograms, box plots | Introduced | ↩ Extended (age-at-sterilization) |  |
| Scatter plots | Introduced |  | ↩ Invoked |
| Correlation (Pearson's *r*) | Introduced |  |  |
| Linear regression, residuals | Introduced |  |  |
| Regression to the mean | Introduced |  |  |
| Conditional probability |  | Introduced |  |
| Base rates & rate ratios |  | Introduced |  |
| Contingency tables |  | Introduced |  |
| Chi-squared test |  | Introduced (Pearson inversion) |  |
| Sensitivity analysis |  | Introduced |  |
| Time series plotting |  | Introduced |  |
| Custom color palettes |  |  | Introduced |
| Visual rhetoric (scale, composition) |  |  | Introduced |
| Counter-visualization |  |  | Introduced |

Because the course assumes no prior programming, Module 1 Session 1 includes a light Python/Jupyter primer embedded in the notebook, enough to load a CSV, run a cell, and read a DataFrame. Students finish the course with the working vocabulary of introductory statistics and real comfort with a subset of pandas and matplotlib, enough to enter Data 8 ahead of peers with no Python background.

---

## Cross-Module Bridges

Three places in the course where students are explicitly required to use what they learned earlier on material they have just encountered. These are the mechanism of bridging: they do not live in reflection prompts, they are structural requirements.

### Bridge 1: Module 1 → Module 2 (opens Module 2)

Module 2 opens with a cold re-audit of the Galton dataset using the concept of **Classification** (which students just introduced in Module 1) and then immediately introduces a new question: what happens when the people classifying have state power to act on the classification? The sterilization data answers that question. Students discover something uncomfortable: even when we *want* to use Galton's inferential tools against eugenic policy, we can't, because the forms the state used to record sterilizations *did not include a race field*. Eugenic categorization decisions, made decades earlier, shaped what we can ever know through this data. The HCE concept of Classification does not stay stable across the modules; it deepens.

### Bridge 2: Module 2 → Module 3 (opens Module 3)

Module 3 opens with the question Module 2 left unanswered: aggregate state data told us 20,000 people were sterilized, but it cannot show us a single face, a single refusal, a single life. What does it look like to produce data differently? Module 3 answers with Du Bois, who faced the same question in 1900: how do you challenge racial science with data without reducing people to statistics? His answer: community members as researchers, rhetorical choices as argument, hand-drawn plates as art. The HCE concept of **Representation**, introduced in Module 2 as the problem of aggregation, returns in Module 3 as the possibility of self-representation. The introduction of **Agency** at this moment is the course's final conceptual shift: the first two modules asked what data does *to* people; the last asks what people *do* with data.

### Bridge 3: Module 2 Data Audit (Cross-Module Synthesis)

The Module 2 Data Audit explicitly requires students to compare the Galton dataset (Module 1) to the sterilization dataset (Module 2) under the concepts of Classification and Performativity. This is the course's single required piece of written cross-module synthesis, and it lives inside the audit rather than as a separate essay.

---

## Data Inversion

Each module contains at least one toggle in code whose output changes the student's interpretation of the entire analysis. These exist because ethical takeaways must live in the technical work, not alongside it.

| Module | Inversion Moment | HCE Concept It Demonstrates | What Shifts |
|---|---|---|---|
| 1. Galton | Toggle the 1.08 female-height multiplier on/off | Performativity + Classification | The regression line changes because a methodological choice (not a fact about the world) has changed. Students see that the "single universal law" Galton promoted required erasing sex differences. |
| 2. Sterilization | Vary the Spanish-surname proxy classification error rate | Classification | The 1.59× disparity remains above 1.0 even at aggressive misclassification (teaching robustness), but its precise value moves, teaching that any single reported number depends on a categorization decision made decades after the data was collected. |
| 3. Du Bois | Re-render Plate 25 with matplotlib defaults (no custom palette, linear axis, no annotation) | Representation + Narratives | The same numerical data, rendered "neutrally," loses the rhetorical force Du Bois built in. Students see that visualization choices are not cosmetic; they are argument. |
