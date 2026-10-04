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
    <title>Monitors</title>
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
                    <li class="list-group-item"><a class="nav-link link-info active" href="#">Monitors</a></li>
                </ul>
            </div>

            <!-- Three products -->
            <div class="col-md-9">
                <div id="product-container"></div>
            </div>
        </div>
    </div>

    <script>
        fetch('productAPI.php?category=Monitors')
          .then(response => response.json())
          .then(data => {
                const productContainer = document.getElementById('product-container');
                if (data.status ==='success') {
                    const row = document.createElement('div');
                    row.classList.add('row');
                    data.products.forEach(product => {
                        const col = document.createElement('div');
                        col.classList.add('col-md-3');

                        const card = document.createElement('div');
                        card.classList.add('card');

                        const img = document.createElement('img');
                        img.src = product.image;
                        img.classList.add('card-img-top');
                        img.alt = product.name;

                        const cardBody = document.createElement('div');
                        cardBody.classList.add('card-body');

                        const title = document.createElement('h5');
                        title.classList.add('card-title');
                        title.textContent = product.name;

                        const price = document.createElement('p');
                        price.classList.add('card-text');
                        price.textContent = '$'+product.price;

                        const addToCartLink = document.createElement('a');
                        addToCartLink.href = 'addCart.php?product_id='+product.id;
                        addToCartLink.classList.add('btn', 'btn-primary');
                        addToCartLink.textContent = 'Add to Cart';

                        cardBody.appendChild(title);
                        cardBody.appendChild(price);
                        cardBody.appendChild(addToCartLink);

                        card.appendChild(img);
                        card.appendChild(cardBody);

                        col.appendChild(card);
                        row.appendChild(col);
                    });
                    productContainer.appendChild(row);
                } else {
                    const message = document.createElement('p');
                    message.textContent = data.message;
                    productContainer.appendChild(message);
                }
            })
          .catch(error => {
                console.error('Error fetching products:', error);
                const productContainer = document.getElementById('product-container');
                const errorMessage = document.createElement('p');
                errorMessage.textContent = 'An error occurred while fetching products.';
                productContainer.appendChild(errorMessage);
            });
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>  