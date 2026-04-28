---
title: Credits
nav_order: 4
permalink: /credits/
---

# Credits

## Team

<!-- 
  TO UPDATE PHOTOS:
  1. Save headshots as 'parshv.jpg', 'ariav.jpg', and 'emett.jpg'
  2. Upload them to the 'assets/images/team/' directory
-->

{% assign team = site.staffers | sort: "name" %}
<div class="team-grid">
  {% for staffer in team %}
  <div class="team-member">
    <div class="member-image">
      <img src="{{ staffer.image | default: '/assets/images/team/placeholder.jpg' | relative_url }}" alt="{{ staffer.name }}">
    </div>
    <div class="member-info">
      <h3>{{ staffer.name }}</h3>
      <p class="role">{{ staffer.role }}</p>
      <div class="bio">
        {{ staffer.content }}
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<style>
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}
.team-member {
  background: #fdfdfd;
  border: 1px solid #eee;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s;
  display: flex;
  flex-direction: column;
}
.team-member:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}
.member-image {
  height: 200px;
  background: #f0f0f0;
  overflow: hidden;
}
.member-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.member-info {
  padding: 1.5rem;
}
.member-info h3 {
  margin: 0 0 0.25rem 0;
  font-size: 1.25rem;
  color: #222;
}
.member-info .role {
  font-weight: 600;
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}
.member-info .bio {
  font-size: 0.95rem;
  line-height: 1.5;
  color: #444;
}
</style>

---

## References

### C4AC Theoretical Anchors

The curriculum's framing of justice as the politics of classification draws directly on three readings from UC Berkeley's Data C4AC (Spring 2026):

- **Charles W. Mills**, *The Racial Contract*, Cornell University Press, 1997. *C4AC Week 4* — the political-theory anchor for treating statistical conventions as the racial contract made quantitative.
- **Khalil Gibran Muhammad**, *The Condemnation of Blackness: Race, Crime, and the Making of Modern Urban America*, Harvard University Press, 2010. *C4AC Week 8* — "The Mismeasure of Crime" introduction.
- **Anna Lauren Hoffmann**, "Terms of Inclusion: Data, Discourse, Violence", *New Media and Society* 23(12), 2021. *C4AC Week 5* — frames measurement itself as a form of harm prior to and independent of any downstream policy.

### Module 1 — Measure (Galton)

- **Aubrey Clayton**, *Bernoulli's Fallacy: Statistical Illogic and the Crisis of Modern Science*, Columbia University Press, 2021. **Required** — Ch. 3 selections on Galton, eugenics, and the birth of inferential statistics.
- **Prakash Gorroochurn**, "On Galton's Change From 'Reversion' to 'Regression'", *The American Statistician*, 2016. **Required** — close reading of Galton's terminology shift.
- **James Hanley**, "'Transmuting' Women into Men: Galton's Family Data on Human Stature", *The American Statistician*, 2012. *Recommended* — the 1.08 transmutation in primary-source detail.
- **HCE Toolkit — *Performativity***. [data104.org/hce](https://data104.org/hce/).

### Module 2 — Mandate (California Sterilization)

- **Novak NL, Lira N, O'Connor KE, Harlow SD, Kardia SLR, Stern AM**. "Disproportionate Sterilization of Latinos Under California's Eugenic Sterilization Program, 1920–1945", *American Journal of Public Health*, 2018. **Required** — the quantitative foundation and the Spanish-surname proxy methodology.
- **Stern AM, Novak NL, Lira N, O'Connor KE, Harlow SD, Kardia SLR**. "California's Sterilization Survivors: An Estimate and Call for Redress", *American Journal of Public Health*, 2017. **Required** — the call for restorative justice and the estimate of living survivors.
- **Natalie Lira, Alexandra Minna Stern**, and colleagues at the [Sterilization and Social Justice Lab](https://www.sterilizationandsocialjustice.org/). *Primary archival access*.
- **Whatcott, Jess**. *Menace to the Future: A Disability and Queer History of Carceral Eugenics*, Duke University Press, 2024. *Recommended* — Prologue + Intro.
- **HCE Toolkit — *Classification*, *Representation***. [data104.org/hce](https://data104.org/hce/).

### Module 3 — Critique (Du Bois)

- **Hua Hsu**, ["What W.E.B. Du Bois Conveyed in His Captivating Infographics"](https://www.newyorker.com/culture/culture-desk/what-w-e-b-du-bois-conveyed-in-his-captivating-infographics), *The New Yorker*, November 6, 2019. **Required** — introduces Du Bois's Paris Exposition plates to a general audience.
- **Ruha Benjamin**, [*Race After Technology: Abolitionist Tools for the New Jim Code*](https://www.ruhabenjamin.com/race-after-technology), Polity, 2019. **Required** — Ch. 5 on data, design, and resistance.
- **Whitney Battle-Baptiste & Britt Rusert** (eds.), *W.E.B. Du Bois's Data Portraits: Visualizing Black America*, Princeton Architectural Press, 2018. *Recommended* — full-color facsimiles of all 63 Paris Exposition plates with scholarly introductions.
- **Anthony Starks** — [#DuBoisChallenge](https://github.com/ajstarks/dubois-data-portraits). Reconstructed CSV data for the Paris Exposition plates.
- **HCE Toolkit — *Agency*, *Narratives***. [data104.org/hce](https://data104.org/hce/).

---

## Acknowledgments

This curriculum draws directly on the Human Contexts and Ethics Toolkit developed by the HCE Program within UC Berkeley's Division of Computing, Data Science, and Society, as deployed in Data C104 (Human Contexts and Ethics of Data) and Data C4AC (Data and Justice). Specific thanks to Cathryn Carson, Mauricio Najarro, Ari Edmundson, and the HCE program faculty and staff. The HCE Toolkit is available at [data104.org/hce](https://data104.org/hce/).

Our treatment of Galton's work follows Aubrey Clayton's *Bernoulli's Fallacy* and James Hanley's scholarship on the 1.08 transmutation. Our sterilization module draws on Alexandra Minna Stern's Sterilization and Social Justice Lab at the University of Michigan and the published work of Nicole L. Novak and colleagues. Our Du Bois module is indebted to Anthony Starks's #DuBoisChallenge project for the reconstructed CSVs and to Whitney Battle-Baptiste and Britt Rusert's *W.E.B. Du Bois's Data Portraits*.

The structural model for this syllabus — HCE concept threading, recurring audits, inversion moments — follows Data C4AC (UC Berkeley, Spring 2026), taught by Daniel Roddy.
