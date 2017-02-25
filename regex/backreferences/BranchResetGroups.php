<?php
// Branch Reset Group
// S consists of 8 digits
// S must have '---', '-', '.' or ':' separator per 2 digit parts
// S must have exactly one kind of separator
// Separators must have integers on both sides
$Regex_Pattern = '/^\d{2}(?|(:)|(\.)|(\-)|(\-{3}))\d{2}\1\d{2}\1\d{2}$/';

$handle = fopen ("php://stdin", "r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)) {
	print ("true");
} else {
	print ("false");
}

fclose($handle);
?>

