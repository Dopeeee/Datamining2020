package perceptron;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;


/**
 * @Auther SUN Pengliang
 * @Date 2020/11/13
 */
public class Point {
    private int lable;
    private double[] points;
    private int dimension;
    private int number;



    public int getLable() {
        return lable;
    }

    public void setLable(int lable) {
        this.lable = lable;
    }

    public double[] getPoints() {
        return points;
    }

    public void setPoints(double[] points) {
        this.points = points;
    }

    public int getDimension() {
        return dimension;
    }

    public void setDimension(int dimension) {
        this.dimension = dimension;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }




    @Override
    public String toString() {
        return "Point{" +
                "lable=" + lable +
                ", points=" + Arrays.toString(points) +
                ", dimension=" + dimension +
                ", number=" + number +
                '}';
    }
}

