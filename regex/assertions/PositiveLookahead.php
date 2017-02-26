<?php
// Positive Lookahead
// Match all occurences of o followed immediately by oo in S
$Regex_Pattern = '/o(?=oo)/';

$handle = fopen ("php://stdin", "r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)) {
	print ("true");
} else {
	print ("false");
}

fclose($handle);
?>

