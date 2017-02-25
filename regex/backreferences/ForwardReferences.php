<?php
// Forward References
// S consists of tic or tac
// The first tic must occur only when tac has appeared twice before
$Regex_Pattern = '/^(tac(tactic|tac)+)$/';

$handle = fopen ("php://stdin", "r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)) {
	print ("true");
} else {
	print ("false");
}

fclose($handle);
?>

