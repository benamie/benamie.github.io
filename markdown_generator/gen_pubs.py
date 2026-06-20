#!/usr/bin/env python3
"""One-off generator: writes _publications/*.md from CV (June 2026). Safe to re-run."""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "_publications")

# (date, slug, category, title, venue, citation, paperurl)
PUBS = [
    # --- Working papers / in progress ---
    ("2026-06-01", "financial-incentives-csa", "working",
     "How and Where Do Financial Incentives Promote Adoption of Climate-Smart Agricultural Practices? A $54 Million Experiment Among US Producers",
     "Working paper (in prep)",
     "Benami, E., Bovay, J., Zhang, W., Ta, C. (in prep). &quot;How and Where Do Financial Incentives Promote Adoption of Climate-Smart Agricultural Practices? A $54 Million Experiment Among US Producers.&quot; [Preanalysis plan in prep for the AEA RCT Registry]", ""),
    ("2026-05-01", "eo-derisk-sustainable-ag", "working",
     "Opportunities for Earth Observation to Help Derisk the Transition to Sustainable Agricultural Systems",
     "Working paper (in prep)",
     "Benami, E., Becker-Reshef, I., Kirchner, E., Cecil, M.J., Chautems, M. (in prep). &quot;Opportunities for EO to Help Derisk the Transition to Sustainable Agricultural Systems.&quot;", ""),
    ("2026-04-01", "weather-landcover-gie", "working",
     "Integrating Weather and Land Cover Data into Geospatial Impact Evaluations",
     "AidData textbook on Geospatial Impact Evaluation (under review)",
     "Benami, E., Cecil, M., Josephson, A., Maskell, G., Michler, J. (under review). &quot;Integrating Weather and Land Cover Data into Geospatial Impact Evaluations.&quot; AidData textbook on Geospatial Impact Evaluation.", ""),
    ("2026-03-01", "causal-inference-eo", "working",
     "Causal Inference and Counterfactuals in Earth Observation Research",
     "AidData textbook on Geospatial Impact Evaluation (under review)",
     "D&#39;Agostino, A., Usmani, F., Benami, E. (under review). &quot;Causal Inference and Counterfactuals in Earth Observation Research.&quot; AidData textbook on Geospatial Impact Evaluation.", ""),

    # --- Peer-reviewed & forthcoming ---
    ("2026-02-01", "get-in-the-zone", "manuscripts",
     "Get in the Zone: The Risk-Adjusted Welfare Effects of Using Machine Learning vs. Administrative Borders to Define Agricultural Index Insurance Zones",
     "Journal of Development Economics",
     "Kirchner, E.*, Benami, E.*, Hobbs, A.W., Carter, M.R., Jin, Z. (2026). &quot;Get in the Zone: The Risk-Adjusted Welfare Effects of Using Machine Learning vs. Administrative Borders to Define Agricultural Index Insurance Zones.&quot; <i>Journal of Development Economics</i>. *Joint first authors.", ""),
    ("2026-01-01", "drop-a-line", "manuscripts",
     "Drop a Line, Submit on Time? Evidence from a Randomized Control Trial on the Effect of Pre-Deadline Reminders on Pollution Discharge Reporting",
     "Journal of the Association of Environmental and Resource Economists (conditionally accepted)",
     "Benami, E., Jo, N., Ragnauth, B., Ho, D.E. (conditionally accepted). &quot;Drop a Line, Submit on Time? Evidence from a Randomized Control Trial on the Effect of Pre-Deadline Reminders on Pollution Discharge Reporting.&quot; <i>Journal of the Association of Environmental and Resource Economists</i>.", ""),
    ("2025-09-01", "seeding-change", "manuscripts",
     "Seeding Change to Manage Climate Change: Growing Insights from Four USDA Programs to Support Climate-Smart Agriculture",
     "Agricultural Economics",
     "Benami, E., Bell, A., Messer, K., Cecil, M., Zhang, W. (2025). &quot;Seeding Change to Manage Climate Change: Growing Insights from Four USDA Programs to Support Climate-Smart Agriculture.&quot; <i>Agricultural Economics</i>.", ""),
    ("2025-06-01", "flood-insurance-data-choice", "manuscripts",
     "Sensitivity to Data Choice Across Scales for Index-Based Flood Insurance",
     "Earth&#39;s Future",
     "Saunders, A., Tellman, B., Benami, E., Anchukaitis, K., Bennett, A., Hossain, S., Islam, A.K.M.S., Giezendanner, J. (2025). &quot;Sensitivity to Data Choice Across Scales for Index-Based Flood Insurance.&quot; <i>Earth&#39;s Future</i>.", ""),
    ("2025-03-01", "rain-check", "manuscripts",
     "Rain Check: Examining How Fine-Scale Precipitation Data Affects Payouts in a U.S. Weather Index Insurance Program",
     "Agricultural and Resource Economics Review",
     "Benami, E., Ramanujan, R., Cecil, M. (2025). &quot;Rain Check: Examining How Fine-Scale Precipitation Data Affects Payouts in a U.S. Weather Index Insurance Program.&quot; <i>Agricultural and Resource Economics Review</i>.", ""),
    ("2024-09-01", "olive-trees-mapping", "manuscripts",
     "Sub-National Scale Mapping of Individual Olive Trees Integrating Earth Observation and Deep Learning",
     "ISPRS Journal of Photogrammetry and Remote Sensing",
     "Lin, C., Zhou, J., Yin, L., Bouabid, R., Mulla, D., Benami, E., Jin, Z. (2024). &quot;Sub-National Scale Mapping of Individual Olive Trees Integrating Earth Observation and Deep Learning.&quot; <i>ISPRS Journal of Photogrammetry and Remote Sensing</i>.", ""),
    ("2024-06-01", "bridging-science-practice", "manuscripts",
     "Bridging Science and Practice to En(in)sure Resilience in a Changing Climate",
     "Journal of Catastrophe Risk and Resilience",
     "Fisher, C., Benami, E., Dolk, E., Baldwin, J., Becker-Reshef, I., Cuppari, R.I., Dalhaus, T., Hobbs, A., Leckebusch, G., Lacovara, P., Sobel, A.H., Tellman, B. (2024). &quot;Bridging Science and Practice to En(in)sure Resilience in a Changing Climate.&quot; <i>Journal of Catastrophe Risk and Resilience</i>.", ""),
    ("2021-09-01", "digital-rural-finance", "manuscripts",
     "Can Digital Technologies Reshape Rural Finance? Implications for Credit, Insurance, and Saving",
     "Applied Economic Perspectives and Policy",
     "Benami, E., Carter, M.R. (2021). &quot;Can Digital Technologies Reshape Rural Finance? Implications for Credit, Insurance, and Saving.&quot; <i>Applied Economic Perspectives and Policy</i>.", ""),
    ("2021-06-01", "uniting-advances", "manuscripts",
     "Uniting Advances in Remote Sensing, Crop Modeling, and Economics for Agricultural Risk Management",
     "Nature Reviews Earth &amp; Environment",
     "Benami, E.*, Jin, Z.*, Carter, M.R., Kenduiywo, B., Ghosh, A., Hobbs, A.W., Hijmans, R., Lobell, D. (2021). &quot;Uniting Advances in Remote Sensing, Crop Modeling, and Economics for Agricultural Risk Management.&quot; <i>Nature Reviews Earth &amp; Environment</i>. *Joint first authors.", ""),
    ("2021-03-01", "distributive-effects-facct", "manuscripts",
     "The Distributive Effects of Risk Prediction in Environmental Compliance: Algorithmic Design, Environmental Justice, and Public Policy",
     "ACM Conference on Fairness, Accountability, and Transparency (FAccT)",
     "Benami, E., Whitaker, R., Anderson, B., Ho, D.E., La, V., Lin, H. (2021). &quot;The Distributive Effects of Risk Prediction in Environmental Compliance: Algorithmic Design, Environmental Justice, and Public Policy.&quot; <i>Proceedings of the ACM Conference on Fairness, Accountability, and Transparency (FAccT)</i>.", ""),
    ("2018-10-01", "ml-environmental-monitoring", "manuscripts",
     "Machine Learning for Environmental Monitoring",
     "Nature Sustainability",
     "Hino, M.*, Benami, E.*, Brooks, N. (2018). &quot;Machine Learning for Environmental Monitoring.&quot; <i>Nature Sustainability</i>. *Joint first authors.", ""),
    ("2018-03-01", "oil-palm-para", "manuscripts",
     "Oil Palm Land Conversion in Par&aacute;, Brazil, 2006-2014: Evaluating the 2010 Brazilian Sustainable Palm Oil Production Program",
     "Environmental Research Letters",
     "Benami, E., Curran, L.M., Cochrane, M., Venturieri, A., Swartos, A., Moraes Franco, R., Kneipp, J. (2018). &quot;Oil Palm Land Conversion in Par&aacute;, Brazil, 2006-2014: Evaluating the 2010 Brazilian Sustainable Palm Oil Production Program.&quot; <i>Environmental Research Letters</i>. 13(3): 1-12.", ""),
    ("2010-01-01", "energy-economic-development", "manuscripts",
     "Energy-Based Economic Development",
     "Renewable and Sustainable Energy Reviews",
     "Carley, S., Lawrence, S., Brown, A., Nourafshan, A., Benami, E. (2010). &quot;Energy-Based Economic Development.&quot; <i>Renewable and Sustainable Energy Reviews</i>. 15(1): 282-295.", ""),

    # --- Reports & other publications ---
    ("2026-01-15", "usda-rfi-comment", "reports",
     "Public Comment in Response to USDA Request for Information on Opportunities, Challenges, and Emerging Areas in Statistical Data, Analysis, and Research",
     "Public Comment (NASA Harvest / Acres)",
     "Becker-Reshef, I., Whitcraft, A., Justice, C., Benami, E., Humber, M., Rejesus, R. (2026). Public Comment in Response to USDA Request for Information on Opportunities, Challenges, and Emerging Areas in Statistical Data, Analysis, and Research, with NASA Harvest/Acres.", ""),
    ("2023-06-01", "epa-neci-comment", "reports",
     "Public Comment on U.S. EPA&#39;s Draft National Enforcement and Compliance Initiatives for Fiscal Years 2024-2027",
     "Public Comment",
     "Rodolfa, K., Ho, D.E., Honigsberg, C., Benami, E. (2023). Public Comment on U.S. EPA&#39;s Draft National Enforcement and Compliance Initiatives for Fiscal Years 2024-2027.", ""),
    ("2020-02-01", "siepr-compliance-brief", "reports",
     "Innovations for Environmental Compliance: Emerging Evidence and Opportunities",
     "Stanford Institute for Economic Policy Research (Policy Brief)",
     "Benami, E., Ho, D.E., McDonough, A. (2020). &quot;Innovations for Environmental Compliance: Emerging Evidence and Opportunities.&quot; <i>Stanford Institute for Economic Policy Research Policy Brief</i>.", ""),
    ("2013-02-01", "prop-39", "reports",
     "Targeting Proposition 39 to Help California&#39;s Schools Save Energy and Money",
     "Climate Policy Initiative report",
     "Zuckerman, J., Deason, J., Benami, E. (2013). &quot;Targeting Proposition 39 to Help California&#39;s Schools Save Energy and Money.&quot; <i>Climate Policy Initiative</i>.", ""),
    ("2013-01-01", "solar-leasing", "reports",
     "Improving Solar Policy: Lessons from the Solar Leasing Boom in California",
     "Climate Policy Initiative report",
     "Pierpont, B., Varadarajan, U., Hobbs, A., Benami, E. (2013). &quot;Improving Solar Policy: Lessons from the Solar Leasing Boom in California.&quot; <i>Climate Policy Initiative</i>.", ""),
]

# Remove old placeholder papers
for f in os.listdir(OUT):
    if "paper-title-number" in f:
        os.remove(os.path.join(OUT, f))

for date, slug, cat, title, venue, citation, paperurl in PUBS:
    fn = f"{date}-{slug}.md"
    lines = [
        "---",
        f'title: "{title}"',
        "collection: publications",
        f"category: {cat}",
        f"permalink: /publication/{date}-{slug}",
        f"date: {date}",
        f'venue: "{venue}"',
    ]
    if paperurl:
        lines.append(f'paperurl: "{paperurl}"')
    lines.append(f'citation: "{citation}"')
    lines.append("---")
    lines.append("")
    with open(os.path.join(OUT, fn), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", fn)

print(f"\nTotal: {len(PUBS)} publications")
