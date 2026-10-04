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
    <title>Online Shopping</title>
</head>

<body>
    <!-- Navigation menu -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <a class="navbar-brand link-info" href="#">Online Store</a>
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
                    <li class="list-group-item"><a class="nav-link" href="Laptop.php">Laptops</a></li>
                    <li class="list-group-item"><a class="nav-link" href="monitor.php">Monitors</a></li>
                </ul>
            </div>

            <!-- Carousel -->
            <div class="col-md-9">
                <div id="carouselDemo" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carouselDemo" data-bs-slide-to="0" class="active" aria-current="true"></button>
                        <button type="button" data-bs-target="#carouselDemo" data-bs-slide-to="1"></button>
                    </div>
                    <div class="carousel-inner">
                        <?php 
                            $get_slides = "SELECT * FROM products LIMIT 1";
                            $run_slides = mysqli_query($conn, $get_slides);
                            $row_slides = mysqli_fetch_array($run_slides);
                            echo '<div class="carousel-item active"><img src="'.$row_slides['image'].'" class="d-block w-100"></div>';

                            $get_slides = "SELECT * FROM products LIMIT 1 OFFSET 1";
                            $run_slides = mysqli_query($conn, $get_slides);
                            while($row_slides = mysqli_fetch_array($run_slides)){
                                echo '<div class="carousel-item"><img src="'.$row_slides['image'].'" class="d-block w-100"></div>';
                            }
                        ?>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselDemo" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon"></span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselDemo" data-bs-slide="next">
                        <span class="carousel-control-next-icon"></span>
                    </button>
                </div>
                <div class="container">
                    <div class="text-center">
                        <h4>Latest Products</h4>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>