<?php
$conn = new mysqli("localhost", "root", "", "library");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $sql = "SELECT * FROM books";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $books = [];
        while ($row = $result->fetch_assoc()) {
            $books[] = $row;
        }
        echo json_encode($books);
    } else {
        echo json_encode([]);
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $inputJSON = file_get_contents('php://input');
    $input = json_decode($inputJSON, TRUE);
    if (isset($input['title']) && isset($input['author'])) {
        $title = $conn->real_escape_string($input['title']);
        $author = $conn->real_escape_string($input['author']);
        $sql = "INSERT INTO books (title, author) VALUES ('$title', '$author')";
        if ($conn->query($sql) === TRUE) {
            echo json_encode(['message' => 'Book added successfully']);
        } else {
            echo json_encode(['error' => 'Error adding book: ' . $conn->error]);
        }
    } else {
        echo json_encode(['error' => 'Title and author are required']);
    }
}

$conn->close();
?>