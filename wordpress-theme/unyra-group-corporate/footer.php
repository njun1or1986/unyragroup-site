<?php
/**
 * Theme footer.
 *
 * @package UnyraGroupCorporate
 */

if (!defined('ABSPATH')) {
	exit;
}

$locale        = unyra_get_locale();
$dict          = unyra_get_dictionary($locale);
$company       = unyra_company();
$nav_items     = unyra_navigation_items($locale);
$contact_items = unyra_contact_items($dict);
?>
	</main>

	<div class="sticky-cta" aria-hidden="false">
		<div class="sticky-cta__inner">
			<div class="sticky-cta__copy">
				<p class="sticky-cta__eyebrow"><?php echo esc_html($company['experience_badge']); ?></p>
				<p class="sticky-cta__title"><?php echo esc_html($dict['labels']['tagline']); ?></p>
			</div>
			<a class="button-primary button-primary-inverse sticky-cta__button" href="<?php echo esc_url(unyra_get_page_url('contact', $locale)); ?>">
				<?php echo esc_html($dict['labels']['cta_short']); ?>
			</a>
		</div>
	</div>

	<footer class="footer-shell">
		<div class="container footer-grid">
			<div class="footer-brand">
				<a class="brand-link brand-link-footer" href="<?php echo esc_url(unyra_get_page_url('home', $locale)); ?>">
					<span class="brand-logo-shell">
						<img
							class="brand-logo-image brand-logo brand-logo-footer"
							src="<?php echo esc_url($company['logo']); ?>"
							alt="<?php echo esc_attr($company['name']); ?>"
							width="1336"
							height="422"
						/>
					</span>
				</a>
				<p class="footer-tagline"><?php echo esc_html($dict['labels']['tagline']); ?></p>
				<p class="footer-copy"><?php echo esc_html($company['summary']); ?></p>
			</div>

			<div class="footer-column">
				<p class="footer-heading"><?php echo esc_html($dict['labels']['footer_navigation']); ?></p>
				<div class="footer-nav">
					<?php foreach ($nav_items as $item) : ?>
						<a class="footer-link" href="<?php echo esc_url($item['url']); ?>"><?php echo esc_html($item['label']); ?></a>
					<?php endforeach; ?>
					<a class="footer-link" href="<?php echo esc_url(unyra_get_page_url('privacy', $locale)); ?>"><?php echo esc_html($dict['labels']['nav']['privacy']); ?></a>
				</div>
			</div>

			<div class="footer-column">
				<p class="footer-heading"><?php echo esc_html($dict['labels']['footer_contact']); ?></p>
				<div class="footer-contact">
					<?php foreach ($contact_items as $item) : ?>
						<div class="footer-contact__item">
							<span class="icon-badge footer-icon"><?php echo unyra_icon_svg($item['icon']); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></span>
							<div class="footer-contact__copy">
								<p class="footer-contact__label"><?php echo esc_html($item['label']); ?></p>
								<?php if (!empty($item['url'])) : ?>
									<a class="footer-link" href="<?php echo esc_url($item['url']); ?>"><?php echo esc_html($item['value']); ?></a>
								<?php else : ?>
									<p class="footer-copy footer-copy-small"><?php echo esc_html($item['value']); ?></p>
								<?php endif; ?>
							</div>
						</div>
					<?php endforeach; ?>
				</div>
			</div>
		</div>

		<div class="container footer-bottom">
			<p class="footer-copy footer-copy-small">
				&copy; <?php echo esc_html(gmdate('Y')); ?> <?php echo esc_html($company['name']); ?>.
			</p>
		</div>
	</footer>
</div>
<?php wp_footer(); ?>
</body>
</html>
