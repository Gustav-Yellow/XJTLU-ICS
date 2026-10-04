<?php
session_start();
$conn = new mysqli("localhost", "root", "", "onlineShop");
if ($conn->connect_error) {
    die("Connection failed: ".$conn->connect_error);
}

$get_slides = "SELECT * FROM products LIMIT 3";
$run_slides = mysqli_query($conn, $get_slides);
$products = [];
while ($row_slides = mysqli_fetch_assoc($run_slides)) {
    $products[] = $row_slides;
}

header('Content-Type: application/json');
echo json_encode($products);

$conn->close();
?>