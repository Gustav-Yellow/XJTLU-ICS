<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Insert Data</title>
    </head>
    <body>
        <?php
            include 'db_connect.php';

            $sql = "INSERT INTO students (sid, name, cohort) VALUES ('U000123', 'Peter Wong', '2022')";

            if ($conn->query($sql) === TRUE) {
                echo "New record inserted successfully <br>";
            } else {
                echo "Error: ".$sql."<br>".$conn->error;
            }
            $conn->close();
        ?>
    </body>
</html>

