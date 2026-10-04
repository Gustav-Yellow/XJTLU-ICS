<?php
    $conn = new mysqli("localhost", "root", "", "onlineStore");
    if ($conn->connect_error) {
        die("Connection failed ".$conn->connect_error);
    }

    $input_username = $_POST['username'];
    $input_password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username='$input_username' AND password='$input_password'";
    $result = $conn->query($sql);
    echo "hello world";
    if ($result->num_rows > 0) {
        session_start();
        $_SESSION['username'] = $input_username;
        header("Location: cart.php");
    } else {
        // header("Location: register.html");
    }

    $conn->close();
?>