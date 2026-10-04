<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Even Numbers</title>
    </head>
    <body>
        <h2>Even numbers in the array are:</h2>
        <?php
            $data = array(1, 3, 5, 2, 4, 5, 33, 31, 24, 54);
            foreach ($data as $i) {
                if ($i%2 == 0)
                    echo "$i ";
            }
            echo "<br>";
        ?>
    </body>
</html>

