<?php
    // Start the session
    session_start();

    // Check if the session data exists
    if (isset($_SESSION["user"]) && isset($_SESSION["role"])) {
        $user = $_SESSION["user"];
        $role = $_SESSION["role"];
        echo "Welcome, $user! Your role is $role.";
    } else {
        echo "Session data not found.";
    }
?>

