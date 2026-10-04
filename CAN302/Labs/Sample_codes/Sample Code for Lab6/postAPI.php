<?php
$books = [
    [
        "id" => 1,
        "title" => "Python Crash Course",
        "author" => "Eric Matthes"
    ],
    [
        "id" => 2,
        "title" => "JavaScript: The Definitive Guide",
        "author" => "David Flanagan"
    ]
];

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $inputJSON = file_get_contents('php://input');
    $input = json_decode($inputJSON, TRUE);
    if (isset($input['author'])) {
        $author = $input['author'];
        $filtered_books = array_filter($books, function ($book) use ($author) {
            return strtolower($book['author']) === strtolower($author);
        });
        echo json_encode(array_values($filtered_books));
    } else {
        echo json_encode(['error' => 'Author parameter is missing']);
    }
} else {
    echo json_encode(['error' => 'Only POST requests are allowed']);
}
?>