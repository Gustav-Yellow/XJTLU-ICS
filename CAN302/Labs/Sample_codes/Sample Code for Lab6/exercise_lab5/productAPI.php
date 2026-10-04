<?php
session_start();
$conn = new mysqli("localhost", "root", "", "onlineShop");
if ($conn->connect_error) {
    die("Connection failed: ".$conn->connect_error);
}

$category = $_GET['category'];
$sql = "SELECT * FROM products WHERE category='$category' LIMIT 3";
$result = $conn->query($sql);

$products = [];
if ($result->num_rows > 0) {
    while ($product = $result->fetch_assoc()) {
        $products[] = $product;
    }
    $response = [
        'status' => 'success',
        'products' => $products
    ];
} else {
    $response = [
        'status' => 'error',
        'message' => 'No products found in this category.'
    ];
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($response);
?>    