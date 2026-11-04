"""The plan for the Kerala Real Estate Business course: modules, lessons and
part-time hours. Weeks are assigned greedily so each week stays near the
target load."""

PARTS = [
    ('A', 'Understand the business', 1, 2),
    ('B', 'Knowledge base', 3, 9),
    ('C', 'Run the business', 10, 22),
]

MODULES = [
    # ---- Part A
    ('How real estate works in Kerala', [
        ('Property types and the people in a deal', 1.0),
        ('Market cycles and what drives demand in Kerala', 1.0)], 0.75),
    ('Business paths and choosing yours', [
        ('Low-capital paths: brokerage, rentals, NRI property care, marketing', 1.0),
        ('Capital-heavy paths: plotting, buy-and-hold, flipping', 1.0)], 0.75),
    # ---- Part B
    ('Land measurement and records in Kerala', [
        ('Cents, ares and square feet: measuring land and buildings', 1.0),
        ('Survey numbers, thandaper and village office certificates', 1.25),
        ('Online land-record portals', 1.0)], 1.0),
    ('The legal framework', [
        ('Transfer of Property Act, Registration Act and stamp duty', 1.25),
        ('RERA and K-RERA', 1.0),
        ('Paddy land, wetland and land reforms law', 1.25),
        ('Building rules, CRZ and ecologically sensitive areas', 1.25),
        ('Rent control, benami property and cash limits', 1.0)], 1.0),
    ('Property documents', [
        ('Agreement for sale and sale deed', 1.25),
        ('Gift, partition and settlement deeds, and powers of attorney', 1.0),
        ('Rental and lease agreements', 1.0),
        ('Building permits, occupancy certificates, tax receipts and NOCs', 1.0)], 1.0),
    ('Due diligence and title verification', [
        ('Tracing the title chain and reading the EC', 1.25),
        ('Physical verification: boundaries, access, flood and zoning', 1.25),
        ('Running the full checklist, and when to call an advocate or surveyor', 1.0)], 1.5),
    ('Valuation', [
        ('Fair value, market value and comparables', 1.25),
        ('Income and cost methods, and what raises or lowers value', 1.0),
        ('Your local market study', 1.5)], 1.0),
    ('Real estate finance', [
        ('Home loans, loans against property, eligibility and EMIs', 1.25),
        ('Rental yield, cap rate, cash-on-cash, IRR and the total cost of owning', 1.5)], 1.0),
    ('Property taxes', [
        ('Taxes when buying and selling: TDS, capital gains and exemptions', 1.25),
        ('Tax on rent and brokerage, and GST', 1.0)], 0.75),
    # ---- Part C
    ('Becoming a registered agent', [
        ('K-RERA agent registration and the rules agents must follow', 1.0),
        ('Owner mandates, commission and building an inventory', 1.25)], 1.0),
    ('Sourcing properties and buyers', [
        ('Local and NRI networks, and learning from local brokers', 1.25),
        ('Builders, online sources and lead quality', 1.0)], 1.0),
    ('Marketing properties', [
        ('Phone photography, video and virtual tours', 1.0),
        ('Honest listing copy and free portals', 1.0),
        ('Social media, WhatsApp and Google Business Profile', 1.0)], 1.25),
    ('Sales and negotiation', [
        ('Understanding clients and running site visits', 1.0),
        ('Objections, negotiation, closing and token advances', 1.25)], 1.0),
    ('Managing a transaction step by step', [
        ('From token advance to agreement and due diligence', 1.0),
        ('Loans, stamp duty and registration at the sub-registrar office', 1.25),
        ('Mutation, handover and working with professionals', 1.0)], 1.0),
    ('Rentals and property management', [
        ('Tenant screening, agreements and verification', 1.25),
        ('Rent collection, maintenance and NRI property care as a service', 1.0)], 1.0),
    ('Plotting and development basics', [
        ('Layouts, land conversion, roads and utilities, and why development is risky', 1.25)], 0.75),
    ('Construction basics', [
        ('Costs, contracts, quality checks and the building permit process', 1.25)], 0.75),
    ('Investing strategies', [
        ('Buy-and-hold rentals, land banking and flipping', 1.0),
        ('REITs and other low-capital options, and the real risks', 1.0)], 0.75),
    ('Tech and AI in real estate', [
        ('A CRM in Google Sheets', 1.0),
        ('Maps, GIS and AI tools', 1.0)], 0.75),
    ('Setting up your business', [
        ('Structure, registration, GST and bookkeeping', 1.0),
        ('Pricing your services, partnerships and growing an agency', 1.0)], 1.0),
    ('Fraud, risk and ethics', [
        ('Common real estate frauds in Kerala and how to catch them', 1.25),
        ('Ethics, conflicts of interest and protecting clients', 1.0)], 0.75),
    ('Capstone: your first deal or your business plan', [
        ('Choose your capstone and plan it', 1.25),
        ('Run the capstone', 20.0),
        ('Final retest, your toolkit and the next 12 months', 1.5)], 1.0),
]

CAPSTONE = 22
TARGET = 5.5
REVIEW_H = 1 / 3        # weekly market log and review, about 20 minutes


def part_of(m):
    for p in PARTS:
        if p[2] <= m <= p[3]:
            return p
    raise ValueError(m)


def assign():
    load = {0: 2.5}
    weeks, pweek = {}, {}
    w = 1

    def fits(week, h):
        return load.get(week, REVIEW_H) + h <= TARGET + 0.4

    def put(week, h):
        if week not in load:
            load[week] = REVIEW_H
        load[week] += h

    for m, (title, lessons, ph) in enumerate(MODULES, 1):
        if any(p[2] == m for p in PARTS) and m > 1 and load.get(w, 0) > 3:
            w += 1
        for l, (lt, h) in enumerate(lessons, 1):
            if m == CAPSTONE and l == 2:
                a = w + 1 if load.get(w, 0) > 2 else w
                for k in range(a, a + 5):
                    put(k, h / 5)
                weeks[(m, l)] = (a, a + 4)
                w = a + 4
                continue
            if not fits(w, h):
                w += 1
            put(w, h)
            weeks[(m, l)] = (w, w)
        if not fits(w, ph):
            w += 1
        put(w, ph)
        pweek[m] = w
    if load.get(w, 0) > TARGET - 1.5:
        w += 1
    put(w, 1.5)
    return weeks, pweek, w, load


if __name__ == '__main__':
    weeks, pweek, last, load = assign()
    for m, (title, lessons, ph) in enumerate(MODULES, 1):
        ws = [weeks[(m, l)] for l in range(1, len(lessons) + 1)]
        print(f'M{m:02d} {title}: weeks {ws[0][0]}-{max(b for a, b in ws)} (project {pweek[m]})')
    print('lessons', sum(len(x[1]) for x in MODULES), 'last week', last)
    print(' '.join(f'{k}:{v:.1f}' for k, v in sorted(load.items())))
    print('total', round(sum(load.values()), 1))
