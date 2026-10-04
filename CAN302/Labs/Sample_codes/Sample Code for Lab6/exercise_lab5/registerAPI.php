<?php
$conn = new mysqli("localhost", "root", "", "onlineShop");
if ($conn->connect_error) {
    die("Connection failed ".$conn->connect_error);
}

header('Content-Type: application/json');
$json = file_get_contents('php://input');
$data = json_decode($json, true);

$input_username = $data['username'];
$input_email = $data['email'];
$input_password = $data['password'];

$sql = "INSERT INTO users (username, email, password) VALUES ('$input_username', '$input_email', '$input_password')";
if ($conn->query($sql) === TRUE) {
    session_start();
    $_SESSION['username'] = $input_username;
    
    $response = [
        'success' => true,
        'message' => 'Registration successful'
    ];
} else {
    $response = [
        'success' => false,
        'message' => "Error: ".$sql."<br>".$conn->error
    ];
}

$conn->close();

echo json_encode($response);
?>