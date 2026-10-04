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

echo json_encode($books);
?>