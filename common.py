"""Shared helpers and the resource registry for the personal finance course.

Every link used in the course lives in R, with the status found when it was
checked on VDATE. Lessons refer to links by key, so the sources page is
generated from exactly the links the course uses.
"""

import collections
import hashlib
import random

VDATE = '2026-11-03'
ASOF = 'as of November 2026'
CHECK = 'check current rules'

STATUS = {
    'v': f'verified {VDATE}',
    'vr': f'verified {VDATE}; check current rules',
    'vt': f'verified {VDATE} (headline checked)',
    'u': 'unverified: the site blocks automated checks',
}

G_TAX = 'Income tax and GST'
G_RBI = 'RBI, banking and credit'
G_SEBI = 'SEBI, AMFI and investing'
G_SAVE = 'Small savings, EPF, NPS and pensions'
G_INS = 'Insurance'
G_KERALA = 'Kerala'
G_SCAM = 'Scams, safety and complaints'
G_ESTATE = 'Nominations, documents and wills'
G_LEARN = 'Free courses and books'
G_TOOLS = 'Free tools'
G_LAW = 'Law and family'


def _r(title, url, s='v', group='Other'):
    assert ' ' not in url and ')' not in url and '(' not in url, url
    return {'title': title, 'url': url, 's': s, 'group': group}


R = {
    # ---- Income tax and GST
    'it-act-2025': _r('Income Tax Department: Income-tax Act, 2025 comes into force from 1 April 2026', 'https://www.incometaxindia.gov.in/w/income-tax-act-2025-comes-into-force-from-1st-april-2026', 'v', G_TAX),
    'it-press-2025': _r('CBDT press release: the Income-tax Act, 2025 replaces the 1961 Act (PDF)', 'https://www.incometaxindia.gov.in/documents/d/guest/press-release-income-tax-act-2025-comes-into-force-from-01-april-2026-pdf', 'v', G_TAX),
    'it-s202': _r('Income-tax Act, 2025, section 202: new tax regime rates', 'https://www.incometaxindia.gov.in/w/section-202-78', 'vr', G_TAX),
    'it-s156': _r('Income-tax Act, 2025, section 156: rebate', 'https://www.incometaxindia.gov.in/w/section-156-88', 'vr', G_TAX),
    'it-s19': _r('Income-tax Act, 2025, section 19: deductions from salary', 'https://www.incometaxindia.gov.in/w/section-19-206', 'vr', G_TAX),
    'it-rates': _r('Income Tax Department: tax rates for individuals (old regime, surcharge, cess)', 'https://incometaxindia.gov.in/Documents/Left%20Menu/TAX%20RATES_Indvl.htm', 'vr', G_TAX),
    'sb18-budget26': _r('Storyboard18: no change in tax rates in Budget 2026 (1 February 2026)', 'https://www.storyboard18.com/special-coverage/budget-2026-no-change-in-tax-rates-in-budget-2026-rebate-continues-for-income-up-to-%e2%82%b912-lakh-88610.htm', 'v', G_TAX),
    'it-s196': _r('Income-tax Act, 2025, section 196: short-term gains on equity', 'https://www.incometaxindia.gov.in/w/section-196-78', 'vr', G_TAX),
    'it-s198': _r('Income-tax Act, 2025, section 198: long-term gains on equity', 'https://www.incometaxindia.gov.in/w/section-198-78', 'vr', G_TAX),
    'it-s197': _r('Income-tax Act, 2025, section 197: long-term gains on other assets', 'https://www.incometaxindia.gov.in/w/section-197-78', 'vr', G_TAX),
    'it-cg': _r('Income Tax Department: income from capital gains (holding periods)', 'https://incometaxindia.gov.in/Documents/Left%20Menu/income-from-capital-gains.htm', 'vr', G_TAX),
    'it-s76': _r('Income-tax Act, 2025, section 76: gains on debt-oriented mutual funds', 'https://www.incometaxindia.gov.in/w/section-76-106', 'vr', G_TAX),
    'amfi-tax': _r('AMFI: tax corner (how mutual funds are taxed)', 'https://amfiindia.com/investor-corner/knowledge-center/tax-corner.html', 'vr', G_TAX),
    'om-budget26': _r('Outlook Money: Budget 2026 changes buyback tax and STT on futures and options', 'https://www.outlookmoney.com/invest/union-budget-2026-buyback-proceeds-to-be-taxed-as-capital-gains-stt-raised-on-futures-and-options', 'vr', G_TAX),
    'it-s263': _r('Income-tax Act, 2025, section 263: return of income and due dates', 'https://www.incometaxindia.gov.in/w/section-263-72', 'vr', G_TAX),
    'fb26-notes': _r('Finance Bill 2026: notes on clauses (PDF): due dates, late fee, TDS', 'https://incometaxindia.gov.in/Budgets%20and%20Bills/2026/Notes-on-clauses-2026.pdf', 'vr', G_TAX),
    'etv-itr27': _r('ETV Bharat: over 7 crore returns filed for AY 2026-27 (31 August 2026)', 'https://www.etvbharat.com/en/business/over-7-crore-itrs-filed-for-ay27-deadline-ends-tonight-enn26083106916', 'v', G_TAX),
    'itr1-manual': _r('Income Tax e-filing: ITR-1 (Sahaj) user manual', 'https://www.incometax.gov.in/iec/foportal/newdownloads/itr/itr-UM', 'vr', G_TAX),
    'it-s58': _r('Income-tax Act, 2025, section 58: presumptive taxation for small businesses and professionals', 'https://www.incometaxindia.gov.in/w/section-58-144', 'vr', G_TAX),
    'it-sched15': _r('Income-tax Act, 2025, Schedule XV: what counts for the section 123 (old 80C) deduction', 'https://www.incometaxindia.gov.in/w/schedule-xv-2', 'vr', G_TAX),
    'bs-s123': _r('Business Standard: 80C becomes section 123 in the new law (17 February 2025)', 'https://www.business-standard.com/amp/finance/personal-finance/i-t-bill-2025-deductions-under-80c-moves-to-section-123-see-changes-125021700699_1.html', 'v', G_TAX),
    'it-s126': _r('Income-tax Act, 2025, section 126: health insurance deduction (old 80D)', 'https://www.incometaxindia.gov.in/w/section-126-96', 'vr', G_TAX),
    'it-ins-benefits': _r('Income Tax Department: tax benefits of life and health insurance', 'https://www.incometaxindia.gov.in/w/tax-benefits-due-to-life-insurance-policy-health-insurance-policy-and-expenditure-on-medical-treatment', 'vr', G_TAX),
    'it-vda': _r('Income Tax Department: taxation of virtual digital assets (PDF)', 'https://www.incometaxindia.gov.in/documents/20117/42998/Taxation-of-Virtual-Digital-Asset-VDA_2026-01-06_06-43-57_cfe04a_en.pdf/153706c8-7b5c-77d4-fc56-624c50ece1b0', 'vr', G_TAX),
    'it-ais': _r('Income Tax Department: steps to access your Annual Information Statement (AIS)', 'https://www.incometaxindia.gov.in/w/steps-to-access-ais-information-online', 'v', G_TAX),
    'sansa-advtax': _r('Sansa Legal: advance tax under the Income-tax Act, 2025 (June 2026)', 'https://www.sansalegal.com/post/advance-tax-under-income-tax-act-2025-due-dates-calculation-and-payment-guide', 'vr', G_TAX),
    'it-calc': _r('Income Tax Department: income and tax calculator (compares regimes)', 'https://www.incometax.gov.in/iec/foportal/income-tax-calculator', 'v', G_TAX),
    'gst-56': _r('GST Council: decisions of the 56th meeting (PDF, September 2025)', 'https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau.pdf', 'vr', G_TAX),
    'cbic-reg': _r('CBIC: registration under GST (PDF)', 'https://cbic-gst.gov.in/pdf/press-release/registrtn-gst-regime.pdf', 'vr', G_TAX),
    # ---- RBI, banking and credit
    'rbi-fe': _r('RBI: Financial Education (messages, films, games, downloads)', 'https://rbi.org.in/financialeducation/', 'v', G_RBI),
    'rbi-repo': _r('SCC Online: RBI raises the repo rate to 5.50% (October 2026)', 'https://www.scconline.com/blog/post/2026/10/09/rbi-hikes-repo-rate-to-5-50-percent-october-2026/', 'v', G_RBI),
    'om-target': _r('Outlook Money: the 4% inflation target continues until 2031 (March 2026)', 'https://www.outlookmoney.com/banking/rbi-to-maintain-4-per-cent-inflation-target-until-2031-centre', 'v', G_RBI),
    'dicgc': _r('DICGC: deposit insurance, what is covered (PDF)', 'https://website.dicgc.org.in/sites/default/files/2024-09/DICGC_Flyer_0.pdf', 'vr', G_RBI),
    'rbi-liability': _r('RBI: customer liability in unauthorised electronic transactions', 'https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=11040', 'vr', G_RBI),
    'ml-bsbd': _r('Moneylife: RBI expands free services in basic savings accounts (December 2025)', 'https://moneylife.in/article/rbi-expands-free-services-under-basic-savings-accounts-makes-switching-easier-for-customers/79041.html', 'vr', G_RBI),
    'rbi-cards': _r('RBI: credit and debit card rules, amendment of March 2024', 'https://rbi.org.in/scripts/FS_Notification.aspx?Id=12620', 'vr', G_RBI),
    'rbi-dla': _r('RBI: Digital Lending Directions, 2025 (press release)', 'https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=60403', 'vr', G_RBI),
    'bs-dla': _r('Business Standard: how to check a loan app on RBI\'s list (July 2025)', 'https://www.business-standard.com/amp/finance/personal-finance/avoiding-fraudulent-loan-apps-rbi-listing-ratings-reviews-key-to-safety-125070900931_1.html', 'v', G_RBI),
    'mn-dla': _r('MediaNama: RBI\'s public directory of digital lending apps (May 2025)', 'https://www.medianama.com/2025/05/223-rbi-digital-lending-apps-centralised-directory/', 'v', G_RBI),
    'rbi-ios': _r('Canara Bank: features of the RBI Integrated Ombudsman Scheme, 2026 (PDF)', 'https://www.canarabank.bank.in/documents/d/guest/salient-features-of-the-scheme-2026', 'vr', G_RBI),
    'ml-fortnight': _r('Moneylife: lenders report your credit data every 15 days (from January 2025)', 'https://moneylife.in/article/credit-report-rbi-asks-lenders-to-submit-borrowers-credit-information-every-15-days/74872.html', 'v', G_RBI),
    'ml-cic30': _r('Moneylife: credit bureaus must fix complaints in 30 days or pay ₹100 a day', 'https://www.moneylife.in/article/credit-bureaus-must-resolve-customer-complaint-within-30-days-else-pay-rs100-fine-per-day-rbi/72398.html', 'vr', G_RBI),
    'om-cic-alert': _r('Outlook Money: credit bureaus must alert you when your report is checked (January 2025)', 'https://www.outlookmoney.com/banking/cics-to-alert-customers-via-sms-or-email-on-credit-report-usage-rbi-issues-master-directions', 'v', G_RBI),
    'sc-freereport': _r('StudyCafe: how to get your free annual credit report (September 2026)', 'https://studycafe.in/how-to-get-your-free-annual-credit-report-in-india-426805.html', 'v', G_RBI),
    'rbi-coop': _r('RBI: caution against co-operative societies using the word "bank" (November 2021)', 'https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=52595', 'v', G_RBI),
    'prepay': _r('Angel One: no prepayment charges on floating-rate loans from 1 January 2026', 'https://www.angelone.in/news/personal-finance/rbi-new-rule-no-prepayment-penalty-on-floating-loans-from-jan-1-2026', 'vr', G_RBI),
    'bs-goldltv': _r('Business Standard: gold loan LTV raised to 85% for loans up to ₹2.5 lakh (June 2025)', 'https://www.business-standard.com/finance/news/gold-loan-ltv-raised-to-85-percent-up-to-rs-2-5-lakh-rbi-125060601173_1.html', 'vt', G_RBI),
    'bs-bankin': _r('Business Standard: banks to move to the bank.in domain by 31 October 2025', 'https://www.business-standard.com/amp/finance/news/rbi-asks-banks-to-complete-migration-to-bank-in-domain-by-october-31-2025-125042201515_1.html', 'vt', G_RBI),
    'pmvl': _r('PIB: PM-Vidyalaxmi education loan scheme approved (PDF, November 2024)', 'https://education.gov.in/sites/upload_files/mhrd/files/PIB2071134.pdf', 'vr', G_RBI),
    # ---- SEBI, AMFI and investing
    'sebi-investor': _r('SEBI investor website: guides and fraud warnings', 'https://investor.sebi.gov.in/', 'v', G_SEBI),
    'sebi-ia-list': _r('SEBI: list of registered investment advisers (search by name or number)', 'https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=13', 'v', G_SEBI),
    'sebi-ia-caution': _r('SEBI: deal only with registered investment advisers and research analysts', 'https://www.sebi.gov.in/media/press-releases/jun-2016/sebi-cautions-public-to-deal-with-only-sebi-registered-investment-advisers-and-research-analysts_32627.html', 'v', G_SEBI),
    'ria-fees': _r('Cafemutual: SEBI fee limits for registered investment advisers (January 2025)', 'https://cafemutual.com/news/industry/33937-rias-can-now-charge-fees-up-to-rs-151-lakh-per-family-in-fixed-fees', 'vr', G_SEBI),
    'saarthi': _r('SEBI: Saa₹thi investor education app launched (January 2022)', 'https://www.sebi.gov.in/media/press-releases/jan-2022/sebi-chairman-launches-saa-thi-sebi-s-mobile-app-on-investor-education_55384.html', 'vt', G_SEBI),
    'scores': _r('SEBI investor website: SCORES complaints', 'https://investor.sebi.gov.in/sebi_scores.html', 'vr', G_SEBI),
    'sebi-valid': _r('Moneylife: SEBI\'s @valid UPI handles and SEBI Check (October 2025)', 'https://www.moneylife.in/article/sebi-launches-at-valid-upi-handles-and-checking-tool-to-curb-payment-frauds/78469.html', 'v', G_SEBI),
    'sebi-fno': _r('Moneylife: SEBI study, 91% of individual F&O traders lost money in 2024-25', 'https://moneylife.in/article/91-percentage-of-retail-traders-lost-money-in-derivatives-losses-in-fo-surged-41-percentage-to-rs105-lakh-crore-in-fy2425-sebi-study/77613.html', 'v', G_SEBI),
    'sebi-digigold': _r('Moneylife: SEBI warns against unregulated digital gold (November 2025)', 'https://moneylife.in/article/sebi-warns-against-investing-in-unregulated-digital-gold-and-egold-products/78789.html', 'v', G_SEBI),
    'bt-finfluencer': _r('Business Today: SEBI rules on finfluencers (August 2024)', 'https://www.businesstoday.in/amp/personal-finance/investment/story/sebi-tweaks-regulations-for-finfluencers-removes-content-of-over-15000-unregulated-entities-443789-2024-08-31', 'v', G_SEBI),
    'amfi-direct': _r('AMFI: direct plans explained', 'https://www.amfiindia.com/investor-corner/investor-center/Direct-Plan.html', 'v', G_SEBI),
    'bs-ber': _r('Business Standard: SEBI\'s new expense ratio limits for mutual funds (December 2025)', 'https://www.business-standard.com/amp/markets/news/sebi-revamps-mf-expense-ratio-framework-125121700968_1.html', 'vr', G_SEBI),
    'amfi-risko': _r('AMFI (Mutual Funds Sahi Hai): the six riskometer levels', 'https://www.mutualfundssahihai.com/en/what-riskometer-and-what-are-different-levels', 'v', G_SEBI),
    'sebi-risko': _r('SEBI investor website: riskometer', 'https://investor.sebi.gov.in/riskometer.html', 'v', G_SEBI),
    'amfi-cas': _r('AMFI: consolidated account statement (CAS)', 'https://www.amfiindia.com/investor-corner/investor-center/cas.html', 'v', G_SEBI),
    'amfi-ter': _r('AMFI: what the total expense ratio is, and where it is disclosed', 'https://amfiindia.com/investor-corner/knowledge-center/Expense-Ratio.html', 'v', G_SEBI),
    'elss-lockin': _r('Edelweiss Mutual Fund: the ELSS three-year lock-in, per instalment', 'https://www.edelweissmf.com/investor-insights/mutual-fund-investment-tips-and-articles/elss-lock-in-period', 'v', G_SEBI),
    'gjepc-huid': _r('GJEPC: hallmarked jewellery with a 6-digit HUID made mandatory from 1 April (2023)', 'https://gjepc.org/solitaire/?p=20069', 'vt', G_SEBI),
    'om-biscare': _r('Outlook Money: check gold jewellery purity with the BIS CARE app', 'https://www.outlookmoney.com/invest/bought-gold-jewellery-recently-heres-how-you-can-check-its-purity-using-the-bis-care-app', 'vt', G_SEBI),
    'rbi-sgb': _r('RBI: SGB premature redemption calendar, April to September 2026', 'https://website.rbi.org.in/web/rbi/-/press-releases/sovereign-gold-bond-sgb-scheme-calendar-for-premature-redemption-during-april-2026-september-2026', 'vt', G_SEBI),
    'nse-iap': _r('NSE: free investor awareness programmes and study material', 'https://www.nseindia.com/invest/investors-awareness-programs', 'v', G_SEBI),
    'nism-fe': _r('NISM: financial education and investor education programmes', 'https://www.nism.ac.in/financial-education', 'v', G_SEBI),
    'quint-crypto': _r('The Quint: crypto will never be legal tender, says the Finance Secretary (February 2022)', 'https://thequint.com/news/business/cryptocurrency-like-bitcoin-ethereum-nft-will-not-be-legal-tender-india-says-finance-secretary-tv-somanathan', 'vr', G_SEBI),
    'inc42-crypto': _r('Inc42: India hasn\'t banned cryptocurrency, says the government (July 2019)', 'https://inc42.com/?p=163021', 'vr', G_SEBI),
    'ml-reit': _r('Moneylife: REIT minimum investment cut, trading lot of one unit (August 2021)', 'https://www.moneylife.in/article/sebi-revises-minimum-application-value-trading-lot-for-reits-invits/64785.html', 'vr', G_SEBI),
    'ob-sgb': _r('Outlook Business: no new Sovereign Gold Bond issues (February 2025)', 'https://www.outlookbusiness.com/economy-and-policy/govt-likely-to-discontinue-sovereign-gold-bond-schemes-confirms-finance-ministry', 'v', G_SEBI),
    # ---- Small savings, EPF, NPS and pensions
    'small-rates': _r('Indian Bank: small savings interest rates, October to December 2026', 'https://indianbank.bank.in/departments/interest-rates-for-small-savings-schemes/', 'vr', G_SAVE),
    'fpj-small': _r('Free Press Journal: small savings rates unchanged for October to December 2026', 'https://www.freepressjournal.in/business/small-savings-interest-rates-unchanged-for-oct-dec-ppf-at-71-per-cent-nsc-at-77-pc', 'v', G_SAVE),
    'indiapost': _r('India Post: saving schemes and current interest rates', 'https://indiapost.gov.in/banking-services/saving', 'vr', G_SAVE),
    'om-small': _r('Outlook Money: post office schemes, deposit limits and features (January 2024)', 'https://www.outlookmoney.com/retirement/invest/fd-small-savings/post-office-small-savings-schemes-know-the-interest-rates-and-key-features', 'vr', G_SAVE),
    'ppf-cbi': _r('Central Bank of India: PPF rules', 'https://centralbank.bank.in/en/node/223409', 'vr', G_SAVE),
    'bt-epf': _r('Business Today: EPF interest of 8.25% for 2025-26 (July 2026)', 'https://www.businesstoday.in/personal-finance/story/your-epf-balance-is-about-to-rise-epfo-orders-8-25-interest-credit-541245-2026-07-06', 'v', G_SAVE),
    'epf-withdraw': _r('Onmanorama: EPFO allows up to 100% partial withdrawal (October 2025)', 'https://www.onmanorama.com/news/business/2025/10/14/epfo-partial-withdrawal-rules-change.html', 'vr', G_SAVE),
    'sbi-nps': _r('SBI: National Pension System (NPS)', 'https://sbi.bank.in/web/personal-banking/investments-deposits/govt-schemes/nps', 'vr', G_SAVE),
    'bs-nps-exit': _r('Business Standard: new NPS exit and withdrawal rules (December 2025)', 'https://www.business-standard.com/finance/personal-finance/pfrda-allows-financial-assistance-against-nps-corpus-under-exit-rule-tweaks-125121601190_1.html', 'vr', G_SAVE),
    'protean-nps': _r('Protean (NPS record-keeper): NPS withdrawal changes and tax', 'https://proteantech.in/articles/nps-withdrawal-rules-2025-changes-december/', 'vr', G_SAVE),
    'apy-faq': _r('PFRDA: Atal Pension Yojana FAQs', 'https://pfrda.org.in/web/pfrda/w/faqs/atal-pension-yojana', 'vr', G_SAVE),
    # ---- Insurance
    'om-cashless': _r('Outlook Money: IRDAI health insurance rules, cashless decision in one hour (May 2024)', 'https://www.outlookmoney.com/retirement/news/health-insurers-to-decide-on-cashless-authorisation-within-one-hour-of-claim-request-irdai', 'v', G_INS),
    'bu-health': _r('BasuNivesh: IRDAI health insurance changes, 2024 (waiting periods, moratorium)', 'https://www.basunivesh.com/irdas-new-health-insurance-changes-2024/', 'vr', G_INS),
    'ins-ombudsman': _r('Council for Insurance Ombudsmen', 'https://www.cioins.co.in/', 'v', G_INS),
    'bima-bharosa': _r('IRDAI Bima Bharosa: register and track an insurance complaint', 'https://bimabharosa.irdai.gov.in/', 'v', G_INS),
    'pmjjby': _r('ICICI Bank: PMJJBY and PMSBY government insurance schemes', 'https://www.icici.bank.in/personal-banking/insurance/government-schemes/pm-service-my-plan', 'vr', G_INS),
    'tg-motor': _r('TaxGuru: motor insurance rules in India, third-party cover (September 2026)', 'https://taxguru.in/finance/irdai-rules-regulations-car-insurance-india.html', 'vr', G_INS),
    'om-seniors': _r('Onmanorama: health cover options for Kerala\'s senior citizens (November 2025)', 'https://www.onmanorama.com/lifestyle/health/2025/11/13/kerala-senior-citizens-health-insurance-options.amp.html', 'v', G_INS),
    # ---- Kerala
    'kl-da': _r('Onmanorama: Kerala raises DA and DR to 37% (October 2026)', 'https://www.onmanorama.com/news/kerala/2026/10/17/kerala-hikes-da-dr-by-2-revised-rates-effective-with-november-payments.html', 'v', G_KERALA),
    'kl-aps': _r('Onmanorama: Assured Pension Scheme sanctioned in principle (March 2026)', 'https://www.onmanorama.com/news/kerala/2026/03/01/assured-pension-scheme-kerala-government.html', 'v', G_KERALA),
    'kl-pension': _r('Onmanorama: Kerala employees still waiting on pension reform (August 2026)', 'https://www.onmanorama.com/news/kerala/2026/08/17/kerala-govt-employees-left-waiting-pension-remains-stuck-between-promises.html', 'v', G_KERALA),
    'kl-fin': _r('Kerala Finance Department: government orders and circulars (DA, pay, Medisep link)', 'https://finance.kerala.gov.in/', 'v', G_KERALA),
    'ml-cps': _r('Moneylife: Kerala introduces the contributory pension scheme for employees joining from 1 April 2013', 'https://moneylife.in/article/introduction-of-contributory-pension-scheme-in-kerala/30913.html', 'v', G_KERALA),
    'medisep2': _r('Onmanorama: Medisep phase 2 from 1 February 2026', 'https://www.onmanorama.com/news/kerala/2026/01/21/medisep-kerala-phase-2-rollout-february1.html', 'v', G_KERALA),
    'ag-gpf': _r('Accountant General (A&E) Kerala: about GPF', 'https://cag.gov.in/ae/kerala/en/page-ae-kerala-about-gpf', 'vr', G_KERALA),
    'gpais': _r('CUSAT: circular on the Group Personal Accident Insurance Scheme (PDF)', 'https://finance.cusat.ac.in/uploads/CIRC_279_CUSAT_NPS.N3_GPAIS_2024-2025.pdf', 'vt', G_KERALA),
    'ksfe-chitty': _r('KSFE: chitty', 'https://ksfe.com/chitty', 'vr', G_KERALA),
    'kl-dgf': _r('TeamLease RegTech: Kerala Co-operative Deposit Guarantee (Amendment) Scheme, 2026', 'https://www.teamleaseregtech.com/updates/article/51730/kerala-co-operative-deposit-guarantee-amendment-scheme-2026', 'vr', G_KERALA),
    'ic-dgf': _r('Indian Cooperative: Kerala raises the co-op deposit guarantee to ₹10 lakh (January 2026)', 'https://www.indiancooperative.com/co-op-news-snippets/kerala-hikes-deposit-guarantee-for-co-op-members/', 'vr', G_KERALA),
    'kl-ptax': _r('Kerala LSGD: profession tax FAQs', 'https://professiontax.lsgkerala.gov.in/faq.php', 'vr', G_KERALA),
    'krera': _r('Kerala Real Estate Regulatory Authority (K-RERA)', 'https://rera.kerala.gov.in/', 'v', G_KERALA),
    'om-highrich': _r('Onmanorama: Highrich scam victims in Kasaragod wait for justice (December 2024)', 'https://onmanorama.com/news/kerala/2024/12/20/high-rich-scam-kasaragod-victims-wait-for-justice.html', 'vt', G_KERALA),
    'om-popular': _r('Onmanorama: High Court on the ₹2,000 crore Popular Finance scam (November 2025)', 'https://www.onmanorama.com/news/kerala/2025/11/12/kerala-high-court-popular-finance-scam.amp.html', 'vt', G_KERALA),
    # ---- Scams, safety and complaints
    'kp-1930': _r('Kerala Police: 1930, the national cyber crime helpline', 'https://ps.keralapolice.gov.in/ernakulamruralcyber-ps/notifications/National-Cyber-Crime-Reporting-Helpline-No-1930-3338', 'v', G_SCAM),
    'cybercrime': _r('National Cyber Crime Reporting Portal', 'https://cybercrime.gov.in/', 'u', G_SCAM),
    'etv-arrest': _r('ETV Bharat: I4C says CBI, ED and police don\'t arrest people on video calls (October 2024)', 'https://www.etvbharat.com/en/!bharat/cbi-ed-police-dont-arrest-people-through-video-calls-indian-cyber-crime-coordination-centre-enn24100602996', 'v', G_SCAM),
    'chakshu': _r('Factly: Chakshu, to report fraud calls, SMS and WhatsApp messages', 'https://factly.in/explainer-government-launches-chakshu-to-report-sms-call-or-whatsapp-messages-attempting-to-commit-fraud/amp', 'v', G_SCAM),
    'ml-mlm': _r('Moneylife: pyramid and money-circulation schemes banned under consumer rules (December 2021)', 'https://moneylife.in/article/indian-govt-bans-pyramid-or-mlm-schemes-under-new-consumer-protection-rules/65986.html', 'v', G_SCAM),
    'ml-buds': _r('Moneylife: rules notified under the Banning of Unregulated Deposit Schemes (BUDS) Act', 'https://www.moneylife.in/article/govt-notifies-rules-for-banning-ponzi-schemes-unregulated-deposits-under-buds-act/59448.html', 'vt', G_SCAM),
    'sachet': _r('RBI Sachet: complain about illegal deposit schemes, check registered entities', 'https://sachet.rbi.org.in/', 'v', G_SCAM),
    # ---- Nominations, documents and wills
    'pib-nominee': _r('PIB: up to four nominees for bank accounts from 1 November 2025', 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2181734', 'vr', G_ESTATE),
    'iibf-nominee': _r('IIBF: nomination under the Banking Laws (Amendment) Act, 2025 (PDF)', 'https://iibf.org.in/documents/Brochure/2025/Nomination_Under_Banking_Laws_AmendmentAct_2025.pdf', 'vr', G_ESTATE),
    'sebi-nominee': _r('SEBI circular on nominations for demat and mutual funds, 29 May 2026 (PDF, via NSDL)', 'https://nsdl.com/nsdl/2026-08/32%20SEBI%20Circular%20dated%2029%20May%202026.pdf', 'vr', G_ESTATE),
    'udgam': _r('RBI: UDGAM FAQs (find unclaimed deposits)', 'https://rbi.org.in/scripts/FS_FAQs.aspx?Id=166', 'v', G_ESTATE),
    'digilocker': _r('DigiLocker', 'https://www.digilocker.gov.in/', 'v', G_ESTATE),
    'will-guide': _r('iPleaders: how to make and register a will in India', 'https://blog.ipleaders.in/register-will-india/', 'v', G_ESTATE),
    'dowry-act': _r('Ministry of Women and Child Development: the Dowry Prohibition Act, 1961', 'https://wcd.nic.in/dowry-prohibition-act-1961-28-1961', 'v', G_LAW),
    # ---- Free courses and books
    'ncfe': _r('NCFE: free basic financial education course (e-LMS, about 5 hours)', 'https://ncfe.org.in/?p=430', 'v', G_LEARN),
    'varsity': _r('Zerodha Varsity: all modules', 'https://zerodha.com/varsity/modules/', 'v', G_LEARN),
    'openstax': _r('OpenStax Principles of Finance on LibreTexts (CC BY 4.0)', 'https://biz.libretexts.org/Bookshelves/Finance/Principles_of_Finance_%28OpenStax%29', 'v', G_LEARN),
    # ---- Free tools
    'libreoffice': _r('LibreOffice (free office suite with Calc)', 'https://www.libreoffice.org/', 'v', G_TOOLS),
    'lo-separators': _r('LibreOffice Help: formula options and separators', 'https://help.libreoffice.org/latest/en-US/text/shared/optionen/01060900.html', 'v', G_TOOLS),
    'gs-pmt': _r('Google Docs Editors Help: PMT function', 'https://support.google.com/docs/answer/3093185', 'v', G_TOOLS),
    'gnucash': _r('GnuCash, free accounting software', 'https://gnucash.org/', 'v', G_TOOLS),
}

USED = []


def use(key):
    if key not in R:
        raise KeyError(f'unknown resource {key}')
    if key not in USED:
        USED.append(key)
    return R[key]


def link(key, text=None):
    r = use(key)
    return f"[{text or r['title']}]({r['url']})"


def rules(key, text=None):
    """A link to an official source, marked check current rules."""
    return f"{link(key, text)} ({CHECK})"


def res_table(rows):
    out = ['| Resource | What to study | Time | Status |', '| --- | --- | --- | --- |']
    for key, what, time in rows:
        r = use(key)
        for cell in (what, time):
            assert '|' not in cell, cell
        out.append(f"| [{r['title']}]({r['url']}) | {what} | {time} | {STATUS[r['s']]} |")
    return '\n'.join(out)


def table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '| ' + ' | '.join('---' for _ in header) + ' |']
    for row in rows:
        assert len(row) == len(header), row
        for c in row:
            assert '|' not in c, c
        out.append('| ' + ' | '.join(row) + ' |')
    return '\n'.join(out)


def numbered(items):
    return '\n'.join(f'{i}. {t}' for i, t in enumerate(items, 1))


def bullets(items):
    return '\n'.join(f'- {t}' for t in items)


def mistakes_list(items):
    return '\n'.join(f'- **{m}** {fix}' for m, fix in items)


def fence(text, lang=''):
    text = text.strip('\n')
    assert '```' not in text
    return f'```{lang}\n{text}\n```'


def inr(n):
    """Indian digit grouping: 1234567 -> '12,34,567'."""
    n = round(n)
    neg = n < 0
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ','.join(parts + [tail])
    return ('-' if neg else '') + '₹' + s


QUIZ_LETTERS = collections.Counter()


def quiz_blocks(quiz):
    """Render questions and answers. Options are shuffled with a seed taken
    from the question text, so the order is stable between builds but the
    correct letter isn't always the same one."""
    qs, ans = [], []
    for i, q in enumerate(quiz, 1):
        assert q['a'] in 'ABCD'[: len(q['o'])], q
        rng = random.Random(int(hashlib.md5(q['q'].encode('utf-8')).hexdigest(), 16))
        order = list(range(len(q['o'])))
        rng.shuffle(order)
        options = [q['o'][k] for k in order]
        letter = 'ABCD'[order.index('ABCD'.index(q['a']))]
        QUIZ_LETTERS[letter] += 1
        opts = '\n'.join(f'    - {chr(65 + j)}) {o}' for j, o in enumerate(options))
        qs.append(f"{i}. {q['q']}\n{opts}")
        ans.append(f"{i}. **{letter}.** {q['why']}")
    return '\n'.join(qs), '\n'.join(ans)


CAPSTONE = 17


def fmt_hours(h):
    if h == int(h):
        return f'{int(h)} hour' + ('' if h == 1 else 's')
    whole = int(h)
    mins = round((h - whole) * 60)
    if whole == 0:
        return f'{mins} minutes'
    return f'{whole} hour' + ('' if whole == 1 else 's') + f' {mins} minutes'


def lesson(m, l, *, title, weeks, hours, outcome, split, core, example, resources,
           steps, proof, templates, mistakes, quiz, study, action, fulltime=None):
    code = f'FIN-M{m:02d}-L{l:02d}'
    sid = code.lower()
    a, b = weeks
    q_text, a_text = quiz_blocks(quiz)
    assert 3 <= len(quiz) <= 5, code
    assert templates, f'{code} needs at least one template'
    assert len(mistakes) >= 3, f'{code} needs common mistakes'
    parts = [
        '## Core lesson',
        core.strip(),
        '## Local example',
        example.strip(),
        '## Free resources',
        res_table(resources),
        '## Action task (on your own money)',
        numbered(steps),
        f'**Proof to record:** {proof}',
    ]
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    for t_title, t_body, t_lang in templates:
        parts += [f'## Template: {t_title}', fence(t_body, t_lang)]
    parts += [
        '## Common mistakes',
        mistakes_list(mistakes),
        '## Quiz',
        'Answer without looking back. The answers are at the bottom of this page.',
        q_text,
        '## Progress checklist',
        'Tick these under **Your tasks** at the top of this page:',
        bullets([
            f'**Study:** {study}',
            f'**Action:** {action}. It is done when your proof is saved: {proof[0].lower() + proof[1:]}',
            f'**Quiz:** at least {len(quiz) - 1} right, or re-read the core lesson and try again.',
        ]),
        '## Answers',
        a_text,
    ]
    content = '\n\n'.join(parts)
    return {
        'id': sid,
        'title': f'{code}: {title}',
        'kind': 'capstone' if m == CAPSTONE else 'level',
        'weeks': [a, b],
        'hours': hours,
        'summary': f'**Outcome:** {outcome} **Time:** about {fmt_hours(hours)} ({split}).',
        'content': content,
        'tasks': [
            {'id': f'{sid}-study', 'text': f'Study: {study}', 'kind': 'task', 'week': a},
            {'id': f'{sid}-action', 'text': f'Action: {action}', 'kind': 'project', 'week': b,
             'detail': f'**Proof to record:** {proof} Save it in your Money Folder and paste its link (or a short note of where it is) in this task\'s note. Never paste account numbers, passwords or OTPs anywhere.'},
            {'id': f'{sid}-quiz', 'text': f'Quiz: at least {len(quiz) - 1} right', 'kind': 'task', 'week': b},
        ],
    }


def module(m, *, title, weeks, hours, overview, outcomes, lessons, project, project_steps,
           project_proof, rubric, short, flashcards, mistakes, fulltime=None, project_week=None):
    sid = f'fin-m{m:02d}'
    a, b = weeks
    pw = project_week or b
    assert a <= pw <= b
    lesson_lines = [f"{s['title']} (about {fmt_hours(s['hours'])})" for s in lessons]
    rub = ['| Criterion | 1: Not yet | 2: Getting there | 3: Ready |', '| --- | --- | --- | --- |']
    for row in rubric:
        assert len(row) == 4 and all('|' not in c for c in row)
        rub.append('| ' + ' | '.join(row) + ' |')
    assert 5 <= len(flashcards) <= 10, f'module {m}: 5-10 flashcards'
    cards = ['| Front (say the answer aloud) | Back |', '| --- | --- |']
    for front, back in flashcards:
        assert '|' not in front and '|' not in back
        cards.append(f'| {front} | {back} |')
    lesson_hours = sum(s['hours'] for s in lessons)
    assert hours > lesson_hours, f'module {m}: hours must include the project'
    paras = overview.strip().split('\n\n')
    assert len(paras) >= 2, 'the first paragraph becomes the summary; the rest is the overview'
    when = f'weeks {a}–{b}' if a != b else f'week {a}'
    parts = [
        '## Overview',
        '\n\n'.join(paras[1:]),
        '## Outcomes',
        'By the end of this module you can:',
        bullets(outcomes),
        '## Time',
        f'About {fmt_hours(hours)} in total: {fmt_hours(lesson_hours)} of lessons and {fmt_hours(hours - lesson_hours)} for the module project. Part-time: {when}' + (f', with the module project due in week {pw}.' if pw != b else '.'),
    ]
    if fulltime:
        parts.append(f'**Full-time track:** {fulltime.strip()}')
    parts += [
        '## Lessons',
        numbered(lesson_lines),
        f'## Module project: {project}',
        numbered(project_steps),
        f'**Proof to record:** {project_proof}',
        '## Self-assessment rubric',
        'Score yourself honestly after the project. Move on when no row is a 1 and at least half the rows are 3. If a row is a 1, redo that part first.',
        '\n'.join(rub),
        '## Short on time?',
        'The minimum version, when PSC prep or work leaves little time:',
        bullets(short),
        '## Revision flashcards',
        'Cover the right-hand column, read the front, say the answer, then check. Repeat the ones you missed the next day.',
        '\n'.join(cards),
        '## Top mistakes in this module',
        mistakes_list(mistakes),
    ]
    return {
        'id': sid,
        'title': f'Module {m}: {title}',
        'kind': 'capstone' if m == CAPSTONE else 'level',
        'weeks': [a, b],
        'hours': hours,
        'summary': paras[0],
        'content': '\n\n'.join(parts),
        'tasks': [
            {'id': f'{sid}-project', 'text': f'Module project: {project}', 'kind': 'project', 'week': pw,
             'detail': f'**Proof to record:** {project_proof}'},
            {'id': f'{sid}-rubric', 'text': 'Self-assessment: rubric scored, no row at 1', 'kind': 'exit', 'week': pw},
        ],
    }
