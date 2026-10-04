<?php
    session_start();
    if (!isset($_SESSION['username'])) {
        header("Location: login.html");
        exit;
    }

    $conn = new mysqli("localhost", "root", "", "onlineShop");
    if ($conn->connect_error) {
        die("Connection failed ".$conn->connect_error);
    }

    $cart_id = $_GET['cart_id'];
    $delete_sql = "DELETE FROM cart WHERE id=$cart_id";
    $conn->query($delete_sql);

    $conn->close();
    header("Location: cart.php");
?>