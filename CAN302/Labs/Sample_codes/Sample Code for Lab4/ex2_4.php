<?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "test_db";

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: ".$conn->connect_error);
    }

    $sql = "SELECT students.sid, hobby.sport 
    FROM students
    JOIN hobby ON students.name = hobby.name";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "Student ID: ".$row["sid"].", Sport: ".$row["sport"]."<br>";
        }
    } else {
        echo "0 record";
    }

    $conn->close();
?>