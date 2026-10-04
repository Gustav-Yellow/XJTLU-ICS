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
    ],
    [
        "id" => 3,
        "title" => "Python for Data Analysis",
        "author" => "Wes McKinney"
    ]
];

header('Content-Type: application/json');

if (isset($_GET['author'])) {
    $author = $_GET['author'];
    $filtered_books = array_filter($books, function ($book) use ($author) {
        return strtolower($book['author']) === strtolower($author);
    });
    echo json_encode(array_values($filtered_books));
} else {
    echo json_encode($books);
}
?>