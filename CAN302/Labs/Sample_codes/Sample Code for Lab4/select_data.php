<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Select Data</title>
    </head>
    <body>
        <?php
            include 'db_connect.php';

            $sql = "SELECT sid, name, cohort FROM students";
            $result = $conn->query($sql);
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    echo "ID: ".$row["sid"]." - Name: ".$row["name"]." - Cohort: ".$row["cohort"]."<br>";
                }
            } else {
                echo "0 results";
            }

            $conn->close();
        ?>
    </body>
</html>

