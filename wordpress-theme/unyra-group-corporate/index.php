<?php
/**
 * Main fallback template.
 *
 * @package UnyraGroupCorporate
 */

if (!defined('ABSPATH')) {
	exit;
}

$locale   = unyra_get_locale();
$dict     = unyra_get_dictionary($locale);
$page_key = unyra_get_page_key();

get_header();
unyra_render_page($page_key, $locale, $dict);
get_footer();
