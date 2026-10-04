import java.util.Scanner;

public class ATMDispenseChain {
    private Dispense c1;

    public ATMDispenseChain() {
        this.c1 = new Dispense100Bill();
        Dispense c2 = new Dollar50Dispenser();
        Dispense c3 = new Dollar20Dispenser();
        Dispense c4 = new Dollar10Dispenser();

        c1.setNextChain(c2);
        c2.setNextChain(c3);
        c3.setNextChain(c4);
    }

    public static void main(String[] args) {
        ATMDispenseChain atmDispenser = new ATMDispenseChain();
        
        System.out.println("Enter amount to dispense: ");
        Scanner input = new Scanner(System.in);
        int amount = input.nextInt();
        input.close();
        
        if (amount % 10 != 0) {
            System.out.println("Amount must be a multiple of 10");
            return;
        }
        atmDispenser.c1.dispense(amount);
    }
}