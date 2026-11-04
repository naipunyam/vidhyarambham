"""Copy-ready tools for the Kerala real estate course. Formulas work in Google
Sheets and LibreOffice Calc (if your LibreOffice uses semicolons, replace
commas between arguments with semicolons)."""

COMPS_HEADER = 'Date seen,Source (portal/broker/owner),Link or contact,Locality,Panchayat/municipality,Type (land/house/flat/commercial),Land area (cents),Built-up area (sq ft),Asking price (Rs),Price per cent (Rs),Price per sq ft (Rs),Road frontage (ft),Road width (ft),Distance to town (km),Flood/slope notes,Status (asking/sold/withdrawn),Notes'
COMPS_FORMULAS = """COMPARABLES SHEET (tab "Comps")  Row 1 = headers above. In row 2:
J2 (price per cent):   =IF(G2>0, I2/G2, "")
K2 (price per sq ft):  =IF(H2>0, I2/H2, "")
Copy J2:K2 down. Summary cells (land only, for one locality):
Median price per cent: =MEDIAN(FILTER(J2:J200, F2:F200="land", D2:D200="Kuttiady"))
Count of land listings: =COUNTIFS(F2:F200,"land",D2:D200,"Kuttiady")
(LibreOffice without FILTER: use a pivot table, or sort and pick the middle value.)
Rule: compare like with like (same area, similar size, similar road access)."""

COST_CALC = """FULL COST OF A PURCHASE (tab "Cost") - rates as of November 2026; check current rules
B1  Agreed price (Rs)                       [type]
B2  Fair value of the land/building (Rs)    [type, from the IGR fair value search]
B3  Value for duty = higher of the two      =MAX(B1,B2)
B4  Stamp duty rate                         0.08   (sale deed; check current rules)
B5  Registration fee rate                   0.02   (check current rules)
B6  Stamp duty (Rs)                         =B3*B4
B7  Registration fee (Rs)                   =B3*B5
B8  Document writer / advocate fee (Rs)     [type quote]
B9  EC, certified copies, sketches (Rs)     [type]
B10 Brokerage rate                          [type, e.g. 0.01 or 0.02]
B11 Brokerage (Rs)                          =B1*B10
B12 GST on brokerage (if charged)           =B11*0.18
B13 Loan processing fee and legal/valuation charges (Rs)  [type]
B14 Mutation, misc. travel (Rs)             [type]
B15 TOTAL extra costs                       =SUM(B6:B9,B11:B14)
B16 TOTAL cost of purchase                  =B1+B15
B17 Extra costs as % of price               =B15/B1
B18 TDS to deduct (if B1 or B2 is Rs 50 lakh or more) =IF(MAX(B1,B2)>=5000000, MAX(B1,B2)*0.01, 0)
(TDS is not an extra cost: it is part of the price paid to the government for the seller.)"""

ROI_CALC = """RENTAL YIELD AND RETURN CALCULATOR (tab "ROI")
B1  Purchase price (Rs)                 [type]
B2  Purchase costs (Rs)                 [from Cost tab B15]
B3  Total investment (Rs)               =B1+B2
B4  Monthly rent (Rs)                   [type]
B5  Gross annual rent                   =B4*12
B6  Gross rental yield                  =B5/B1
B7  Vacancy allowance (months a year)   [type, e.g. 1]
B8  Building tax + land tax per year    [type]
B9  Maintenance and repairs per year    [type, e.g. 1% of building value]
B10 Insurance and management fees       [type]
B11 Net operating income (NOI)          =B4*(12-B7)-B8-B9-B10
B12 Net yield / cap rate                =B11/B1
B13 Loan amount (Rs)                    [type, 0 if none]
B14 Annual interest rate                [type, e.g. 0.085]
B15 Loan term (years)                   [type]
B16 Monthly EMI                         =IF(B13>0, -PMT(B14/12, B15*12, B13), 0)
B17 Annual loan payments                =B16*12
B18 Cash invested (own money)           =B3-B13
B19 Annual cash flow after EMI          =B11-B17
B20 Cash-on-cash return                 =IF(B18>0, B19/B18, "")
IRR (tab "IRR"): list year 0 cash flow as minus own cash invested, then each
year's cash flow, and in the final year add the expected sale price minus
selling costs and loan balance. =IRR(B2:B12)"""

EMI = """EMI FORMULAS
Monthly EMI:      =-PMT(annual_rate/12, years*12, loan_amount)
Example:          =-PMT(0.085/12, 20*12, 2500000)   -> about Rs 21,700
Total paid:       =EMI*years*12
Total interest:   =EMI*years*12 - loan_amount
Max loan from an EMI you can afford: =-PV(annual_rate/12, years*12, EMI)"""

DUE_DILIGENCE = """DUE-DILIGENCE CHECKLIST (one per property; tick and attach proof)
OWNERSHIP AND TITLE                                          Done  Proof file
[ ] Copy of the current title deed (aadharam) seen and read     __    ______
[ ] Prior deeds (title chain) for at least 30 years, if possible __   ______
[ ] Encumbrance certificate (EC) for 30+ years (mortgages, sales, attachments) __ ______
[ ] Seller's name matches deed, EC, thandaper, land tax receipt and ID __ ______
[ ] All co-owners / legal heirs identified and willing to sign  __    ______
[ ] Power of attorney (if any): original, registered, still valid, principal alive __ ______
[ ] Possession certificate / location certificate from the village office __ ______
[ ] Latest land tax (karam) receipt                             __    ______
[ ] Mutation (pokkuvaravu) done in the seller's name            __    ______
LAND RECORDS AND SURVEY
[ ] Survey / resurvey number and sub-division match all papers  __    ______
[ ] Sketch / FMB from the village or e-Rekha; area matches the deed __ ______
[ ] Land type in revenue records (purayidam / nilam / thottam / data bank) __ ______
[ ] Not in the paddy/wetland data bank (or conversion order exists) __ ______
[ ] Not government, puramboke, forest or excess (surplus) land  __    ______
BUILDING (if any)
[ ] Building permit and approved plan from the panchayat/municipality __ ______
[ ] Occupancy certificate / building number; building tax receipt __ ______
[ ] Built area matches the permit (no unauthorised additions)   __    ______
LOCATION AND RISK
[ ] Physical visit: boundaries match sketch; neighbours confirm __    ______
[ ] Access road: public road or registered right of way; width __    ______
[ ] Flood, landslide and water-logging check (KSDMA maps, neighbours, 2018/2019 floods) __ ______
[ ] CRZ (coastal), ESA (Western Ghats), forest buffer, quarry nearby __ ______
[ ] Land-use / master plan zoning (municipalities) if known      __    ______
[ ] Electricity, water, drainage, mobile signal                  __    ______
DISPUTES AND DEBTS
[ ] No pending case (ask seller in writing; advocate searches)  __    ______
[ ] No bank loan or attachment on EC; loan closure letter if there was one __ ______
[ ] No tenant or occupant claim; no encroachment                __    ______
PROFESSIONAL SIGN-OFF
[ ] Advocate's title opinion (written)                          __    ______
[ ] Licensed surveyor's measurement (if boundaries or area are unclear) __ ______
DECISION: proceed / proceed with conditions / walk away   Reason: ______"""

DOC_CHECKLIST = """DOCUMENT CHECKLIST BY DEAL TYPE
SALE (land or house)          Seller brings           Buyer brings
  Title deed + prior deeds    [ ]                     ID, PAN, photos [ ]
  EC (30 years)               [ ]                     Funds by bank transfer [ ]
  Thandaper, land tax receipt [ ]                     Loan sanction (if any) [ ]
  Possession / location cert. [ ]                     TDS paid (if Rs 50 lakh+) [ ]
  Sketch / FMB                [ ]
  Building permit, OC, building tax (if building) [ ]
  ID, PAN, photos; all co-owners [ ]
RENTAL
  Owner: ownership proof, building tax receipt, ID  [ ]
  Tenant: ID, address proof, employer/college letter, references, photos [ ]
  Signed agreement (and registration if lease is longer than 11 months / over a year: check) [ ]
  Inventory list with photos; meter readings [ ]
NRI OWNER
  Registered power of attorney (if not attending) [ ]  Passport copy [ ]
  NRO/NRE bank details for funds [ ]  Tax advice from a CA [ ]"""

MANDATE = """OWNER MANDATE (agreement to market a property) - review with an advocate before use
This agreement is made on ______ at ______ between:
OWNER: ______ (address ______, phone ______) and
AGENT: ______ (K-RERA agent registration no. ______, if registered; address ______)
1. Property: survey no. ______, ______ village, ______ taluk, area ______ cents,
   building ______ sq ft, as per title deed no. ______ of ______ SRO.
2. Purpose: the owner authorises the agent to market the property for SALE / RENT.
3. Type: exclusive / non-exclusive. Period: from ______ to ______ (e.g. 90 days).
4. Asking price / rent: Rs ______. Minimum acceptable: to be decided by the owner only.
5. Commission: ______% of the final sale price (or ___ month's rent), payable by the
   owner only on registration of the sale deed / signing of the rental agreement,
   by bank transfer, with a GST invoice if the agent is GST-registered.
6. The owner confirms that the information given is true and that they have the
   right to sell / let. The agent will not publish anything the owner has not approved.
7. The agent will: market honestly, share all offers in writing, not take money from
   buyers on the owner's behalf without written approval, and keep documents private.
8. Photos and videos may be published on: ______ (portals / social media).
9. Either party may end this agreement with ___ days' written notice.
Owner signature ______  Agent signature ______  Witnesses 1 ______ 2 ______"""

INTAKE = """CLIENT INTAKE (buyer or tenant)              Date ______  Source ______
Name ______  Phone ______  WhatsApp Y/N  Email ______  NRI? Y/N (country ______)
Looking for: buy / rent    Type: land / house / flat / commercial
Areas (in order): 1 ______ 2 ______ 3 ______
Budget: Rs ______ to ______   Loan needed? Y/N   Pre-approved? Y/N
Land size ______ cents   Bedrooms ______   Must-haves: road access / water / school nearby / ______
Deal-breakers: flood-prone / steep slope / narrow road / ______
Timeline: move/buy by ______   Decision makers: ______
Viewing availability: ______   Consent to store details in my CRM: Y/N"""

SITE_VISIT = """SITE-VISIT CHECKLIST           Property ______  Date ______  With ______
BEFORE: owner permission [ ]  route and timing [ ]  documents summary in hand [ ]
        client's must-haves list [ ]  measuring tape, phone charged [ ]
ON SITE
[ ] Road: public or private? width ___ ft; vehicle access in monsoon?
[ ] Boundaries: walls/stones match sketch? neighbours' names ______
[ ] Slope, soil, rock; water-logging signs; flood level marks from 2018/2019?
[ ] Water: well depth/level ___; KWA connection? Electricity: phase ___
[ ] Building: cracks, dampness, roof leaks, wiring, plumbing, septic tank location
[ ] Surroundings: quarry, stream, high-tension line, temple/mosque/church, school, shops
[ ] Mobile signal ___; nearest bus stop ___ km
[ ] Photos: front, road, boundaries, each room, issues found
AFTER: client feedback (1-5) ___ ; questions for owner ______ ; next step ______"""

LISTING = """LISTING TEMPLATE (honest, specific, owner-approved)
TITLE: [Size] [Type] for [sale/rent] in [Locality], [distance] from [landmark]
e.g. "12 cents residential land for sale, 1.5 km from Kuttiady bus stand"
PRICE: Rs ______ (negotiable / fixed)   Price per cent: Rs ______
KEY FACTS: land ___ cents | built-up ___ sq ft | road ___ ft wide | ___ km to ___
           water: well / KWA | electricity | facing ___ | title: clear (advocate-checked? Y/N)
DESCRIPTION (3-5 short lines, facts not hype):
______________________________________________
NOT INCLUDED / HONEST NOTES: e.g. "Narrow private road for last 50 m" "Part of land slopes"
DOCUMENTS AVAILABLE: deed, EC, thandaper, tax receipts, permit/OC
CONTACT: ______ (K-RERA agent reg. no. ______ if applicable)
Owner approval of this text and photos: signed / WhatsApp message saved on ______"""

CRM_HEADER = 'Lead ID,Date,Name,Phone,Source,Buy/Rent/Sell/Let,Type,Area wanted,Budget (Rs),Stage (new/contacted/visit booked/visited/offer/agreement/closed/lost),Next action,Next action date,Properties shown,Notes,Consent (Y/N)'
CRM_FORMULAS = """CRM SHEET (tab "Leads"). Row 1 = headers above.
Overdue follow-ups: add column P "Overdue?" with =IF(AND(L2<>"", L2<TODAY(), J2<>"closed", J2<>"lost"),"OVERDUE","")
Pipeline count by stage (on a "Dashboard" tab): =COUNTIF(Leads!J:J,"visited")
Conversion rate: =COUNTIF(Leads!J:J,"closed")/COUNTA(Leads!A2:A)
Use Data > Data validation on column J so stages are always spelled the same."""

TIMELINE = """TRANSACTION TIMELINE (sale)                    Target date   Done
Day 0    Offer accepted; token advance by bank transfer with signed receipt  ____  [ ]
Day 1-7  Documents collected; EC applied; advocate engaged          ____  [ ]
Day 7-21 Due diligence; advocate's written title opinion           ____  [ ]
Day 7-30 Agreement for sale signed (advance, balance date, conditions) ____ [ ]
Day 15-60 Loan sanction, bank's legal and technical check (if loan) ____  [ ]
         Fair value check; stamp duty and fee calculated; e-stamp bought ____ [ ]
         Draft sale deed by a licensed document writer or advocate; both sides read it ____ [ ]
         TDS deducted and paid (if Rs 50 lakh or more)              ____  [ ]
Day X    Registration at the Sub-Registrar Office (SRO); balance paid by bank transfer ____ [ ]
Day X+   Original deed collected; mutation (pokkuvaravu) applied / auto-mutation checked ____ [ ]
         Land tax paid in buyer's name; building tax/electricity/water transferred ____ [ ]
         Keys and possession handed over; handover note signed       ____  [ ]
         Commission invoice and payment by bank transfer             ____  [ ]"""

RENTAL_AGREEMENT = """RENTAL AGREEMENT CHECKLIST (have an advocate review your template)
[ ] Parties' full names, addresses, ID numbers (last 4 digits only in copies you share)
[ ] Property address, what is included (rooms, furniture, parking)
[ ] Term (start, end), renewal, notice period for both sides
[ ] Monthly rent, due date, payment method (bank transfer/UPI), late fee
[ ] Security deposit amount, how and when it is refunded, permitted deductions
    (note: the Kerala rent control law limits advances; ask an advocate what applies)
[ ] Rent increase terms
[ ] Who pays electricity, water, building tax, maintenance, minor and major repairs
[ ] Use (residential / commercial), number of occupants, no subletting without consent
[ ] Owner's entry for inspection with notice
[ ] Inventory and condition at move-in (photos, meter readings) and at move-out
[ ] Stamp paper value and registration requirement checked for the term (check current rules)
[ ] Police/tenant verification done as required locally
[ ] Signatures of both parties and two witnesses"""

NRI_CARE = """NRI PROPERTY CARE SERVICE MENU (example; set your own prices)
BASIC (monthly)       Visit once a month, 20 photos + short video, check locks,
                      leaks, cleanliness, encroachment, neighbours' news   Rs ______
STANDARD (monthly)    Basic + pay land/building tax, electricity, water bills
                      (owner's money, receipts shared), garden clearing    Rs ______
RENTAL MANAGEMENT     Find and screen tenants, agreement, rent collection to owner's
                      account, repairs coordination, monthly statement     ___% of rent
ONE-TIME              Document collection (EC, tax receipts, certificates),
                      representation at offices with written authority      Rs ______ per task
RULES: written service agreement; owner's money never mixed with yours; every
payment with receipt; monthly report on the same date; no sale or legal act without
a registered power of attorney and the owner's written instruction."""

WEEKLY_LOG = """WEEKLY MARKET LOG (Sunday, 20 minutes)          Week ___
1. Listings added to the Comps sheet this week: ___ (target 3)
2. New contacts: brokers ___ owners ___ buyers/tenants ___ professionals ___
3. Leads in CRM: new ___ ; follow-ups done ___ ; overdue ___
4. One thing I learned about how deals work here: ______________________
5. One rule or rate I checked on an official source (with date): ______
6. Next week's three actions: 1 ______ 2 ______ 3 ______"""

TOOLKIT = [
    ('Comparables sheet with formulas', COMPS_HEADER + '\n\n' + COMPS_FORMULAS, 'RE-M07-L01'),
    ('Full cost of a purchase', COST_CALC, 'RE-M04-L01 and RE-M14-L02'),
    ('Rental yield and return calculator', ROI_CALC, 'RE-M08-L02'),
    ('EMI formulas', EMI, 'RE-M08-L01'),
    ('Due-diligence checklist', DUE_DILIGENCE, 'RE-M06-L03'),
    ('Document checklist by deal type', DOC_CHECKLIST, 'RE-M05-L04'),
    ('Owner mandate template', MANDATE, 'RE-M10-L02'),
    ('Client intake form', INTAKE, 'RE-M13-L01'),
    ('Site-visit checklist', SITE_VISIT, 'RE-M13-L01'),
    ('Listing template', LISTING, 'RE-M12-L02'),
    ('CRM sheet', CRM_HEADER + '\n\n' + CRM_FORMULAS, 'RE-M19-L01'),
    ('Transaction timeline', TIMELINE, 'RE-M14-L01'),
    ('Rental agreement checklist', RENTAL_AGREEMENT, 'RE-M05-L03 and RE-M15-L01'),
    ('NRI property care service menu', NRI_CARE, 'RE-M15-L02'),
    ('Weekly market log', WEEKLY_LOG, 'Week 1 onwards'),
]
