<?php
    session_start();
    $conn = new mysqli("localhost", "root", "", "onlineShop");
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
    <title>Online Shop</title>
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
                            echo '<li class="nav-item"><a class="nav-link" href="logout.php">Logout</a></li>';
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
                    <li class="list-group-item"><a class="nav-link" href="laptop.php">Laptops</a></li>
                    <li class="list-group-item"><a class="nav-link" href="monitor.php">Monitors</a></li>
                </ul>
            </div>

            <!-- Carousel -->
            <div class="col-md-9">
                <div id="carouselDemo" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                        <!-- Indicators will be added dynamically -->
                    </div>
                    <div class="carousel-inner">
                        <!-- Carousel items will be added dynamically -->
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

    <script>
        fetch('carouselAPI.php')
           .then(response => response.json())
           .then(products => {
                const carouselInner = document.querySelector('.carousel-inner');
                const carouselIndicators = document.querySelector('.carousel-indicators');

                products.forEach((product, index) => {
                    const carouselItem = document.createElement('div');
                    carouselItem.classList.add('carousel-item');
                    if (index === 0) {
                        carouselItem.classList.add('active');
                    }
                    const img = document.createElement('img');
                    img.src = product.image;
                    img.classList.add('d-block', 'w-100');
                    carouselItem.appendChild(img);
                    carouselInner.appendChild(carouselItem);

                    const indicator = document.createElement('button');
                    indicator.type = 'button';
                    indicator.dataset.bsTarget = '#carouselDemo';
                    indicator.dataset.bsSlideTo = index;
                    if (index === 0) {
                        indicator.classList.add('active');
                        indicator.ariaCurrent = 'true';
                    }
                    carouselIndicators.appendChild(indicator);
                });
            })
           .catch(error => console.error('Error fetching products:', error));
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>