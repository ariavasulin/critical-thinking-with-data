---
title: Syllabus
nav_order: 2
permalink: /syllabus/
---

# Syllabus

## Nine-Session Schedule

Each module is three ~50-minute sessions. Session lengths are flexible; the Core sessions may run long.

| # | Module | Session | Focus |
|---|---|---|---|
| 1 | Measure | Hook + Setup | 1884 Anthropometric Laboratory; eugenics coined; HCE *Classification* + *Performativity* introduced; notebook opens with light Python/Jupyter primer and EDA of the Galton dataset |
| 2 | Measure | Core Technical | Correlation (Pearson's *r*), linear regression, regression to the mean; **the 1.08 inversion moment** |
| 3 | Measure | Close | Three-part critique of Galton; Data Audit #1; bridge to Module 2 |
| 4 | Mandate | Hook + Setup | Theory → law (Davenport, ERO, Popenoe); the 1926 recommendation form as primary source; HCE *Classification* deepens and *Representation* enters |
| 5 | Mandate | Core Technical | Conditional probability, rate ratios, contingency tables, **Pearson inversion (chi-squared)**; sensitivity analysis; demographics of harm |
| 6 | Mandate | Close | Measurement vs. diagnosis; what aggregate data cannot show; Data Audit #2 (with cross-module synthesis to Module 1); bridge to Module 3 |
| 7 | Critique | Hook + Setup | 1900 as dual moment (Pearson ↔ Du Bois); the Paris Exposition and the Negro Exhibit; insider citizen researcher methodology; HCE *Agency* + *Narratives* introduced |
| 8 | Critique | Core Technical | Recreate Plate 25 in Du Bois's hand; **defaults inversion**; Kallikak side-by-side |
| 9 | Critique | Close | Student counter-visualization; formal Data Audit #3 (the four-question protocol as a reusable habit); course synthesis and closing |
{: .schedule-table}

Each module's three sessions are supported by:

- **One Jupyter notebook** (the main student-facing artifact)
- **One lecture guide** covering the three sessions (teacher-facing: narrative beats, board work, discussion facilitation, misconception watchlist)
- **One reading assignment** (two required readings + one to two recommended, with reflection prompts)

---

## Module 1: Measure — Numbers Never Lie? Galton, Eugenics, and the Birth of Statistics

**Concepts: Classification, Performativity**

Students meet Francis Galton, the Victorian polymath who coined the word "eugenics" and invented regression analysis, and work with his original 1886 dataset of 934 parent-child height observations. They compute correlation and linear regression the way any introductory statistics course would — but through the module they discover two things Galton's own work never quite admitted: that his data undermines his eugenic thesis via *regression to the mean*, and that his "transmutation" of female heights by a factor of 1.08 encoded sexism directly into the math.

- **Required Reading:** Aubrey Clayton, *Bernoulli's Fallacy*, Ch. 3 selections; Prakash Gorroochurn, "On Galton's Change From 'Reversion' to 'Regression'"
- **Recommended:** James Hanley, "'Transmuting' Women into Men"; HCE Toolkit: *Performativity*

## Module 2: Mandate — From Theory to Law: California's Forced Sterilization Program

**Lead: Ariav Asulin** · **HCE concepts: Classification, Representation**

Between 1909 and 1952, California forcibly sterilized over 20,000 people using standardized recommendation forms descended directly from Galton's measurement apparatus. Students encounter a difficult discovery: the forms the state used to record sterilizations *did not include a race field*, so researchers had to invent a racial category using Spanish surnames as a proxy. The module introduces conditional probability, rate ratios, and the chi-squared test — including the "Pearson inversion," in which students use Karl Pearson's own test (invented in 1900 to argue for racial hierarchies) to quantify the racial disparities of a eugenic policy. The module also introduces the distinction between a *measurement* and a *diagnosis*.

- **Required Reading:** Novak et al. 2018 (*AJPH*); Stern et al. 2017 (*AJPH*)
- **Recommended:** Whatcott, *Menace to the Future*, Prologue + Intro; HCE Toolkit: *Classification*, *Representation*

## Module 3: Critique — Data as Counter-Narrative: W.E.B. Du Bois and the 1900 Paris Exposition

**Lead: Emett Mendel** · **HCE concepts: Agency, Representation**

In 1900 — the same year Karl Pearson was inventing the chi-squared test students used in Module 2 — W.E.B. Du Bois and his students at Atlanta University presented 63 hand-drawn data visualizations of Black life in Georgia at the Exposition Universelle in Paris. Students study Du Bois's plates as both statistical artifacts and rhetorical arguments, learn to read his design choices, and recreate Plate 25 in Python. The module refuses the easy story that "community data" is automatically liberatory: Du Bois made strategic omissions and centered metrics legible to a white European audience. Students sit with that tension with the HCE vocabulary and the technical skill to do so rigorously.

- **Required Reading:** Hua Hsu, "What W.E.B. Du Bois Conveyed in His Captivating Infographics"; Ruha Benjamin, *Race After Technology*, Ch. 5
- **Recommended:** Battle-Baptiste & Rusert, *W.E.B. Du Bois's Data Portraits*; HCE Toolkit: *Agency*, *Narratives*

---

## Assignments and Grading

| Component | Weight | What it tests |
|---|---|---|
| Data Audits (3, one per module) | 45% | Consistent application of the critical-reading protocol; specific evidence from notebook output |
| Reading reflections (6 total, one per required reading) | 30% | Engagement with assigned readings |
| Notebook completion (3) | 25% | Technical skill demonstration |

**Data Audits** (500–800 words each) are graded on the published rubric. They are due at the end of each module and anchor the transition to the next. The Module 2 audit includes an explicit cross-module synthesis component.

**Reading reflections** (150–250 words each) are short written responses to one reading at a time, submitted before the class session that uses that reading. The format follows the Data C4AC weekly reflection model:

> ### The Weekly Reflection Model
>
> **Part 1 — Response to specific readings**
>
> For the two readings assigned each week, please complete the following four components (#1–4):
>
> 1. **Quotation:** Select one substantive quote from the reading that you believe requires explanation or elucidation. Copy the quote and then restate the author's point as you understand it, including who the author is responding to as well as what the author is arguing for and against.
> 2. **Argument:** In at least 3 sentences, describe the reading’s main arguments with respect to its relevance for the course and the week’s sessions. How does the quotation selected support or complicate this argument? (Note: this is not just a summary of key points, but a synthetic account of the text's argument. Write in full sentences, not bullet points.)
> 3. **Question:** Form a clear question that you think is not satisfactorily answered by the text. The question should be a question of interpretation, inquiry, or method, not simply a question of fact.
> 4. **Connection:** Based on that question, write a critical reflection in which you discuss either a shortcoming of the text or a way in which the argument might be extended. Then, write a brief paragraph connecting this reading to the other readings we have read in the course or themes and concepts discussed in lecture.
>
> **Part 2 — Weekly synthesis**
>
> Write one paragraph discussing your major takeaways from the week's material (lectures and readings). How did the material connect to your previous knowledge of or experience with the topics presented?

**Notebook completion** is scored on whether each code cell was run and each reflection prompt inside the notebook was answered; the notebook is a workbook, not a performance.
