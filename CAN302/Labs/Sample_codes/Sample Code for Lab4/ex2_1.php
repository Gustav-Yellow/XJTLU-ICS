<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "test_db";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: ".$conn->connect_error);
    }

    $sql = "CREATE TABLE hobby (
        name VARCHAR(100) PRIMARY KEY,
        sport VARCHAR(50) NOT NULL
    )";

    if ($conn->query($sql) === TRUE) {
        echo "Table 'hobby' created successfully <br>";
    } else {
        echo "Error creating table: ".$conn->error;
    }

    $conn->close();
?>