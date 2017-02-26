<?php
// Positive Lookahead
// Match all characters not immediately followed by that same character
$Regex_Pattern = '/(.)(?!\1)/';

$handle = fopen ("php://stdin", "r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)) {
	print ("true");
} else {
	print ("false");
}

fclose($handle);
?>

