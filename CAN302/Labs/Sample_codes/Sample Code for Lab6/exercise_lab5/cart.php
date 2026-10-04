<?php
    session_start();
    if (!isset($_SESSION['username'])) {
        header("Location: login.html");
        exit;
    }
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <title>Cart</title>
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
                    <li class="nav-item"><a class="nav-link link-info active" href="#">Cart</a></li>
                    <li class="nav-item"><a class="nav-link" href="logout.php">Logout</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>Welcome, <?php echo $_SESSION['username']; ?>! Your Cart: </h1>
        <table class="table">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody id="cart-body">
            </tbody>
            <tr>
                <td colspan="3"><strong>Total Amount</strong></td>
                <td><strong id="total-amount">$0</strong></td>
                <td></td>
            </tr>
        </table>
    </div>

    <script>
        fetch('cartAPI.php')
          .then(response => response.json())
          .then(data => {
                const cartBody = document.getElementById('cart-body');
                const totalAmountElement = document.getElementById('total-amount');

                if (data.cart_items.length > 0) {
                    data.cart_items.forEach(item => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${item.name}</td>
                            <td>$${item.price}</td>
                            <td>${item.quantity}</td>
                            <td>$${item.item_total}</td>
                            <td><a href="removeCart.php?cart_id=${item.id}" class="btn btn-danger">Remove</a></td>
                        `;
                        cartBody.appendChild(row);
                    });
                } else {
                    const row = document.createElement('tr');
                    row.innerHTML = '<td colspan="5">Your cart is empty.</td>';
                    cartBody.appendChild(row);
                }

                totalAmountElement.textContent = `$${data.total_amount}`;
            })
          .catch(error => {
                console.error('Error fetching cart data:', error);
            });
    </script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>