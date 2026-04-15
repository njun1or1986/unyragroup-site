<?php

if (!defined('ABSPATH')) {
	exit;
}

function unyra_render_page($page_key, $locale, $dict) {
	switch ($page_key) {
		case 'home':
			unyra_render_home_page($locale, $dict);
			break;
		case 'about':
			unyra_render_about_page($locale, $dict);
			break;
		case 'markets':
			unyra_render_markets_page($locale, $dict);
			break;
		case 'solutions':
			unyra_render_solutions_page($locale, $dict);
			break;
		case 'buyers':
			unyra_render_buyers_page($locale, $dict);
			break;
		case 'producers':
			unyra_render_producers_page($locale, $dict);
			break;
		case 'contact':
			unyra_render_contact_page($locale, $dict);
			break;
		case 'privacy':
			unyra_render_privacy_page($locale, $dict);
			break;
		case 'thank_you':
			unyra_render_thank_you_page($locale, $dict);
			break;
		default:
			unyra_render_default_page();
			break;
	}
}

function unyra_render_home_page($locale, $dict) {
	$hero = $dict['home']['hero'];
	?>
	<div class="site-stack">
		<section class="section-shell">
			<div class="container grid-shell grid-shell-hero">
				<div class="hero-copy">
					<div class="hero-badge"><?php echo esc_html($hero['experience']); ?></div>
					<div class="copy-stack">
						<p class="eyebrow"><?php echo esc_html($hero['eyebrow']); ?></p>
						<h1 class="hero-title"><?php echo esc_html($hero['title']); ?></h1>
						<p class="hero-description"><?php echo esc_html($hero['description']); ?></p>
						<p class="hero-market-line"><?php echo esc_html($hero['market_line']); ?></p>
					</div>
					<div class="button-row">
						<a class="button-primary" href="<?php echo esc_url(unyra_get_page_url('contact', $locale)); ?>"><?php echo esc_html($hero['primary_cta']); ?></a>
						<a class="button-secondary" href="<?php echo esc_url(unyra_get_page_url('producers', $locale)); ?>"><?php echo esc_html($hero['secondary_cta']); ?></a>
					</div>
					<div class="chip-row">
						<?php foreach ($hero['highlights'] as $highlight) : ?>
							<span class="surface-chip"><?php echo esc_html($highlight); ?></span>
						<?php endforeach; ?>
					</div>
				</div>

				<div class="premium-panel-dark hero-panel">
					<div class="hero-network" aria-hidden="true"></div>
					<div class="hero-panel__content">
						<p class="eyebrow-light"><?php echo esc_html($hero['panel_title']); ?></p>
						<h2 class="hero-panel__title"><?php echo esc_html($dict['labels']['tagline']); ?></h2>
						<p class="hero-panel__description"><?php echo esc_html($hero['panel_text']); ?></p>
						<div class="hero-panel__cards">
							<?php foreach ($hero['panel_cards'] as $card) : ?>
								<div class="dark-float-card">
									<p class="eyebrow-light"><?php echo esc_html($card['eyebrow']); ?></p>
									<p class="dark-float-card__title"><?php echo esc_html($card['title']); ?></p>
								</div>
							<?php endforeach; ?>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section class="section-shell">
			<div class="container four-up-grid">
				<?php foreach ($dict['home']['trust'] as $item) : ?>
					<article class="premium-card">
						<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
						<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
					</article>
				<?php endforeach; ?>
			</div>
		</section>

		<section class="section-shell">
			<div class="container split-grid">
				<div class="copy-stack">
					<?php unyra_section_heading($dict['home']['about']['eyebrow'], $dict['home']['about']['title'], $dict['home']['about']['description']); ?>
					<?php foreach ($dict['home']['about']['paragraphs'] as $paragraph) : ?>
						<p class="body-copy"><?php echo esc_html($paragraph); ?></p>
					<?php endforeach; ?>
				</div>
				<div class="editorial-card">
					<p class="eyebrow"><?php echo esc_html($dict['home']['about']['eyebrow']); ?></p>
					<div class="feature-list">
						<?php foreach ($dict['home']['about']['markers'] as $marker) : ?>
							<div class="feature-line"><span class="feature-line__dot"></span><span><?php echo esc_html($marker); ?></span></div>
						<?php endforeach; ?>
					</div>
				</div>
			</div>
		</section>

		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($dict['home']['solutions']['eyebrow'], $dict['home']['solutions']['title'], $dict['home']['solutions']['description']); ?>
				<div class="three-up-grid">
					<?php foreach ($dict['home']['solutions']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('pin'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>

		<section class="section-shell">
			<div class="container split-grid split-grid-dark">
				<div class="premium-panel-dark content-panel">
					<?php unyra_section_heading($dict['home']['expertise']['eyebrow'], $dict['home']['expertise']['title'], $dict['home']['expertise']['description'], true); ?>
					<div class="stack-grid">
						<?php foreach ($dict['home']['expertise']['pillars'] as $item) : ?>
							<article class="dark-list-card">
								<h3 class="dark-card-title"><?php echo esc_html($item['title']); ?></h3>
								<p class="dark-card-copy"><?php echo esc_html($item['description']); ?></p>
							</article>
						<?php endforeach; ?>
					</div>
				</div>
				<div class="premium-card premium-card-flex">
					<div>
						<p class="eyebrow"><?php echo esc_html($dict['home']['expertise']['aside_title']); ?></p>
						<p class="aside-copy"><?php echo esc_html($dict['home']['expertise']['aside_text']); ?></p>
					</div>
					<div class="stack-grid chips-left">
						<?php foreach ($dict['home']['network']['cards'] as $card) : ?>
							<div class="surface-chip surface-chip-left"><?php echo esc_html($card['title']); ?></div>
						<?php endforeach; ?>
					</div>
				</div>
			</div>
		</section>

		<section class="section-shell">
			<div class="container">
				<?php unyra_render_global_map($dict['home']['network']); ?>
			</div>
		</section>

		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($dict['home']['audiences']['eyebrow'], $dict['home']['audiences']['title'], $dict['home']['audiences']['description']); ?>
				<div class="two-up-grid">
					<?php foreach ($dict['home']['audiences']['cards'] as $card) : ?>
						<article class="premium-card audience-card">
							<p class="eyebrow"><?php echo esc_html($card['eyebrow']); ?></p>
							<h3 class="card-title"><?php echo esc_html($card['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($card['description']); ?></p>
							<div class="feature-list">
								<?php foreach ($card['bullets'] as $bullet) : ?>
									<div class="feature-line"><span class="feature-line__dot"></span><span><?php echo esc_html($bullet); ?></span></div>
								<?php endforeach; ?>
							</div>
							<a class="text-link" href="<?php echo esc_url(unyra_get_page_url($card['key'], $locale)); ?>"><?php echo esc_html($card['cta']); ?> <span aria-hidden="true">&rarr;</span></a>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>

		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($dict['home']['why']['eyebrow'], $dict['home']['why']['title'], $dict['home']['why']['description']); ?>
				<div class="three-up-grid">
					<?php foreach ($dict['home']['why']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('mail'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>

		<?php unyra_render_simple_cta_band($dict['home']['cta'], $locale, 'contact', 'buyers'); ?>
		<?php unyra_render_lead_section($locale, $dict, $dict['home']['lead'], 'home'); ?>
	</div>
	<?php
}

function unyra_render_about_page($locale, $dict) {
	$page = $dict['about'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'about', $page['hero']); ?>
		<section class="section-shell">
			<div class="container split-grid">
				<div class="copy-stack">
					<?php unyra_section_heading($page['overview']['eyebrow'], $page['overview']['title'], $page['overview']['description']); ?>
					<?php foreach ($page['overview']['paragraphs'] as $paragraph) : ?>
						<p class="body-copy"><?php echo esc_html($paragraph); ?></p>
					<?php endforeach; ?>
				</div>
				<div class="premium-card">
					<p class="eyebrow"><?php echo esc_html($dict['labels']['tagline']); ?></p>
					<p class="aside-copy"><?php echo esc_html($page['overview']['description']); ?></p>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($page['values']['eyebrow'], $page['values']['title'], $page['values']['description']); ?>
				<div class="three-up-grid">
					<?php foreach ($page['values']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('pin'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container split-grid split-grid-dark">
				<div class="premium-panel-dark content-panel">
					<?php unyra_section_heading($page['experience']['eyebrow'], $page['experience']['title'], $page['experience']['description'], true); ?>
					<div class="three-up-grid tablet-three">
						<?php foreach ($page['experience']['pillars'] as $item) : ?>
							<article class="dark-list-card">
								<h3 class="dark-card-title"><?php echo esc_html($item['title']); ?></h3>
								<p class="dark-card-copy"><?php echo esc_html($item['description']); ?></p>
							</article>
						<?php endforeach; ?>
					</div>
				</div>
				<div class="editorial-card">
					<p class="eyebrow"><?php echo esc_html(unyra_company()['experience_badge']); ?></p>
					<div class="feature-list">
						<?php foreach ($page['experience']['timeline'] as $item) : ?>
							<div class="feature-line"><span class="feature-line__dot"></span><span><?php echo esc_html($item); ?></span></div>
						<?php endforeach; ?>
					</div>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container premium-card-shell">
				<div class="premium-card-shell__inner">
					<h2 class="section-heading__title"><?php echo esc_html($page['relationships']['title']); ?></h2>
					<p class="section-heading__description"><?php echo esc_html($page['relationships']['description']); ?></p>
					<div class="three-up-grid tablet-three">
						<?php foreach ($page['relationships']['bullets'] as $item) : ?>
							<div class="surface-chip surface-chip-block"><?php echo esc_html($item); ?></div>
						<?php endforeach; ?>
					</div>
				</div>
			</div>
		</section>
		<?php unyra_render_simple_cta_band($page['cta'], $locale, 'contact'); ?>
	</div>
	<?php
}

function unyra_render_markets_page($locale, $dict) {
	$page = $dict['markets'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'markets', $page['hero']); ?>
		<section class="section-shell"><div class="container"><?php unyra_render_global_map($dict['home']['network']); ?></div></section>
		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($page['connectivity']['eyebrow'], $page['connectivity']['title'], $page['connectivity']['description']); ?>
				<div class="three-up-grid">
					<?php foreach ($page['connectivity']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('pin'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container premium-card-shell"><div class="premium-card-shell__inner">
				<h2 class="section-heading__title"><?php echo esc_html($page['opportunity']['title']); ?></h2>
				<p class="section-heading__description"><?php echo esc_html($page['opportunity']['description']); ?></p>
				<div class="three-up-grid tablet-three">
					<?php foreach ($page['opportunity']['bullets'] as $item) : ?>
						<div class="surface-chip surface-chip-block"><?php echo esc_html($item); ?></div>
					<?php endforeach; ?>
				</div>
			</div></div>
		</section>
		<?php unyra_render_simple_cta_band($page['cta'], $locale, 'contact'); ?>
	</div>
	<?php
}

function unyra_render_solutions_page($locale, $dict) {
	$page = $dict['solutions'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'solutions', $page['hero']); ?>
		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($page['capabilities']['eyebrow'], $page['capabilities']['title'], $page['capabilities']['description']); ?>
				<div class="three-up-grid">
					<?php foreach ($page['capabilities']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('mail'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container premium-card-shell"><div class="premium-card-shell__inner">
				<?php unyra_section_heading($page['process']['eyebrow'], $page['process']['title'], $page['process']['description']); ?>
				<div class="three-up-grid">
					<?php foreach ($page['process']['steps'] as $index => $step) : ?>
						<article class="premium-card premium-card-muted">
							<p class="step-number"><?php echo esc_html(sprintf('%02d', $index + 1)); ?></p>
							<h3 class="card-title"><?php echo esc_html($step['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($step['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div></div>
		</section>
		<section class="section-shell">
			<div class="container cta-band-dark">
				<h2 class="cta-band-dark__title"><?php echo esc_html($page['expertise']['title']); ?></h2>
				<p class="cta-band-dark__description"><?php echo esc_html($page['expertise']['description']); ?></p>
				<div class="three-up-grid tablet-three">
					<?php foreach ($page['expertise']['bullets'] as $item) : ?>
						<div class="surface-chip surface-chip-dark surface-chip-block"><?php echo esc_html($item); ?></div>
					<?php endforeach; ?>
				</div>
			</div>
		</section>
		<?php unyra_render_simple_cta_band($page['cta'], $locale, 'contact'); ?>
	</div>
	<?php
}

function unyra_render_buyers_page($locale, $dict) {
	$page = $dict['buyers'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'buyers', $page['hero']); ?>
		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($page['priorities']['eyebrow'], $page['priorities']['title'], $page['priorities']['description']); ?>
				<div class="four-up-grid buyers-grid">
					<?php foreach ($page['priorities']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('pin'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container premium-card-shell"><div class="premium-card-shell__inner">
				<?php unyra_section_heading($page['approach']['eyebrow'], $page['approach']['title'], $page['approach']['description']); ?>
				<div class="three-up-grid tablet-three">
					<?php foreach ($page['approach']['bullets'] as $item) : ?>
						<div class="surface-chip surface-chip-block"><?php echo esc_html($item); ?></div>
					<?php endforeach; ?>
				</div>
			</div></div>
		</section>
		<?php unyra_render_lead_section($locale, $dict, ['eyebrow' => $dict['form']['badge'], 'title' => $page['form_panel']['title'], 'description' => $page['form_panel']['description'], 'bullets' => []], 'buyers'); ?>
	</div>
	<?php
}

function unyra_render_producers_page($locale, $dict) {
	$page = $dict['producers'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'producers', $page['hero']); ?>
		<section class="section-shell">
			<div class="container">
				<?php unyra_section_heading($page['priorities']['eyebrow'], $page['priorities']['title'], $page['priorities']['description']); ?>
				<div class="four-up-grid buyers-grid">
					<?php foreach ($page['priorities']['items'] as $item) : ?>
						<article class="premium-card">
							<span class="icon-badge"><?php echo unyra_icon_svg('pin'); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<h3 class="card-title"><?php echo esc_html($item['title']); ?></h3>
							<p class="card-copy"><?php echo esc_html($item['description']); ?></p>
						</article>
					<?php endforeach; ?>
				</div>
			</div>
		</section>
		<section class="section-shell">
			<div class="container premium-card-shell"><div class="premium-card-shell__inner">
				<?php unyra_section_heading($page['approach']['eyebrow'], $page['approach']['title'], $page['approach']['description']); ?>
				<div class="three-up-grid tablet-three">
					<?php foreach ($page['approach']['bullets'] as $item) : ?>
						<div class="surface-chip surface-chip-block"><?php echo esc_html($item); ?></div>
					<?php endforeach; ?>
				</div>
			</div></div>
		</section>
		<?php unyra_render_lead_section($locale, $dict, ['eyebrow' => $dict['form']['badge'], 'title' => $page['form_panel']['title'], 'description' => $page['form_panel']['description'], 'bullets' => []], 'producers'); ?>
	</div>
	<?php
}

function unyra_render_contact_page($locale, $dict) {
	$page = $dict['contact'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'contact', $page['hero']); ?>
		<section class="section-shell">
			<div class="container four-up-grid buyers-grid">
				<?php foreach (unyra_contact_items($dict) as $item) : ?>
					<article class="premium-card">
						<span class="icon-badge"><?php echo unyra_icon_svg($item['icon']); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
						<h3 class="card-title"><?php echo esc_html($item['label']); ?></h3>
						<?php if ($item['url']) : ?>
							<p class="card-copy"><a class="inline-link" href="<?php echo esc_url($item['url']); ?>"><?php echo esc_html($item['value']); ?></a></p>
						<?php else : ?>
							<p class="card-copy"><?php echo esc_html($item['value']); ?></p>
						<?php endif; ?>
					</article>
				<?php endforeach; ?>
			</div>
		</section>
		<?php unyra_render_lead_section($locale, $dict, ['eyebrow' => $dict['form']['badge'], 'title' => $dict['form']['title'], 'description' => $dict['form']['description'], 'bullets' => []], 'contact'); ?>
		<section class="section-shell">
			<div class="container premium-card-shell"><div class="premium-card-shell__inner">
				<h2 class="section-heading__title"><?php echo esc_html($page['response']['title']); ?></h2>
				<p class="section-heading__description"><?php echo esc_html($page['response']['description']); ?></p>
				<div class="three-up-grid tablet-three">
					<?php foreach ($page['response']['bullets'] as $item) : ?>
						<div class="surface-chip surface-chip-block"><?php echo esc_html($item); ?></div>
					<?php endforeach; ?>
				</div>
			</div></div>
		</section>
	</div>
	<?php
}

function unyra_render_privacy_page($locale, $dict) {
	$page = $dict['privacy'];
	?>
	<div class="site-stack">
		<?php unyra_render_page_hero($locale, $dict, 'privacy', $page['hero']); ?>
		<section class="section-shell">
			<div class="container privacy-stack">
				<?php foreach ($page['sections'] as $section) : ?>
					<article class="premium-card">
						<h2 class="privacy-title"><?php echo esc_html($section['title']); ?></h2>
						<div class="copy-stack copy-stack-tight">
							<?php foreach ($section['paragraphs'] as $paragraph) : ?>
								<p class="card-copy"><?php echo esc_html($paragraph); ?></p>
							<?php endforeach; ?>
						</div>
					</article>
				<?php endforeach; ?>
			</div>
		</section>
		<?php unyra_render_simple_cta_band(['title' => $dict['labels']['privacy_note'], 'description' => $dict['labels']['footer_launch']], $locale, 'home'); ?>
	</div>
	<?php
}

function unyra_render_thank_you_page($locale, $dict) {
	$page = $dict['thank_you'];
	?>
	<section class="section-shell">
		<div class="container thank-you-shell">
			<div class="premium-panel-dark thank-you-panel">
				<p class="eyebrow-light"><?php echo esc_html($page['eyebrow']); ?></p>
				<h1 class="thank-you-title"><?php echo esc_html($page['title']); ?></h1>
				<p class="thank-you-description"><?php echo esc_html($page['description']); ?></p>
				<div class="button-row button-row-centered">
					<a class="button-primary button-primary-inverse" href="<?php echo esc_url(unyra_get_page_url('home', $locale)); ?>"><?php echo esc_html($page['primary']); ?></a>
					<a class="button-secondary button-secondary-dark" href="<?php echo esc_url(unyra_get_page_url('contact', $locale)); ?>"><?php echo esc_html($page['secondary']); ?></a>
				</div>
			</div>
		</div>
	</section>
	<?php
}

function unyra_render_default_page() {
	?>
	<section class="section-shell">
		<div class="container premium-card-shell"><div class="premium-card-shell__inner">
			<?php
			if (have_posts()) {
				while (have_posts()) {
					the_post();
					echo '<h1 class="section-heading__title">' . esc_html(get_the_title()) . '</h1>';
					echo '<div class="body-content">';
					the_content();
					echo '</div>';
				}
			}
			?>
		</div></div>
	</section>
	<?php
}

function unyra_render_page_hero($locale, $dict, $page_key, $hero) {
	?>
	<section class="section-shell">
		<div class="container page-hero">
			<div class="page-hero__copy">
				<nav class="breadcrumbs" aria-label="Breadcrumb">
					<a href="<?php echo esc_url(unyra_get_page_url('home', $locale)); ?>"><?php echo esc_html($dict['labels']['nav']['home']); ?></a>
					<span>/</span>
					<span><?php echo esc_html($dict['labels']['nav'][$page_key]); ?></span>
				</nav>
				<p class="eyebrow"><?php echo esc_html($hero['eyebrow']); ?></p>
				<h1 class="page-hero__title"><?php echo esc_html($hero['title']); ?></h1>
				<p class="page-hero__description"><?php echo esc_html($hero['description']); ?></p>
			</div>
			<div class="page-hero__chips">
				<div class="surface-chip surface-chip-block"><?php echo esc_html($dict['home']['hero']['experience']); ?></div>
				<div class="surface-chip surface-chip-block"><?php echo esc_html($dict['labels']['tagline']); ?></div>
			</div>
		</div>
	</section>
	<?php
}

function unyra_render_global_map($section) {
	$coords = [
		'united-states' => ['x' => 17, 'y' => 33],
		'canada'        => ['x' => 17, 'y' => 22],
		'brazil'        => ['x' => 31, 'y' => 58],
		'chile'         => ['x' => 23, 'y' => 70],
		'argentina'     => ['x' => 27, 'y' => 77],
		'egypt'         => ['x' => 55, 'y' => 43],
		'turkey'        => ['x' => 61, 'y' => 36],
		'europe'        => ['x' => 55, 'y' => 25],
		'china'         => ['x' => 77, 'y' => 34],
	];
	?>
	<section class="premium-panel-dark map-panel">
		<div class="map-copy">
			<p class="eyebrow-light"><?php echo esc_html($section['eyebrow']); ?></p>
			<h3 class="map-title"><?php echo esc_html($section['title']); ?></h3>
			<p class="map-description"><?php echo esc_html($section['description']); ?></p>
		</div>
		<div class="map-grid">
			<div class="map-stage">
				<svg viewBox="0 0 100 100" class="map-svg" preserveAspectRatio="none" aria-hidden="true">
					<defs>
						<linearGradient id="unyra-trade-route" x1="0%" y1="0%" x2="100%" y2="100%">
							<stop offset="0%" stop-color="#D4B082" />
							<stop offset="52%" stop-color="#F7E6C9" />
							<stop offset="100%" stop-color="#799D8B" />
						</linearGradient>
					</defs>
					<path d="M17 33 C 25 29, 40 24, 55 25" fill="none" stroke="url(#unyra-trade-route)" stroke-width="0.35" stroke-linecap="round" class="route-dash" />
					<path d="M17 33 C 28 42, 31 51, 31 58" fill="none" stroke="url(#unyra-trade-route)" stroke-width="0.35" stroke-linecap="round" class="route-dash-slow" />
					<path d="M31 58 C 40 51, 49 46, 55 43" fill="none" stroke="url(#unyra-trade-route)" stroke-width="0.35" stroke-linecap="round" class="route-dash" />
					<path d="M55 25 C 66 24, 72 28, 77 34" fill="none" stroke="url(#unyra-trade-route)" stroke-width="0.35" stroke-linecap="round" class="route-dash-slow" />
				</svg>
				<?php foreach ($section['cards'] as $card) : ?>
					<?php $coord = $coords[$card['key']]; ?>
					<div class="map-node" style="left: <?php echo esc_attr($coord['x']); ?>%; top: <?php echo esc_attr($coord['y']); ?>%;">
						<span class="map-node__ping"></span>
						<span class="map-node__dot"></span>
						<span class="map-node__label"><?php echo esc_html($card['title']); ?></span>
					</div>
				<?php endforeach; ?>
			</div>
			<div class="map-card-grid">
				<?php foreach ($section['cards'] as $card) : ?>
					<article class="dark-list-card">
						<h4 class="dark-card-title"><?php echo esc_html($card['title']); ?></h4>
						<p class="dark-card-copy"><?php echo esc_html($card['description']); ?></p>
					</article>
				<?php endforeach; ?>
			</div>
		</div>
	</section>
	<?php
}

function unyra_render_simple_cta_band($cta, $locale, $primary_key, $secondary_key = '') {
	$primary_label   = isset($cta['primary']) ? $cta['primary'] : unyra_get_dictionary($locale)['labels']['secondary_cta'];
	$secondary_label = isset($cta['secondary']) ? $cta['secondary'] : '';
	?>
	<section class="section-shell">
		<div class="container cta-band-dark cta-band-dark-inline">
			<div class="cta-band-dark__copy">
				<p class="eyebrow-light"><?php echo esc_html(unyra_company()['experience_badge']); ?></p>
				<h2 class="cta-band-dark__title"><?php echo esc_html($cta['title']); ?></h2>
				<p class="cta-band-dark__description"><?php echo esc_html($cta['description']); ?></p>
			</div>
			<div class="button-row">
				<a class="button-primary button-primary-inverse" href="<?php echo esc_url(unyra_get_page_url($primary_key, $locale)); ?>"><?php echo esc_html($primary_label); ?></a>
				<?php if ($secondary_key && $secondary_label) : ?>
					<a class="button-secondary button-secondary-dark" href="<?php echo esc_url(unyra_get_page_url($secondary_key, $locale)); ?>"><?php echo esc_html($secondary_label); ?></a>
				<?php endif; ?>
			</div>
		</div>
	</section>
	<?php
}

function unyra_render_lead_section($locale, $dict, $intro, $source) {
	$bullets = !empty($intro['bullets']) ? $intro['bullets'] : [];
	$status  = unyra_form_status();
	?>
	<section class="section-shell">
		<div class="container split-grid split-grid-form">
			<div class="premium-card premium-card-flex">
				<?php unyra_section_heading($intro['eyebrow'], $intro['title'], $intro['description']); ?>
				<?php if ($bullets) : ?>
					<div class="feature-list">
						<?php foreach ($bullets as $bullet) : ?>
							<div class="feature-line"><span class="feature-line__dot"></span><span><?php echo esc_html($bullet); ?></span></div>
						<?php endforeach; ?>
					</div>
				<?php endif; ?>
			</div>

			<div class="premium-panel-dark form-panel">
				<?php if ('error' === $status) : ?>
					<p class="form-status form-status-error"><?php echo esc_html($dict['form']['error']); ?></p>
				<?php endif; ?>
				<form class="lead-form" method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
					<input type="hidden" name="action" value="unyra_contact" />
					<input type="hidden" name="locale" value="<?php echo esc_attr($locale); ?>" />
					<input type="hidden" name="source" value="<?php echo esc_attr($source); ?>" />
					<input type="hidden" name="redirect_to" value="<?php echo esc_url(unyra_get_page_url('thank_you', $locale)); ?>" />
					<?php wp_nonce_field('unyra_contact_submit', 'unyra_contact_nonce'); ?>

					<div class="form-grid">
						<?php
						$fields = ['full_name', 'company', 'email', 'phone', 'country'];
						foreach ($fields as $field) :
							?>
							<label class="form-label">
								<span><?php echo esc_html($dict['form']['fields'][ $field ]); ?></span>
								<input class="form-field" type="<?php echo esc_attr('email' === $field ? 'email' : ('phone' === $field ? 'tel' : 'text')); ?>" name="<?php echo esc_attr($field); ?>" placeholder="<?php echo esc_attr($dict['form']['placeholders'][ $field ]); ?>" />
							</label>
						<?php endforeach; ?>
					</div>

					<div class="form-grid">
						<label class="form-label">
							<span><?php echo esc_html($dict['form']['fields']['role']); ?></span>
							<select class="form-field" name="role">
								<option value=""><?php echo esc_html($dict['form']['fields']['role']); ?></option>
								<?php foreach ($dict['form']['role_options'] as $value => $label) : ?>
									<option value="<?php echo esc_attr($value); ?>"><?php echo esc_html($label); ?></option>
								<?php endforeach; ?>
							</select>
						</label>
						<label class="form-label">
							<span><?php echo esc_html($dict['form']['fields']['interest']); ?></span>
							<select class="form-field" name="interest">
								<option value=""><?php echo esc_html($dict['form']['fields']['interest']); ?></option>
								<?php foreach ($dict['form']['interest_options'] as $value => $label) : ?>
									<option value="<?php echo esc_attr($value); ?>"><?php echo esc_html($label); ?></option>
								<?php endforeach; ?>
							</select>
						</label>
					</div>

					<label class="form-label">
						<span><?php echo esc_html($dict['form']['fields']['message']); ?></span>
						<textarea class="form-field form-textarea" name="message" placeholder="<?php echo esc_attr($dict['form']['placeholders']['message']); ?>"></textarea>
					</label>

					<label class="screen-reader-text" for="website"><?php echo esc_html($dict['form']['honeypot']); ?></label>
					<input id="website" type="text" name="website" value="" class="unyra-honeypot" tabindex="-1" autocomplete="off" />

					<div class="form-submit-row">
						<p class="form-privacy-note"><?php echo esc_html($dict['form']['privacy_note']); ?></p>
						<button class="button-primary button-primary-inverse form-submit" type="submit"><?php echo esc_html($dict['form']['submit']); ?></button>
					</div>
				</form>
			</div>
		</div>
	</section>
	<?php
}
