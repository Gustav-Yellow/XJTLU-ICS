<?php
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        $name = $_GET["name"];
        $sid = $_GET["sid"];
        echo "Your name is $name and your student ID is $sid.";
    }
?>

