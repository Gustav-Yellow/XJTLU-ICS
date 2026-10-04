<?php
// Create database connection
$conn = new mysqli("localhost", "root", "", "newStore");

// Set response header to JSON
header("Content-Type: application/json");

// Query product data
$sql = "SELECT * FROM products LIMIT 3";
$result = $conn->query($sql);

$products = array();
while($row = $result->fetch_assoc()) {
    array_push($products, $row);
}

// Output JSON
echo json_encode($products);

$conn->close();
?>