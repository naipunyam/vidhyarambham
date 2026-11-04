from common import lesson, module, link, rules, xref, table, fence, Q, RULE, ASOF, CHECK

CONTRACTS = [
    ('Labour contract', 'Owner buys materials; contractor supplies labour', 'Cheapest on paper; owner must manage materials, quality and waste'),
    ('Item-rate contract', 'Paid per unit of work (per cubic metre of concrete, per sq ft of plastering)', 'Clear for each item; needs careful measurement'),
    ('Lump-sum / turnkey (full contract)', 'Fixed price per sq ft or total, materials and labour, to an agreed specification', 'Simple for owners (popular with NRIs); risk of cheaper materials unless the specification is detailed'),
    ('Cost-plus', 'Actual cost plus a percentage fee', 'Transparent if bills are shared; little incentive to save'),
]

STAGES = [
    ('Foundation', 'Soil and foundation depth as per the engineer; anti-termite treatment; proper compaction'),
    ('Concrete (columns, beams, slab)', 'Correct mix or ready-mix grade; steel size and spacing as per drawing; cover blocks; curing with water for the specified days'),
    ('Walls', 'Brick or block quality; mortar mix; straight, plumb walls'),
    ('Roof', 'Slope and waterproofing; sunshades; gutters (heavy Kerala monsoon)'),
    ('Plumbing and electrical', 'ISI-marked pipes and wires; pressure test of pipes; earthing; wiring by a licensed electrician'),
    ('Finishing', 'Plaster without cracks; tiles level with even joints; doors and windows close properly; painting over a primer'),
]

L1 = lesson(
    17, 1,
    outcome='You can estimate construction costs per sq ft, explain the main contract types, run basic quality checks at each stage and describe the building permit process.',
    split='25 minutes reading, 50 minutes on quotes and a site visit',
    core=f"""
You won't be a builder, but clients ask: "What will it cost to build?", "Is this house well built?", "Should I build or buy?". Knowing the basics makes you a better adviser and helps you spot poor construction in houses you sell.

**Cost per sq ft.** Construction cost in Kerala depends on design, materials, finish and labour, and changes with steel, cement and wage prices. There is no reliable official figure for private houses; get **two or three current quotes from local contractors or engineers** for basic, standard and premium finishes, and date them. Add for compound wall, well, septic tank, gate, interior work and contingency (10% to 15%).

**Contract types:**
{table(['Type', 'How it works', 'Pros and risks'], CONTRACTS)}
Always have a **written contract** with the drawings, a detailed specification (brands and grades of cement, steel, tiles, fittings), a payment schedule linked to stages, the completion date, penalties for delay and a defects period.

**Quality checks by stage:**
{table(['Stage', 'What to check'], STAGES)}
An independent engineer's stage inspections are worth paying for, especially for NRI owners.

**The building permit process** (RE-M04-L04):
1. A licensed engineer, architect or building designer prepares the plan to the building rules ({link('kpbr', 'KPBR 2019')} or KMBR).
2. The application goes to the local body through **K-SMART** ({link('week-ksmart', 'The Week')}), with ownership documents, the tax receipt, the site plan and other papers as required.
3. After the permit, build to the approved plan; changes may need a revised permit.
4. On completion, apply for the **occupancy certificate** and then the building number and property tax assessment.
Building without a permit, or deviating from it, can lead to regularisation fees, refusal of building numbers, loan problems and lower resale value.

**Build or buy?** Building gives control but takes 12 to 24 months, needs supervision and often goes over budget. Buying a completed house is faster but needs careful checks of quality and permits.
""",
    example="""
An NRI client wants a 1,400 sq ft two-bedroom house on her 8-cent plot near Velom. Sachin collects three dated quotes (illustrative): basic ₹2,000, standard ₹2,400 and premium ₹3,000 per sq ft (turnkey).
- Standard: 1,400 × 2,400 = **₹33.6 lakh**.
- Extras: compound wall and gate ₹2.5 lakh; septic tank ₹0.8 lakh; well cleaning and pump ₹0.5 lakh; permit drawings and fees ₹0.6 lakh (quote); interior work ₹2 lakh.
- Contingency 10%: about ₹4 lakh.
- **Total ≈ ₹44 lakh.**
He suggests she hire an independent engineer for stage inspections and insist on a detailed specification and stage-linked payments.
""",
    calc="""
- Construction cost: `=area_sqft * rate_per_sqft`
- Total budget: `=construction + SUM(extras) + (construction + SUM(extras))*contingency`
- Example: `=1400*2400` = 33,60,000; extras 6,40,000; contingency 10% of 40,00,000 = 4,00,000 → **₹44,00,000**.
""",
    rules_rows=[
        ('Permit system', 'K-SMART for local body building permits', 'The Week, April 2025'),
        ('Building rules', 'KPBR / KMBR 2019, as amended', 'LSGD PDF'),
    ],
    pro="""
- **Licensed engineer, architect or building designer:** plans, permit, structural design and stage inspections.
- **Licensed electrician:** wiring.
- **Advocate:** construction contracts with large amounts.
""",
    resources=[
        ('kpbr', 'Find the rules on permits and occupancy', '15 minutes'),
        ('week-ksmart', 'K-SMART services', '5 minutes'),
        ('sanketham', 'See the notice on the move from Sanketham', '5 minutes'),
    ],
    steps=[
        'Get two or three dated cost-per-sq-ft quotes from local contractors or engineers for basic, standard and premium finishes.',
        'Visit a house under construction (with the owner\'s permission) and use the stage checklist to note what you see.',
        'Build a construction budget sheet with extras and contingency.',
        'Write a one-page "build or buy?" guide for clients.',
    ],
    proof='The dated quotes, site visit notes, the budget sheet and your guide.',
    templates=[('Construction budget and stage checklist', """CONSTRUCTION BUDGET (tab "Build")   quotes dated ______
B1 Area (sq ft)   B2 Rate per sq ft (quote)   B3 Construction =B1*B2
Extras: compound wall ___ gate ___ septic tank ___ well/pump ___ permit/drawings ___ interiors ___ -> B4 =SUM(...)
B5 Contingency rate (0.10-0.15)   B6 TOTAL =(B3+B4)*(1+B5)
CONTRACT MUST HAVE: drawings | specification with brands/grades | stage payments | completion date | delay penalty | defects period
STAGE CHECKS (independent engineer for NRI clients)
Foundation [ ] Concrete + curing [ ] Walls [ ] Roof + waterproofing [ ] Plumbing pressure test [ ] Electrical + earthing [ ] Finishing [ ]
PERMIT: plan by licensed professional [ ] K-SMART application [ ] permit no. ______ [ ] build to plan [ ] OC applied [ ] building number [ ]""")],
    mistakes=[
        ('Quoting a cost per sq ft from memory.', 'Get dated local quotes.'),
        ('Vague contracts.', 'Detailed specification and stage payments.'),
        ('Building without or beyond the permit.', 'Follow the approved plan; apply for revisions.'),
    ],
    fraud="""
**Contractor advance scams.** Some contractors take large advances and abandon work, or use cheaper materials than promised. Pay by stage, with an engineer's check, against a written specification.
""",
    quiz=[
        Q('Where should a construction cost per sq ft come from?', 'Dated quotes from local contractors or engineers', 'A WhatsApp forward', 'Memory', 'The broker\'s guess', why='Costs change.'),
        Q('Which contract type is simplest for NRI owners but needs a detailed specification?', 'Lump-sum / turnkey', 'Labour contract', 'No contract', 'Cash daily', why='Risk of cheaper materials otherwise.'),
        Q('What must happen after construction is complete?', 'Apply for the occupancy certificate, then the building number', 'Nothing', 'Sell immediately', 'Apply for RERA', why='OC confirms the building matches the permit.'),
        Q('How should a contractor be paid?', 'By stage, linked to completed work and checks', 'All in advance', 'In cash only', 'At random', why='Reduces the risk of abandonment.'),
    ],
    study='read the lesson and both tables',
    action='collect dated construction quotes, visit a site and build a budget sheet',
)

LESSONS = [L1]

MODULE = module(
    17,
    overview=f"""
Construction basics: cost per sq ft and how to get real quotes, contract types, quality checks at each stage, and the building permit and occupancy process.

This helps you advise clients who want to build, judge the quality of houses you sell and avoid recommending poorly built or unpermitted buildings. Everything is {RULE}.
""",
    outcomes=[
        'Estimate a construction budget from local quotes.',
        'Explain the main contract types and what a contract must contain.',
        'Run basic stage-by-stage quality checks.',
        'Describe the permit and occupancy process.',
    ],
    lessons=LESSONS,
    project='a construction guide for clients',
    project_steps=[
        'Budget sheet with dated quotes.',
        'Stage checklist from a site visit.',
        'A one-page "build or buy?" guide.',
    ],
    project_proof='The three items.',
    rubric=[
        ('Costs', 'Guessed', 'One quote', 'Several dated quotes with extras and contingency'),
        ('Contracts', 'Unknown', 'Types known', 'Types and contract essentials explained'),
        ('Quality', 'Not checked', 'Some checks', 'Stage checklist used on a real site'),
    ],
    short=[
        'Get two construction quotes.',
        'Learn the four contract types.',
    ],
    flashcards=[
        ('Turnkey contract', 'Fixed price for materials and labour to a specification.'),
        ('Labour contract', 'Owner buys materials.'),
        ('Curing', 'Keeping concrete wet for the specified days.'),
        ('Contingency', '10% to 15% for overruns.'),
        ('After completion', 'OC, then building number and tax.'),
    ],
    mistakes=[
        ('Ignoring extras.', 'Compound wall, septic tank and interiors add up.'),
        ('No independent checks.', 'Hire an engineer for stage inspections.'),
        ('Promising build costs to clients.', 'Share dated quotes, not promises.'),
    ],
    tools=[
        'Construction budget and stage checklist (RE-M17-L01).',
    ],
    toolkit=[
        'Construction budget sheet and stage checklist.',
    ],
)
