#!/usr/bin/env python3
"""One-off generator: writes _publications/*.md from CV (June 2026). Safe to re-run."""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "_publications")

# (date, slug, category, title, venue, citation, paperurl)
PUBS = [
    # --- Working papers / in progress (dates encode display order) ---
    # Book chapters (Geospatial Impact Evaluation in Practice) first
    ("2026-06-15", "gie-design-choices", "working",
     "Design Choices for Integrating Earth Observation and Socioeconomic Data",
     "Geospatial Impact Evaluation in Practice (eds. A. BenYishay & K. Singh) — accepted, in copy-editing",
     "Michler, J.D., Josephson, A., Benami, E., Behrer, P., Cecil, M.J., Gourlay, S., Heilmayr, R., Kirchner, E., Maskell, G., Singh, K. (accepted, in copy-editing). &quot;Design Choices for Integrating Earth Observation and Socioeconomic Data.&quot; In <i>Geospatial Impact Evaluation in Practice</i> (eds. A. BenYishay &amp; K. Singh).", ""),
    ("2026-06-10", "weather-landcover-gie", "working",
     "Integrating Weather and Land Cover Data into Geospatial Impact Evaluations",
     "Geospatial Impact Evaluation in Practice (eds. A. BenYishay & K. Singh) — under review",
     "Benami, E., Cecil, M., Josephson, A., Maskell, G., Michler, J. (under review). &quot;Integrating Weather and Land Cover Data into Geospatial Impact Evaluations.&quot; In <i>Geospatial Impact Evaluation in Practice</i> (eds. A. BenYishay &amp; K. Singh).", ""),
    ("2026-06-05", "causal-inference-eo", "working",
     "Causal Inference and Counterfactuals in Earth Observation Research",
     "Geospatial Impact Evaluation in Practice (eds. A. BenYishay & K. Singh) — under review",
     "D&#39;Agostino, A., Usmani, F., Benami, E. (under review). &quot;Causal Inference and Counterfactuals in Earth Observation Research.&quot; In <i>Geospatial Impact Evaluation in Practice</i> (eds. A. BenYishay &amp; K. Singh).", ""),
    # Index insurance
    ("2026-06-01", "forecasts-adverse-selection", "working",
     "Forecasts and Adverse Selection in Index Insurance",
     "Working paper (in prep)",
     "Carroll, A., Benami, E., Cecil, M.J. (in prep). &quot;Forecasts and Adverse Selection in Index Insurance.&quot;", ""),
    ("2026-05-15", "rainfall-exceptional-drought", "working",
     "Rainfall Index Insurance Under Exceptional Drought: Payout Alignment and Producer Response",
     "Working paper (in prep)",
     "Cecil, M.J., Benami, E., Carroll, A., Yu, J., Ifft, J. (in prep). &quot;Rainfall Index Insurance Under Exceptional Drought: Payout Alignment and Producer Response.&quot;", ""),
    # Financial incentives
    ("2026-05-01", "financial-incentives-csa", "working",
     "How and Where Do Financial Incentives Promote Adoption of Conservation (Regenerative) Agricultural Practices? A $54 Million Experiment Among US Producers",
     "Working paper (in prep)",
     "Benami, E., Bovay, J., Zhang, W., Ta, C. (in prep). &quot;How and Where Do Financial Incentives Promote Adoption of Conservation (Regenerative) Agricultural Practices? A $54 Million Experiment Among US Producers.&quot; [Preanalysis plan in prep for the AEA RCT Registry]", ""),
    # Sahel
    ("2026-04-15", "drought-vulnerability-niger", "working",
     "Measures and Mediators of Drought-Related Household Vulnerability to Poverty in Niger",
     "Working paper (in prep)",
     "Poghosyan, A., Benami, E., Brunelin, S., Ng, O. (in prep). &quot;Measures and Mediators of Drought-Related Household Vulnerability to Poverty in Niger.&quot;", ""),
    # Other risk work
    ("2026-04-01", "eo-derisk-sustainable-ag", "working",
     "Opportunities for Earth Observation to Help Derisk the Transition to Sustainable Agricultural Systems",
     "Working paper (in prep)",
     "Benami, E., Becker-Reshef, I., Kirchner, E., Cecil, M.J., Chautems, M. (in prep). &quot;Opportunities for EO to Help Derisk the Transition to Sustainable Agricultural Systems.&quot;", ""),

    # --- Peer-reviewed & forthcoming ---
    ("2026-02-01", "get-in-the-zone", "manuscripts",
     "Get in the Zone: The Risk-Adjusted Welfare Effects of Using Machine Learning vs. Administrative Borders to Define Agricultural Index Insurance Zones",
     "Journal of Development Economics",
     "Kirchner, E.*, Benami, E.*, Hobbs, A.W., Carter, M.R., Jin, Z. (2026). &quot;Get in the Zone: The Risk-Adjusted Welfare Effects of Using Machine Learning vs. Administrative Borders to Define Agricultural Index Insurance Zones.&quot; <i>Journal of Development Economics</i>. *Joint first authors.", ""),
    ("2026-06-20", "drop-a-line", "working",
     "Drop a Line, Submit on Time? Evidence from a Randomized Control Trial on the Effect of Pre-Deadline Reminders on Pollution Discharge Reporting",
     "Journal of the Association of Environmental and Resource Economists (conditionally accepted)",
     "Benami, E., Jo, N., Ragnauth, B., Ho, D.E. (conditionally accepted). &quot;Drop a Line, Submit on Time? Evidence from a Randomized Control Trial on the Effect of Pre-Deadline Reminders on Pollution Discharge Reporting.&quot; <i>Journal of the Association of Environmental and Resource Economists</i>.", ""),
    ("2025-09-01", "seeding-change", "manuscripts",
     "Seeding change: Growing insights from four programs to support climate-resilient soil and water conservation in US agriculture",
     "Agricultural Economics",
     "Benami, E., Carroll, A., Messer, K.D., Zhang, W., Cecil, M. (2025). &quot;Seeding change: Growing insights from four programs to support climate-resilient soil and water conservation in US agriculture.&quot; <i>Agricultural Economics</i> 56(3): 457-473.", ""),
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

# External links only (DOIs/publisher/SSRN/regulations.gov from the CV + prior site).
# Papers whose only copy is hosted on the old personal site are intentionally left unlinked.
PAPERURLS = {
    "ml-environmental-monitoring": "https://doi.org/10.1038/s41893-018-0142-9",
    "olive-trees-mapping":         "https://doi.org/10.1016/j.isprsjprs.2024.08.003",
    "rain-check":                  "https://doi.org/10.1017/age.2025.10004",
    "flood-insurance-data-choice": "https://doi.org/10.1029/2025EF005966",
    "oil-palm-para":               "https://doi.org/10.1088/1748-9326/aaa270",
    "seeding-change":              "https://doi.org/10.1111/agec.70034",
    "uniting-advances":            "https://rdcu.be/cdQpO",
    "digital-rural-finance":       "https://doi.org/10.1002/aepp.13151",
    "bridging-science-practice":   "https://doi.org/10.63024/dpc1-nhv2",
    "drop-a-line":                 "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4355984",
    "siepr-compliance-brief":      "https://siepr.stanford.edu/research/publications/innovations-environmental-compliance-emerging-evidence-and-opportunities",
    "usda-rfi-comment":            "https://www.regulations.gov/comment/USDA-2026-0034-0218",
    "epa-neci-comment":            "https://www.regulations.gov/comment/EPA-HQ-OECA-2022-0981-0010",
}

# Optional local PDF copies (rendered as a second "[pdf]" link)
PDFS = {
    "epa-neci-comment": "/files/OMB-2023-0020-0198_attachment.pdf",
}

# Wipe existing publication files and regenerate (this script is the source of truth)
for f in os.listdir(OUT):
    if f.endswith(".md"):
        os.remove(os.path.join(OUT, f))

for date, slug, cat, title, venue, citation, paperurl in PUBS:
    paperurl = PAPERURLS.get(slug, paperurl)
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
    pdf = PDFS.get(slug, "")
    if pdf:
        lines.append(f'pdf: "{pdf}"')
    lines.append(f'citation: "{citation}"')
    lines.append("---")
    lines.append("")
    with open(os.path.join(OUT, fn), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", fn)

print(f"\nTotal: {len(PUBS)} publications")
