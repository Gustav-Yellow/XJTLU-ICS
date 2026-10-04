public abstract class BaseDispenser implements Dispense {
    private Dispense nextChain;

    @Override
    public void setNextChain(Dispense nextChain) {
        this.nextChain = nextChain;
    }

    @Override
    public void dispense(int amount) {
        if (amount >= getDenomination()) {
            int num = amount / getDenomination();
            int remainder = amount % getDenomination();
            System.out.println("Dispensing " + num + " pieces of $" + getDenomination() + " note");
            if (remainder > 0 && nextChain != null) {
                nextChain.dispense(remainder);
            }
        } else if (nextChain != null) {
            nextChain.dispense(amount);
        }
    }

    // Abstract method to be implemented by concrete classes
    protected abstract int getDenomination();
}