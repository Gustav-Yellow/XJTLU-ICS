public interface Dispense {
    void setNextChain(Dispense nextChain);
    void dispense(int amount);
}