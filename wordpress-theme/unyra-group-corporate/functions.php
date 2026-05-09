<?php

if (!defined('ABSPATH')) {
	exit;
}

require_once get_template_directory() . '/inc/theme-data.php';
require_once get_template_directory() . '/inc/helpers.php';
require_once get_template_directory() . '/inc/render.php';
require_once get_template_directory() . '/inc/form-handler.php';

function unyra_theme_setup() {
	add_theme_support('title-tag');
	add_theme_support('post-thumbnails');
	add_theme_support('menus');
	add_theme_support(
		'custom-logo',
		[
			'height'      => 422,
			'width'       => 1336,
			'flex-height' => true,
			'flex-width'  => true,
		]
	);

	register_nav_menus(
		[
			'primary' => __('Primary Navigation', 'unyra-group-corporate'),
			'footer'  => __('Footer Navigation', 'unyra-group-corporate'),
		]
	);
}
add_action('after_setup_theme', 'unyra_theme_setup');

function unyra_theme_enqueue_assets() {
	$theme = wp_get_theme();

	wp_enqueue_style(
		'unyra-theme',
		get_template_directory_uri() . '/assets/css/theme.css',
		[],
		$theme->get('Version')
	);

	wp_enqueue_script(
		'unyra-theme',
		get_template_directory_uri() . '/assets/js/theme.js',
		[],
		$theme->get('Version'),
		true
	);

	wp_localize_script(
		'unyra-theme',
		'unyraTheme',
		[
			'locale'  => unyra_get_locale(),
			'pageKey' => unyra_get_page_key(),
		]
	);
}
add_action('wp_enqueue_scripts', 'unyra_theme_enqueue_assets');

function unyra_theme_body_classes($classes) {
	$classes[] = 'unyra-body';
	$classes[] = 'unyra-locale-' . unyra_get_locale();
	$classes[] = 'unyra-page-' . unyra_get_page_key();

	return $classes;
}
add_filter('body_class', 'unyra_theme_body_classes');

function unyra_theme_customize_register($wp_customize) {
	$wp_customize->add_section(
		'unyra_contact_details',
		[
			'title'       => __('Unyra Contact Details', 'unyra-group-corporate'),
			'description' => __('Update the contact information shown across the theme.', 'unyra-group-corporate'),
			'priority'    => 35,
		]
	);

	$fields = [
		'unyra_company_email' => [
			'label'   => __('Company Email', 'unyra-group-corporate'),
			'default' => 'sales@unyragroup.com',
		],
		'unyra_sales_email' => [
			'label'   => __('Sales Email', 'unyra-group-corporate'),
			'default' => 'sales@unyragroup.com',
		],
		'unyra_phone_display' => [
			'label'   => __('Phone / WhatsApp', 'unyra-group-corporate'),
			'default' => '+1 888 789 8843',
		],
		'unyra_location' => [
			'label'   => __('Business Location', 'unyra-group-corporate'),
			'default' => 'Orlando, Florida, 32801, US',
		],
		'unyra_tagline' => [
			'label'   => __('Default Tagline', 'unyra-group-corporate'),
			'default' => 'Connecting Markets. Building Trust. Delivering Value.',
		],
	];

	foreach ($fields as $setting_id => $field) {
		$wp_customize->add_setting(
			$setting_id,
			[
				'default'           => $field['default'],
				'sanitize_callback' => 'sanitize_text_field',
			]
		);

		$wp_customize->add_control(
			$setting_id,
			[
				'label'   => $field['label'],
				'section' => 'unyra_contact_details',
				'type'    => 'text',
			]
		);
	}
}
add_action('customize_register', 'unyra_theme_customize_register');
