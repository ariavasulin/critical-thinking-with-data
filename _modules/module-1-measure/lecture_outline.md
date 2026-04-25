# Lecture Outline: "Where Did Statistics Come From? Galton, Eugenics, and the Hidden History of Data Science"

**Format:** 30-40 minute teacher-led lecture, paired with slides
**Audience:** Grades 10-12 high school students
**Paired with:** notebook Parts 1-2, Reading 1 (assigned after this lecture)
**Goal:** Provide the historical context that the notebook alone cannot provide, specifically, why this dataset exists, who made it and for what purpose, and what it means that the foundational tools of modern statistics were built in service of an ideological program

---

## Opening Hook (5 minutes)

Write this question on the board before students enter the room:

> "What statistical concepts have you heard of?"

As students settle, invite them to call out terms they know: correlation, average, regression, standard deviation, normal distribution, p-value, whatever they have. Write every response on the board without comment. Fill the board.

Then say: "Most of the concepts on this board were invented by the same person. He invented them because he needed mathematical tools that didn't yet exist, tools to prove that some human beings are genetically superior to others, that talent and intelligence run in certain bloodlines and not others, and that society should be reorganized to encourage the 'right' people to reproduce and discourage or prevent the 'wrong' people from doing so."

"That man was Francis Galton. He was Darwin's half-cousin, a Victorian gentleman scientist, and one of the most influential figures in the history of statistics. His dataset is what we are working with in this module."

---

## Section 1: Who Was Francis Galton? (7 minutes)

**The basic biography:**

Francis Galton was born in 1822 into a wealthy English family, the same family as Charles Darwin on his mother's side. He died in 1911. He had the resources and the time to pursue whatever interested him, and what interested him, ultimately, was the question of whether human talent and character were inherited.

He was widely traveled, he made several expeditions through parts of Africa and the Middle East that were under British colonial influence. He came back from those travels with a set of conclusions about innate racial hierarchy that he spent the rest of his scientific life trying to prove with data.

**The key publications:**

- **1869: "Hereditary Genius."** Galton's first major work in this area. He examined the family trees of prominent men, judges, scientists, artists, military officers, and argued that eminence runs in families, therefore talent is heritable, therefore the right response is to selectively encourage reproduction among the talented and discourage it among everyone else.
- **1883: "Inquiries into Human Faculty and Its Development."** This is where Galton coined the word "eugenics," from the Greek for "good in stock" or "well-born." He was explicitly borrowing the logic of livestock breeding, the selective breeding of cattle and horses for desired traits, and proposing to apply it to human populations.
- **1884: The Anthropometric Laboratory, International Health Exhibition, South Kensington, London.** This is the origin of our dataset. Galton set up a laboratory at a public exhibition, charged visitors three pennies to be measured, height, weight, arm span, visual acuity, reaction time, and other physical variables, and kept all the data. Approximately 9,000 visitors passed through. The families in our dataset are a subset of those measurements: 205 families, 934 children, collected specifically to study the heritability of height.

**Who came to the exhibition?**

A public exhibition in London in 1884, charging admission: who would have been there? Middle- and upper-class English families, overwhelmingly. White. English-speaking. Able-bodied enough to visit an exhibition. The working class was largely absent. Immigrants were largely absent. Non-white residents of London were largely absent. The entire colonized world that British imperial policy touched, India, West Africa, the Caribbean, the Middle East, does not appear in this data at all.

It is one of the central problems with every conclusion Galton drew.

---

## Section 2: The Statistical Innovations (7 minutes)

Galton needed mathematical tools to answer the questions he was asking, and those tools did not yet exist. He could not do this work alone. He was a gifted observer and synthesizer, but not a mathematician. He recruited Karl Pearson, a mathematician and statistician at University College London, who became his closest collaborator and the keeper of his scientific legacy. Pearson was, if anything, more extreme in his eugenicist convictions than Galton.

Together, and with Ronald Fisher in the generation that followed, they produced the foundational toolkit of modern statistics:

| Tool | What it measures |
|---|---|
| Correlation coefficient | The strength and direction of a linear relationship between two variables |
| Linear regression | A line of best fit predicting one variable from another |
| Scatter plot | Visual representation of the relationship between two continuous variables |
| Standard deviation | Spread of a distribution around its mean |
| Normal distribution (as a framework for human variation) | The theoretical basis for treating continuous human traits as bell-curved |

These are not obscure historical artifacts. They are in every statistics course taught at every level. They are used in clinical trials, economic models, public health research, and social science. They appear in every data science curriculum. They are genuinely powerful and useful tools.

But they were invented for an ideological purpose.

**An analogy that may help:**

The U.S. Interstate Highway System was designed in the 1950s, and highway planners in cities across the country made deliberate choices to route highways through Black neighborhoods, destroying homes, fracturing communities, and redirecting investment away from those areas. Robert Moses in New York is the most documented case, but the pattern was national. The highway system, as a piece of infrastructure, is not "bad" in the sense that driving is harmful. But knowing that history shapes how we think about urban planning, zoning law, infrastructure investment, and the distribution of environmental burden today. The tool and its history are not separable.

The same logic applies to statistical tools. Knowing that correlation and regression were invented to quantify heredity in service of a program of racial hierarchy does not make the math wrong. But it shapes what questions we think to ask about how and why these tools are used, and on whom.

---

## Section 3: What Galton Found, and Why It Undermined Him (7 minutes)

Here is the irony at the center of this module: when Galton analyzed his own height data, he found something he did not expect, and the thing he found is mathematically devastating to his eugenics program.

**What he found:**

Tall parents do tend to have tall children. That part was expected, it is what Galton was looking for. But the children of tall parents are not, on average, as tall as their parents. They are taller than average, but closer to average than their parents were. And the children of very short parents are shorter than average, but not as short as their parents. In both directions, the offspring move toward the population mean.

Galton called this "regression toward mediocrity." We call it regression to the mean.

**The numbers from our dataset:**

The slope of the regression line predicting child height from mid-parent height (the average of the father's and mother's height) is approximately 0.665. This number comes directly from the data. It means: for every one inch above average that the mid-parent height is, the child's predicted height is only 0.665 inches above average. Not one inch. Not more than one inch. About two-thirds of an inch.

Write on the board:

> **Slope = 0.665, not 1.0**

Ask students: if the slope were exactly 1.0, what would that mean? It would mean: children are, on average, exactly as extreme as their parents. Heredity transfers perfectly. If the slope were greater than 1.0, the population would diverge over generations, each generation more extreme than the last. A slope less than 1.0 means the opposite: the population converges. Extreme traits become less extreme over generations.

**Why this is devastating for eugenics:**

If you implement a selective breeding program, if you select only the tallest people and allow only them to reproduce, their children will be taller than average, yes. But they will not be as tall as the parents. And if you select only the tallest of those children, their children will again regress toward the mean. You cannot compound height. You cannot compound any continuously distributed trait this way. The mathematics does not permit the kind of generational accumulation that eugenics requires.

Galton saw this result. He understood it. And he continued to believe in eugenics.

This is perhaps the most important lesson in the module: data alone does not determine what conclusions people draw from it. The ideology comes first. The interpretation follows. Galton encountered a mathematical result that undermined his program and rationalized it away. That is not a mistake unique to Victorian scientists. It is a pattern that appears wherever people with strong prior beliefs encounter data that challenges those beliefs.

---

## Section 4: Three Problems with This Dataset (5 minutes)

Keep these short and memorable. Students should be able to recall all three.

**Problem 1: Sampling Bias**

The data comes from middle- and upper-class white English families who paid admission to a London exhibition in 1884. That is not a sample of humanity. That is not even a sample of London. Every conclusion Galton drew, and that subsequent researchers have drawn using this dataset, applies only to this population, not to the full range of human variation. When Galton used this data to make claims about heredity across the human species, he was generalizing from a single, narrow slice of Victorian English society to all of humanity. That is not a minor methodological limitation. It is a fundamental category error.

**Problem 2: Purpose Shapes Design**

Galton was not engaged in neutral scientific curiosity. He had a political program, eugenics, and he was building the empirical case for it. That means every design choice he made, from what to measure to how to organize his laboratory to which families to invite and which to ignore, was shaped by the conclusion he was working toward. We cannot look at the data as if it were collected by a disinterested observer asking open questions. It was not.

**Problem 3: The Erasure of Women**

Galton multiplied every female height in his dataset by 1.08 before running his analysis. His term for this was "transmutation." The stated reason was to convert female measurements to "male equivalents" so that the dataset could be analyzed on a single scale. What this actually means: the male body was treated as the default unit. The female body was treated as a deviation from that default, requiring correction before it could be analyzed. This is not a neutral technical decision. It is an assumption about which body is the standard and which requires adjustment, and that assumption is baked into the data before any analysis begins.

---

## Closing: The Bigger Question (4 minutes)

Ask students directly: "If you were handed this dataset with no information about its origin, just a CSV file with columns for father height, mother height, and child height, could you detect these problems from the numbers alone?"

Give them ten seconds to think. Then work through it honestly: you might notice that the heights cluster in a narrow range, not the full distribution you would expect across a truly diverse human population. You might notice the gender gap in the height distributions. If you looked carefully at the female heights you might notice they follow a suspiciously clean scaling relationship to the male heights. But you would not know, from the numbers, that this data was collected by a Victorian aristocrat at a paid exhibition to build the case for a racial hierarchy program. That information is not in the dataset.

This is why "who collected this data and why?" is not just a history question. It is a data science question. Every dataset comes from somewhere. Every dataset was collected by someone, for some purpose, using some method that determined who was included and who was not, what was measured and what was not, and what conclusions the collector was hoping to reach.

The question "where did this data come from?" is not a distraction from the technical work. It is part of the technical work.

Leave students with this:

> "In our next module, we are going to look at what happens when the ideas Galton put into motion become government policy. What we have been discussing as a scientific and methodological problem becomes, in Module 2, a policy problem with real names and real consequences."

---

## Slides Outline

**12 slides. Minimal text on each slide, the words belong in the teacher's voice, not on the screen. Each slide pairs a visual anchor or a question with no more than three brief supporting bullets.**

**Slide 1, Title**
"Where Did Statistics Come From?"
Subtitle: Galton, Eugenics, and the Hidden History of Data Science

**Slide 2, Warm-Up**
"What statistical concepts have you heard of?"
[Blank, fill in real time as students respond]

**Slide 3, Portrait of Francis Galton**
- Born 1822, died 1911. Victorian England.
- Darwin's half-cousin.
- Invented the word "eugenics," 1883.

**Slide 4, "The International Health Exhibition, 1884"**
- London, South Kensington. Paid public exhibition.
- Galton's Anthropometric Laboratory: 3 pennies admission.
- ~9,000 visitors measured. He kept the data.

**Slide 5, "Who Paid Three Pennies to Be Measured?"**
- Inner circle: those included (middle/upper-class white English families)
- Middle circle: those excluded but present in London (working class, immigrants)
- Outer circle: those never considered (colonized populations across the empire)

**Slide 6, Timeline**
- 1869: "Hereditary Genius" published
- 1883: "Eugenics" coined
- 1884: Anthropometric Laboratory
- 1886: Height paper published, regression to the mean described for the first time

**Slide 7, "What Tools Did He Create?"**
Two-column table:

| Statistical Tool | What It Measures |
|---|---|
| Correlation coefficient | Strength and direction of relationship between two variables |
| Linear regression | Predicting one variable from another |
| Scatter plot | Visualizing relationships between continuous variables |
| Standard deviation | Spread around the mean |
| Normal distribution framework | Model for human variation as bell-curved |

**Slide 8, "What Did He Find?"**
[Scatter plot: mid-parent height vs. child height, from our dataset]
- Each point: one child, plotted against parents' average height
- Question to students: what pattern do you see?

**Slide 9, Regression to the Mean**
[Simple conceptual diagram: three generations, each bar shorter than the last as it approaches average]
- Tall parents → tall children, but not as tall
- Short parents → short children, but not as short
- Population converges toward the mean over generations
- Slope = 0.665, not 1.0

**Slide 10, "Three Problems"**
1. Sampling bias, who was in the room?
2. Purpose shapes design, what was he trying to prove?
3. Erasure of women, the 1.08 "transmutation"

**Slide 11, "Data Is Never Neutral"**
- Every dataset comes from somewhere.
- Every dataset has a purpose.
- "Who collected this and why?" is a data science question, not only a history question.

**Slide 12, Preview: Module 2**
"What happens when these ideas become government policy?"
- California, 1909: forced sterilization law passed
- Over 20,000 Californians sterilized without consent under eugenics programs
- The science of Galton and Pearson provided the justification
