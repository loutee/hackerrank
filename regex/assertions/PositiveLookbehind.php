<?php
// Positive Lookbehind
// Match all occurences of digits immediately preceded by an odd digit
$Regex_Pattern = '/(?<=[13579])\d/';

$handle = fopen ("php://stdin", "r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)) {
	print ("true");
} else {
	print ("false");
}

fclose($handle);
?>

