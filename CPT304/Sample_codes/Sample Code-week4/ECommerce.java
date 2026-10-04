interface PaymentStrategy {
    void pay(double amount);
}

class CreditCardPaymentStrategy implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        // Process credit card payment
    }
}

class PayPalPaymentStrategy implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        // Process PayPal payment
    }
}

// Other payment strategies ...

class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public void setPaymentStrategy(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void checkout(double amount) {
        paymentStrategy.pay(amount);
    }
}

// Usage:
public class ECommerce{
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        cart.setPaymentStrategy(new PayPalPaymentStrategy());
        cart.checkout(100.0);
    }
}


