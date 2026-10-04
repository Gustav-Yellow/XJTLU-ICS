<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Insert Monitors</title>
    </head>
    <body>
        <?php
            $conn = new mysqli("localhost", "root", "", "onlineStore");
            if ($conn->connect_error) {
                die("Connection failed ".$conn->connect_error);
            }

            $sql = "INSERT INTO products (name, price, image, category) VALUES 
            ('BENQ', 3999, 'img/monitor1.jpg', 'Monitors'),
            ('DELL', 3999, 'img/monitor2.jpg', 'Monitors'),
            ('LG', 3999, 'img/monitor3.jpg', 'Monitors')";

            if ($conn->query($sql) === TRUE) {
                echo "Multiple records inserted successfully <br>";
            } else {
                echo "Error: ".$sql."<br>".$conn->error;
            }
        ?>
    </body>
</html>