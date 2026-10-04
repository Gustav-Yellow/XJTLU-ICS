<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Time</title>
    </head>
    <body>
        <h2>Now is: </h2>
        <?php 
            date_default_timezone_set("Asia/Shanghai");
            echo date("H:i:s");
        ?>
    </body>
</html>

