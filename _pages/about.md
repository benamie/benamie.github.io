---
permalink: /
title: "Elinor Benami"
excerpt: "Assistant Professor of Agricultural & Applied Economics at Virginia Tech"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

## About
{: #about}

Hi! I’m Elinor, an Assistant Professor at Virginia Tech in the [Agricultural and Applied Economics Department](https://aaec.vt.edu). I’m also a faculty affiliate of the [VT Remote Sensing Graduate Education Group](https://rsigep.frec.vt.edu/), the [Global Change Center](https://www.globalchange.vt.edu/), the [Center for Advanced Innovation in Agriculture](https://caia.cals.vt.edu/), and the [Stanford RegLab](https://reglab.stanford.edu/), and I co-lead the Insurance & Climate Finance impact area for [NASA Harvest](https://nasaharvest.org/).

My research centers on environment, development, and agriculture, with a focus on how advances in remote sensing and machine learning can help equitably enhance environmental compliance in the U.S. and improve programs to manage weather risk around the globe.

Previously, I was a postdoc in the [Markets, Risk, and Resilience (MRR) Innovation Lab](https://basis.ucdavis.edu/) in the Agricultural and Resource Economics department at UC Davis, following my Ph.D. from the [Emmett Interdisciplinary Program in Environment and Resources (E-IPER)](https://pangea.stanford.edu/eiper) at Stanford. Before grad school I was a research analyst at [Climate Policy Initiative](https://climatepolicyinitiative.org/), after studying economics and environmental science at UNC-Chapel Hill. I’m also a licensed [amateur radio operator](https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service) (call sign K6NMI).

## News & opportunities
{: #news}

> 🔬 **I’m hiring a Research Associate / Research Scientist** in computational spatial science and agricultural insurance, affiliated with [NASA Harvest](https://nasaharvest.org/). See the [full job description](https://docs.google.com/document/d/1Unjme3blWjJTNJ9is0-UMJTaq6uPuQ6FJkoyuBL3LgE/edit) for details, and [email me](mailto:elinor@vt.edu) with your CV and research interests by **July 30, 2026**.

> 🗓️ **AGU 2026 — call for abstracts (now open).** I’m co-convening **NH011: Applications at the Intersection of Science, Practice, and Policy to Proactively Address Natural Hazard Risk** (Natural Hazards section · Session ID 282342). If your work bridges science, practice, and policy on natural-hazard risk, please [submit an abstract](https://agu.confex.com/agu/agu26/prelim.cgi/Home/0) by **5 August 2026** (23:59 EDT / 03:59 UTC).

> 🎓 **Prospective students:** I’m actively recruiting motivated PhD and MS students, postdocs, and research assistants interested in risk prediction and management, and I have opportunities for Virginia Tech undergraduates. **Prospective PhD students** — apply to the [VT AAEC program](https://aaec.vt.edu/academics/graduate/visiting.html) and mention my name. **Current VT students, prospective postdocs, and RAs** — email me a note on your interests, relevant skills, and your CV/resume.

## Research
{: #research}

My work spans several connected themes:

- **Environmental compliance & enforcement** — using machine learning and remote sensing to make monitoring (e.g., of the Clean Water Act) more effective and equitable.
- **Agricultural index insurance** — designing and evaluating weather- and area-based index insurance, including how data resolution and zone definitions shape farmer welfare and payouts.
- **Climate-smart agriculture** — measuring how financial incentives and USDA programs drive adoption of climate-smart practices among U.S. producers.
- **Remote sensing for agricultural risk** — uniting Earth observation, crop modeling, and economics for agricultural risk management.
- **Digital technologies & rural finance** — implications of digital tools for credit, insurance, and savings.
- **Algorithmic fairness & environmental justice** — the distributive effects of risk-prediction tools in public policy.

**Selected current projects & funding**

- Insurance & Climate Finance co-lead, **NASA Harvest** (Co-PI, 2023–2028)
- **VT Alliance for Climate-Smart Agriculture** (Co-PI; part of an $80M USDA grant, 2023–2026)
- VT CALS Strategic Plan seed grant (PI, 2023–2026)
- NASA Land-Cover/Land-Use Change Early Career Scientist grant (Co-Lead PI); Stanford Impact Labs grant for modernizing environmental compliance (Co-PI)

## Publications
{: #publications}

{% if author.googlescholar %}You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a></u>.{% endif %}

{% include base_path %}
{% assign ordered = site.publications | sort: 'date' | reverse %}

### Peer-reviewed & forthcoming articles
{% for post in ordered %}{% if post.category == 'manuscripts' %}{% include archive-single.html %}{% endif %}{% endfor %}

### Working papers & in progress
{% for post in ordered %}{% if post.category == 'working' %}{% include archive-single.html %}{% endif %}{% endfor %}

### Reports & other publications
{% for post in ordered %}{% if post.category == 'reports' %}{% include archive-single.html %}{% endif %}{% endfor %}

## Teaching
{: #teaching}

**At Virginia Tech**

- **Remote Sensing in the Social Sciences** — graduate course, instructor of record (Fall 2021, 2022, 2024)
- **Climate Risk Management** — upper-level undergraduate course, instructor of record (Fall 2023)
- **Environmental & Sustainable Development Economics** — undergraduate course, instructor of record (Spring 2021 & 2022)

**Short courses & earlier**

- **The Economics of Index Insurance** — co-instructor, short course for remote-sensing specialists, Nairobi, Kenya (Summer 2019)
- Teaching assistant: Environmental Governance and World Food Economy (Stanford); Energy in Transition (UNC-Chapel Hill)

## Team
{: #team}

The **HECTA Lab** (Human Environment CompuTing and Ag Lab) brings together students and scholars working at the intersection of environment, development, agriculture, remote sensing, and economics.

**Postdoctoral scholars**

- **Ella Kirchner** — VT Agricultural & Applied Economics; VT Presidential Postdoctoral Fellow (2025–present)
- **Michael J. Cecil** — University of Maryland, Geographical Sciences / NASA Harvest (2024–present)

**Graduate students (co-advised)**

- **Anne Bell Carroll** — PhD, Agricultural & Applied Economics (expected ~2029)

**Graduate committees (current)**

- **Alex Saunders** — PhD, Geography, Development & Environment, University of Arizona (expected ~2027)
- **Matthew Mair** — PhD, Agricultural & Applied Economics (expected May 2028)
- **Nitheshnirmal Sadhasivam** — PhD, Geosciences (expected ~2027)

**Undergraduate research assistants**

- **Riley Rudd**
- **Ari Liverpool**

**Alumni**

- **Armine Poghosyan** — PhD, Agricultural & Applied Economics, 2024 (co-advised)
- **Ram Ramanujan** — MS, Computer Science, 2024 (co-advised)
- **Yuetong Zhang** — PhD, Agricultural & Applied Economics, 2025 (committee)
- **Kristen Swedberg** — PhD, Agricultural & Applied Economics, 2024 (committee)
- **Maguette Sembene** — MS, Agricultural & Applied Economics, 2023 (committee)

## Contact
{: #contact}

- **Email:** [elinor@vt.edu](mailto:elinor@vt.edu)
- **Office:** Agricultural & Applied Economics, Virginia Tech, Blacksburg, VA
- Find me on [Google Scholar]({{ author.googlescholar }}), [GitHub](https://github.com/{{ author.github }}), [LinkedIn](https://www.linkedin.com/in/{{ author.linkedin }}), and [ORCID]({{ author.orcid }}).
