<?php
require __DIR__ . '/dompdf/autoload.inc.php';
use Dompdf\Dompdf;
use Dompdf\Options;

if (isset($_GET['action'])) {
	// Simulate a payment processing
	$type = $_GET['type'];
	$name = $_GET['name'];
	$address = $_GET['address'];

	$options = new Options();
	$options->setIsRemoteEnabled(true);

	$dompdf = new Dompdf($options);

	global $_dompdf_show_warnings;
	$_dompdf_show_warnings = true;

	
	$dompdf->loadHtml("<h1>Payment Receipt</h1>
		<p>Name: $name</p>
		<p>Address: $address</p>
		<table>
			<tr>
				<th>Type</th>
				<th>Price</th>
			</tr>
			<tr>
				<td>$type</td>
				<td>Rp. 75.000</td>
			</tr>");
	$dompdf->setPaper('A4', 'portrait');
	$dompdf->render();
	$dompdf->stream("payment_receipt.pdf", array("Attachment" => false));

	exit;
}
?>
<!------ Copyright ------
Designed by: Emily Feng
Dribbble: https://dribbble.com/emilyfeng
Developed by Yago Rocha for educational purpose
-->
<!DOCTYPE html>
<html lang='en'>
<head>
	<meta charset='UTF-8'>
	<meta name='viewport' content='width=device-width, initial-scale=1.0'>
	<title>Payment</title>
	<link rel='stylesheet' href='./main.css'>
</head>

<body>
	<main id='container'>
		<aside id='info'>
			<form id='paymentForm'>
				<label for='type'>Tipe Bendera</label>
				<select name='type'>
					<option>Bendera Indonesia</option>
					<option disabled>Bendera Anime</option>
				</select>

				<!-- Credit Card Number -->
				<label for='name'>Nama</label>
				<input type='text' name='name' />

				<!-- Credit Card Holder Name -->
				<label for='address'>Alamat</label>
				<input type='text' name='address' />

				<input type='hidden' name='action' value='makePayment' />

				<button type="submit" id='makePayment'>MAKE A PAYMENT</button>
			</form>
        </aside>
        <aside id='description'>
          <h2>Bendera Indonesia</h2>
          <h3>Size 100cm</h3>
          <img src='bendera.jpg'>
          <h1>Rp. 75.000</h1>
          <button id='editOrder'>Edit the Order</button>
        </aside>
	</main>
</body>
