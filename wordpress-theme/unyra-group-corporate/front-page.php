<?php
/**
 * Front page template.
 *
 * @package UnyraGroupCorporate
 */

if (!defined('ABSPATH')) {
	exit;
}

$locale = unyra_get_locale();
$dict   = unyra_get_dictionary($locale);

get_header();
unyra_render_page('home', $locale, $dict);
get_footer();
