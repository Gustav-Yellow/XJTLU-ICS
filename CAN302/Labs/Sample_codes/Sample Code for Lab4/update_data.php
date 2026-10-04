<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Update Data</title>
    </head>
    <body>
        <?php
            include 'db_connect.php';

            $sql = "UPDATE students SET cohort = '2024' WHERE name = 'John Chen'";
            if ($conn->query($sql) === TRUE) {
                echo "Record updated successfully <br>";
            } else {
                echo "Error updating record: ".$conn->error;
            }

            $conn->close();
        ?>
    </body>
</html>

