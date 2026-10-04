<?php
    session_start();
    $conn = new mysqli("localhost", "root", "", "onlineStore");
    if ($conn->connect_error) {
        die("Connection failed ".$conn->connect_error);
    }
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <title>Desktops</title>
</head>

<body>
    <!-- Navigation menu -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand" href="index.php">Online Store</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <?php
                        if (isset($_SESSION['username'])) {
                            echo '<li class="nav-item"><a class="nav-link" href="cart.php">Cart</a></li>';
                        } else {
                            echo '<li class="nav-item"><a class="nav-link" href="login.html">Login</a></li>';
                        }
                    ?>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container-fluid">
        <div class="row">
            <!-- Left sidebar -->
            <div class="col-md-3 bg-light">
                <ul class="list-group">
                    <li class="list-group-item"><a class="nav-link link-info active" href="#">Laptops</a></li>
                    <li class="list-group-item"><a class="nav-link" href="monitor.php">Monitors</a></li>
                </ul>
            </div>

            <!-- Three products -->
            <div class="col-md-9">
                <?php
                    echo '<h3>Laptops</h3>';
                    $sql = "SELECT * FROM products WHERE category='Laptops' LIMIT 3";
                    $result = $conn->query($sql);
                    if ($result->num_rows > 0) {
                        echo '<div class="row">';
                        while ($row = $result->fetch_assoc()) {
                            echo '<div class="col-md-3">';
                            echo '<div class="card">';
                            echo '<img src="'.$row['image'].'" class="card-img-top" alt="'.$row['name'].'">';
                            echo '<div class="card-body">';
                            echo '<h5 class="card-title">'.$row['name'].'</h5>';
                            echo '<p class="card-text">$'.$row['price'].'</p>';
                            echo '<a href="addCart.php?product_id='.$row['id'].'" class="btn btn-primary">Add to Cart</a>';
                            echo '</div>';
                            echo '</div>';
                            echo '</div>';
                        }
                        echo '</div>';
                    } else {
                        echo '<p>No products found in this category.</p>';
                    }
                    $conn->close();
                ?>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>  