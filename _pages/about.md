---
permalink: /
excerpt: "Assistant Professor of Agricultural & Applied Economics at Virginia Tech"
author_profile: true
header:
  image: banner-fall.jpg
  caption: 'Blue Ridge Mountains, SW Virginia · Photo by <a href="https://unsplash.com/@sickhews?utm_source=unsplash&utm_medium=referral">Wes Hicks</a> on <a href="https://unsplash.com/photos/green-mountains-under-white-sky-during-daytime-ZW6RUvsaFTc?utm_source=unsplash&utm_medium=referral">Unsplash</a>'
redirect_from:
  - /about/
  - /about.html
---

## About
{: #about}

I am an applied microeconomist whose research bridges environmental, agricultural, and development economics, often drawing upon geospatial and Earth-observation data. I study how producers, firms, and regulators respond to risk and information, with the goal of improving the design of policies and programs for public benefit in both international as well as U.S. contexts. 

Much of my current work centers on agricultural index insurance — how these programs are designed and evaluated as well as how enrollment responds to past weather, realized payouts, and seasonal forecasts. Other active work evaluates the impacts of programs that pay producers to adopt soil and water conservation practices as well as how firms respond to information about regulatory compliance risk. 

Institutionally, I'm an Assistant Professor at Virginia Tech in the [Agricultural and Applied Economics Department](https://aaec.vt.edu). I’m also a faculty affiliate of the [VT Remote Sensing Graduate Education Group](https://rsigep.frec.vt.edu/), the [Global Change Center](https://www.globalchange.vt.edu/), and the [Stanford RegLab](https://reglab.stanford.edu/). I co-lead the Agricultural Insurance & Finance impact area for [NASA Harvest](https://nasaharvest.org/), a consortium for monitoring global food production with Earth Observations. Previously, I was a postdoc in the [Markets, Risk, and Resilience (MRR) Innovation Lab](https://basis.ucdavis.edu/) in the Agricultural and Resource Economics department at UC Davis, following my Ph.D. from the [Emmett Interdisciplinary Program in Environment and Resources (E-IPER)](https://pangea.stanford.edu/eiper) at Stanford. Before grad school I was a research analyst at [Climate Policy Initiative](https://climatepolicyinitiative.org/), after studying economics and environmental science at UNC-Chapel Hill. 

**Full CV linked [here](https://benamie.github.io/files/cv_Benami_june2026.pdf)**

## News & announcements
{: #news}

<div class="news-feed" markdown="1">

<p class="news-highlight" markdown="1"><span class="flip-x">📣</span> **Jun 2026 · Now hiring — Research Associate or Research Scientist.** A position in Agricultural Economics and Remote Sensing, affiliated with [NASA Harvest](https://nasaharvest.org/) and based at Virginia Tech with me. See the [job description and application instructions here](https://docs.google.com/document/d/1Unjme3blWjJTNJ9is0-UMJTaq6uPuQ6FJkoyuBL3LgE/edit). **Priority application deadline: July 30, 2026.**</p>

<p class="news-course" markdown="1">💺 **Hoping to take Remote Sensing in the Social Sciences (AAEC/FREC/GEOG 5544) in Fall 2026?** I have heard from multiple students that the course is listed as full. I am working with administrators to expand capacity, either by raising the cap or moving to a larger room. If you also want to enroll and cannot, please [email me](mailto:elinor@vt.edu?subject=AAEC%2FFREC%2FGEOG%205544%20-%20Fall%202026%20-%20Course%20Enrollment%20Request) with "AAEC/FREC/GEOG 5544" in the subject line so I can track how many students are affected.</p>

🗓️ **AGU 2026 — call for abstracts.** I’m co-convening a session **NH011: Applications at the Intersection of Science, Practice, and Policy to Proactively Address Natural Hazard Risk** (Session #282342). [Submit an abstract](https://agu.confex.com/agu/agu26/prelim.cgi/Home/0) by **5 August 2026** (23:59 EDT / 03:59 UTC).

🎤 **AGU 2026 · Invited speaker.** I’ll be speaking in the joint [NASA Harvest](https://nasaharvest.org/)/[NASA Acres](https://www.nasaacres.org/) session **GC108: Satellite Solutions: Agricultural Monitoring Through Remote Sensing** on the opportunities (and challenges) of integrating Earth observation into agricultural insurance and finance.

🗣️ **Jun 2026 · Presenting at the [Geofield Convening](https://www.aiddata.org/events/geofield-2026-convening) at the Food and Agriculture Organization (FAO) in Rome** on our open-access paper in the [*Journal of Development Economics*](https://www.sciencedirect.com/science/article/pii/S0304387825002093) and *Geospatial Impact Evaluation in Practice* book chapters.

📄 **Apr 2026 · New public comment to USDA.** Along with the leadership of [NASA Harvest](https://nasaharvest.org/) and NASA Acres, I submitted a public comment synthesizing the use of Earth observation data to strengthen US Agricultural Statistics, in response to a USDA Request for Information on Opportunities, Challenges, and Emerging Areas in Statistical Data, Analysis, and Research (FRN 2026-03497). [Read it](https://www.regulations.gov/comment/USDA-2026-0034-0218).

🎉 **March 2026 · Anne Carroll received the (sole) Agricultural Risk Analysis travel award** to present our work at the SCC-76 (Coordinating Committee on Economics and Management of Risk in Agriculture) meeting at the Federal Reserve Bank of Kansas City.

🎉 **March 2025 · Ella Kirchner named a VT Presidential Postdoctoral Fellow.** [Read more](https://www.research.vt.edu/about/postdoctoral-associates/virginia-tech-presidential-postdoctoral-fellowships/current-fellows/kirchner-ella.html).

🎓 **Ongoing · Recruiting students.** I’m actively recruiting PhD and MS students, postdocs, and research assistants interested in risk prediction and management, with opportunities for Virginia Tech undergraduates. Prospective PhD students: apply to the [VT AAEC program](https://aaec.vt.edu/academics/graduate/visiting.html) and mention my name.

📰 **In the news.** Coverage of [Virginia Tech’s alliance to advance soil and water conservation practices agriculture](https://news.vt.edu/articles/2024/05/cals-slabach.html) and [our work with NASA Harvest on agricultural insurance](https://news.vt.edu/articles/2024/01/cals_nasa.html).

</div>


## Publications
{: #publications}

{% if author.googlescholar %}You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a></u>.{% endif %}

{% assign manuscripts = site.publications | where: "category", "manuscripts" | sort: "date" | reverse %}
{% assign working = site.publications | where: "category", "working" | sort: "date" | reverse %}
{% assign reports = site.publications | where: "category", "reports" | sort: "date" | reverse %}

<ol class="pub-list">{% for post in manuscripts %}<li>{{ post.citation }}{% if post.paperurl %} <a class="pub-link" href="{{ post.paperurl }}">[link]</a>{% endif %}{% if post.pdf %} <a class="pub-link" href="{{ post.pdf }}">[pdf]</a>{% endif %}{% if post.relatedurl %} <a class="pub-link" href="{{ post.relatedurl }}">[{{ post.relatedlabel }}]</a>{% endif %}{% if post.press %}{% for item in post.press %} <a class="pub-link" href="{{ item.url }}">[{{ item.label }}]</a>{% endfor %}{% endif %}</li>{% endfor %}</ol>

### Working papers
<ol class="pub-list">{% for post in working %}<li>{{ post.citation }}{% if post.paperurl %} <a class="pub-link" href="{{ post.paperurl }}">[link]</a>{% endif %}{% if post.pdf %} <a class="pub-link" href="{{ post.pdf }}">[pdf]</a>{% endif %}{% if post.relatedurl %} <a class="pub-link" href="{{ post.relatedurl }}">[{{ post.relatedlabel }}]</a>{% endif %}{% if post.press %}{% for item in post.press %} <a class="pub-link" href="{{ item.url }}">[{{ item.label }}]</a>{% endfor %}{% endif %}</li>{% endfor %}</ol>

### Reports & other publications
<ol class="pub-list">{% for post in reports %}<li>{{ post.citation }}{% if post.paperurl %} <a class="pub-link" href="{{ post.paperurl }}">[link]</a>{% endif %}{% if post.pdf %} <a class="pub-link" href="{{ post.pdf }}">[pdf]</a>{% endif %}{% if post.relatedurl %} <a class="pub-link" href="{{ post.relatedurl }}">[{{ post.relatedlabel }}]</a>{% endif %}{% if post.press %}{% for item in post.press %} <a class="pub-link" href="{{ item.url }}">[{{ item.label }}]</a>{% endfor %}{% endif %}</li>{% endfor %}</ol>

## Teaching
{: #teaching}

Full course descriptions, syllabi, and guidance for students (including requesting reference letters) are on my **[Teaching & Mentoring](/teaching-and-mentoring/)** page.

- **Remote Sensing in the Social Sciences** — graduate course, instructor of record (Fall 2021, 2022, 2024, 2026). How remotely sensed data is and can be appropriately used in social science research, with a focus on readings in environment, agriculture, and economic development and hands-on lab exercises with cloud-based geospatial platforms. 
- **Climate Risk Management** — upper-level undergraduate course, instructor of record (Fall 2023). The science and economics of extreme weather and climate change; how we detect shifting weather patterns, their implications for society, and policy options to manage the risks.
- **Environmental & Sustainable Development Economics** — undergraduate course, instructor of record (Spring 2021, 2022, 2027). How approaches from economics can help society weigh policy questions relating to pollution and sustainable development; how environmental problems and policies vary between developing and developed country contexts. 

**Prior experience**

- **The Economics of Index Insurance** — co-instructor, short course for remote-sensing specialists (Nairobi, Kenya, Summer 2019). An applied short course on the design, pricing, and evaluation of agricultural index insurance for managing risk - for pracitioners.
- **World Food Economy** (ECON/ESS 106/206) — teaching assistant, Stanford University (undergraduate and graduate). The economics of global food production, agricultural markets, hunger, and food and environmental policy.
- **Environmental Governance** (ENVRES 250) — teaching assistant, Stanford University (undergraduate). Seminar on governing shared, common-pool resources (fisheries, forests, and water), and the human behaviors and institutions that shape environmental outcomes in socio-environmental systems. 
- **Energy in Transition: De-Carbonizing America** — teaching assistant, University of North Carolina at Chapel Hill (honors undergraduate seminar). The policies, technologies, and economics of the U.S. transition to lower-carbon energy.

## HECTARE Lab
{: #team}

The **HECTARE Lab** (Human Environment CompuTing and Agricultural Research Lab) brings together students and scholars engaged at the intersection of economics and data science related to issues affecting humans, agriculture, and the environment. We meet ~weekly during the academic year to present and get feedback on ongoing research as well as discuss issues and skills of common interest.

**Postdoctoral scholars**

- **[Ella Kirchner](https://www.linkedin.com/in/ella-kirchner-4993a8150/)** — VT Agricultural & Applied Economics; VT Presidential Postdoctoral Fellow / NASA Harvest (2024–2026). *Starting August 2026 as an Assistant Professor in Business Economics at Wageningen University.* 
- **[Michael J. Cecil](https://geog.umd.edu/facultyprofile/cecil/michael)** — University of Maryland, Geographical Sciences / NASA Harvest (2024–present)

**Graduate students**

- **[Anne Bell Carroll](https://www.linkedin.com/in/anne-carroll-9a56b9253/)** — PhD, Agricultural & Applied Economics (expected ~2029)
- **[Alex Saunders](https://alex-saunders00.github.io/)** — PhD, Geography, Development & Environment, University of Arizona (expected ~2027)
- **Ivy (Shengke) Wang** — PhD, Agricultural & Applied Economics (expected ~2031)

**Additional Advisees**

- **Matthew Mair** — PhD, Agricultural & Applied Economics (expected May 2028)
- **Yi-Tien Lu** — PhD, Agricultural & Applied Economics (expected May 2029)
- **Nitheshnirmal Sadhasivam** — PhD, Geosciences (expected ~2027)

## Alumni/ae
Current and former advisees, as well as their last known position:

- **[Yuetong Zhang](https://www.linkedin.com/in/yuetong-zhang-44595887)** — PhD, Agricultural & Applied Economics, 2025 (committee): postdoc, University of North Carolina, Chapel Hill Department of Public Policy, Data-Driven Envirolab 
- **[Armine Poghosyan](https://www.linkedin.com/in/poghosyan-armine/)** — PhD, Agricultural & Applied Economics, 2024 (co-advised): assistant professor, Tennessee State University
- **[Ramaraja Ramanujan](https://www.linkedin.com/in/ramaraja)** — MS, Computer Science, 2024 (co-advised): Microsoft 
- **[Kristen Swedberg](https://kristen-swedberg.com/)** — PhD, Agricultural & Applied Economics, 2024 (committee): PRODiG+ Postdoctoral Fellow in the Department of Public Administration and Policy at Binghamton University 
- **[Maguette Sembene](https://aaec.vt.edu/people/phd_students.html)** — MS, Agricultural & Applied Economics, 2023 (committee): PhD Student, Virginia Tech Agricultural & Applied Economics 
- **[Riley Rudd](https://www.linkedin.com/in/riley-rudd-1166a3192)** — Data Science for the Public Good mentee & Undergrad Research Assistant: Data Engineer, MITRE 
- **[Ari Liverpool](https://www.linkedin.com/in/ari-liverpool)** — Undergrad Research Assistant: Business Analyst, Capital One


