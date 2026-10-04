interface State {
    void changeLight(TrafficLight trafficLight);
}

class Red implements State {
    @Override
    public void changeLight(TrafficLight trafficLight) {
        System.out.println("Red light - vehicles must stop.");
        trafficLight.setState(new Green());
    }
}

class Green implements State {
    @Override
    public void changeLight(TrafficLight trafficLight) {
        System.out.println("Green light - vehicles can go.");
        trafficLight.setState(new Yellow());
    }
}

class Yellow implements State {
    @Override
    public void changeLight(TrafficLight trafficLight) {
        System.out.println("Yellow light - vehicles should prepare to stop.");
        trafficLight.setState(new Red());
    }
}

class TrafficLight {
    private State state;

    public TrafficLight() {
        state = new Red(); // initial state
    }

    public void setState(State state) {
        this.state = state;
    }

    public void changeLight() {
        this.state.changeLight(this);
    }
}

class TrafficController {
    public static void main(String[] args) {
        TrafficLight trafficLight = new TrafficLight();

        trafficLight.changeLight(); // Red light - vehicles must stop.
        trafficLight.changeLight(); // Green light - vehicles can go.
        trafficLight.changeLight(); // Yellow light - vehicles should prepare to stop.
        trafficLight.changeLight(); // Red light - vehicles must stop.
    }
}