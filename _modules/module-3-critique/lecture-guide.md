---
title: Lecture Guide
parent: "Module 3: Critique"
nav_order: 1
permalink: /modules/module-3-critique/lecture-guide/
---

# Lecture Guide — Module 3: Critique

Module 3 closes the course arc by asking a harder question than "Is this dataset biased?": **what does responsible, strategic, community-centered data practice look like in public?** Students examine Du Bois's Paris plates as both statistical artifacts and rhetorical interventions, then build their own counter-visualization with explicit design intent.

This guide covers three ~50-minute sessions (Hook → Core → Close) and includes narrative beats, board work, facilitation prompts, misconception watchlist, and the formal HCE Audit #3 protocol.

## Module arc at a glance

- **Session 7 (Hook + Setup):** 1900 as a dual moment (Pearson and Du Bois); introduce Agency and Narratives.
- **Session 8 (Core Technical):** Recreate Plate 25; run the defaults inversion; compare rhetorical effects.
- **Session 9 (Close):** Student counter-visualization and formal HCE Audit #3 using all four questions.

## Learning goals

By the end of Module 3, students should be able to:

1. Explain how visual design choices (color, scale, annotation, composition) change an argument without changing the underlying numbers.
2. Use `matplotlib` intentionally rather than accepting defaults as neutral.
3. Apply HCE concepts of Agency, Narratives, and Representation to historical and contemporary data visualizations.
4. Produce a short, evidence-based critique using the formal four-question HCE Audit protocol.
5. Build a counter-visualization that makes a clear claim about what the original representation obscures.

## Session 7 — Hook + Setup (Du Bois in 1900)

### Session objective

Students understand why Du Bois's exhibit is a data intervention, not just "good design," and can name the difference between data collected **about** a community and data produced **by/with** a community.

### Suggested flow (~50 min)

- **Hook (8 min):** Project one Du Bois plate with no caption. Ask: "What claim does this image make before we read any title?"
- **Context mini-lecture (12 min):** 1900 as dual moment: Pearson formalizes inferential statistics while Du Bois stages a counter-narrative in Paris.
- **Close reading in pairs (15 min):** Students annotate one assigned plate: data source clues, audience clues, argument clues.
- **Whole-class synthesis (10 min):** Build class definition of Agency and Narratives in this module.
- **Exit ticket (5 min):** "One design choice in this plate that acts like evidence is ___ because ___."

### Board plan

- Left: **Key terms** — Agency, Narratives, Representation (review).
- Center: **Prompt** — "What does this chart say? How does it say it?"
- Right: **Tension statement** — "Counter-narrative can still involve strategic omission."

### Facilitation moves

- If students call the charts "objective," ask: "What would this look like if the audience were Black Georgians only? What changed when the audience is Paris 1900?"
- If students focus only on style, redirect: "Which design choice changes interpretation of the same values?"
- Ask students to ground claims in a visible element of the plate (axis, color block, label wording, ordering).

### Misconception watchlist

- "Hand-drawn means less rigorous."  
  Clarify that rigor depends on method and evidence use, not software choice.
- "Community-produced data is automatically unbiased."  
  Emphasize strategic framing and audience constraints.
- "Narrative is the opposite of statistics."  
  Reinforce that all statistical communication constructs narrative structure.

### Homework

- Read/annotate one required text passage and identify one sentence that helps explain a design choice in a Du Bois plate.

## Session 8 — Core Technical (Plate 25 + defaults inversion)

### Session objective

Students recreate Plate 25 in Python, then re-render with library defaults to observe how rhetorical force shifts when aesthetics are treated as neutral defaults.

### Suggested flow (~50 min)

- **Do now (5 min):** Predict which chart decisions will be hardest to replicate and why.
- **Notebook build (25 min):** Step-by-step recreation of Plate 25 (data prep, layout, palette, annotations).
- **Inversion run (10 min):** Toggle to default `matplotlib` style (palette, axis treatment, labeling density).
- **Compare and discuss (8 min):** "Same data, different argument" quickwrite and pair-share.
- **Wrap (2 min):** Name one design choice students will intentionally control in Session 9.

### Board plan

- Left: **Technical checkpoints** — data correctness, axis logic, color mapping, annotation.
- Center: **Inversion prompt** — "What disappears when defaults take over?"
- Right: **Claim template** — "Keeping values constant, changing ___ shifts interpretation from ___ to ___."

### Facilitation moves

- Encourage debugging as interpretation: if a chart "looks wrong," ask what claim the accidental version now makes.
- Require side-by-side display before critique so students compare like-for-like.
- Push for specificity beyond "looks cleaner": "Cleaner for which audience and what purpose?"

### Misconception watchlist

- "Defaults are neutral."  
  Defaults encode a design culture and audience assumptions.
- "Aesthetic choices are cosmetic."  
  In this module, aesthetics are part of evidence framing.
- "If values are unchanged, meaning is unchanged."  
  Interpretation depends on representation, not values alone.

### Homework

- Draft a one-sentence claim for your counter-visualization: what the original view obscures and what your revision surfaces.

## Session 9 — Close (Counter-Visualization + HCE Audit #3)

### Session objective

Students finalize a counter-visualization and complete HCE Audit #3 using evidence from both Du Bois's original plate and their own redesigned chart.

### Suggested flow (~50 min)

- **Launch (5 min):** Revisit the module's central tension: strategic advocacy vs. omission risk.
- **Build time (18 min):** Students finish counter-visualizations and export figures.
- **Gallery walk (12 min):** Peer feedback on claim clarity, evidence use, and audience fit.
- **HCE Audit writing (12 min):** Formal four-question protocol (Classification, Performativity, Representation, Agency).
- **Closing reflection (3 min):** "What does responsible data storytelling require from us?"

### Board plan

- Left: **Deliverables** — figure, caption, 4-question audit.
- Center: **Feedback stems** — "I see your claim as ___ because ___."
- Right: **Quality bar** — each audit response cites concrete notebook/figure evidence.

### Facilitation moves

- During gallery walk, ask reviewers to identify the intended audience before evaluating success.
- When claims are vague, require a concrete "before/after" statement tied to one visual decision.
- Support students in distinguishing ethical critique from personal preference ("I like it") by using evidence language.

### Misconception watchlist

- "Counter-visualization means adding more decoration."  
  It means changing framing to surface a hidden pattern or assumption.
- "Audit answers are opinion."  
  Audit claims must cite specific chart elements or notebook output.
- "Agency belongs only to historical actors."  
  Students are exercising agency through their own representational choices.

## HCE Audit #3 implementation notes

- Use the same four questions from prior modules, but hold a higher evidence standard.
- Require students to reference:
  - one feature of Du Bois's original plate,
  - one feature of their own chart, and
  - one concrete computational or data step from the notebook.
- Suggested scoring: 1-4 per question, aligned to concept accuracy + evidence specificity.

## Materials and prep checklist

- Projector-ready images of selected Du Bois plates (including Plate 25).
- Module 3 notebook pre-run through the plotting cells once for sanity checks.
- Side-by-side display template for original vs default vs student counter-render.
- Printed or digital HCE Audit #3 prompt and rubric.
- Timer for gallery walk and quick transitions.

## Required readings

- Hua Hsu, "What W.E.B. Du Bois Conveyed in His Captivating Infographics", *The New Yorker*, 2018
- Ruha Benjamin, *Race After Technology*, Ch. 5

*Recommended:* Battle-Baptiste & Rusert (eds.), *W.E.B. Du Bois's Data Portraits*; HCE Toolkit — [Agency, Narratives](https://data104.org/hce/).