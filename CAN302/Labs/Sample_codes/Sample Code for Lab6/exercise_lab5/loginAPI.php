<?php
$conn = new mysqli("localhost", "root", "", "onlineShop");
if ($conn->connect_error) {
    die("Connection failed ".$conn->connect_error);
}

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $inputJSON = file_get_contents('php://input');
    $input = json_decode($inputJSON, TRUE);

    $username = $conn->real_escape_string($input['username']);
    $password = $conn->real_escape_string($input['password']);

    $sql = "SELECT id, username FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        session_start();
        $_SESSION['username'] = $username;

        $row = $result->fetch_assoc();
        $response = [
          'status' => 'success',
            'id' => $row['id'],
            'username' => $row['username']
        ];
    } else {
        $response = [
          'status' => 'error',
        ];
    }
    echo json_encode($response);
} else {
    echo json_encode(['status' => 'error']);
}

$conn->close();
?>