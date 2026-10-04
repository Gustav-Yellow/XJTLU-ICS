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

    $user_id_query = "SELECT id FROM users WHERE username='{$_SESSION['username']}'";
    $user_id_result = $conn->query($user_id_query);
    $user_id_row = $user_id_result->fetch_assoc();
    $user_id = $user_id_row['id'];

    $cart_sql = "SELECT cart.id, products.name, products.price, cart.quantity 
                 FROM cart 
                 JOIN products ON cart.product_id=products.id 
                 WHERE cart.user_id=$user_id";
    $cart_result = $conn->query($cart_sql);

    $cart_items = [];
    $total_amount = 0;
    if ($cart_result->num_rows > 0) {
        while ($row = $cart_result->fetch_assoc()) {
            $item_total = $row['price']*$row['quantity'];
            $total_amount += $item_total;
            $cart_items[] = [
                'id' => $row['id'],
                'name' => $row['name'],
                'price' => $row['price'],
                'quantity' => $row['quantity'],
                'item_total' => $item_total
            ];
        }
    }

    $response = [
        'cart_items' => $cart_items,
        'total_amount' => $total_amount
    ];

    header('Content-Type: application/json');
    echo json_encode($response);
?>