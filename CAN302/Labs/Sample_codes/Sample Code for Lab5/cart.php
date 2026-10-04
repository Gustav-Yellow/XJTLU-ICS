<?php
    session_start();
    if (!isset($_SESSION['username'])) {
        header("Location: login.html");
        exit;
    }

    $conn = new mysqli("localhost", "root", "", "onlineStore");
    if ($conn->connect_error) {
        die("Connection failed ".$conn->connect_error);
    }

    $user_id_query = "SELECT id FROM users WHERE username='{$_SESSION['username']}'";
    $user_id_result = $conn->query($user_id_query);
    $user_id_row = $user_id_result->fetch_assoc();
    $user_id = $user_id_row['id'];

    $cart_sql = "SELECT cart.id, products.name, products.price, cart.quantity 
                 FROM cart 
                 JOIN products ON cart.product_id=products.id 
                 WHERE cart.user_id=$user_id";
    $cart_result = $conn->query($cart_sql);
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
            <tbody>
                <?php
                    $total_amount = 0;
                    if ($cart_result->num_rows > 0) {
                        while ($row = $cart_result->fetch_assoc()) {
                            $item_total = $row['price']*$row['quantity'];
                            $total_amount += $item_total;
                            echo '<tr>';
                            echo '<td>'.$row['name'].'</td>';
                            echo '<td>$'.$row['price'].'</td>';
                            echo '<td>'.$row['quantity'].'</td>';
                            echo '<td>$'.$item_total.'</td>';
                            echo '<td><a href="removeCart.php?cart_id='.$row['id'].'" class="btn btn-danger">Remove</a></td>';
                            echo '</tr>';
                        }
                    } else {
                        echo '<tr><td colspan="5">Your cart is empty.</td></tr>';
                    }
                ?>
                <tr>
                    <td colspan="3"><strong>Total Amount</strong></td>
                    <td><strong>$<?php echo $total_amount; ?></strong></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>