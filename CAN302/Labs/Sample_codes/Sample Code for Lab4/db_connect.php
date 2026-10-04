<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Database Connection</title>
    </head>
    <body>
        <?php
            $servername = "localhost";
            $username = "root";
            $password = "";
            $dbname = "test_db";

            $conn = new mysqli($servername, $username, $password, $dbname);
            if ($conn->connect_error) {
                die("Connection failed ".$conn->connect_error);
            }
            echo "Connect successfully <br>";
        ?>
    </body>
</html>

