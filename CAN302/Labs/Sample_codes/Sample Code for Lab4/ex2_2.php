<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "test_db";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: ".$conn->connect_error);
    }

    $sql = "INSERT INTO hobby (name, sport) VALUES 
    ('Alice Sun', 'badminton'),
    ('Peter Wong', 'basketball'),
    ('John Chen', 'swimming')";

    if ($conn->query($sql) === TRUE) {
        echo "Multiple records inserted successfully <br>";
    } else {
        echo "Error: ".$sql."<br>".$conn->error;
    }

    $conn->close();
?>