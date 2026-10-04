<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "test_db";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: ".$conn->connect_error);
    }

    $sid = $_POST["sid"];
    $name = $_POST["name"];
    $cohort = $_POST["cohort"];

    $sql = "INSERT INTO students (sid, name, cohort) VALUES ('$sid', '$name', '$cohort')";

    if ($conn->query($sql) === TRUE) {
        echo "Register successfully <br>";
    } else {
        echo "Error: ".$sql."<br>".$conn->error;
    }

    $conn->close();
?>