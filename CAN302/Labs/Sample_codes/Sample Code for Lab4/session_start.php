<?php
    // Start the session
    session_start();

    // Store data in the session
    $_SESSION["user"] = "Alice Sun";
    $_SESSION["role"] = "Admin";

    echo "Session data has been set.";
?>

