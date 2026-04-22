---
title: Credits
nav_order: 4
permalink: /credits/
---

# Credits

## Team

{% assign team = site.staffers | sort: "name" %}
<div class="staff">
{% for staffer in team %}
  {{ staffer.content | default: staffer.excerpt }}
{% endfor %}
</div>

---

## References

### Module 1 — Measure (Galton)

- **Aubrey Clayton**, *Bernoulli's Fallacy: Statistical Illogic and the Crisis of Modern Science*, Columbia University Press, 2021. **Required** — Ch. 3 selections on Galton, eugenics, and the birth of inferential statistics.
- **Prakash Gorroochurn**, "On Galton's Change From 'Reversion' to 'Regression'", *The American Statistician*, 2016. **Required** — close reading of Galton's terminology shift.
- **James Hanley**, "'Transmuting' Women into Men: Galton's Family Data on Human Stature", *The American Statistician*, 2004. *Recommended* — the 1.08 transmutation in primary-source detail.
- **HCE Toolkit — *Performativity***. [data104.org/hce](https://data104.org/hce/).

### Module 2 — Mandate (California Sterilization)

- **Novak NL, Lira N, O'Connor KE, Harlow SD, Kardia SLR, Stern AM**. "Disproportionate Sterilization of Latinos Under California's Eugenic Sterilization Program, 1920–1945", *American Journal of Public Health*, 2018. **Required** — the quantitative foundation and the Spanish-surname proxy methodology.
- **Stern AM, Novak NL, Lira N, O'Connor KE, Harlow SD, Kardia SLR**. "California's Sterilization Survivors: An Estimate and Call for Redress", *American Journal of Public Health*, 2017. **Required** — the call for restorative justice and the estimate of living survivors.
- **Natalie Lira, Alexandra Minna Stern**, and colleagues at the [Sterilization and Social Justice Lab](https://www.sterilizationandsocialjustice.org/). *Primary archival access*.
- **Whatcott, Jess**. *Menace to the Future: A Disability and Queer History of Carceral Eugenics*, Duke University Press, 2024. *Recommended* — Prologue + Intro.
- **HCE Toolkit — *Classification*, *Representation***. [data104.org/hce](https://data104.org/hce/).

### Module 3 — Critique (Du Bois)

- **Hua Hsu**, "What W.E.B. Du Bois Conveyed in His Captivating Infographics", *The New Yorker*, 2018. **Required** — introduces Du Bois's Paris Exposition plates to a general audience.
- **Ruha Benjamin**, *Race After Technology: Abolitionist Tools for the New Jim Code*, Polity, 2019. **Required** — Ch. 5 on data, design, and resistance.
- **Whitney Battle-Baptiste & Britt Rusert** (eds.), *W.E.B. Du Bois's Data Portraits: Visualizing Black America*, Princeton Architectural Press, 2018. *Recommended* — full-color facsimiles of all 63 Paris Exposition plates with scholarly introductions.
- **Anthony Starks** — [#DuBoisChallenge](https://github.com/ajstarks/dubois-data-portraits). Reconstructed CSV data for the Paris Exposition plates.
- **HCE Toolkit — *Agency*, *Narratives***. [data104.org/hce](https://data104.org/hce/).

---

## Acknowledgments

This curriculum draws directly on the Human Contexts and Ethics Toolkit developed by the HCE Program within UC Berkeley's Division of Computing, Data Science, and Society, as deployed in Data C104 (Human Contexts and Ethics of Data) and Data C4AC (Data and Justice). Specific thanks to Cathryn Carson, Mauricio Najarro, Ari Edmundson, and the HCE program faculty and staff. The HCE Toolkit is available at [data104.org/hce](https://data104.org/hce/).

Our treatment of Galton's work follows Aubrey Clayton's *Bernoulli's Fallacy* and James Hanley's scholarship on the 1.08 transmutation. Our sterilization module draws on Alexandra Minna Stern's Sterilization and Social Justice Lab at the University of Michigan and the published work of Nicole L. Novak and colleagues. Our Du Bois module is indebted to Anthony Starks's #DuBoisChallenge project for the reconstructed CSVs and to Whitney Battle-Baptiste and Britt Rusert's *W.E.B. Du Bois's Data Portraits*.

The structural model for this syllabus — HCE concept threading, recurring audits, inversion moments — follows Data C4AC (UC Berkeley, Spring 2026), taught by Daniel Roddy.
