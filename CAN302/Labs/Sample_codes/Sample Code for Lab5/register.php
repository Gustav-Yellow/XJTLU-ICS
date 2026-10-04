<?php
    $conn = new mysqli("localhost", "root", "", "onlineStore");
    if ($conn->connect_error) {
        die("Connection failed ".$conn->connect_error);
    }

    $input_username = $_POST['username'];
    $input_email = $_POST['email'];
    $input_password = $_POST['password'];

    $sql = "INSERT INTO users (username, email, password) VALUES ('$input_username', '$input_email', '$input_password')";
    if ($conn->query($sql) === TRUE) {
        session_start();
        $_SESSION['username'] = $input_username;
        header("Location: cart.php");
    } else {
        echo "Error: ".$sql."<br>".$conn->error;
    }

    $conn->close();
?>