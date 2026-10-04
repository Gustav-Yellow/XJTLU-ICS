<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Delete Data</title>
    </head>
    <body>
        <?php
            include 'db_connect.php';

            $sql = "DELETE FROM students WHERE name = 'Jenney Li'";
            if ($conn->query($sql) === TRUE) {
                echo "Record deleted successfully <br>";
            } else {
                echo "Error deleting record: ".$conn->error;
            }

            $conn->close();
        ?>
    </body>
</html>

