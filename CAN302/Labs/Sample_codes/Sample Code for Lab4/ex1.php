<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Exercise 1</title>
    </head>
    <body>
        <?php
            function h1($msg) {
                echo "<h1>$msg</h1>";
            }

            h1("Hello CAN302");
            h1("This is a level one heading");

            function heading($msg, $level) {
                echo "<h$level>$msg</h$level>";
            }

            heading("Hello CAN302", 1);
            heading("Lab Session", 2);

            for ($i=1; $i<=6; $i++)
                heading("Hello CAN302", $i);
        ?>
    </body>
</html>
