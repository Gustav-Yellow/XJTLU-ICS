<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Insert Laptops</title>
    </head>
    <body>
        <?php
            $conn = new mysqli("localhost", "root", "", "onlineStore");
            if ($conn->connect_error) {
                die("Connection failed ".$conn->connect_error);
            }

            $sql = "INSERT INTO products (name, price, image, category) VALUES 
            ('MacBook', 7999, 'img/laptop1.jpg', 'Laptops'),
            ('Surface', 7999, 'img/laptop2.jpg', 'Laptops'),
            ('MateBook', 7999, 'img/laptop3.jpg', 'Laptops')";

            if ($conn->query($sql) === TRUE) {
                echo "Multiple records inserted successfully <br>";
            } else {
                echo "Error: ".$sql."<br>".$conn->error;
            }
        ?>
    </body>
</html>