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

    $product_id = $_GET['product_id'];
    $user_id_query = "SELECT id FROM users WHERE username='{$_SESSION['username']}'";
    $user_id_result = $conn->query($user_id_query);
    $user_id_row = $user_id_result->fetch_assoc();
    $user_id = $user_id_row['id'];

    $check_sql = "SELECT * FROM cart WHERE user_id=$user_id AND product_id=$product_id";
    $check_result = $conn->query($check_sql);
    if ($check_result->num_rows > 0) {
        $update_sql = "UPDATE cart SET quantity=quantity+1 WHERE user_id=$user_id AND product_id=$product_id";
        $conn->query($update_sql);
    } else {
        $insert_sql = "INSERT INTO cart (user_id, product_id, quantity) VALUES ($user_id, $product_id, 1)";
        $conn->query($insert_sql);
    }

    $conn->close();
    header("Location: cart.php");
?>