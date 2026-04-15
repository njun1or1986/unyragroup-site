<?php
/**
 * Theme header.
 *
 * @package UnyraGroupCorporate
 */

if (!defined('ABSPATH')) {
	exit;
}

$locale      = unyra_get_locale();
$dict        = unyra_get_dictionary($locale);
$company     = unyra_company();
$page_key    = unyra_get_page_key();
$nav_items   = unyra_navigation_items($locale);
$lang_items  = unyra_language_switcher_items();
$header_cta  = unyra_get_page_url('contact', $locale);
$header_copy = $dict['labels']['secondary_cta'];
?>
<!doctype html>
<html lang="<?php echo esc_attr($locale); ?>" dir="<?php echo is_rtl() ? 'rtl' : 'ltr'; ?>">
<head>
	<meta charset="<?php bloginfo('charset'); ?>" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="skip-link" href="#primary-content"><?php esc_html_e('Skip to content', 'unyra-group-corporate'); ?></a>
<div class="site-background">
	<header class="site-header">
		<div class="container">
			<div class="site-header__bar">
				<a class="brand-link" href="<?php echo esc_url(unyra_get_page_url('home', $locale)); ?>" aria-label="<?php echo esc_attr($company['name']); ?>">
					<span class="brand-logo-shell">
						<img
							class="brand-logo-image brand-logo"
							src="<?php echo esc_url($company['logo']); ?>"
							alt="<?php echo esc_attr($company['name']); ?>"
							width="1336"
							height="422"
						/>
					</span>
				</a>

				<button
					class="menu-toggle"
					type="button"
					aria-expanded="false"
					aria-controls="unyra-navigation-panel"
					data-menu-toggle
				>
					<span></span>
					<span></span>
					<span></span>
					<span class="screen-reader-text"><?php esc_html_e('Toggle navigation', 'unyra-group-corporate'); ?></span>
				</button>

				<div class="site-header__panel" id="unyra-navigation-panel" data-menu-panel>
					<nav class="site-nav" aria-label="<?php esc_attr_e('Primary navigation', 'unyra-group-corporate'); ?>">
						<?php foreach ($nav_items as $item) : ?>
							<a
								class="site-nav__link <?php echo $item['key'] === $page_key ? 'site-nav__link-active' : ''; ?>"
								href="<?php echo esc_url($item['url']); ?>"
							>
								<?php echo esc_html($item['label']); ?>
							</a>
						<?php endforeach; ?>
					</nav>

					<div class="site-header__meta">
						<div class="language-switcher" aria-label="<?php esc_attr_e('Language switcher', 'unyra-group-corporate'); ?>">
							<?php foreach ($lang_items as $item) : ?>
								<a
									class="language-switcher__link <?php echo $item['active'] ? 'language-switcher__link-active' : ''; ?>"
									href="<?php echo esc_url($item['url']); ?>"
									lang="<?php echo esc_attr($item['locale']); ?>"
									hreflang="<?php echo esc_attr($item['locale']); ?>"
								>
									<?php echo esc_html($item['label']); ?>
								</a>
							<?php endforeach; ?>
						</div>

						<a class="button-primary header-cta" href="<?php echo esc_url($header_cta); ?>">
							<?php echo esc_html($header_copy); ?>
						</a>
					</div>
				</div>
			</div>
		</div>
	</header>

	<main id="primary-content" class="site-main">
