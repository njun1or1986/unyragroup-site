<?php

if (!defined('ABSPATH')) {
	exit;
}

function unyra_boot_locale_cookie() {
	if (isset($_GET['unyra_lang'])) {
		$locale = sanitize_key(wp_unslash($_GET['unyra_lang']));

		if (in_array($locale, unyra_supported_locales(), true)) {
			setcookie('unyra_lang', $locale, time() + MONTH_IN_SECONDS, COOKIEPATH ?: '/', COOKIE_DOMAIN, is_ssl(), false);
			$_COOKIE['unyra_lang'] = $locale;
		}
	}
}
add_action('init', 'unyra_boot_locale_cookie');

function unyra_get_locale() {
	if (function_exists('pll_current_language')) {
		$locale = pll_current_language('slug');
		if (in_array($locale, unyra_supported_locales(), true)) {
			return $locale;
		}
	}

	if (!empty($_COOKIE['unyra_lang']) && in_array($_COOKIE['unyra_lang'], unyra_supported_locales(), true)) {
		return $_COOKIE['unyra_lang'];
	}

	$wp_locale = determine_locale();

	if (str_starts_with($wp_locale, 'pt')) {
		return 'pt';
	}

	if (str_starts_with($wp_locale, 'es')) {
		return 'es';
	}

	return unyra_default_locale();
}

function unyra_get_dictionary($locale = null) {
	$locale  = $locale ?: unyra_get_locale();
	$content = unyra_theme_content();

	return $content[$locale] ?? $content[unyra_default_locale()];
}

function unyra_company() {
	$defaults = unyra_company_defaults();
	$logo_id  = get_theme_mod('custom_logo');

	if ($logo_id) {
		$logo = wp_get_attachment_image_url($logo_id, 'full');
		if ($logo) {
			$defaults['logo'] = $logo;
		}
	}

	return $defaults;
}

function unyra_phone_href($value) {
	return 'tel:' . preg_replace('/[^0-9+]/', '', $value);
}

function unyra_get_page_key() {
	if (is_front_page() || is_home()) {
		return 'home';
	}

	if (is_page()) {
		$slug       = get_post_field('post_name', get_queried_object_id());
		$page_slugs = unyra_page_slugs();

		foreach ($page_slugs as $page_key => $translations) {
			if (in_array($slug, $translations, true)) {
				return $page_key;
			}
		}
	}

	return 'home';
}

function unyra_get_page_url($page_key, $locale = null) {
	$locale     = $locale ?: unyra_get_locale();
	$page_slugs = unyra_page_slugs();

	if ('home' === $page_key) {
		$url = home_url('/');
	} else {
		$slug = $page_slugs[$page_key][$locale] ?? '';
		$page = $slug ? get_page_by_path($slug) : null;
		$url  = $page ? get_permalink($page) : home_url('/' . $slug . '/');
	}

	if (!function_exists('pll_current_language')) {
		$url = add_query_arg('unyra_lang', $locale, $url);
	}

	return $url;
}

function unyra_navigation_items($locale = null) {
	$locale = $locale ?: unyra_get_locale();
	$dict   = unyra_get_dictionary($locale);
	$keys   = ['about', 'markets', 'solutions', 'buyers', 'producers', 'contact'];
	$items  = [];

	foreach ($keys as $key) {
		$items[] = [
			'key'   => $key,
			'label' => $dict['labels']['nav'][$key],
			'url'   => unyra_get_page_url($key, $locale),
		];
	}

	return $items;
}

function unyra_language_switcher_items() {
	$current  = unyra_get_locale();
	$meta     = unyra_locale_meta();
	$items    = [];

	if (function_exists('pll_the_languages')) {
		$languages = pll_the_languages(['raw' => 1]);
		if (is_array($languages)) {
			foreach ($languages as $entry) {
				if (!in_array($entry['slug'], unyra_supported_locales(), true)) {
					continue;
				}

				$items[] = [
					'locale' => $entry['slug'],
					'label'  => $meta[$entry['slug']]['short'],
					'url'    => $entry['url'],
					'active' => !empty($entry['current_lang']),
				];
			}

			return $items;
		}
	}

	foreach (unyra_supported_locales() as $locale) {
		$items[] = [
			'locale' => $locale,
			'label'  => $meta[$locale]['short'],
			'url'    => unyra_get_page_url(unyra_get_page_key(), $locale),
			'active' => $locale === $current,
		];
	}

	return $items;
}

function unyra_contact_items($dict = null) {
	$dict    = $dict ?: unyra_get_dictionary();
	$company = unyra_company();

	return [
		[
			'icon'  => 'mail',
			'label' => $dict['contact_labels']['email'],
			'value' => $company['company_email'],
			'url'   => 'mailto:' . $company['company_email'],
		],
		[
			'icon'  => 'mail',
			'label' => $dict['contact_labels']['sales'],
			'value' => $company['sales_email'],
			'url'   => 'mailto:' . $company['sales_email'],
		],
		[
			'icon'  => 'phone',
			'label' => $dict['contact_labels']['phone'],
			'value' => $company['phone_display'],
			'url'   => unyra_phone_href($company['phone_display']),
		],
		[
			'icon'  => 'pin',
			'label' => $dict['contact_labels']['location'],
			'value' => $company['location'],
			'url'   => '',
		],
	];
}

function unyra_form_status() {
	$status = isset($_GET['unyra_form']) ? sanitize_key(wp_unslash($_GET['unyra_form'])) : '';

	if (!in_array($status, ['success', 'error'], true)) {
		return '';
	}

	return $status;
}

function unyra_icon_svg($icon) {
	if ('mail' === $icon) {
		return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6.75h16a1 1 0 0 1 1 1v8.5a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-8.5a1 1 0 0 1 1-1Zm0 1.3v.16l8 5.22 8-5.22v-.16H4Zm16 7.9V9.75l-7.45 4.87a1 1 0 0 1-1.1 0L4 9.75v6.2h16Z" fill="currentColor"/></svg>';
	}

	if ('phone' === $icon) {
		return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.08 4.55c.3-.3.74-.4 1.13-.26l2.18.76c.5.18.8.7.71 1.22l-.37 2.11a1 1 0 0 1-.76.81l-1.16.28a14.7 14.7 0 0 0 5.72 5.72l.28-1.16a1 1 0 0 1 .81-.76l2.11-.37a1.1 1.1 0 0 1 1.22.71l.76 2.18c.14.39.04.83-.26 1.13l-1.46 1.46c-.5.5-1.22.72-1.92.58-7.57-1.48-13.34-7.25-14.82-14.82a1.93 1.93 0 0 1 .58-1.92l1.46-1.46Z" fill="currentColor"/></svg>';
	}

	return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5a7 7 0 0 1 7 7c0 4.67-5.06 9.4-6.28 10.48a1.08 1.08 0 0 1-1.44 0C10.06 19.9 5 15.17 5 10.5a7 7 0 0 1 7-7Zm0 9.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z" fill="currentColor"/></svg>';
}

function unyra_section_heading($eyebrow, $title, $description, $light = false) {
	$eyebrow_class = $light ? 'eyebrow-light' : 'eyebrow';
	$title_class   = $light ? 'section-heading__title section-heading__title-light' : 'section-heading__title';
	$text_class    = $light ? 'section-heading__description section-heading__description-light' : 'section-heading__description';

	echo '<div class="section-heading">';
	echo '<p class="' . esc_attr($eyebrow_class) . '">' . esc_html($eyebrow) . '</p>';
	echo '<h2 class="' . esc_attr($title_class) . '">' . esc_html($title) . '</h2>';
	echo '<p class="' . esc_attr($text_class) . '">' . esc_html($description) . '</p>';
	echo '</div>';
}
