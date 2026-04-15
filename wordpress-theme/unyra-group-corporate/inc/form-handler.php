<?php

if (!defined('ABSPATH')) {
	exit;
}

function unyra_handle_contact_submission() {
	$referer      = wp_get_referer() ? wp_get_referer() : home_url('/');
	$locale       = isset($_POST['locale']) ? sanitize_key(wp_unslash($_POST['locale'])) : unyra_get_locale();
	$success_url  = isset($_POST['redirect_to']) ? esc_url_raw(wp_unslash($_POST['redirect_to'])) : unyra_get_page_url('thank_you', $locale);

	if (!isset($_POST['unyra_contact_nonce']) || !wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['unyra_contact_nonce'])), 'unyra_contact_submit')) {
		wp_safe_redirect(add_query_arg('unyra_form', 'error', $referer));
		exit;
	}

	if (!empty($_POST['website'])) {
		wp_safe_redirect(add_query_arg('unyra_form', 'success', $success_url));
		exit;
	}

	$fields = [
		'full_name' => sanitize_text_field(wp_unslash($_POST['full_name'] ?? '')),
		'company'   => sanitize_text_field(wp_unslash($_POST['company'] ?? '')),
		'email'     => sanitize_email(wp_unslash($_POST['email'] ?? '')),
		'phone'     => sanitize_text_field(wp_unslash($_POST['phone'] ?? '')),
		'country'   => sanitize_text_field(wp_unslash($_POST['country'] ?? '')),
		'role'      => sanitize_text_field(wp_unslash($_POST['role'] ?? '')),
		'interest'  => sanitize_text_field(wp_unslash($_POST['interest'] ?? '')),
		'message'   => sanitize_textarea_field(wp_unslash($_POST['message'] ?? '')),
		'source'    => sanitize_text_field(wp_unslash($_POST['source'] ?? '')),
	];

	foreach (['full_name', 'company', 'email', 'phone', 'country', 'role', 'interest', 'message'] as $required) {
		if (empty($fields[ $required ])) {
			wp_safe_redirect(add_query_arg('unyra_form', 'error', $referer));
			exit;
		}
	}

	if (!is_email($fields['email']) || strlen($fields['message']) < 20) {
		wp_safe_redirect(add_query_arg('unyra_form', 'error', $referer));
		exit;
	}

	$company = unyra_company();
	$to      = array_unique(array_filter([$company['company_email'], $company['sales_email']]));
	$subject = sprintf('[Unyra Inquiry] %s - %s', $fields['company'], $fields['full_name']);

	$body = implode(
		"\n",
		[
			'Unyra Group LLC website inquiry',
			'',
			'Submitted: ' . gmdate('c'),
			'Locale: ' . $locale,
			'Source page: ' . $fields['source'],
			'',
			'Full Name: ' . $fields['full_name'],
			'Company: ' . $fields['company'],
			'Email: ' . $fields['email'],
			'Phone / WhatsApp: ' . $fields['phone'],
			'Country: ' . $fields['country'],
			'Role: ' . $fields['role'],
			'Interest: ' . $fields['interest'],
			'',
			'Message:',
			$fields['message'],
		]
	);

	$headers = ['Reply-To: ' . $fields['full_name'] . ' <' . $fields['email'] . '>'];
	$sent    = wp_mail($to, $subject, $body, $headers);

	if (!$sent) {
		wp_safe_redirect(add_query_arg('unyra_form', 'error', $referer));
		exit;
	}

	wp_safe_redirect(add_query_arg('unyra_form', 'success', $success_url));
	exit;
}
add_action('admin_post_nopriv_unyra_contact', 'unyra_handle_contact_submission');
add_action('admin_post_unyra_contact', 'unyra_handle_contact_submission');
