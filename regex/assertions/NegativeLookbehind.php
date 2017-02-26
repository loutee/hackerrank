<?php
// Negative Lookbehind
// Match all occurences of characters not immediately preceded by vowels
$Regex_Pattern = '/(?<![AEIOUaeiou])./';

$handle = fopen ("php://stdin", "r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)) {
	print ("true");
} else {
	print ("false");
}

fclose($handle);
?>

