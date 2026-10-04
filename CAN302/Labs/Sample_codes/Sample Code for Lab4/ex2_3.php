<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "test_db";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: ".$conn->connect_error);
    }

    $sql = "SELECT name, sport FROM hobby";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "Name: ".$row["name"].", Sport: ".$row["sport"]."<br>";
        }
    } else {
        echo "0 record";
    }

    $conn->close();
?>