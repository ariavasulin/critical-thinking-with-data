---
title: Discussion Lesson Plan
parent: Extra Resources
grand_parent: "Module 1: Measure"
nav_order: 2
permalink: /modules/module-1-measure/extra/discussion_lesson_plan/
---

# Module 1 Discussion Questions and Lesson Plan

---

## Section 1: Lesson Plan: Three 50-Minute Class Periods

### Day 1: The History and the Hook (50 minutes)

**Goal:** Students understand who Galton was, why this dataset exists, and what sampling problems they can already identify before doing any computation.

**5 min, Entry Ticket**

Students write independently in response to the prompt on the board:

> "What do you know about eugenics? What do you know about statistics? Have these two things ever been connected for you before today?"

Collect or have students hold for reference at end of Day 3. No sharing yet.

**10 min, Teacher Mini-Lecture**

Use the lecture outline (see `lecture_outline.md`) to establish: who Galton was, what eugenics is, why the dataset from the 1884 Anthropometric Laboratory exists, and what Galton was trying to prove with it. Keep this tight. Students do not need the full history today. They need enough to understand the context of the data they are about to work with.

Key points to land before moving on:
- Galton was Darwin's half-cousin and believed talent and intelligence were heritable traits that could be selectively bred.
- He collected height data from families as part of an attempt to quantify heredity.
- The data was not a neutral scientific curiosity. It was collected to build the empirical case for a political program.

**15 min, Independent Reading and Annotation**

Students read Part 1 of the Jupyter notebook (the historical narrative section) independently. Ask them to annotate as they go using three markers: one for facts they did not know, one for claims they find surprising or questionable, and one for anything that connects to something outside this class.

This is not the time to run code. The goal is careful reading.

**15 min, Pair Discussion**

Students discuss with a partner using the "STOP AND THINK" prompt from Cell 1.2 of the notebook. The core questions: Who is represented in this dataset? Who is absent? What does it mean for a scientific conclusion if the data comes only from one narrow slice of the population?

Circulate and listen. Note the range of responses to represent that range in the whole-class debrief.

**5 min, Whole-Class Debrief**

Bring the room back together. Ask: what sampling issues did you and your partner identify? Take 3-4 responses. Do not resolve the discussion. The goal of Day 1 is not to close anything down but to open up the questions that the rest of the module will work through.

**Homework:** Reading 1 (Aubrey Clayton, Nautilus). Students should complete the pre-reading warm-up questions before reading and bring written responses to Day 2.

---

### Day 2: The Technical Work (50 minutes)

**Goal:** Students execute the core computational work, calculating correlation, fitting the regression line, and identifying regression to the mean from the data itself.

**5 min, Check-In on Reading 1**

A quick temperature check: what is one thing from the article that surprised you, bothered you, or that you found yourself pushing back against? Take 3-4 responses. Note that you will return to the reading's arguments once students have done the technical work, because the technical results will make those arguments more concrete.

**5 min, Quick Jupyter Intro**

If any students are new to Jupyter notebooks, run a brief demo: how to run a cell, what happens when a cell produces output, the difference between a code cell and a markdown cell. Keep this to five minutes maximum. Students who already know the environment can use this time to open the notebook and get oriented.

**30 min, Pair Work on Parts 2 and 3**

Students work in pairs through the notebook's computational sections:
- Part 2: Exploratory data analysis, distributions of height by gender and by family role
- Part 3: Correlation and regression, computing r, fitting the regression line, interpreting the slope

The most common sticking point is the interpretation of slope. When a pair has the slope value, push them: "What would it mean if this number were 1.0? What does it mean that it's less than 1.0?"

A second common confusion is the difference between the father-child correlation (0.266) and the mid-parent-child correlation (0.322). If a pair asks why these are different, that is an excellent sign, use it: "Why do you think averaging two parents gives a stronger predictor than using one parent alone?"

**10 min, Whole-Class Convergence**

Bring the room back together. Ask: what slope did you find? (Target: approximately 0.665.) Then ask: what does a slope less than 1.0 mean? Take several student attempts at this before you offer the formal definition. Students articulating "regression to the mean" in their own imperfect words is more valuable than hearing you say it correctly.

Write on the board: **"Tall parents have tall children, but not as tall as the parents."** Ask: does that match what you found? Is that surprising?

**Homework:** Finish any incomplete notebook cells from Parts 2-3.

---

### Day 3: Critique and Synthesis (50 minutes)

**Goal:** Students connect the technical results to the critical framework, understanding what the data shows, what it cannot show, and what was built into the data before the analysis began.

**5 min, Entry Ticket**

Students write: "In your own words, what is regression to the mean? Use the height data as your example."

Glance at responses as students write. If a significant portion of the class has it wrong or cannot articulate it, address that before moving forward.

**10 min, Teacher-Led Walkthrough: Transmutation Cells (Part 4)**

Project the notebook and walk through the transmutation cells live, but let students narrate. Pull up Cell 4.1 and ask: "What is Galton doing here? Say it in plain language." The target answer: he is multiplying all female heights by 1.08 to convert them to "male equivalents" before running his analysis. Once a student has said it, ask: "What assumption is baked into that operation?" Take several responses. Then ask: "What is lost when you do this?"

The goal is for students to see, clearly and in the code itself, that a choice was made before the analysis began, and that the choice encoded an assumption about gender.

**15 min, Small-Group Discussion**

Groups of 3-4 students. Each group discusses the five questions from Cell 4.4 (the critical analysis section of the notebook).

**10 min, Whole-Class Share-Out**

Draw two columns on the board:

| What the data shows | What the data cannot tell us |

Take one item from each group for the left column, then push each group: what belongs in the right column based on what you just discussed? Fill both columns with student contributions. This visual distinction, between what the data actually demonstrates and what interpretations require external assumptions, is the central conceptual payoff of the module.

**10 min, Individual Reflection Writing**

Students write independently in response to the Cell 5.3 prompts. This is the beginning of the written reflection component of the assessment. Tell students they will finish this for homework and that their writing should be substantive paragraphs.

**Homework:** Finish individual reflection writing. Reading 2 (Greenwood, Bhavnani, & Harmon, or Clayton, LARB) due next class.

---

## Section 2: Discussion Questions by Cognitive Level

These questions are organized by the type of thinking they ask for. In practice, the most productive class discussions move fluidly between levels, begin with an entry-level question to establish shared ground, then use it as a launching point toward the higher-level questions.

---

### Entry-Level: Recall and Comprehension

These questions check whether students have the basic factual and conceptual foundation to engage in deeper analysis. If students cannot answer these, the higher-level questions will be difficult to understand.

1. Who was Francis Galton and what was he trying to prove with this dataset? What specific claim about human heredity was he building toward?

2. What is "regression to the mean"? Give a concrete example using the height data, what pattern in the data illustrates this concept, and what does the slope of 0.665 tell us about it?

3. What is the difference between a correlation of 0.3 and a correlation of 0.9? What does each number tell you about the relationship between two variables, and what does neither number tell you about causation?

4. What is "sampling bias"? Why does it matter for drawing conclusions from data? What is the difference between a conclusion that holds for a sample and a conclusion that holds for a population?

5. What did Galton mean by "transmuting" female heights? What mathematical operation did he perform, and what was the stated rationale for it?

---

### Mid-Level: Analysis and Application

These questions ask students to do something with what they know, apply concepts to new situations, examine assumptions, and think about what follows from what.

6. We found that the correlation between father height and child height is 0.266. What does this number tell us about the role of genetics in determining height? Be precise: what can a correlation of 0.266 claim, and what can it not claim? What other factors might be driving the relationship we observe?

7. Galton collected data from families who paid admission to an exhibition in London in 1884. The sample is overwhelmingly middle- and upper-class white English families. If you were redesigning this study to produce a more representative picture of human height inheritance, what would you change? Who would you include that Galton excluded? How would you recruit participants, and what would you do about the language and access barriers that would arise?

8. The mid-parent regression slope in our data is 0.665. If the slope were exactly 1.0, what would that mean biologically and statistically? What does a slope of less than 1.0 actually mean, what is happening across generations? Why is this result significant for evaluating Galton's eugenics program?

9. Nutrition, access to healthcare, and socioeconomic status all affect height. How would the presence of these factors in Galton's data, even if unmeasured, complicate his interpretation that the height correlation he found reflects pure genetic inheritance? What would you need to control for to make his interpretation defensible, and did he have the tools or the data to do that?

10. What is the difference between a dataset being "wrong" and being "limited"? A dataset that contains errors is wrong. A dataset that accurately records measurements from a narrow, unrepresentative sample is limited. Is Galton's dataset wrong, limited, or both? Does the distinction matter for how we use it?

---

### High-Level: Synthesis, Evaluation, and Transfer

These questions ask students to build arguments, evaluate claims, and carry ideas across contexts. They do not have single correct answers. They are designed for extended discussion or written response.

11. "Data is never neutral." Argue for or against this claim using at least two specific examples from this module. If you argue for it, explain what it means for data to be non-neutral, what is it carrying, and how does that affect what we can conclude from it? If you argue against it, explain what conditions would need to hold for data to be genuinely neutral, and whether those conditions can be achieved.

12. The statistical methods Galton invented, correlation, regression, the scatter plot, are used today in medical research, economic modeling, public health, and social science. Given their origins, should we stop using them? Rename them? Continue as-is, without requiring users to know the history? What responsibility, if any, do users of these methods have toward the history they carry?

13. If Galton had collected a truly representative sample, including working-class families, families from West Africa, South Asia, and East Asia, rural and urban populations, families from the Americas, do you think his results would have been different? Would the correlation between parental and child height have been stronger or weaker? Would his eugenic thesis have been supported or undermined? Explain your reasoning carefully.

14. Regression to the mean tells us that extreme parental traits tend to become less extreme in children across generations, and less extreme still in grandchildren. What does this mathematical fact mean for any selective breeding program that aims to produce consistently "superior" offspring over many generations? Why does it make the core mechanism of eugenics statistically incoherent, not just morally wrong?

15. In Module 3, we will examine W.E.B. Du Bois, who used data visualization and statistical argument to challenge racial hierarchy rather than to justify it, working in the same era as Galton and Pearson, with far fewer resources. What would a "just" version of Galton's study look like? Who would you include in the sample? What questions would you ask, and what would you refrain from asking? What would count as a meaningful finding?

---

## Section 3: Assessment Criteria

The following rubric is for teacher use in evaluating the complete module assessment, which combines the computational notebook work, written reflection, and class participation.

### Technical Component, 40 points

| Criterion | Points |
|---|---|
| Runs all notebook cells without errors and produces the expected outputs | 10 |
| Correctly interprets the correlation coefficients (0.266 father-child; 0.322 mid-parent-child) in plain language | 10 |
| Identifies regression to the mean from the data and explains what the slope of 0.665 means | 10 |
| Completes all coding exercises with correct output | 10 |

### Critical Thinking, 40 points

| Criterion | Points |
|---|---|
| Identifies at least two specific sampling biases and explains why each matters for Galton's conclusions | 10 |
| Explains how regression to the mean mathematically undermines the central premise of Galton's eugenics program | 10 |
| Analyzes the 1.08 transmutation of female heights and explains what assumption it encodes and what it erases | 10 |
| Makes at least one substantive connection between this module's material and a contemporary data practice, policy, or system | 10 |

### Reflection Writing, 20 points

| Criterion | Points |
|---|---|
| Addresses all five reflection prompts from Cell 5.3 with genuine depth and developed thinking | 20 |

**Total: 100 points**

### Notes for Graders

The technical component should be evaluated for correctness and completeness. A student who gets the right numerical answer with messy code should receive full credit on that criterion.

The critical thinking component is the most important section for assessing the module's core learning goals. A student who aces the computation but cannot explain what sampling bias means for Galton's conclusions has not met the module's objectives.

The reflection writing should be evaluated for depth and honesty, not for arriving at a particular conclusion. A student who argues that we should continue using statistical methods without requiring historical context, and who argues that position with rigor and self-awareness, is meeting the standard. A student who simply endorses the "correct" critical view without showing genuine reasoning is not.
