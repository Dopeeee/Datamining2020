package perceptron;

import java.util.Arrays;

/**
 * @Auther SUN Pengliang
 * @Date 2020/11/14
 */
public class W {
    private double[] w;
    private double b;

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    private int index;

    public double[] getW() {
        return w;
    }

    public void setW(double[] w) {
        this.w = w;
    }

    public double getB() {
        return b;
    }

    public void setB(double b) {
        this.b = b;
    }

    @Override
    public String toString() {
        return "W{" +
                "w=" + Arrays.toString(w) +
                ", b=" + b +
                '}';
    }
}
