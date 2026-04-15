<?php

if (!defined('ABSPATH')) {
	exit;
}

function unyra_supported_locales() {
	return ['en', 'pt', 'es'];
}

function unyra_default_locale() {
	return 'en';
}

function unyra_locale_meta() {
	return [
		'en' => [
			'label' => 'English',
			'short' => 'EN',
			'tag'   => 'en-US',
		],
		'pt' => [
			'label' => 'Português',
			'short' => 'PT',
			'tag'   => 'pt-BR',
		],
		'es' => [
			'label' => 'Español',
			'short' => 'ES',
			'tag'   => 'es-ES',
		],
	];
}

function unyra_page_slugs() {
	return [
		'home'      => ['en' => '', 'pt' => '', 'es' => ''],
		'about'     => ['en' => 'about', 'pt' => 'sobre', 'es' => 'nosotros'],
		'markets'   => ['en' => 'markets-global-network', 'pt' => 'mercados-rede-global', 'es' => 'mercados-red-global'],
		'solutions' => ['en' => 'solutions', 'pt' => 'solucoes', 'es' => 'soluciones'],
		'buyers'    => ['en' => 'for-buyers', 'pt' => 'para-compradores', 'es' => 'para-compradores'],
		'producers' => ['en' => 'for-producers-exporters', 'pt' => 'para-produtores-exportadores', 'es' => 'para-productores-exportadores'],
		'contact'   => ['en' => 'contact', 'pt' => 'contato', 'es' => 'contacto'],
		'privacy'   => ['en' => 'privacy-policy', 'pt' => 'politica-de-privacidade', 'es' => 'politica-de-privacidad'],
		'thank_you' => ['en' => 'thank-you', 'pt' => 'obrigado', 'es' => 'gracias'],
	];
}

function unyra_company_defaults() {
	return [
		'name'             => 'Unyra Group LLC',
		'legal_name'       => 'Unyra Group LLC',
		'url'              => home_url('/'),
		'experience_badge' => '20+ years',
		'description'      => 'A global company specialized in connecting buyers and producer-exporters worldwide, especially in the garlic market and agricultural commodities.',
		'markets'          => ['United States', 'Canada', 'Brazil', 'Chile', 'Argentina', 'Egypt', 'Turkey', 'Europe', 'China'],
		'company_email'    => get_theme_mod('unyra_company_email', 'sales@unyragroup.com'),
		'sales_email'      => get_theme_mod('unyra_sales_email', 'sales@unyragroup.com'),
		'phone_display'    => get_theme_mod('unyra_phone_display', '+1 888 789 843'),
		'location'         => get_theme_mod('unyra_location', 'Orlando, Florida, 32801, US'),
		'logo'             => get_template_directory_uri() . '/assets/images/unyra-logo.png',
		'icon'             => get_template_directory_uri() . '/assets/images/unyra-icon.svg',
	];
}

function unyra_theme_content() {
	return [
		'en' => [
			'labels' => [
				'site_title'        => 'Unyra Group LLC',
				'skip_to_content'   => 'Skip to main content',
				'language'          => 'Language',
				'nav'               => [
					'home'      => 'Home',
					'about'     => 'About',
					'markets'   => 'Markets & Global Network',
					'solutions' => 'Solutions',
					'buyers'    => 'For Buyers',
					'producers' => 'For Producers & Exporters',
					'contact'   => 'Contact',
					'privacy'   => 'Privacy Policy',
				],
				'primary_cta'       => 'Request a Trade Consultation',
				'secondary_cta'     => 'Speak With Our Team',
				'sticky_cta'        => 'Start a Conversation',
				'tagline'           => 'Connecting Markets. Building Trust. Delivering Value.',
				'footer_summary'    => 'A global company specialized in connecting buyers and producer-exporters worldwide, especially in the garlic market and agricultural commodities.',
				'footer_navigation' => 'Navigation',
				'footer_contact'    => 'Contact',
				'privacy_note'      => 'Questions about privacy or submitted information?',
				'footer_launch'     => 'Contact our team if you have questions about privacy or information submitted through this website.',
				'back_home'         => 'Back to home',
			],
			'contact_labels' => [
				'email'    => 'Email',
				'sales'    => 'Sales Email',
				'phone'    => 'Phone / WhatsApp',
				'location' => 'Business Location',
			],
			'form' => [
				'badge'          => 'Qualified Business Inquiry',
				'title'          => 'Start a focused trade conversation',
				'description'    => 'Share your company profile, market interest, and commercial priorities. We will review your inquiry and respond with the appropriate next step.',
				'submit'         => 'Send Inquiry',
				'sending'        => 'Sending...',
				'success'        => 'Your inquiry was submitted successfully. We are preparing your next step.',
				'error'          => 'We could not submit your inquiry right now. Please try again.',
				'privacy_note'   => 'By submitting this form, you agree to be contacted regarding your inquiry and acknowledge the privacy policy.',
				'honeypot'       => 'Leave this field empty',
				'fields'         => [
					'full_name' => 'Full Name',
					'company'   => 'Company',
					'email'     => 'Email',
					'phone'     => 'Phone / WhatsApp',
					'country'   => 'Country',
					'role'      => 'I am a...',
					'interest'  => 'Interest',
					'message'   => 'Message',
				],
				'placeholders'   => [
					'full_name' => 'Your full name',
					'company'   => 'Your company',
					'email'     => 'name@company.com',
					'phone'     => '+1...',
					'country'   => 'Country',
					'message'   => 'Briefly describe your company, market focus, and what you are looking to discuss.',
				],
				'role_options'   => [
					'buyer'              => 'Buyer',
					'producer-exporter'  => 'Producer-Exporter',
					'distributor'        => 'Distributor',
					'other'              => 'Other',
				],
				'interest_options' => [
					'garlic'                   => 'Garlic',
					'agricultural-commodities' => 'Agricultural Commodities',
					'strategic-partnership'    => 'Strategic Partnership',
					'other'                    => 'Other',
				],
			],
			'home' => [
				'hero' => [
					'eyebrow'      => 'Global trading | Garlic market | Agricultural commodities | 20+ years of experience',
					'title'        => 'A premium international trading partner connecting buyers and producer-exporters across global markets.',
					'description'  => 'Unyra Group LLC helps connect supply and demand with commercial clarity, strategic coordination, and long-term perspective across the United States, Canada, Brazil, Chile, Argentina, Egypt, Turkey, Europe, and China.',
					'experience'   => '20+ years in the garlic market and agricultural commodities',
					'market_line'  => 'Connecting opportunities across the United States, Canada, Brazil, Chile, Argentina, Egypt, Turkey, Europe, and China.',
					'primary_cta'  => 'Request a Trade Consultation',
					'secondary_cta'=> 'Become a Business Partner',
					'panel_title'  => 'Strategic bridge between supply and demand',
					'panel_text'   => 'Commercial coordination shaped by sector knowledge, disciplined communication, and trusted international relationships.',
					'highlights'   => [
						'Global buyer-exporter connectivity',
						'Executive-level commercial positioning',
						'Reliable long-term relationship focus',
					],
					'panel_cards'  => [
						['eyebrow' => 'Experience', 'title' => '20+ years of sector perspective'],
						['eyebrow' => 'Markets', 'title' => 'North America, South America, Europe, Egypt, Turkey, China'],
					],
				],
				'trust' => [
					['title' => '20+ Years of Market Experience', 'description' => 'Built around long-standing experience in the garlic market and agricultural commodities.'],
					['title' => 'Garlic & Commodity Expertise', 'description' => 'A focused understanding of agricultural trade dynamics, sourcing realities, and buyer expectations.'],
					['title' => 'Global Buyer-Exporter Connectivity', 'description' => 'Positioned to connect serious counterparties across multiple international markets.'],
					['title' => 'Strategic International Reach', 'description' => 'Commercially active across North America, South America, Europe, the Middle East, and China.'],
				],
				'about' => [
					'eyebrow'     => 'About Unyra',
					'title'       => 'An experienced company built to connect markets with seriousness, continuity, and commercial intelligence.',
					'description' => 'Unyra Group LLC operates as a strategic bridge between buyers and producer-exporters, helping structure valuable relationships across international trade environments.',
					'paragraphs'  => [
						'More than 20 years of sector experience matters because agricultural trade is shaped by timing, trust, coordination, and a clear understanding of counterparties.',
						'Unyra brings a calm, disciplined approach to business development, commercial coordination, and market connectivity, helping opportunities move forward with credibility.',
					],
					'markers'     => [
						'Global orientation with a relationship-driven mindset',
						'Focused expertise in garlic and agricultural commodities',
						'Commercial positioning designed for qualified business leads',
					],
				],
				'solutions' => [
					'eyebrow'     => 'What We Do',
					'title'       => 'Business capabilities designed for real international trade execution.',
					'description' => 'Unyra helps serious opportunities move with clarity, coordination, and commercially intelligent follow-through.',
					'items'       => [
						['title' => 'Global Trading', 'description' => 'Coordinating international business opportunities with strategic commercial discipline.'],
						['title' => 'International Sourcing', 'description' => 'Connecting buyers with qualified producer-exporters in relevant markets and product categories.'],
						['title' => 'Business Development', 'description' => 'Opening conversations and growth paths that support long-term commercial value.'],
						['title' => 'Commercial Coordination', 'description' => 'Aligning counterparties, priorities, and communication so opportunities advance with consistency.'],
						['title' => 'Supply Chain Coordination', 'description' => 'Supporting trade discussions with practical awareness of timing, flow, and market realities.'],
						['title' => 'Strategic Market Connectivity', 'description' => 'Linking supply and demand across markets where trusted relationships matter.'],
					],
				],
				'expertise' => [
					'eyebrow'     => 'Industry Expertise',
					'title'       => 'Specialized knowledge in garlic and agricultural commodities.',
					'description' => 'Deep sector understanding helps reduce friction, strengthen dialogue, and create more credible international business opportunities.',
					'pillars'     => [
						['title' => 'Garlic Market', 'description' => 'Experience shaped by years of market observation, commercial interaction, and product-specific understanding.'],
						['title' => 'Agricultural Commodities', 'description' => 'A broader view of commodity trade supported by strategic relationship-building and disciplined coordination.'],
					],
					'aside_title' => 'Long-term value in international trade',
					'aside_text'  => 'Unyra works with an international perspective, commercial seriousness, and relationship-first execution that supports continuity over short-term transactions.',
				],
				'network' => [
					'eyebrow'     => 'Markets & Global Network',
					'title'       => 'A commercially active network across key global trade regions.',
					'description' => 'Unyra connects opportunities across established and emerging trade environments where experience, timing, and trusted relationships matter.',
					'cards'       => [
						['key' => 'united-states', 'title' => 'United States', 'description' => 'A strategic market for demand-side relationships, sourcing conversations, and long-term business coordination.'],
						['key' => 'canada', 'title' => 'Canada', 'description' => 'Relevant for importers, distributors, and structured commercial opportunities in agricultural trade.'],
						['key' => 'brazil', 'title' => 'Brazil', 'description' => 'A major regional reference point for buyer relationships, producer visibility, and trade connectivity.'],
						['key' => 'chile', 'title' => 'Chile', 'description' => 'An important South American trade environment for export-oriented business development.'],
						['key' => 'argentina', 'title' => 'Argentina', 'description' => 'A market where agricultural trade knowledge and strong business relationships remain essential.'],
						['key' => 'egypt', 'title' => 'Egypt', 'description' => 'A relevant origin and trade connection point in broader international commodity flows.'],
						['key' => 'turkey', 'title' => 'Turkey', 'description' => 'A strategic market bridge between regional opportunity and broader international connectivity.'],
						['key' => 'europe', 'title' => 'Europe', 'description' => 'A mature trade environment where trust, professionalism, and disciplined commercial coordination matter.'],
						['key' => 'china', 'title' => 'China', 'description' => 'A major market reference in global agricultural trade and strategic sourcing conversations.'],
					],
				],
				'audiences' => [
					'eyebrow'     => 'Two Commercial Paths',
					'title'       => 'Built for buyers and for producer-exporters.',
					'description' => 'The same disciplined market approach is adapted to the needs of both sides of the trade relationship.',
					'cards'       => [
						[
							'key'         => 'buyers',
							'eyebrow'     => 'For Buyers',
							'title'       => 'Structured access to reliable international sourcing conversations.',
							'description' => 'For importers, distributors, and commercial partners seeking seriousness, market understanding, and dependable coordination.',
							'bullets'     => ['Trusted sourcing relationships', 'Commercial clarity', 'Reliable international coordination'],
							'cta'         => 'Explore the buyer path',
						],
						[
							'key'         => 'producers',
							'eyebrow'     => 'For Producers & Exporters',
							'title'       => 'Support for expanding visibility and access to international buyers.',
							'description' => 'For producers and exporters looking to build qualified business relationships and open credible new market opportunities.',
							'bullets'     => ['Access to international counterparties', 'Business development support', 'Long-term relationship building'],
							'cta'         => 'Explore the exporter path',
						],
					],
				],
				'why' => [
					'eyebrow'     => 'Why Unyra',
					'title'       => 'Why serious companies choose to work with Unyra.',
					'description' => 'The value is built through experience, international perspective, disciplined coordination, and trusted commercial relationships.',
					'items'       => [
						['title' => 'Experience', 'description' => '20+ years of perspective in the garlic market and agricultural commodities.'],
						['title' => 'Market Understanding', 'description' => 'A clear view of how counterparties, priorities, and trade realities need to align.'],
						['title' => 'International Connections', 'description' => 'Commercial reach across relevant markets in the Americas, Europe, the Middle East, and China.'],
						['title' => 'Reliable Coordination', 'description' => 'Structured communication and disciplined follow-through in business conversations.'],
						['title' => 'Long-Term Partnerships', 'description' => 'Relationship-driven execution focused on continuity, not one-off transactions.'],
						['title' => 'Strategic Vision', 'description' => 'A commercially strong, calm, and premium approach to international trade.'],
					],
				],
				'cta' => [
					'title'       => 'Open the right conversation for your next business opportunity.',
					'description' => 'Whether you are buying, sourcing, exporting, or building new partnerships, Unyra is positioned to help connect the opportunity with the right market relationship.',
					'primary'     => 'Request a Trade Consultation',
					'secondary'   => 'For Buyers',
				],
				'lead' => [
					'eyebrow'     => 'Qualified Business Inquiry',
					'title'       => 'Start a direct commercial conversation with Unyra.',
					'description' => 'Share your market context, your company profile, and what you want to discuss. Our team will review the inquiry and define the best next step.',
					'bullets'     => [
						'Built to capture qualified international trade leads',
						'Prepared for buyers, distributors, producers, and exporters',
						'Designed for low-friction but serious business conversion',
					],
				],
			],
			'about' => [
				'hero' => [
					'eyebrow'     => 'About Unyra',
					'title'       => 'An experienced international company connecting markets with trust and continuity.',
					'description' => 'Unyra Group LLC acts as a strategic bridge between buyers and producer-exporters, supporting commercially serious opportunities in garlic and agricultural commodities.',
				],
				'overview' => [
					'eyebrow'     => 'Who We Are',
					'title'       => 'A relationship-driven company with an international trade mindset.',
					'description' => 'Unyra combines market understanding, business discipline, and long-term commercial vision.',
					'paragraphs'  => [
						'The company is positioned to connect supply and demand through trusted conversations, careful coordination, and market relevance.',
						'Its value comes from combining sector familiarity with international connectivity and commercially grounded execution.',
					],
				],
				'values' => [
					'eyebrow'     => 'What We Stand For',
					'title'       => 'Trust, continuity, and credible market relationships.',
					'description' => 'Unyra is built around steady business conduct and lasting value creation in international trade.',
					'items'       => [
						['title' => 'Trust', 'description' => 'Business relationships move faster and further when built on consistency and credibility.'],
						['title' => 'Continuity', 'description' => 'Long-term thinking matters in markets where reliability defines opportunity.'],
						['title' => 'Commercial Intelligence', 'description' => 'Good coordination depends on reading counterparties and market conditions with clarity.'],
					],
				],
				'experience' => [
					'eyebrow'     => '20+ Years of Experience',
					'title'       => 'Sector familiarity that strengthens decisions and market dialogue.',
					'description' => 'More than two decades of perspective in garlic and agricultural commodities helps Unyra support serious conversations with maturity.',
					'pillars'     => [
						['title' => 'Sector Perspective', 'description' => 'Experience helps clarify what matters, what creates friction, and how opportunity should be approached.'],
						['title' => 'Commercial Discipline', 'description' => 'Structured coordination supports better communication and stronger business continuity.'],
						['title' => 'Relationship Depth', 'description' => 'International trade works better when trust and timing are managed with professionalism.'],
					],
					'timeline'    => [
						'20+ years linked to the garlic market and agricultural commodities',
						'Strategic focus on connecting buyers and producer-exporters',
						'Relationship-first execution shaped by international business realities',
					],
				],
				'relationships' => [
					'title'       => 'Built for trust, continuity, and long-term commercial value.',
					'description' => 'Unyra works to help qualified relationships become commercially sustainable and internationally relevant.',
					'bullets'     => [
						'Structured and serious market coordination',
						'International trade perspective',
						'Long-term relationship building',
						'Focus on valuable commercial fit',
					],
				],
				'cta' => [
					'title'       => 'Start a conversation with a company built for lasting international business relationships.',
					'description' => 'If you are looking for experienced market coordination and a stronger bridge between supply and demand, Unyra is prepared to engage.',
				],
			],
			'markets' => [
				'hero' => [
					'eyebrow'     => 'Markets & Global Network',
					'title'       => 'A global commercial network connecting supply, demand, and opportunity.',
					'description' => 'Unyra operates as a bridge between market relationships across the United States, Canada, Brazil, Chile, Argentina, Egypt, Turkey, Europe, and China.',
				],
				'connectivity' => [
					'eyebrow'     => 'Global Connectivity',
					'title'       => 'Connecting trade opportunities across multiple market environments.',
					'description' => 'International trade requires more than reach. It requires timing, trust, and commercially intelligent coordination.',
					'items'       => [
						['title' => 'Cross-Market Perspective', 'description' => 'Understanding the commercial logic of different regions helps counterparties align more effectively.'],
						['title' => 'Supply-Demand Bridge', 'description' => 'Unyra helps connect relevant opportunities where buyer needs and exporter capabilities can meet.'],
						['title' => 'Relationship-Based Access', 'description' => 'Credible international trade opportunities are built through trusted conversations over time.'],
					],
				],
				'opportunity' => [
					'title'       => 'Positioned to connect opportunities across established and strategic trade corridors.',
					'description' => 'The company’s global orientation supports commercially relevant conversations in mature, emerging, and cross-regional markets.',
					'bullets'     => [
						'North America and South America',
						'Europe, Egypt, and Turkey',
						'China and broader international sourcing flows',
					],
				],
				'cta' => [
					'title'       => 'Discuss how your market opportunity fits into Unyra’s global network.',
					'description' => 'Reach out to explore buyer-side, exporter-side, or partnership opportunities.',
				],
			],
			'solutions' => [
				'hero' => [
					'eyebrow'     => 'Solutions',
					'title'       => 'Commercial capabilities designed for serious international trade execution.',
					'description' => 'Unyra’s role is built around sourcing, coordination, and strategic market relationships that help opportunities move forward.',
				],
				'capabilities' => [
					'eyebrow'     => 'Capabilities',
					'title'       => 'A clear, business-oriented approach to global trade support.',
					'description' => 'Each capability is designed to strengthen international commercial conversations and execution.',
					'items'       => [
						['title' => 'International Sourcing', 'description' => 'Connecting demand with relevant supply-side opportunities in the right markets.'],
						['title' => 'Global Trading Coordination', 'description' => 'Supporting commercially structured conversations across international counterparts.'],
						['title' => 'Business Development Support', 'description' => 'Helping create market visibility and qualified introductions that can generate long-term value.'],
						['title' => 'Commercial Relationship Building', 'description' => 'Strengthening buyer-exporter alignment through disciplined communication and trust.'],
						['title' => 'Supply Chain Coordination', 'description' => 'Bringing practical awareness to how timing, flow, and market expectations affect trade decisions.'],
						['title' => 'Strategic Market Connections', 'description' => 'Linking businesses to the right commercial environments and relationship pathways.'],
					],
				],
				'process' => [
					'eyebrow'     => 'How We Work',
					'title'       => 'A structured path from commercial interest to serious opportunity.',
					'description' => 'The process is designed to reduce friction and improve quality in international trade conversations.',
					'steps'       => [
						['title' => 'Understand the Business Need', 'description' => 'Clarify objectives, market context, and commercial priorities.'],
						['title' => 'Align the Right Market Relationship', 'description' => 'Connect the opportunity with relevant buyers, exporters, or trade counterparts.'],
						['title' => 'Support Credible Progress', 'description' => 'Help the conversation move with coordination, seriousness, and continuity.'],
					],
				],
				'expertise' => [
					'title'       => 'Specialized market experience supports stronger execution.',
					'description' => 'Garlic and agricultural commodities require commercial discipline, product understanding, and trusted coordination.',
					'bullets'     => [
						'Focused garlic market knowledge',
						'Strategic commodity trade perspective',
						'Relationship-centered international coordination',
					],
				],
				'cta' => [
					'title'       => 'Discuss the right commercial solution for your market objective.',
					'description' => 'Unyra is prepared to engage with sourcing, buyer-side, exporter-side, and partnership opportunities.',
				],
			],
			'buyers' => [
				'hero' => [
					'eyebrow'     => 'For Buyers',
					'title'       => 'A trusted commercial bridge for buyers, importers, distributors, and serious market partners.',
					'description' => 'Unyra supports buyers through structured sourcing conversations, international relationship management, and clear commercial coordination.',
				],
				'priorities' => [
					'eyebrow'     => 'Buyer Priorities',
					'title'       => 'What buyers need from a serious international trade partner.',
					'description' => 'The value is not just access. It is clarity, reliability, and commercially intelligent coordination.',
					'items'       => [
						['title' => 'Trusted Sourcing Connections', 'description' => 'Relevant counterparties supported by disciplined market relationships.'],
						['title' => 'Market Understanding', 'description' => 'Sector context and international perspective help reduce friction in key decisions.'],
						['title' => 'Commercial Coordination', 'description' => 'A more structured process for moving serious opportunities forward.'],
						['title' => 'Long-Term Value Creation', 'description' => 'Partnership-oriented execution rather than transactional short-termism.'],
					],
				],
				'approach' => [
					'eyebrow'     => 'How Unyra Helps',
					'title'       => 'Buyer-side value built around reliability and relationship quality.',
					'description' => 'Unyra is designed to support commercially serious buyers that value trust and structured coordination.',
					'bullets'     => [
						'Reliable international relationship management',
						'Commercially disciplined communication',
						'Strategic sourcing conversations with long-term perspective',
					],
				],
				'form_panel' => [
					'title'       => 'Tell us what you are buying and what kind of relationship you want to build.',
					'description' => 'Share your market focus, region, and sourcing priorities so we can assess the right next step.',
				],
			],
			'producers' => [
				'hero' => [
					'eyebrow'     => 'For Producers & Exporters',
					'title'       => 'Support for producers and exporters looking to expand international visibility and buyer access.',
					'description' => 'Unyra helps producer-exporters connect with relevant buyers, strengthen commercial visibility, and pursue long-term market growth.',
				],
				'priorities' => [
					'eyebrow'     => 'Exporter Priorities',
					'title'       => 'What serious producer-exporters need in international market development.',
					'description' => 'Commercial progress comes from the right market relationships, not just exposure.',
					'items'       => [
						['title' => 'Access to International Buyers', 'description' => 'Support in opening relevant commercial pathways beyond existing networks.'],
						['title' => 'Commercial Visibility', 'description' => 'Better positioning for opportunities that require stronger international reach.'],
						['title' => 'Strategic Connections', 'description' => 'Relationship-building that supports qualified discussions and serious business fit.'],
						['title' => 'Long-Term Commercial Growth', 'description' => 'A focus on continuity and value rather than short-lived transactional volume.'],
					],
				],
				'approach' => [
					'eyebrow'     => 'How Unyra Helps',
					'title'       => 'Exporter-side support shaped by market access and relationship depth.',
					'description' => 'The goal is to help credible producers and exporters build stronger commercial opportunities in relevant markets.',
					'bullets'     => [
						'Support in expanding buyer-side access',
						'Business development aligned to real market opportunities',
						'Long-term commercial relationship building',
					],
				],
				'form_panel' => [
					'title'       => 'Tell us what you produce, where you want to grow, and how you want to expand.',
					'description' => 'Share your product focus, current markets, and international objectives so we can evaluate a qualified next step.',
				],
			],
			'contact' => [
				'hero' => [
					'eyebrow'     => 'Contact',
					'title'       => 'Start a serious business conversation with Unyra Group LLC.',
					'description' => 'Whether the opportunity is buyer-side, exporter-side, or strategic partnership related, our team is positioned to review and respond.',
				],
				'response' => [
					'title'       => 'What to expect after you get in touch.',
					'description' => 'Your inquiry is reviewed with commercial focus and routed according to market relevance and next-step potential.',
					'bullets'     => [
						'Review of your business context and priorities',
						'Assessment of the right market path or relationship direction',
						'Follow-up with the most relevant next conversation',
					],
				],
			],
			'privacy' => [
				'hero' => [
					'eyebrow'     => 'Privacy Policy',
					'title'       => 'How Unyra Group LLC handles website inquiries and submitted information.',
					'description' => 'This policy explains, in general terms, how information submitted through this website may be collected, used, and retained.',
				],
				'sections' => [
					['title' => 'Information We Collect', 'paragraphs' => ['We may collect the information you submit through inquiry forms, including name, company, email, phone number, country, business role, commercial interest, and message content.', 'We may also receive limited technical information required for website operation and security.']],
					['title' => 'How Information May Be Used', 'paragraphs' => ['Submitted information may be used to review your inquiry, respond to your request, assess business relevance, and continue commercial communication related to the subject you submitted.', 'Unyra does not present this website as a consumer marketing platform; communications are intended for business and trade-related purposes.']],
					['title' => 'Information Sharing', 'paragraphs' => ['Your information is not sold. It may be shared internally or with service providers strictly as needed to operate the website, process inquiries, or support business communication.', 'Information may also be disclosed when required by law or when necessary to protect legitimate business interests.']],
					['title' => 'Retention and Security', 'paragraphs' => ['Information may be retained for as long as reasonably necessary to manage inquiries, business relationships, and operational records.', 'Reasonable administrative and technical measures may be used to reduce unauthorized access, misuse, or loss.']],
					['title' => 'Questions', 'paragraphs' => ['If you have questions regarding privacy or information submitted through this website, please contact Unyra Group LLC using the contact information provided on this site.']],
				],
			],
			'thank_you' => [
				'eyebrow'     => 'Thank You',
				'title'       => 'Your inquiry has been received.',
				'description' => 'Thank you for contacting Unyra Group LLC. Our team will review your message and respond with the most appropriate next step.',
				'primary'     => 'Back to home',
				'secondary'   => 'Contact page',
			],
		],
		'pt' => [
			'labels' => [
				'site_title'        => 'Unyra Group LLC',
				'skip_to_content'   => 'Ir para o conteúdo principal',
				'language'          => 'Idioma',
				'nav'               => [
					'home'      => 'Início',
					'about'     => 'Sobre',
					'markets'   => 'Mercados e Rede Global',
					'solutions' => 'Soluções',
					'buyers'    => 'Para Compradores',
					'producers' => 'Para Produtores e Exportadores',
					'contact'   => 'Contato',
					'privacy'   => 'Política de Privacidade',
				],
				'primary_cta'       => 'Solicitar uma Consulta Comercial',
				'secondary_cta'     => 'Fale com Nossa Equipe',
				'sticky_cta'        => 'Iniciar uma Conversa',
				'tagline'           => 'Conectando Mercados. Construindo Confiança. Gerando Valor.',
				'footer_summary'    => 'Empresa global especializada em conectar compradores e produtores-exportadores no mundo todo, especialmente no mercado de alho e em commodities agrícolas.',
				'footer_navigation' => 'Navegação',
				'footer_contact'    => 'Contato',
				'privacy_note'      => 'Dúvidas sobre privacidade ou informações enviadas?',
				'footer_launch'     => 'Fale com nossa equipe se tiver dúvidas sobre privacidade ou sobre informações enviadas por este site.',
				'back_home'         => 'Voltar para o início',
			],
			'contact_labels' => [
				'email'    => 'E-mail',
				'sales'    => 'E-mail Comercial',
				'phone'    => 'Telefone / WhatsApp',
				'location' => 'Localização Comercial',
			],
			'form' => [
				'badge'          => 'Consulta Comercial Qualificada',
				'title'          => 'Inicie uma conversa comercial objetiva',
				'description'    => 'Compartilhe o perfil da sua empresa, seu interesse de mercado e suas prioridades comerciais. Vamos analisar sua mensagem e direcionar o próximo passo adequado.',
				'submit'         => 'Enviar Consulta',
				'sending'        => 'Enviando...',
				'success'        => 'Sua consulta foi enviada com sucesso. Estamos preparando o próximo passo.',
				'error'          => 'Não foi possível enviar sua consulta agora. Tente novamente.',
				'privacy_note'   => 'Ao enviar este formulário, você concorda em ser contatado sobre sua consulta e reconhece a política de privacidade.',
				'honeypot'       => 'Deixe este campo em branco',
				'fields'         => [
					'full_name' => 'Nome Completo',
					'company'   => 'Empresa',
					'email'     => 'E-mail',
					'phone'     => 'Telefone / WhatsApp',
					'country'   => 'País',
					'role'      => 'Eu sou...',
					'interest'  => 'Interesse',
					'message'   => 'Mensagem',
				],
				'placeholders'   => [
					'full_name' => 'Seu nome completo',
					'company'   => 'Sua empresa',
					'email'     => 'nome@empresa.com',
					'phone'     => '+55...',
					'country'   => 'País',
					'message'   => 'Descreva brevemente sua empresa, seu foco de mercado e o que você deseja discutir.',
				],
				'role_options'   => [
					'buyer'              => 'Comprador',
					'producer-exporter'  => 'Produtor-Exportador',
					'distributor'        => 'Distribuidor',
					'other'              => 'Outro',
				],
				'interest_options' => [
					'garlic'                   => 'Alho',
					'agricultural-commodities' => 'Commodities Agrícolas',
					'strategic-partnership'    => 'Parceria Estratégica',
					'other'                    => 'Outro',
				],
			],
			'home' => [
				'hero' => [
					'eyebrow'      => 'Trading global | Mercado de alho | Commodities agrícolas | Mais de 20 anos de experiência',
					'title'        => 'Um parceiro internacional de alto nível conectando compradores e produtores-exportadores em mercados globais.',
					'description'  => 'A Unyra Group LLC conecta oferta e demanda com clareza comercial, coordenação estratégica e visão de longo prazo nos Estados Unidos, Canadá, Brasil, Chile, Argentina, Egito, Turquia, Europa e China.',
					'experience'   => 'Mais de 20 anos no mercado de alho e em commodities agrícolas',
					'market_line'  => 'Conectando oportunidades nos Estados Unidos, Canadá, Brasil, Chile, Argentina, Egito, Turquia, Europa e China.',
					'primary_cta'  => 'Solicitar uma Consulta Comercial',
					'secondary_cta'=> 'Tornar-se um Parceiro Comercial',
					'panel_title'  => 'Ponte estratégica entre oferta e demanda',
					'panel_text'   => 'Coordenação comercial apoiada por conhecimento setorial, comunicação disciplinada e relações internacionais de confiança.',
					'highlights'   => [
						'Conectividade global entre compradores e exportadores',
						'Posicionamento comercial executivo',
						'Foco confiável em relacionamentos de longo prazo',
					],
					'panel_cards'  => [
						['eyebrow' => 'Experiência', 'title' => 'Mais de 20 anos de visão setorial'],
						['eyebrow' => 'Mercados', 'title' => 'Américas, Europa, Egito, Turquia e China'],
					],
				],
				'trust' => [
					['title' => '20+ Anos de Experiência de Mercado', 'description' => 'Base construída sobre uma longa trajetória no mercado de alho e em commodities agrícolas.'],
					['title' => 'Especialização em Alho e Commodities', 'description' => 'Visão focada sobre dinâmica agrícola, origens, exigências de compradores e oportunidades comerciais.'],
					['title' => 'Conexão Global entre Compradores e Exportadores', 'description' => 'Posicionamento voltado a conectar contrapartes sérias em diferentes mercados internacionais.'],
					['title' => 'Alcance Estratégico Internacional', 'description' => 'Atuação comercial com relevância na América do Norte, América do Sul, Europa, Oriente Médio e China.'],
				],
				'about' => [
					'eyebrow'     => 'Sobre a Unyra',
					'title'       => 'Uma empresa experiente, criada para conectar mercados com seriedade, continuidade e inteligência comercial.',
					'description' => 'A Unyra Group LLC atua como ponte estratégica entre compradores e produtores-exportadores, ajudando a estruturar relações valiosas no comércio internacional.',
					'paragraphs'  => [
						'Mais de 20 anos de experiência fazem diferença porque o comércio agrícola depende de timing, confiança, coordenação e compreensão clara das contrapartes.',
						'A Unyra reúne uma abordagem serena e disciplinada para business development, coordenação comercial e conectividade de mercado, ajudando oportunidades a avançarem com credibilidade.',
					],
					'markers'     => [
						'Visão global com mentalidade orientada a relacionamentos',
						'Especialização em alho e commodities agrícolas',
						'Posicionamento comercial pensado para gerar leads qualificados',
					],
				],
				'solutions' => [
					'eyebrow'     => 'O Que Fazemos',
					'title'       => 'Capacidades comerciais desenhadas para a execução real no comércio internacional.',
					'description' => 'A Unyra ajuda oportunidades relevantes a avançarem com clareza, coordenação e inteligência comercial.',
					'items'       => [
						['title' => 'Trading Global', 'description' => 'Coordenação de oportunidades internacionais com disciplina e visão comercial.'],
						['title' => 'Sourcing Internacional', 'description' => 'Conexão entre compradores e produtores-exportadores qualificados em mercados relevantes.'],
						['title' => 'Business Development', 'description' => 'Abertura de conversas e caminhos de crescimento com valor comercial de longo prazo.'],
						['title' => 'Coordenação Comercial', 'description' => 'Alinhamento entre contrapartes, prioridades e comunicação para que as oportunidades avancem com consistência.'],
						['title' => 'Coordenação de Supply Chain', 'description' => 'Apoio às discussões comerciais com consciência prática de timing, fluxo e realidade de mercado.'],
						['title' => 'Conexões Estratégicas de Mercado', 'description' => 'Ligação entre oferta e demanda em mercados onde relações de confiança fazem diferença.'],
					],
				],
				'expertise' => [
					'eyebrow'     => 'Especialização Setorial',
					'title'       => 'Conhecimento especializado em alho e commodities agrícolas.',
					'description' => 'Uma compreensão profunda do setor ajuda a reduzir atritos, fortalecer o diálogo e criar oportunidades comerciais mais consistentes.',
					'pillars'     => [
						['title' => 'Mercado de Alho', 'description' => 'Experiência construída por anos de observação de mercado, interação comercial e entendimento específico do produto.'],
						['title' => 'Commodities Agrícolas', 'description' => 'Visão mais ampla do comércio de commodities apoiada por conexões estratégicas e coordenação disciplinada.'],
					],
					'aside_title' => 'Valor de longo prazo no comércio internacional',
					'aside_text'  => 'A Unyra trabalha com perspectiva internacional, seriedade comercial e execução orientada por relacionamentos duradouros.',
				],
				'network' => [
					'eyebrow'     => 'Mercados e Rede Global',
					'title'       => 'Uma rede comercial ativa em regiões estratégicas do comércio internacional.',
					'description' => 'A Unyra conecta oportunidades em ambientes comerciais consolidados e estratégicos, onde experiência, timing e confiança fazem diferença.',
					'cards'       => [
						['key' => 'united-states', 'title' => 'Estados Unidos', 'description' => 'Mercado estratégico para relações de demanda, sourcing e coordenação comercial de longo prazo.'],
						['key' => 'canada', 'title' => 'Canadá', 'description' => 'Ambiente relevante para importadores, distribuidores e oportunidades estruturadas em comércio agrícola.'],
						['key' => 'brazil', 'title' => 'Brasil', 'description' => 'Ponto de referência regional para relacionamentos com compradores, visibilidade de produtores e conectividade comercial.'],
						['key' => 'chile', 'title' => 'Chile', 'description' => 'Mercado importante na América do Sul para desenvolvimento comercial orientado à exportação.'],
						['key' => 'argentina', 'title' => 'Argentina', 'description' => 'Mercado em que conhecimento agrícola e relações comerciais sólidas continuam essenciais.'],
						['key' => 'egypt', 'title' => 'Egito', 'description' => 'Origem e ponto de conexão relevante em fluxos internacionais de commodities.'],
						['key' => 'turkey', 'title' => 'Turquia', 'description' => 'Ponte estratégica entre oportunidades regionais e conectividade internacional mais ampla.'],
						['key' => 'europe', 'title' => 'Europa', 'description' => 'Ambiente comercial maduro em que confiança, profissionalismo e coordenação disciplinada são fundamentais.'],
						['key' => 'china', 'title' => 'China', 'description' => 'Referência central no comércio agrícola global e em discussões estratégicas de sourcing.'],
					],
				],
				'audiences' => [
					'eyebrow'     => 'Dois Caminhos Comerciais',
					'title'       => 'Preparada para compradores e para produtores-exportadores.',
					'description' => 'A mesma disciplina de mercado é adaptada às necessidades dos dois lados da relação comercial.',
					'cards'       => [
						[
							'key'         => 'buyers',
							'eyebrow'     => 'Para Compradores',
							'title'       => 'Acesso estruturado a conversas confiáveis de sourcing internacional.',
							'description' => 'Para importadores, distribuidores e parceiros comerciais que buscam seriedade, visão de mercado e coordenação confiável.',
							'bullets'     => ['Relações confiáveis de sourcing', 'Clareza comercial', 'Coordenação internacional consistente'],
							'cta'         => 'Conheça a jornada do comprador',
						],
						[
							'key'         => 'producers',
							'eyebrow'     => 'Para Produtores e Exportadores',
							'title'       => 'Apoio para ampliar visibilidade e acesso a compradores internacionais.',
							'description' => 'Para produtores e exportadores que desejam construir relações qualificadas e abrir oportunidades relevantes em novos mercados.',
							'bullets'     => ['Acesso a contrapartes internacionais', 'Suporte em business development', 'Construção de relacionamentos duradouros'],
							'cta'         => 'Conheça a jornada do exportador',
						],
					],
				],
				'why' => [
					'eyebrow'     => 'Por Que Unyra',
					'title'       => 'Por que empresas sérias escolhem trabalhar com a Unyra.',
					'description' => 'O valor é construído por experiência, visão internacional, coordenação disciplinada e relações comerciais de confiança.',
					'items'       => [
						['title' => 'Experiência', 'description' => 'Mais de 20 anos de visão prática no mercado de alho e em commodities agrícolas.'],
						['title' => 'Entendimento de Mercado', 'description' => 'Clareza sobre como contrapartes, prioridades e realidades comerciais precisam se alinhar.'],
						['title' => 'Conexões Internacionais', 'description' => 'Atuação em mercados relevantes das Américas, Europa, Oriente Médio e China.'],
						['title' => 'Coordenação Confiável', 'description' => 'Comunicação estruturada e acompanhamento disciplinado em conversas de negócio.'],
						['title' => 'Parcerias de Longo Prazo', 'description' => 'Execução orientada por relacionamento e continuidade, não por transações pontuais.'],
						['title' => 'Visão Estratégica', 'description' => 'Uma abordagem comercial forte, serena e premium para o comércio internacional.'],
					],
				],
				'cta' => [
					'title'       => 'Abra a conversa certa para a sua próxima oportunidade de negócio.',
					'description' => 'Se você está comprando, buscando origem, exportando ou desenvolvendo parcerias, a Unyra está posicionada para conectar a oportunidade ao relacionamento de mercado certo.',
					'primary'     => 'Solicitar uma Consulta Comercial',
					'secondary'   => 'Para Compradores',
				],
				'lead' => [
					'eyebrow'     => 'Consulta Comercial Qualificada',
					'title'       => 'Inicie uma conversa comercial direta com a Unyra.',
					'description' => 'Compartilhe seu contexto de mercado, o perfil da sua empresa e o que você deseja discutir. Nossa equipe avaliará a mensagem e definirá o melhor próximo passo.',
					'bullets'     => [
						'Pensado para captar leads qualificados de comércio internacional',
						'Preparado para compradores, distribuidores, produtores e exportadores',
						'Desenhado para conversão séria com baixa fricção',
					],
				],
			],
			'about' => [
				'hero' => [
					'eyebrow'     => 'Sobre a Unyra',
					'title'       => 'Uma empresa internacional experiente, conectando mercados com confiança e continuidade.',
					'description' => 'A Unyra Group LLC atua como ponte estratégica entre compradores e produtores-exportadores, apoiando oportunidades comercialmente sérias em alho e commodities agrícolas.',
				],
				'overview' => [
					'eyebrow'     => 'Quem Somos',
					'title'       => 'Uma empresa orientada por relacionamentos e visão internacional de comércio.',
					'description' => 'A Unyra combina entendimento de mercado, disciplina comercial e visão de longo prazo.',
					'paragraphs'  => [
						'A empresa está posicionada para conectar oferta e demanda por meio de conversas confiáveis, coordenação cuidadosa e relevância comercial.',
						'Seu valor nasce da combinação entre familiaridade setorial, conectividade internacional e execução comercialmente consistente.',
					],
				],
				'values' => [
					'eyebrow'     => 'O Que Representamos',
					'title'       => 'Confiança, continuidade e relações comerciais credíveis.',
					'description' => 'A Unyra foi construída sobre conduta comercial estável e criação de valor duradoura no comércio internacional.',
					'items'       => [
						['title' => 'Confiança', 'description' => 'Relações de negócio avançam melhor quando são sustentadas por consistência e credibilidade.'],
						['title' => 'Continuidade', 'description' => 'Visão de longo prazo importa em mercados onde confiabilidade define oportunidade.'],
						['title' => 'Inteligência Comercial', 'description' => 'Boa coordenação depende de leitura clara de mercado, timing e contrapartes.'],
					],
				],
				'experience' => [
					'eyebrow'     => 'Mais de 20 Anos de Experiência',
					'title'       => 'Vivência setorial que fortalece decisões e conversas de mercado.',
					'description' => 'Mais de duas décadas no alho e em commodities agrícolas ajudam a Unyra a apoiar conversas sérias com maturidade e visão comercial.',
					'pillars'     => [
						['title' => 'Perspectiva Setorial', 'description' => 'Experiência ajuda a entender o que importa, o que gera atrito e como a oportunidade deve ser conduzida.'],
						['title' => 'Disciplina Comercial', 'description' => 'Coordenação estruturada favorece comunicação melhor e maior continuidade de negócio.'],
						['title' => 'Profundidade de Relacionamento', 'description' => 'O comércio internacional funciona melhor quando confiança e timing são tratados com profissionalismo.'],
					],
					'timeline'    => [
						'Mais de 20 anos ligados ao mercado de alho e às commodities agrícolas',
						'Foco estratégico em conectar compradores e produtores-exportadores',
						'Execução orientada por relacionamento e realidade de negócios internacionais',
					],
				],
				'relationships' => [
					'title'       => 'Construída para confiança, continuidade e valor comercial de longo prazo.',
					'description' => 'A Unyra trabalha para ajudar relações qualificadas a se tornarem comercialmente sustentáveis e internacionalmente relevantes.',
					'bullets'     => [
						'Coordenação de mercado estruturada e séria',
						'Perspectiva internacional de comércio',
						'Construção de relacionamentos duradouros',
						'Foco em aderência comercial valiosa',
					],
				],
				'cta' => [
					'title'       => 'Inicie uma conversa com uma empresa preparada para relações comerciais internacionais duradouras.',
					'description' => 'Se você busca experiência de mercado, coordenação comercial e uma ponte mais forte entre oferta e demanda, a Unyra está pronta para conversar.',
				],
			],
			'markets' => [
				'hero' => [
					'eyebrow'     => 'Mercados e Rede Global',
					'title'       => 'Uma rede comercial global conectando oferta, demanda e oportunidade.',
					'description' => 'A Unyra atua como ponte entre relações comerciais nos Estados Unidos, Canadá, Brasil, Chile, Argentina, Egito, Turquia, Europa e China.',
				],
				'connectivity' => [
					'eyebrow'     => 'Conectividade Global',
					'title'       => 'Conectando oportunidades comerciais em diferentes ambientes de mercado.',
					'description' => 'O comércio internacional exige mais do que alcance. Exige timing, confiança e coordenação comercial inteligente.',
					'items'       => [
						['title' => 'Perspectiva Multimercado', 'description' => 'Entender a lógica comercial de diferentes regiões ajuda a alinhar contrapartes com mais eficiência.'],
						['title' => 'Ponte entre Oferta e Demanda', 'description' => 'A Unyra ajuda a conectar oportunidades relevantes onde necessidades de compradores e capacidades de exportadores podem convergir.'],
						['title' => 'Acesso Baseado em Relacionamento', 'description' => 'Oportunidades internacionais credíveis se constroem por meio de confiança e tempo.'],
					],
				],
				'opportunity' => [
					'title'       => 'Posicionada para conectar oportunidades em corredores estratégicos do comércio internacional.',
					'description' => 'A orientação global da empresa apoia conversas comercialmente relevantes em mercados maduros, emergentes e inter-regionais.',
					'bullets'     => [
						'América do Norte e América do Sul',
						'Europa, Egito e Turquia',
						'China e fluxos globais de sourcing',
					],
				],
				'cta' => [
					'title'       => 'Converse sobre como sua oportunidade se encaixa na rede global da Unyra.',
					'description' => 'Entre em contato para explorar oportunidades do lado comprador, do lado exportador ou de parceria estratégica.',
				],
			],
			'solutions' => [
				'hero' => [
					'eyebrow'     => 'Soluções',
					'title'       => 'Capacidades comerciais desenhadas para execução séria no comércio internacional.',
					'description' => 'O papel da Unyra está baseado em sourcing, coordenação e relações estratégicas de mercado que ajudam oportunidades a avançarem.',
				],
				'capabilities' => [
					'eyebrow'     => 'Capacidades',
					'title'       => 'Uma abordagem clara e orientada a negócios para apoiar o comércio global.',
					'description' => 'Cada capacidade foi pensada para fortalecer conversas comerciais internacionais e sua execução.',
					'items'       => [
						['title' => 'Sourcing Internacional', 'description' => 'Conectar demanda a oportunidades relevantes de oferta nos mercados certos.'],
						['title' => 'Coordenação de Trading Global', 'description' => 'Apoiar conversas comerciais estruturadas entre contrapartes internacionais.'],
						['title' => 'Suporte em Business Development', 'description' => 'Ajudar a criar visibilidade de mercado e introduções qualificadas com potencial de longo prazo.'],
						['title' => 'Construção de Relacionamentos Comerciais', 'description' => 'Fortalecer o alinhamento entre compradores e exportadores por meio de comunicação disciplinada e confiança.'],
						['title' => 'Coordenação de Supply Chain', 'description' => 'Levar consciência prática de timing, fluxo e expectativa de mercado para decisões comerciais.'],
						['title' => 'Conexões Estratégicas de Mercado', 'description' => 'Ligar empresas aos ambientes comerciais e relacionamentos mais adequados.'],
					],
				],
				'process' => [
					'eyebrow'     => 'Como Trabalhamos',
					'title'       => 'Um caminho estruturado do interesse comercial à oportunidade séria.',
					'description' => 'O processo foi pensado para reduzir atritos e elevar a qualidade das conversas de comércio internacional.',
					'steps'       => [
						['title' => 'Entender a Necessidade de Negócio', 'description' => 'Clarificar objetivos, contexto de mercado e prioridades comerciais.'],
						['title' => 'Alinhar o Relacionamento de Mercado Certo', 'description' => 'Conectar a oportunidade com compradores, exportadores ou contrapartes relevantes.'],
						['title' => 'Apoiar um Progresso Credível', 'description' => 'Fazer a conversa avançar com coordenação, seriedade e continuidade.'],
					],
				],
				'expertise' => [
					'title'       => 'Experiência setorial fortalece a execução.',
					'description' => 'Alho e commodities agrícolas exigem disciplina comercial, entendimento do produto e coordenação confiável.',
					'bullets'     => [
						'Conhecimento focado do mercado de alho',
						'Visão estratégica de commodities agrícolas',
						'Coordenação internacional orientada por relacionamento',
					],
				],
				'cta' => [
					'title'       => 'Converse sobre a solução comercial mais adequada para o seu objetivo de mercado.',
					'description' => 'A Unyra está pronta para dialogar sobre sourcing, oportunidades para compradores, exportadores e parcerias estratégicas.',
				],
			],
			'buyers' => [
				'hero' => [
					'eyebrow'     => 'Para Compradores',
					'title'       => 'Uma ponte comercial confiável para compradores, importadores, distribuidores e parceiros sérios.',
					'description' => 'A Unyra apoia compradores por meio de sourcing estruturado, gestão internacional de relacionamentos e coordenação comercial clara.',
				],
				'priorities' => [
					'eyebrow'     => 'Prioridades do Comprador',
					'title'       => 'O que compradores sérios precisam de um parceiro internacional.',
					'description' => 'O valor não está apenas no acesso. Está em clareza, confiabilidade e coordenação comercial inteligente.',
					'items'       => [
						['title' => 'Conexões Confiáveis de Sourcing', 'description' => 'Contrapartes relevantes apoiadas por relações de mercado disciplinadas.'],
						['title' => 'Entendimento de Mercado', 'description' => 'Contexto setorial e visão internacional ajudam a reduzir atritos nas decisões-chave.'],
						['title' => 'Coordenação Comercial', 'description' => 'Um processo mais estruturado para fazer oportunidades sérias avançarem.'],
						['title' => 'Geração de Valor de Longo Prazo', 'description' => 'Execução orientada a parceria, e não a transações de curto prazo.'],
					],
				],
				'approach' => [
					'eyebrow'     => 'Como a Unyra Ajuda',
					'title'       => 'Valor para compradores construído sobre confiabilidade e qualidade de relacionamento.',
					'description' => 'A Unyra foi desenhada para apoiar compradores comercialmente sérios que valorizam confiança e coordenação estruturada.',
					'bullets'     => [
						'Gestão confiável de relacionamentos internacionais',
						'Comunicação comercialmente disciplinada',
						'Conversas estratégicas de sourcing com visão de longo prazo',
					],
				],
				'form_panel' => [
					'title'       => 'Conte o que você compra e que tipo de relacionamento deseja construir.',
					'description' => 'Compartilhe seu foco de mercado, região e prioridades de sourcing para avaliarmos o próximo passo mais adequado.',
				],
			],
			'producers' => [
				'hero' => [
					'eyebrow'     => 'Para Produtores e Exportadores',
					'title'       => 'Apoio para produtores e exportadores que buscam ampliar visibilidade internacional e acesso a compradores.',
					'description' => 'A Unyra ajuda produtores-exportadores a se conectarem com compradores relevantes, fortalecerem sua presença comercial e buscarem crescimento de longo prazo.',
				],
				'priorities' => [
					'eyebrow'     => 'Prioridades do Exportador',
					'title'       => 'O que produtores-exportadores sérios precisam para crescer internacionalmente.',
					'description' => 'Progresso comercial vem do relacionamento certo com o mercado, e não apenas de exposição.',
					'items'       => [
						['title' => 'Acesso a Compradores Internacionais', 'description' => 'Apoio para abrir caminhos comerciais relevantes além da rede atual.'],
						['title' => 'Visibilidade Comercial', 'description' => 'Melhor posicionamento para oportunidades que exigem maior alcance internacional.'],
						['title' => 'Conexões Estratégicas', 'description' => 'Construção de relações que apoiam discussões qualificadas e aderência comercial real.'],
						['title' => 'Crescimento Comercial de Longo Prazo', 'description' => 'Foco em continuidade e valor, e não em volume transacional de curto prazo.'],
					],
				],
				'approach' => [
					'eyebrow'     => 'Como a Unyra Ajuda',
					'title'       => 'Apoio ao exportador moldado por acesso de mercado e profundidade de relacionamento.',
					'description' => 'O objetivo é ajudar produtores e exportadores credíveis a construírem oportunidades comerciais mais fortes em mercados relevantes.',
					'bullets'     => [
						'Apoio para ampliar acesso a compradores',
						'Business development alinhado a oportunidades reais',
						'Construção de relacionamentos comerciais duradouros',
					],
				],
				'form_panel' => [
					'title'       => 'Conte o que você produz, onde deseja crescer e como pretende expandir.',
					'description' => 'Compartilhe seu foco de produto, mercados atuais e objetivos internacionais para avaliarmos um próximo passo qualificado.',
				],
			],
			'contact' => [
				'hero' => [
					'eyebrow'     => 'Contato',
					'title'       => 'Inicie uma conversa de negócios séria com a Unyra Group LLC.',
					'description' => 'Se a oportunidade está ligada ao lado comprador, ao lado exportador ou a uma parceria estratégica, nossa equipe está posicionada para avaliar e responder.',
				],
				'response' => [
					'title'       => 'O que esperar depois do seu contato.',
					'description' => 'Sua mensagem é analisada com foco comercial e direcionada conforme relevância de mercado e potencial de próximo passo.',
					'bullets'     => [
						'Revisão do seu contexto de negócio e prioridades',
						'Avaliação do caminho de mercado ou relacionamento mais adequado',
						'Retorno com a conversa mais relevante para o próximo passo',
					],
				],
			],
			'privacy' => [
				'hero' => [
					'eyebrow'     => 'Política de Privacidade',
					'title'       => 'Como a Unyra Group LLC trata consultas do site e informações enviadas.',
					'description' => 'Esta política explica, em termos gerais, como informações enviadas por este website podem ser coletadas, utilizadas e armazenadas.',
				],
				'sections' => [
					['title' => 'Informações Coletadas', 'paragraphs' => ['Podemos coletar as informações enviadas em formulários de contato, incluindo nome, empresa, e-mail, telefone, país, papel comercial, interesse e conteúdo da mensagem.', 'Também podemos receber informações técnicas limitadas necessárias para operação e segurança do site.']],
					['title' => 'Como as Informações Podem Ser Utilizadas', 'paragraphs' => ['As informações enviadas podem ser utilizadas para revisar sua consulta, responder à sua solicitação, avaliar relevância comercial e dar continuidade à comunicação relacionada ao assunto informado.', 'Este website é voltado a propósitos empresariais e de comércio internacional.']],
					['title' => 'Compartilhamento de Informações', 'paragraphs' => ['As informações não são vendidas. Elas podem ser compartilhadas internamente ou com prestadores de serviço apenas quando necessário para operar o site, processar consultas ou apoiar comunicação comercial.', 'As informações também podem ser divulgadas quando exigidas por lei ou para proteger interesses comerciais legítimos.']],
					['title' => 'Retenção e Segurança', 'paragraphs' => ['As informações podem ser mantidas pelo período razoavelmente necessário para gestão de consultas, relacionamentos comerciais e registros operacionais.', 'Medidas administrativas e técnicas razoáveis podem ser utilizadas para reduzir acesso não autorizado, uso indevido ou perda.']],
					['title' => 'Contato', 'paragraphs' => ['Se tiver dúvidas sobre privacidade ou sobre informações enviadas por este site, entre em contato com a Unyra Group LLC usando os dados disponíveis na página de contato.']],
				],
			],
			'thank_you' => [
				'eyebrow'     => 'Obrigado',
				'title'       => 'Sua consulta foi recebida.',
				'description' => 'Obrigado por entrar em contato com a Unyra Group LLC. Nossa equipe analisará sua mensagem e retornará com o próximo passo mais adequado.',
				'primary'     => 'Voltar para o início',
				'secondary'   => 'Página de contato',
			],
		],
		'es' => [
			'labels' => [
				'site_title'        => 'Unyra Group LLC',
				'skip_to_content'   => 'Ir al contenido principal',
				'language'          => 'Idioma',
				'nav'               => [
					'home'      => 'Inicio',
					'about'     => 'Nosotros',
					'markets'   => 'Mercados y Red Global',
					'solutions' => 'Soluciones',
					'buyers'    => 'Para Compradores',
					'producers' => 'Para Productores y Exportadores',
					'contact'   => 'Contacto',
					'privacy'   => 'Política de Privacidad',
				],
				'primary_cta'       => 'Solicitar una Consulta Comercial',
				'secondary_cta'     => 'Hablar con Nuestro Equipo',
				'sticky_cta'        => 'Iniciar una Conversación',
				'tagline'           => 'Conectando Mercados. Construyendo Confianza. Generando Valor.',
				'footer_summary'    => 'Empresa global especializada en conectar compradores y productores-exportadores en todo el mundo, especialmente en el mercado del ajo y en commodities agrícolas.',
				'footer_navigation' => 'Navegación',
				'footer_contact'    => 'Contacto',
				'privacy_note'      => '¿Dudas sobre privacidad o información enviada?',
				'footer_launch'     => 'Póngase en contacto con nuestro equipo si tiene preguntas sobre privacidad o sobre información enviada a través de este sitio web.',
				'back_home'         => 'Volver al inicio',
			],
			'contact_labels' => [
				'email'    => 'Correo',
				'sales'    => 'Correo Comercial',
				'phone'    => 'Teléfono / WhatsApp',
				'location' => 'Ubicación Comercial',
			],
			'form' => [
				'badge'          => 'Consulta Comercial Calificada',
				'title'          => 'Inicie una conversación comercial enfocada',
				'description'    => 'Comparta el perfil de su empresa, su interés de mercado y sus prioridades comerciales. Revisaremos su mensaje y definiremos el siguiente paso adecuado.',
				'submit'         => 'Enviar Consulta',
				'sending'        => 'Enviando...',
				'success'        => 'Su consulta fue enviada con éxito. Estamos preparando el siguiente paso.',
				'error'          => 'No pudimos enviar su consulta en este momento. Inténtelo nuevamente.',
				'privacy_note'   => 'Al enviar este formulario, usted acepta ser contactado respecto de su consulta y reconoce la política de privacidad.',
				'honeypot'       => 'Deje este campo vacío',
				'fields'         => [
					'full_name' => 'Nombre Completo',
					'company'   => 'Empresa',
					'email'     => 'Correo',
					'phone'     => 'Teléfono / WhatsApp',
					'country'   => 'País',
					'role'      => 'Yo soy...',
					'interest'  => 'Interés',
					'message'   => 'Mensaje',
				],
				'placeholders'   => [
					'full_name' => 'Su nombre completo',
					'company'   => 'Su empresa',
					'email'     => 'nombre@empresa.com',
					'phone'     => '+34...',
					'country'   => 'País',
					'message'   => 'Describa brevemente su empresa, su enfoque de mercado y qué desea conversar.',
				],
				'role_options'   => [
					'buyer'              => 'Comprador',
					'producer-exporter'  => 'Productor-Exportador',
					'distributor'        => 'Distribuidor',
					'other'              => 'Otro',
				],
				'interest_options' => [
					'garlic'                   => 'Ajo',
					'agricultural-commodities' => 'Commodities Agrícolas',
					'strategic-partnership'    => 'Alianza Estratégica',
					'other'                    => 'Otro',
				],
			],
			'home' => [
				'hero' => [
					'eyebrow'      => 'Trading global | Mercado del ajo | Commodities agrícolas | Más de 20 años de experiencia',
					'title'        => 'Un socio internacional de alto nivel que conecta compradores y productores-exportadores en mercados globales.',
					'description'  => 'Unyra Group LLC conecta oferta y demanda con claridad comercial, coordinación estratégica y visión de largo plazo en Estados Unidos, Canadá, Brasil, Chile, Argentina, Egipto, Turquía, Europa y China.',
					'experience'   => 'Más de 20 años en el mercado del ajo y en commodities agrícolas',
					'market_line'  => 'Conectando oportunidades en Estados Unidos, Canadá, Brasil, Chile, Argentina, Egipto, Turquía, Europa y China.',
					'primary_cta'  => 'Solicitar una Consulta Comercial',
					'secondary_cta'=> 'Convertirse en Socio Comercial',
					'panel_title'  => 'Puente estratégico entre oferta y demanda',
					'panel_text'   => 'Coordinación comercial respaldada por conocimiento sectorial, comunicación disciplinada y relaciones internacionales de confianza.',
					'highlights'   => [
						'Conectividad global entre compradores y exportadores',
						'Posicionamiento comercial ejecutivo',
						'Enfoque confiable en relaciones de largo plazo',
					],
					'panel_cards'  => [
						['eyebrow' => 'Experiencia', 'title' => 'Más de 20 años de perspectiva sectorial'],
						['eyebrow' => 'Mercados', 'title' => 'Américas, Europa, Egipto, Turquía y China'],
					],
				],
				'trust' => [
					['title' => '20+ Años de Experiencia de Mercado', 'description' => 'Base construida sobre una trayectoria sólida en el mercado del ajo y en commodities agrícolas.'],
					['title' => 'Especialización en Ajo y Commodities', 'description' => 'Visión enfocada sobre la dinámica agrícola, los orígenes, las exigencias de compra y las oportunidades comerciales.'],
					['title' => 'Conexión Global entre Compradores y Exportadores', 'description' => 'Posicionamiento orientado a conectar contrapartes serias en distintos mercados internacionales.'],
					['title' => 'Alcance Estratégico Internacional', 'description' => 'Actuación comercial relevante en Norteamérica, Sudamérica, Europa, Medio Oriente y China.'],
				],
				'about' => [
					'eyebrow'     => 'Sobre Unyra',
					'title'       => 'Una empresa experimentada, creada para conectar mercados con seriedad, continuidad e inteligencia comercial.',
					'description' => 'Unyra Group LLC actúa como puente estratégico entre compradores y productores-exportadores, ayudando a estructurar relaciones valiosas en el comercio internacional.',
					'paragraphs'  => [
						'Más de 20 años de experiencia marcan diferencia porque el comercio agrícola depende de timing, confianza, coordinación y comprensión clara de las contrapartes.',
						'Unyra reúne un enfoque sereno y disciplinado para business development, coordinación comercial y conectividad de mercado, ayudando a que las oportunidades avancen con credibilidad.',
					],
					'markers'     => [
						'Visión global con mentalidad orientada a relaciones',
						'Especialización en ajo y commodities agrícolas',
						'Posicionamiento comercial pensado para generar leads calificados',
					],
				],
				'solutions' => [
					'eyebrow'     => 'Qué Hacemos',
					'title'       => 'Capacidades comerciales diseñadas para la ejecución real en el comercio internacional.',
					'description' => 'Unyra ayuda a que oportunidades relevantes avancen con claridad, coordinación e inteligencia comercial.',
					'items'       => [
						['title' => 'Trading Global', 'description' => 'Coordinación de oportunidades internacionales con disciplina y visión comercial.'],
						['title' => 'Sourcing Internacional', 'description' => 'Conexión entre compradores y productores-exportadores calificados en mercados relevantes.'],
						['title' => 'Business Development', 'description' => 'Apertura de conversaciones y caminos de crecimiento con valor comercial de largo plazo.'],
						['title' => 'Coordinación Comercial', 'description' => 'Alineación de contrapartes, prioridades y comunicación para que las oportunidades avancen con consistencia.'],
						['title' => 'Coordinación de Supply Chain', 'description' => 'Apoyo a las discusiones comerciales con conciencia práctica de timing, flujo y realidad de mercado.'],
						['title' => 'Conexiones Estratégicas de Mercado', 'description' => 'Vínculo entre oferta y demanda en mercados donde las relaciones de confianza marcan diferencia.'],
					],
				],
				'expertise' => [
					'eyebrow'     => 'Especialización Sectorial',
					'title'       => 'Conocimiento especializado en ajo y commodities agrícolas.',
					'description' => 'Una comprensión profunda del sector ayuda a reducir fricciones, fortalecer el diálogo y crear oportunidades comerciales más consistentes.',
					'pillars'     => [
						['title' => 'Mercado del Ajo', 'description' => 'Experiencia construida durante años de observación de mercado, interacción comercial y entendimiento específico del producto.'],
						['title' => 'Commodities Agrícolas', 'description' => 'Visión más amplia del comercio de commodities apoyada por conexiones estratégicas y coordinación disciplinada.'],
					],
					'aside_title' => 'Valor de largo plazo en el comercio internacional',
					'aside_text'  => 'Unyra trabaja con perspectiva internacional, seriedad comercial y ejecución orientada por relaciones duraderas.',
				],
				'network' => [
					'eyebrow'     => 'Mercados y Red Global',
					'title'       => 'Una red comercial activa en regiones estratégicas del comercio internacional.',
					'description' => 'Unyra conecta oportunidades en entornos comerciales consolidados y estratégicos, donde la experiencia, el timing y la confianza hacen diferencia.',
					'cards'       => [
						['key' => 'united-states', 'title' => 'Estados Unidos', 'description' => 'Mercado estratégico para relaciones de demanda, sourcing y coordinación comercial de largo plazo.'],
						['key' => 'canada', 'title' => 'Canadá', 'description' => 'Entorno relevante para importadores, distribuidores y oportunidades estructuradas en comercio agrícola.'],
						['key' => 'brazil', 'title' => 'Brasil', 'description' => 'Punto de referencia regional para relaciones con compradores, visibilidad de productores y conectividad comercial.'],
						['key' => 'chile', 'title' => 'Chile', 'description' => 'Mercado importante en Sudamérica para desarrollo comercial orientado a la exportación.'],
						['key' => 'argentina', 'title' => 'Argentina', 'description' => 'Mercado donde el conocimiento agrícola y las relaciones comerciales sólidas siguen siendo esenciales.'],
						['key' => 'egypt', 'title' => 'Egipto', 'description' => 'Origen y punto de conexión relevante en flujos internacionales de commodities.'],
						['key' => 'turkey', 'title' => 'Turquía', 'description' => 'Puente estratégico entre oportunidades regionales y conectividad internacional más amplia.'],
						['key' => 'europe', 'title' => 'Europa', 'description' => 'Entorno comercial maduro donde la confianza, el profesionalismo y la coordinación disciplinada son fundamentales.'],
						['key' => 'china', 'title' => 'China', 'description' => 'Referencia central en el comercio agrícola global y en conversaciones estratégicas de sourcing.'],
					],
				],
				'audiences' => [
					'eyebrow'     => 'Dos Caminos Comerciales',
					'title'       => 'Preparada para compradores y para productores-exportadores.',
					'description' => 'La misma disciplina de mercado se adapta a las necesidades de ambos lados de la relación comercial.',
					'cards'       => [
						[
							'key'         => 'buyers',
							'eyebrow'     => 'Para Compradores',
							'title'       => 'Acceso estructurado a conversaciones confiables de sourcing internacional.',
							'description' => 'Para importadores, distribuidores y socios comerciales que buscan seriedad, visión de mercado y coordinación confiable.',
							'bullets'     => ['Relaciones confiables de sourcing', 'Claridad comercial', 'Coordinación internacional consistente'],
							'cta'         => 'Conocer el camino del comprador',
						],
						[
							'key'         => 'producers',
							'eyebrow'     => 'Para Productores y Exportadores',
							'title'       => 'Apoyo para ampliar visibilidad y acceso a compradores internacionales.',
							'description' => 'Para productores y exportadores que desean construir relaciones calificadas y abrir oportunidades relevantes en nuevos mercados.',
							'bullets'     => ['Acceso a contrapartes internacionales', 'Apoyo en business development', 'Construcción de relaciones duraderas'],
							'cta'         => 'Conocer el camino del exportador',
						],
					],
				],
				'why' => [
					'eyebrow'     => 'Por Qué Unyra',
					'title'       => 'Por qué empresas serias eligen trabajar con Unyra.',
					'description' => 'El valor se construye a partir de experiencia, visión internacional, coordinación disciplinada y relaciones comerciales de confianza.',
					'items'       => [
						['title' => 'Experiencia', 'description' => 'Más de 20 años de visión práctica en el mercado del ajo y en commodities agrícolas.'],
						['title' => 'Entendimiento de Mercado', 'description' => 'Claridad sobre cómo deben alinearse contrapartes, prioridades y realidades comerciales.'],
						['title' => 'Conexiones Internacionales', 'description' => 'Actuación en mercados relevantes de las Américas, Europa, Medio Oriente y China.'],
						['title' => 'Coordinación Confiable', 'description' => 'Comunicación estructurada y seguimiento disciplinado en conversaciones de negocio.'],
						['title' => 'Alianzas de Largo Plazo', 'description' => 'Ejecución orientada por relación y continuidad, no por transacciones puntuales.'],
						['title' => 'Visión Estratégica', 'description' => 'Un enfoque comercial fuerte, sereno y premium para el comercio internacional.'],
					],
				],
				'cta' => [
					'title'       => 'Abra la conversación correcta para su próxima oportunidad de negocio.',
					'description' => 'Si está comprando, buscando origen, exportando o desarrollando alianzas, Unyra está posicionada para conectar la oportunidad con la relación de mercado adecuada.',
					'primary'     => 'Solicitar una Consulta Comercial',
					'secondary'   => 'Para Compradores',
				],
				'lead' => [
					'eyebrow'     => 'Consulta Comercial Calificada',
					'title'       => 'Inicie una conversación comercial directa con Unyra.',
					'description' => 'Comparta su contexto de mercado, el perfil de su empresa y lo que desea conversar. Nuestro equipo evaluará el mensaje y definirá el siguiente paso adecuado.',
					'bullets'     => [
						'Pensado para captar leads calificados de comercio internacional',
						'Preparado para compradores, distribuidores, productores y exportadores',
						'Diseñado para una conversión seria con baja fricción',
					],
				],
			],
			'about' => [
				'hero' => [
					'eyebrow'     => 'Sobre Unyra',
					'title'       => 'Una empresa internacional experimentada que conecta mercados con confianza y continuidad.',
					'description' => 'Unyra Group LLC actúa como puente estratégico entre compradores y productores-exportadores, apoyando oportunidades comercialmente serias en ajo y commodities agrícolas.',
				],
				'overview' => [
					'eyebrow'     => 'Quiénes Somos',
					'title'       => 'Una empresa orientada por relaciones y por una visión internacional del comercio.',
					'description' => 'Unyra combina entendimiento de mercado, disciplina comercial y visión de largo plazo.',
					'paragraphs'  => [
						'La empresa está posicionada para conectar oferta y demanda mediante conversaciones confiables, coordinación cuidadosa y relevancia comercial.',
						'Su valor nace de combinar familiaridad sectorial, conectividad internacional y ejecución comercial consistente.',
					],
				],
				'values' => [
					'eyebrow'     => 'Lo Que Representamos',
					'title'       => 'Confianza, continuidad y relaciones comerciales creíbles.',
					'description' => 'Unyra fue construida sobre conducta comercial estable y creación de valor duradera en el comercio internacional.',
					'items'       => [
						['title' => 'Confianza', 'description' => 'Las relaciones de negocio avanzan mejor cuando están respaldadas por consistencia y credibilidad.'],
						['title' => 'Continuidad', 'description' => 'La visión de largo plazo importa en mercados donde la confiabilidad define la oportunidad.'],
						['title' => 'Inteligencia Comercial', 'description' => 'Una buena coordinación depende de leer el mercado, el timing y las contrapartes con claridad.'],
					],
				],
				'experience' => [
					'eyebrow'     => 'Más de 20 Años de Experiencia',
					'title'       => 'Experiencia sectorial que fortalece decisiones y conversaciones de mercado.',
					'description' => 'Más de dos décadas en ajo y commodities agrícolas ayudan a Unyra a apoyar conversaciones serias con madurez y visión comercial.',
					'pillars'     => [
						['title' => 'Perspectiva Sectorial', 'description' => 'La experiencia ayuda a entender qué importa, qué genera fricción y cómo debe abordarse la oportunidad.'],
						['title' => 'Disciplina Comercial', 'description' => 'La coordinación estructurada favorece una mejor comunicación y mayor continuidad de negocio.'],
						['title' => 'Profundidad de Relación', 'description' => 'El comercio internacional funciona mejor cuando la confianza y el timing se manejan con profesionalismo.'],
					],
					'timeline'    => [
						'Más de 20 años vinculados al mercado del ajo y a las commodities agrícolas',
						'Foco estratégico en conectar compradores y productores-exportadores',
						'Ejecución orientada por relación y realidad de negocios internacionales',
					],
				],
				'relationships' => [
					'title'       => 'Construida para confianza, continuidad y valor comercial de largo plazo.',
					'description' => 'Unyra trabaja para ayudar a que relaciones calificadas se vuelvan comercialmente sostenibles e internacionalmente relevantes.',
					'bullets'     => [
						'Coordinación de mercado estructurada y seria',
						'Perspectiva internacional de comercio',
						'Construcción de relaciones duraderas',
						'Enfoque en encaje comercial valioso',
					],
				],
				'cta' => [
					'title'       => 'Inicie una conversación con una empresa preparada para relaciones comerciales internacionales duraderas.',
					'description' => 'Si busca experiencia de mercado, coordinación comercial y un puente más fuerte entre oferta y demanda, Unyra está lista para conversar.',
				],
			],
			'markets' => [
				'hero' => [
					'eyebrow'     => 'Mercados y Red Global',
					'title'       => 'Una red comercial global que conecta oferta, demanda y oportunidad.',
					'description' => 'Unyra actúa como puente entre relaciones comerciales en Estados Unidos, Canadá, Brasil, Chile, Argentina, Egipto, Turquía, Europa y China.',
				],
				'connectivity' => [
					'eyebrow'     => 'Conectividad Global',
					'title'       => 'Conectando oportunidades comerciales en distintos entornos de mercado.',
					'description' => 'El comercio internacional exige más que alcance. Exige timing, confianza y coordinación comercial inteligente.',
					'items'       => [
						['title' => 'Perspectiva Multimercado', 'description' => 'Comprender la lógica comercial de diferentes regiones ayuda a alinear contrapartes con mayor eficiencia.'],
						['title' => 'Puente entre Oferta y Demanda', 'description' => 'Unyra ayuda a conectar oportunidades relevantes donde las necesidades de los compradores y las capacidades de los exportadores pueden encontrarse.'],
						['title' => 'Acceso Basado en Relaciones', 'description' => 'Las oportunidades internacionales creíbles se construyen mediante confianza y tiempo.'],
					],
				],
				'opportunity' => [
					'title'       => 'Posicionada para conectar oportunidades en corredores estratégicos del comercio internacional.',
					'description' => 'La orientación global de la empresa apoya conversaciones comercialmente relevantes en mercados maduros, emergentes e interregionales.',
					'bullets'     => [
						'Norteamérica y Sudamérica',
						'Europa, Egipto y Turquía',
						'China y flujos globales de sourcing',
					],
				],
				'cta' => [
					'title'       => 'Converse sobre cómo su oportunidad encaja en la red global de Unyra.',
					'description' => 'Póngase en contacto para explorar oportunidades del lado comprador, del lado exportador o de alianza estratégica.',
				],
			],
			'solutions' => [
				'hero' => [
					'eyebrow'     => 'Soluciones',
					'title'       => 'Capacidades comerciales diseñadas para una ejecución seria en el comercio internacional.',
					'description' => 'El papel de Unyra está basado en sourcing, coordinación y relaciones estratégicas de mercado que ayudan a que las oportunidades avancen.',
				],
				'capabilities' => [
					'eyebrow'     => 'Capacidades',
					'title'       => 'Un enfoque claro y orientado al negocio para apoyar el comercio global.',
					'description' => 'Cada capacidad fue pensada para fortalecer conversaciones comerciales internacionales y su ejecución.',
					'items'       => [
						['title' => 'Sourcing Internacional', 'description' => 'Conectar demanda con oportunidades relevantes de oferta en los mercados adecuados.'],
						['title' => 'Coordinación de Trading Global', 'description' => 'Apoyar conversaciones comerciales estructuradas entre contrapartes internacionales.'],
						['title' => 'Soporte en Business Development', 'description' => 'Ayudar a crear visibilidad de mercado e introducciones calificadas con potencial de largo plazo.'],
						['title' => 'Construcción de Relaciones Comerciales', 'description' => 'Fortalecer el alineamiento entre compradores y exportadores mediante comunicación disciplinada y confianza.'],
						['title' => 'Coordinación de Supply Chain', 'description' => 'Aportar conciencia práctica de timing, flujo y expectativas de mercado a las decisiones comerciales.'],
						['title' => 'Conexiones Estratégicas de Mercado', 'description' => 'Vincular empresas con los entornos comerciales y relaciones más adecuados.'],
					],
				],
				'process' => [
					'eyebrow'     => 'Cómo Trabajamos',
					'title'       => 'Un camino estructurado desde el interés comercial hasta la oportunidad seria.',
					'description' => 'El proceso fue diseñado para reducir fricciones y elevar la calidad de las conversaciones de comercio internacional.',
					'steps'       => [
						['title' => 'Entender la Necesidad de Negocio', 'description' => 'Clarificar objetivos, contexto de mercado y prioridades comerciales.'],
						['title' => 'Alinear la Relación de Mercado Correcta', 'description' => 'Conectar la oportunidad con compradores, exportadores o contrapartes relevantes.'],
						['title' => 'Apoyar un Progreso Creíble', 'description' => 'Hacer avanzar la conversación con coordinación, seriedad y continuidad.'],
					],
				],
				'expertise' => [
					'title'       => 'La experiencia sectorial fortalece la ejecución.',
					'description' => 'Ajo y commodities agrícolas exigen disciplina comercial, entendimiento del producto y coordinación confiable.',
					'bullets'     => [
						'Conocimiento enfocado del mercado del ajo',
						'Visión estratégica de commodities agrícolas',
						'Coordinación internacional orientada por relaciones',
					],
				],
				'cta' => [
					'title'       => 'Converse sobre la solución comercial más adecuada para su objetivo de mercado.',
					'description' => 'Unyra está preparada para dialogar sobre sourcing, oportunidades para compradores, exportadores y alianzas estratégicas.',
				],
			],
			'buyers' => [
				'hero' => [
					'eyebrow'     => 'Para Compradores',
					'title'       => 'Un puente comercial confiable para compradores, importadores, distribuidores y socios serios.',
					'description' => 'Unyra apoya a compradores mediante sourcing estructurado, gestión internacional de relaciones y coordinación comercial clara.',
				],
				'priorities' => [
					'eyebrow'     => 'Prioridades del Comprador',
					'title'       => 'Lo que los compradores serios necesitan de un socio internacional.',
					'description' => 'El valor no está solo en el acceso. Está en la claridad, la confiabilidad y la coordinación comercial inteligente.',
					'items'       => [
						['title' => 'Conexiones Confiables de Sourcing', 'description' => 'Contrapartes relevantes respaldadas por relaciones de mercado disciplinadas.'],
						['title' => 'Entendimiento de Mercado', 'description' => 'Contexto sectorial y visión internacional ayudan a reducir fricciones en decisiones clave.'],
						['title' => 'Coordinación Comercial', 'description' => 'Un proceso más estructurado para hacer avanzar oportunidades serias.'],
						['title' => 'Generación de Valor de Largo Plazo', 'description' => 'Ejecución orientada a alianza, no a transacciones de corto plazo.'],
					],
				],
				'approach' => [
					'eyebrow'     => 'Cómo Ayuda Unyra',
					'title'       => 'Valor para compradores construido sobre confiabilidad y calidad de relación.',
					'description' => 'Unyra fue diseñada para apoyar a compradores comercialmente serios que valoran confianza y coordinación estructurada.',
					'bullets'     => [
						'Gestión confiable de relaciones internacionales',
						'Comunicación comercialmente disciplinada',
						'Conversaciones estratégicas de sourcing con visión de largo plazo',
					],
				],
				'form_panel' => [
					'title'       => 'Cuéntenos qué compra y qué tipo de relación desea construir.',
					'description' => 'Comparta su foco de mercado, región y prioridades de sourcing para evaluar el siguiente paso adecuado.',
				],
			],
			'producers' => [
				'hero' => [
					'eyebrow'     => 'Para Productores y Exportadores',
					'title'       => 'Apoyo para productores y exportadores que buscan ampliar visibilidad internacional y acceso a compradores.',
					'description' => 'Unyra ayuda a productores-exportadores a conectarse con compradores relevantes, fortalecer su presencia comercial y buscar crecimiento de largo plazo.',
				],
				'priorities' => [
					'eyebrow'     => 'Prioridades del Exportador',
					'title'       => 'Lo que productores-exportadores serios necesitan para crecer internacionalmente.',
					'description' => 'El progreso comercial surge de la relación correcta con el mercado, no solo de la exposición.',
					'items'       => [
						['title' => 'Acceso a Compradores Internacionales', 'description' => 'Apoyo para abrir caminos comerciales relevantes más allá de la red actual.'],
						['title' => 'Visibilidad Comercial', 'description' => 'Mejor posicionamiento para oportunidades que exigen mayor alcance internacional.'],
						['title' => 'Conexiones Estratégicas', 'description' => 'Construcción de relaciones que apoyan discusiones calificadas y encaje comercial real.'],
						['title' => 'Crecimiento Comercial de Largo Plazo', 'description' => 'Enfoque en continuidad y valor, no en volumen transaccional de corto plazo.'],
					],
				],
				'approach' => [
					'eyebrow'     => 'Cómo Ayuda Unyra',
					'title'       => 'Apoyo al exportador moldeado por acceso de mercado y profundidad de relación.',
					'description' => 'El objetivo es ayudar a productores y exportadores creíbles a construir oportunidades comerciales más fuertes en mercados relevantes.',
					'bullets'     => [
						'Apoyo para ampliar acceso a compradores',
						'Business development alineado con oportunidades reales',
						'Construcción de relaciones comerciales duraderas',
					],
				],
				'form_panel' => [
					'title'       => 'Cuéntenos qué produce, dónde desea crecer y cómo quiere expandirse.',
					'description' => 'Comparta su foco de producto, mercados actuales y objetivos internacionales para evaluar un siguiente paso calificado.',
				],
			],
			'contact' => [
				'hero' => [
					'eyebrow'     => 'Contacto',
					'title'       => 'Inicie una conversación de negocios seria con Unyra Group LLC.',
					'description' => 'Si la oportunidad está vinculada al lado comprador, al lado exportador o a una alianza estratégica, nuestro equipo está preparado para evaluar y responder.',
				],
				'response' => [
					'title'       => 'Qué esperar después de su contacto.',
					'description' => 'Su mensaje se analiza con enfoque comercial y se dirige según relevancia de mercado y potencial de siguiente paso.',
					'bullets'     => [
						'Revisión de su contexto de negocio y prioridades',
						'Evaluación del camino de mercado o relación más adecuada',
						'Respuesta con la conversación más relevante para el siguiente paso',
					],
				],
			],
			'privacy' => [
				'hero' => [
					'eyebrow'     => 'Política de Privacidad',
					'title'       => 'Cómo Unyra Group LLC gestiona consultas del sitio e información enviada.',
					'description' => 'Esta política explica, en términos generales, cómo la información enviada a través de este sitio web puede ser recopilada, utilizada y almacenada.',
				],
				'sections' => [
					['title' => 'Información Recopilada', 'paragraphs' => ['Podemos recopilar la información enviada en formularios de contacto, incluyendo nombre, empresa, correo, teléfono, país, rol comercial, interés y contenido del mensaje.', 'También podemos recibir información técnica limitada necesaria para la operación y seguridad del sitio.']],
					['title' => 'Cómo Puede Utilizarse la Información', 'paragraphs' => ['La información enviada puede utilizarse para revisar su consulta, responder a su solicitud, evaluar relevancia comercial y dar continuidad a la comunicación relacionada con el asunto informado.', 'Este sitio está orientado a propósitos empresariales y de comercio internacional.']],
					['title' => 'Compartición de Información', 'paragraphs' => ['La información no se vende. Puede compartirse internamente o con prestadores de servicio solo cuando sea necesario para operar el sitio, procesar consultas o apoyar comunicación comercial.', 'La información también puede divulgarse cuando sea exigida por ley o para proteger intereses comerciales legítimos.']],
					['title' => 'Retención y Seguridad', 'paragraphs' => ['La información puede conservarse durante el tiempo razonablemente necesario para la gestión de consultas, relaciones comerciales y registros operativos.', 'Pueden utilizarse medidas administrativas y técnicas razonables para reducir acceso no autorizado, uso indebido o pérdida.']],
					['title' => 'Contacto', 'paragraphs' => ['Si tiene preguntas sobre privacidad o sobre información enviada a través de este sitio, póngase en contacto con Unyra Group LLC utilizando los datos disponibles en la página de contacto.']],
				],
			],
			'thank_you' => [
				'eyebrow'     => 'Gracias',
				'title'       => 'Su consulta ha sido recibida.',
				'description' => 'Gracias por contactar a Unyra Group LLC. Nuestro equipo revisará su mensaje y responderá con el siguiente paso más adecuado.',
				'primary'     => 'Volver al inicio',
				'secondary'   => 'Página de contacto',
			],
		],
	];
}
