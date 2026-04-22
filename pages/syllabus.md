---
title: Syllabus
nav_order: 2
permalink: /syllabus/
---

# Syllabus

## Nine-Session Schedule

Each module is three ~50-minute sessions organized as **Hook → Core → Close**. Session lengths are flexible; the Core sessions may run long, the Hook sessions may run short.

| # | Module | Session | Focus |
|---|---|---|---|
| 1 | Galton | Hook + Setup | 1884 Anthropometric Laboratory; eugenics coined; HCE *Classification* + *Performativity* introduced; notebook opens with light Python/Jupyter primer and EDA of the Galton dataset |
| 2 | Galton | Core Technical | Correlation (Pearson's *r*), linear regression, regression to the mean; **the 1.08 inversion moment** |
| 3 | Galton | Close | Three-part critique of Galton; HCE Audit #1; bridge to Module 2 |
| 4 | Sterilization | Hook + Setup | Theory → law (Davenport, ERO, Popenoe); the 1926 recommendation form as primary source; HCE *Classification* deepens and *Representation* enters |
| 5 | Sterilization | Core Technical | Conditional probability, rate ratios, contingency tables, **Pearson inversion (chi-squared)**; sensitivity analysis; demographics of harm |
| 6 | Sterilization | Close | Measurement vs. diagnosis; what aggregate data cannot show; HCE Audit #2 (with cross-module synthesis to Module 1); bridge to Module 3 |
| 7 | Du Bois | Hook + Setup | 1900 as dual moment (Pearson ↔ Du Bois); the Paris Exposition and the Negro Exhibit; insider citizen researcher methodology; HCE *Agency* + *Narratives* introduced |
| 8 | Du Bois | Core Technical | Recreate Plate 25 in Du Bois's hand; **defaults inversion**; Kallikak side-by-side |
| 9 | Du Bois | Close | Student counter-visualization; formal HCE Audit #3 (the four-question protocol as a reusable habit); course synthesis and closing |

Each module's three sessions are supported by:

- **One Jupyter notebook** (the main student-facing artifact)
- **One lecture guide** covering the three sessions (teacher-facing: narrative beats, board work, discussion facilitation, misconception watchlist)
- **One reading assignment** (two required readings + one to two recommended, with reflection prompts)

---

## Module 1: Measure — Numbers Never Lie? Galton, Eugenics, and the Birth of Statistics

**Lead: Parshv Patel** · **HCE concepts: Classification, Performativity**

Students meet Francis Galton, the Victorian polymath who coined the word "eugenics" and invented regression analysis, and work with his original 1886 dataset of 934 parent-child height observations. They compute correlation and linear regression the way any introductory statistics course would — but through the module they discover two things Galton's own work never quite admitted: that his data undermines his eugenic thesis via *regression to the mean*, and that his "transmutation" of female heights by a factor of 1.08 encoded sexism directly into the math.

- **Required Reading:** Aubrey Clayton, *Bernoulli's Fallacy*, Ch. 3 selections; Prakash Gorroochurn, "On Galton's Change From 'Reversion' to 'Regression'"
- **Recommended:** James Hanley, "'Transmuting' Women into Men"; HCE Toolkit: *Performativity*
- **Inversion Moment:** the 1.08 toggle
- **HCE Audit #1:** Classification and Performativity applied to the Galton dataset

## Module 2: Mandate — From Theory to Law: California's Forced Sterilization Program

**Lead: Ariav Asulin** · **HCE concepts: Classification, Representation, Vulnerability**

Between 1909 and 1952, California forcibly sterilized over 20,000 people using standardized recommendation forms descended directly from Galton's measurement apparatus. Students encounter a difficult discovery: the forms the state used to record sterilizations *did not include a race field*, so researchers had to invent a racial category using Spanish surnames as a proxy. The module introduces conditional probability, rate ratios, and the chi-squared test — including the "Pearson inversion," in which students use Karl Pearson's own test (invented in 1900 to argue for racial hierarchies) to quantify the racial disparities of a eugenic policy. The module also introduces the distinction between a *measurement* and a *diagnosis*.

- **Required Reading:** Novak et al. 2018 (*AJPH*); Stern et al. 2017 (*AJPH*)
- **Recommended:** Whatcott, *Menace to the Future*, Prologue + Intro; HCE Toolkit: *Classification*, *Representation*
- **Inversion Moment:** the proxy sweep (Spanish-surname false-positive rate)
- **HCE Audit #2:** applied to the sterilization dataset, with explicit cross-module synthesis comparing Module 1 and Module 2 under Classification and Performativity

## Module 3: Critique — Data as Counter-Narrative: W.E.B. Du Bois and the 1900 Paris Exposition

**Lead: Emett Mendel** · **HCE concepts: Agency, Narratives, Representation**

In 1900 — the same year Karl Pearson was inventing the chi-squared test students used in Module 2 — W.E.B. Du Bois and his students at Atlanta University presented 63 hand-drawn data visualizations of Black life in Georgia at the Exposition Universelle in Paris. Students study Du Bois's plates as both statistical artifacts and rhetorical arguments, learn to read his design choices, and recreate Plate 25 in Python. The module refuses the easy story that "community data" is automatically liberatory: Du Bois made strategic omissions and centered metrics legible to a white European audience. Students sit with that tension with the HCE vocabulary and the technical skill to do so rigorously.

- **Required Reading:** Hua Hsu, "What W.E.B. Du Bois Conveyed in His Captivating Infographics"; Ruha Benjamin, *Race After Technology*, Ch. 5
- **Recommended:** Battle-Baptiste & Rusert, *W.E.B. Du Bois's Data Portraits*; HCE Toolkit: *Agency*, *Narratives*
- **Inversion Moment:** Plate 25 with matplotlib defaults
- **HCE Audit #3:** the formal four-question protocol, applied both to Du Bois's plate and to the student's own counter-visualization

---

## Assignments and Grading

| Component | Weight | What it tests |
|---|---|---|
| HCE Audits (3, one per module) | 45% | Consistent application of the critical-reading protocol; specific evidence from notebook output |
| Reading reflections (6 total, one per required reading) | 30% | Engagement with assigned readings |
| Notebook completion (3) | 25% | Technical skill demonstration |

**HCE Audits** (500–800 words each) are graded on the published rubric. They are due at the end of each module and anchor the transition to the next. The Module 2 audit includes an explicit cross-module synthesis component.

**Reading reflections** (150–250 words each) are short written responses to one reading at a time, submitted before the class session that uses that reading. The format follows the Data C4AC weekly reflection model.

**Notebook completion** is scored on whether each code cell was run and each reflection prompt inside the notebook was answered; the notebook is a workbook, not a performance.

---

## Optional Extension: Final Project

The final project is an **optional extension** to the 9-session core curriculum. It is framed as an opportunity rather than a requirement; the course's central instrument of assessment is the three [HCE Audits](../pedagogy/#the-hce-audit-recurring-assessment), not this project.

Students who wish to extend the course may choose a dataset that was **not** covered in the three modules and apply:

1. The full **four-question HCE Audit** (Classification, Performativity, Representation, Agency) to the dataset
2. A **Du Bois-style counter-visualization** — a deliberate rhetorical rendering of one finding from the audit

The final project is where students can show the course's instincts against data that actually resembles the world they live in — a contemporary algorithmic system, a public dataset, a news-article data table — rather than one of the curated historical cases.

*Detailed final-project prompt and rubric coming soon.*
