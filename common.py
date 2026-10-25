"""Shared helpers and the resource registry for the social media marketing course.

Every link used in the course lives in R, with the status found when it was
checked on VDATE. Lessons refer to links by key, so the sources page is
generated from exactly the links the course uses.
"""

import collections
import hashlib
import random

VDATE = '2026-10-25'
ASOF = 'as of October 2026'

STATUS = {
    'v': f'verified {VDATE}',
    'vt': f'verified {VDATE} (page title checked)',
    'vr': f'verified {VDATE}; check current rules',
    'u': 'unverified: the site blocks automated checks',
}

G_YT = 'YouTube and Google help'
G_META = 'Meta: Instagram, Facebook, WhatsApp and Threads'
G_OTHER = 'Other platforms'
G_NEWS = 'News reports on platform changes'
G_COURSES = 'Free courses and guides'
G_APPS = 'Free apps for your phone'
G_OSS = 'Free and open-source software for the laptop'
G_FONTS = 'Malayalam fonts and typing'
G_AI = 'AI tools'
G_INDIA = 'India: rules and law'
G_SAFETY = 'Help and safety'
G_MONEY = 'Earning programmes'


def _r(title, url, s='v', group='Other'):
    return {'title': title, 'url': url, 's': s, 'group': group}


R = {
    # ---- YouTube and Google
    'yt-recs': _r('YouTube Help: How YouTube recommendations work', 'https://support.google.com/youtube/answer/16089387', 'v', G_YT),
    'yt-search': _r('YouTube Help: How YouTube search works', 'https://support.google.com/youtube/answer/16090438', 'v', G_YT),
    'yt-shorts3': _r('YouTube Help: Understand three-minute YouTube Shorts', 'https://support.google.com/youtube/answer/15424877', 'v', G_YT),
    'yt-ypp': _r('YouTube Help: Overview of the expanded YouTube Partner Program', 'https://support.google.com/youtube/answer/13429240', 'vr', G_YT),
    'yt-thumbs': _r('YouTube Help: Add custom thumbnails', 'https://support.google.com/youtube/answer/72431', 'v', G_YT),
    'yt-abtest': _r('YouTube Help: A/B test titles and thumbnails', 'https://support.google.com/youtube/answer/16391400', 'v', G_YT),
    'yt-ai': _r('YouTube Help: Disclosing use of altered or synthetic content', 'https://support.google.com/youtube/answer/14328491', 'vr', G_YT),
    'yt-hashtags': _r('YouTube Help: Find playlists and videos using hashtags (hashtag rules)', 'https://support.google.com/youtube/answer/6390658', 'v', G_YT),
    'yt-chapters': _r('YouTube Help: Video chapters', 'https://support.google.com/youtube/answer/9884579', 'v', G_YT),
    'yt-captions': _r('YouTube Help: Add subtitles and captions', 'https://support.google.com/youtube/answer/2734796', 'v', G_YT),
    'yt-audio': _r('YouTube Help: Use music and sound effects from the Audio Library', 'https://support.google.com/youtube/answer/3376882', 'v', G_YT),
    'yt-dispute': _r('YouTube Help: Dispute a Content ID claim (claims and strikes)', 'https://support.google.com/youtube/answer/2797454', 'v', G_YT),
    'yt-impressions': _r('YouTube Help: Check your impressions and watch time', 'https://support.google.com/youtube/answer/7577430', 'v', G_YT),
    'yt-retention': _r('YouTube Help: Measure key moments for audience retention', 'https://support.google.com/youtube/answer/9314415', 'v', G_YT),
    'yt-monetisation': _r('YouTube Help: Channel monetization policies (inauthentic and reused content)', 'https://support.google.com/youtube/answer/1311392', 'vr', G_YT),
    'yt-fake': _r('YouTube Help: Fake engagement policy', 'https://support.google.com/youtube/answer/3399767', 'v', G_YT),
    'yt-moderation': _r('YouTube Help: Manage your channel\'s moderation settings', 'https://support.google.com/youtube/answer/16622701', 'v', G_YT),
    'yt-harassment': _r('YouTube Help: Harassment and cyberbullying policies', 'https://support.google.com/youtube/answer/2802268', 'v', G_YT),
    'yt-burnout': _r('YouTube Help: Tips for dealing with creator burnout', 'https://support.google.com/youtube/answer/13616108', 'v', G_YT),
    'yt-wellbeing': _r('YouTube Help: Well-being tips for creators', 'https://support.google.com/youtube/answer/12930055', 'v', G_YT),
    'g-2sv': _r('Google Account Help: Turn on 2-Step Verification', 'https://support.google.com/accounts/answer/185839', 'v', G_SAFETY),
    'ga4-setup': _r('Analytics Help: Set up Analytics for a website and/or app', 'https://support.google.com/analytics/answer/9304153', 'v', G_YT),
    'ga4-utm': _r('Analytics Help: URL builders (collect campaign data with UTM links)', 'https://support.google.com/analytics/answer/10917952', 'v', G_YT),
    'ga-builder': _r('Google Analytics demos and tools: Campaign URL Builder', 'https://ga-dev-tools.web.app/ga4/campaign-url-builder/', 'v', G_YT),
    'sites-ga': _r('Sites Help: Use Analytics with your site', 'https://support.google.com/sites/answer/97459', 'v', G_YT),
    'gads-formats': _r('Google Ads Help: About video ad formats', 'https://support.google.com/google-ads/answer/2375464', 'v', G_YT),
    'gads-tax': _r('Google Ads Help: Taxes in your country (India: GST)', 'https://support.google.com/google-ads/answer/2375370', 'vr', G_YT),
    'gtrends-start': _r('Trends Help: Get started with Google Trends', 'https://support.google.com/trends/answer/6248105', 'v', G_YT),
    'gtrends-faq': _r('Trends Help: FAQ about Google Trends data', 'https://support.google.com/trends/answer/4365533', 'v', G_YT),
    'gbp-start': _r('Business Profile Help: Get started with Google Business Profile', 'https://support.google.com/business/answer/7039811', 'v', G_YT),
    'gbp-rank': _r('Business Profile Help: Tips to improve your local ranking', 'https://support.google.com/business/answer/7091', 'v', G_YT),
    'gbp-reviews': _r('Business Profile Help: Tips to get more reviews', 'https://support.google.com/business/answer/3474122', 'v', G_YT),
    'maps-fake': _r('Maps content policy: Fake engagement', 'https://support.google.com/contributionpolicy/answer/11414422', 'v', G_YT),
    'maps-incent': _r('Maps content policy: Incentivized or biased reviews', 'https://support.google.com/contributionpolicy/answer/16597558', 'v', G_YT),
    # ---- Meta: Instagram, Facebook, WhatsApp, Threads
    'meta-ai-ranking': _r('Meta AI blog: How AI powers experiences on Facebook and Instagram', 'https://ai.meta.com/blog/how-ai-powers-experiences-facebook-instagram-system-cards/', 'v', G_META),
    'meta-ranking-tc': _r('Meta Transparency Center: Our approach to explaining ranking (system cards)', 'https://transparency.meta.com/features/explaining-ranking', 'vt', G_META),
    'meta-demote': _r('Meta Transparency Center: Types of content we demote', 'https://transparency.meta.com/features/approach-to-ranking/types-of-content-we-demote/', 'vt', G_META),
    'meta-inauthentic': _r('Meta Community Standards: Inauthentic behavior', 'https://transparency.meta.com/policies/community-standards/inauthentic-behavior/', 'vt', G_META),
    'meta-ad-library': _r('Meta Transparency Center: Meta Ad Library tools', 'https://transparency.meta.com/researchtools/ad-library-tools/', 'vt', G_META),
    'meta-ai-labels': _r('Meta: Our approach to labeling AI-generated content', 'https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/', 'vr', G_META),
    'ig-reco': _r('Instagram for Creators: What creators need to know about recommendations', 'https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators', 'v', G_META),
    'ig-reels-2025': _r('Instagram for Creators: Finding success on reels in 2025', 'https://creators.instagram.com/blog/the-latest-with-instagram', 'v', G_META),
    'ig-small': _r('Instagram for Creators: Helping creators of all sizes break through', 'https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through', 'v', G_META),
    'ig-best': _r('Instagram for Creators: Best practices hub', 'https://creators.instagram.com/best-practices', 'v', G_META),
    'ig-status': _r('Instagram: Account Status for professional accounts (announcement)', 'https://about.instagram.com/blog/announcements/instagram-outages-and-account-status', 'v', G_META),
    'ig-status-help': _r('Instagram Help: Account Status', 'https://help.instagram.com/539126347315373', 'vt', G_META),
    'ig-pro': _r('Instagram Help: Set up a professional account', 'https://help.instagram.com/502981923235522', 'vt', G_META),
    'ig-pro-types': _r('Instagram Help: About business and creator accounts', 'https://help.instagram.com/iphone-app/138925576505882', 'vt', G_META),
    'ig-music': _r('Instagram Help: Access to the licensed music library', 'https://help.instagram.com/ipad-app/402084904469945', 'vt', G_META),
    'ig-fakeapps': _r('Instagram Help: Avoid apps that offer likes and followers', 'https://help.instagram.com/263751177667145/', 'vt', G_META),
    'ig-inauthentic': _r('Instagram: Removing fake likes, follows and comments', 'https://about.instagram.com/blog/announcements/reducing-inauthentic-activity-on-instagram', 'v', G_META),
    'ig-abuse': _r('Instagram: New ways to protect our community from abuse (Limits, Hidden Words)', 'https://about.instagram.com/blog/announcements/introducing-new-ways-to-protect-our-community-from-abuse', 'v', G_META),
    'ig-sleep': _r('Meta: Instagram Sleep mode (formerly Quiet mode)', 'https://about.fb.com/news/2023/01/instagram-quiet-mode-manage-your-time-and-focus/', 'v', G_META),
    'wa-tools': _r('WhatsApp Business: the built-in business tools', 'https://whatsappbusiness.com/resources/resource-library/small-business-use-whatsapp-business-app/', 'v', G_META),
    'wa-broadcasts': _r('WhatsApp Business: business broadcasts', 'https://whatsappbusiness.com/resources/resource-library/business-broadcasts-whatsapp/', 'vr', G_META),
    'wa-channels': _r('WhatsApp Help: About creating a WhatsApp Channel', 'https://faq.whatsapp.com/265055289421317', 'v', G_META),
    'threads-500m': _r('Meta: New Threads features at 500 million monthly users (June 2026)', 'https://about.fb.com/news/2026/06/meta-launching-new-features-500-million-monthly-threads-users/', 'v', G_META),
    'threads-communities': _r('Meta: Introducing Threads Communities', 'https://about.fb.com/news/2025/10/introducing-threads-communities-find-your-people/', 'v', G_META),
    # ---- Other platforms
    'li-pages': _r('LinkedIn: LinkedIn Pages best practices', 'https://business.linkedin.com/advertise/linkedin-pages/best-practices', 'v', G_OTHER),
    'x-algo': _r('X: recommendation algorithm source code (GitHub)', 'https://github.com/twitter/the-algorithm', 'v', G_OTHER),
    'tg-channels': _r('Telegram: Channels FAQ', 'https://telegram.org/faq_channels', 'v', G_OTHER),
    'pib-apps': _r('PIB: Government blocks 59 apps, including TikTok (June 2020)', 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=1635206&reg=48&lang=2', 'v', G_OTHER),
    # ---- News reports on platform changes
    'sel-ig-ranking': _r('Search Engine Land: How Instagram ranks content (2023)', 'https://searchengineland.com/how-instagram-ranks-content-feed-stories-explore-reels-search-427774', 'v', G_NEWS),
    'bt-reels3': _r('Business Today: Instagram Reels up to 3 minutes (January 2025)', 'https://www.businesstoday.in/technology/news/story/instagram-head-announces-big-changes-3-minute-reels-and-new-look-for-profile-grid-461527-2025-01-21', 'v', G_NEWS),
    'tc-trial': _r('TechCrunch: Instagram trial reels (December 2024)', 'https://techcrunch.com/2024/12/10/instagram-rolls-out-trial-reels-that-arent-shown-to-a-creators-followers', 'v', G_NEWS),
    'ss-hashtags': _r('Social Samosa: Instagram limits hashtags to five per post (December 2025)', 'https://www.socialsamosa.com/news-2/instagram-hashtags-five-per-post-10923075', 'v', G_NEWS),
    'ss-views': _r('Social Samosa: Instagram makes Views its main metric (August 2024)', 'https://socialsamosa.com/news-2/instagram-updates-metrics-creators-prioritise-reach-6807009', 'v', G_NEWS),
    'mc-carousel': _r('Metricool: Instagram carousels up to 20 photos or videos (August 2024)', 'https://metricool.com/instagram-increases-carousel-content-limit/', 'v', G_NEWS),
    'gz-original': _r('GIGAZINE: Instagram ranking change that favours original content (May 2024)', 'https://www.gigazine.net/gsc_news/en/20240502-instagram-updated-algorithm-prioritizes-original-content', 'v', G_NEWS),
    'tc-fb-original': _r('TechCrunch: Meta cracks down on unoriginal Facebook content (July 2025)', 'https://techcrunch.com/2025/07/14/following-youtube-meta-announces-crackdown-on-unoriginal-facebook-content', 'v', G_NEWS),
    'tc-links': _r('TechCrunch: Instagram allows up to five links in bio (April 2023)', 'https://techcrunch.com/2023/04/18/instagram-takes-on-linktree-and-others-with-support-for-up-to-5-links-in-bio/', 'v', G_NEWS),
    'tribune-hacked': _r('The Tribune: Instagram.com/hacked helps users regain access (December 2022)', 'https://www.tribuneindia.com/news/science-technology/instagram-to-help-hacked-users-regain-account-access-461596', 'v', G_NEWS),
    'smt-linkedin': _r('Social Media Today: LinkedIn removes Creator Mode (February 2024)', 'https://www.socialmediatoday.com/news/linkedins-removing-its-creator-mode-option/706585/', 'v', G_NEWS),
    'bt-koo': _r('Business Today: Koo shuts down (July 2024)', 'https://businesstoday.in/technology/news/story/little-yellow-bird-says-final-goodbye-indias-twitter-rival-koo-shuts-down-435555-2024-07-03', 'v', G_NEWS),
    'threads-india': _r('DT Next (IANS): India among the most active countries on Threads (July 2024)', 'https://www.dtnext.in/lifestyle/technology/india-one-of-the-most-active-countries-for-metas-threads-globally-793241', 'v', G_NEWS),
    'tc-wa-limits': _r('TechCrunch: WhatsApp to limit broadcast messages (March 2025)', 'https://techcrunch.com/2025/03/18/whatsapp-will-soon-limit-number-of-broadcast-messages-users-and-businesses-can-send/', 'vr', G_NEWS),
    'tc-wa-unreplied': _r('TechCrunch: WhatsApp tests limits on messages that get no reply (October 2025)', 'https://techcrunch.com/2025/10/17/whatsapp-will-curb-the-number-of-messages-people-and-businesses-can-send-without-a-response', 'vr', G_NEWS),
    'mn-creator-mkt': _r('MediaNama: Instagram Creator Marketplace launches in India (February 2024)', 'https://www.medianama.com/2024/02/223-instagram-creator-marketplace-india-2/', 'v', G_NEWS),
    'yt-shopping-in': _r('YourStory: YouTube Shopping affiliate programme in India (October 2024)', 'https://yourstory.com/2024/10/youtube-expands-shopping-programme-india', 'vr', G_NEWS),
    'bt-it-rules': _r('Business Today: Government notifies rules on AI-generated content (February 2026)', 'https://www.businesstoday.in/amp/technology/story/govt-tightens-rules-on-ai-generated-content-mandates-labels-and-faster-takedowns-515505-2026-02-10', 'vr', G_NEWS),
    'bt-is19000': _r('Business Today: BIS standard IS 19000:2022 for online reviews (December 2022)', 'https://businesstoday.in/latest/trends/story/fake-online-reviews-bis-releases-new-standard-for-online-consumer-reviews-356195-2022-12-13', 'vr', G_NEWS),
    # ---- Free courses and guides
    'yt-creators': _r('YouTube Creators (free official guides)', 'https://www.youtube.com/creators/', 'v', G_COURSES),
    'bp-free': _r('Meta Blueprint: Browse free courses from the Blueprint catalog', 'https://www.facebookblueprint.com/student/page/512235-browse-free-courses-from-the-blueprint-catalog', 'v', G_COURSES),
    'bp-intro': _r('Meta Blueprint: Start marketing with Meta technologies', 'https://www.facebookblueprint.com/student/path/211554-meta-marketing', 'v', G_COURSES),
    'bp-ads': _r('Meta Blueprint: Get started with advertising on Facebook and Instagram', 'https://www.facebookblueprint.com/student/path/211543-meta-advertising-course', 'v', G_COURSES),
    'bp-audiences': _r('Meta Blueprint: Create audiences in Meta Ads Manager', 'https://www.facebookblueprint.com/student/path/211545-ads-manager-audiences', 'v', G_COURSES),
    'skillshop-ads': _r('Google Skillshop: Free Google Ads training', 'https://skillshop.withgoogle.com/googleads/', 'v', G_COURSES),
    'ga-academy': _r('Analytics Help: Analytics Academy on Skillshop (free courses)', 'https://support.google.com/analytics/answer/15440208', 'v', G_COURSES),
    'hubspot-res': _r('HubSpot: free social media courses', 'https://www.hubspot.com/resources/courses/social-media', 'v', G_COURSES),
    'hubspot-social': _r('HubSpot Academy: Social Media Certification Course (free)', 'https://academy.hubspot.com/courses/social-media', 'v', G_COURSES),
    'hubspot-cert-blog': _r('HubSpot: what the Social Media Certification covers', 'https://blog.hubspot.com/customers/introducing-hubspot-academy-social-media-certification', 'v', G_COURSES),
    'hubspot-ig': _r('HubSpot Academy: Instagram marketing strategy course (free)', 'https://academy.hubspot.com/courses/instagram-marketing', 'v', G_COURSES),
    'canva-ds': _r('Canva Design School (free courses)', 'https://www.canva.com/design-school/', 'v', G_COURSES),
    'canva-gde': _r('Canva Design School: Graphic design essentials', 'https://www.canva.com/design-school/courses/graphic-design-essentials/', 'v', G_COURSES),
    'canva-mkt': _r('Canva Design School: Marketing with Canva', 'https://www.canva.com/en/design-school/courses/marketing-with-canva', 'v', G_COURSES),
    'os-pom': _r('OpenStax: Principles of Marketing (free textbook, CC BY-NC-SA 4.0)', 'https://openstax.org/books/principles-marketing/pages/preface', 'v', G_COURSES),
    'os-5-1': _r('OpenStax Principles of Marketing 5.1: Market Segmentation and Consumer Markets', 'https://openstax.org/books/principles-marketing/pages/5-1-market-segmentation-and-consumer-markets', 'v', G_COURSES),
    'os-13-3': _r('OpenStax Principles of Marketing 13.3: Integrated Marketing Communications', 'https://openstax.org/books/principles-marketing/pages/13-3-integrated-marketing-communications', 'v', G_COURSES),
    'os-16-2': _r('OpenStax Principles of Marketing 16.2: Social Media and Mobile Marketing', 'https://openstax.org/books/principles-marketing/pages/16-2-social-media-and-mobile-marketing', 'v', G_COURSES),
    'dcn-boost': _r('Digital Culture Network: boosted posts vs ad campaigns', 'https://digitalculturenetwork.org.uk/knowledge/whats-the-difference-between-boosted-posts-and-ad-campaigns-on-facebook-and-instagram/', 'v', G_COURSES),
    'dcn-audience': _r('Digital Culture Network: reaching your audience with Meta ads', 'https://digitalculturenetwork.org.uk/knowledge/reaching-your-audience-making-your-meta-ads-more-effective/', 'v', G_COURSES),
    # ---- Free apps
    'edits': _r('Edits video editor by Instagram (Google Play)', 'https://play.google.com/store/apps/details?id=com.instagram.basel', 'v', G_APPS),
    'yt-create': _r('YouTube Create video editor (Google Play)', 'https://play.google.com/store/apps/details?id=com.google.android.apps.youtube.producer', 'v', G_APPS),
    'yt-studio-app': _r('YouTube Studio app (Google Play)', 'https://play.google.com/store/apps/details?id=com.google.android.apps.youtube.creator', 'v', G_APPS),
    'vn': _r('VN photo and video editor (Google Play)', 'https://play.google.com/store/apps/details?id=com.frontrow.vlog', 'v', G_APPS),
    'inshot': _r('InShot video editor (Google Play)', 'https://play.google.com/store/apps/details?id=com.camerasideas.instashot', 'v', G_APPS),
    'snapseed': _r('Snapseed photo editor by Google (Google Play)', 'https://play.google.com/store/apps/details?id=com.niksoftware.snapseed', 'v', G_APPS),
    'opencamera': _r('Open Camera, open-source camera app (Google Play)', 'https://play.google.com/store/apps/details?id=net.sourceforge.opencamera', 'v', G_APPS),
    'canva-app': _r('Canva app (Google Play)', 'https://play.google.com/store/apps/details?id=com.canva.editor', 'v', G_APPS),
    'canva-license': _r('Canva Free Media License', 'https://www.canva.com/policies/free-media', 'v', G_APPS),
    'mbs-app': _r('Meta Business Suite app (Google Play)', 'https://play.google.com/store/apps/details?id=com.facebook.pages.app', 'v', G_APPS),
    'wa-business': _r('WhatsApp Business app (Google Play)', 'https://play.google.com/store/apps/details?id=com.whatsapp.w4b', 'v', G_APPS),
    'sharechat': _r('ShareChat (Google Play)', 'https://play.google.com/store/apps/details?id=in.mohalla.sharechat', 'v', G_APPS),
    'moj': _r('Moj short videos (Google Play)', 'https://play.google.com/store/apps/details?id=in.mohalla.video', 'v', G_APPS),
    # ---- Open-source software for the laptop
    'gimp': _r('GIMP image editor', 'https://www.gimp.org/', 'v', G_OSS),
    'inkscape': _r('Inkscape vector graphics editor', 'https://inkscape.org/about/', 'v', G_OSS),
    'krita': _r('Krita painting program', 'https://krita.org/en/', 'v', G_OSS),
    'kdenlive': _r('Kdenlive video editor (features, including proxy clips)', 'https://kdenlive.org/en/features/', 'v', G_OSS),
    'shotcut': _r('Shotcut video editor', 'https://shotcut.org/', 'v', G_OSS),
    'audacity': _r('Audacity audio editor', 'https://www.audacityteam.org/', 'v', G_OSS),
    'obs': _r('OBS Studio screen recorder', 'https://obsproject.com/', 'v', G_OSS),
    # ---- Malayalam fonts and typing
    'font-manjari': _r('Google Fonts: Manjari (Malayalam and Latin)', 'https://fonts.google.com/specimen/Manjari', 'v', G_FONTS),
    'font-chilanka': _r('Google Fonts: Chilanka (Malayalam handwriting style)', 'https://fonts.google.com/specimen/Chilanka', 'v', G_FONTS),
    'font-noto-ml': _r('Google Fonts: Noto Sans Malayalam', 'https://fonts.google.com/noto/specimen/Noto+Sans+Malayalam', 'v', G_FONTS),
    'smc-fonts': _r('Swathanthra Malayalam Computing: Manjari, Gayathri and Chilanka in Google Fonts', 'https://blog.smc.org.in/manjari-gayathri-chilanka-in-google-fonts/', 'v', G_FONTS),
    'gboard-ml': _r('Gboard Help: Type in a different language', 'https://support.google.com/gboard/answer/7068494', 'v', G_FONTS),
    'indic-kbd': _r('Indic Keyboard, free and open source (Google Play)', 'https://play.google.com/store/apps/details?id=org.smc.inputmethod.indic', 'v', G_FONTS),
    # ---- AI tools
    'gemini-plans': _r('Google Gemini plans (has a free plan)', 'https://gemini.google/subscriptions/', 'vr', G_AI),
    'chatgpt-plans': _r('ChatGPT plans (has a free plan)', 'https://chatgpt.com/pricing', 'vr', G_AI),
    'claude-plans': _r('Claude plans (has a free plan)', 'https://claude.com/pricing', 'vr', G_AI),
    # ---- India: rules and law
    'asci-guidelines': _r('ASCI: Guidelines for influencer advertising in digital media (PDF)', 'https://www.ascionline.in/social/wp-content/uploads/2025/04/ASCI-Influencer-Guidelines.pdf', 'vr', G_INDIA),
    'asci-faqs': _r('ASCI: influencer advertising FAQs', 'https://www.ascionline.in/social/faqs/', 'vr', G_INDIA),
    'pib-endorse': _r('PIB: Endorsement guidelines for celebrities and influencers (January 2023)', 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=1892527&reg=48&lang=2', 'vr', G_INDIA),
    'pib-misleading': _r('PIB: Misleading advertisement guidelines and penalties (February 2023, PDF)', 'https://consumeraffairs.nic.in/sites/default/files/PIB1897389.pdf', 'vr', G_INDIA),
    'pib-dark': _r('PIB: Guidelines for Prevention and Regulation of Dark Patterns, 2023', 'https://pib.gov.in/PressReleasePage.aspx?PRID=1983994', 'vr', G_INDIA),
    'dpdp': _r('PIB: Digital Personal Data Protection Rules, 2025 explained (PDF)', 'https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf', 'vr', G_INDIA),
    'copyright-act': _r('India Code: The Copyright Act, 1957 (PDF)', 'https://www.indiacode.nic.in/bitstream/123456789/1367/1/a195714.pdf', 'vr', G_INDIA),
    # ---- Help and safety
    'telemanas': _r('Tele-MANAS mental health helpline, 14416 (IIIT Bangalore page)', 'https://ehrc.iiitb.ac.in/project/tele-manas', 'v', G_SAFETY),
    'kp-1930': _r('Kerala Police: 1930 cyber crime helpline', 'https://ps.keralapolice.gov.in/ernakulamruralcyber-ps/notifications/National-Cyber-Crime-Reporting-Helpline-No-1930-3338', 'v', G_SAFETY),
    'cybercrime': _r('National Cyber Crime Reporting Portal', 'https://cybercrime.gov.in/', 'u', G_SAFETY),
    'who-burnout': _r('WHO: Burn-out an "occupational phenomenon"', 'https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases', 'v', G_SAFETY),
    # ---- Earning programmes
    'amazon-assoc': _r('Amazon.in Associates (affiliate programme)', 'https://affiliate-program.amazon.in/', 'vr', G_MONEY),
    'amazon-fees': _r('Amazon.in Associates: advertising fee schedule', 'https://affiliate-program.amazon.in/help/operating/advertisingfees/', 'vr', G_MONEY),
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
    return f"{link(key, text)} (check current rules)"


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


def lesson(m, l, *, title, weeks, hours, outcome, split, core, example, resources,
           steps, proof, templates, mistakes, quiz, study, action, fulltime=None):
    code = f'SMM-M{m:02d}-L{l:02d}'
    sid = code.lower()
    a, b = weeks
    q_text, a_text = quiz_blocks(quiz)
    assert 3 <= len(quiz) <= 5
    assert templates, f'{code} needs at least one template'
    parts = [
        '## Core lesson',
        core.strip(),
        '## Local example',
        example.strip(),
        '## Free resources',
        res_table(resources),
        '## Action task',
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
             'detail': f'**Proof to record:** {proof} Paste the link to your proof (a Google Drive file, a post link or a screenshot) in this task\'s note.'},
            {'id': f'{sid}-quiz', 'text': f'Quiz: at least {len(quiz) - 1} right', 'kind': 'task', 'week': b},
        ],
    }


def fmt_hours(h):
    if h == int(h):
        return f'{int(h)} hour' + ('' if h == 1 else 's')
    whole = int(h)
    mins = round((h - whole) * 60)
    if whole == 0:
        return f'{mins} minutes'
    return f'{whole} hour' + ('' if whole == 1 else 's') + f' {mins} minutes'


def module(m, *, title, weeks, hours, overview, outcomes, lessons, project, project_steps,
           project_proof, rubric, short, flashcards, mistakes, fulltime=None, project_week=None):
    sid = f'smm-m{m:02d}'
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
