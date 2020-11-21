package perceptron;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

/**
 * @Auther SUN Pengliang
 * @Date 2020/11/13
 */
public class Perceptron {

    public double findR(HashMap<Integer,Point> hashMap){
        double R = 0;
            for(int i = 0; i < hashMap.size()  ; i++){
             double distance = 0;
             double[] array = hashMap.get(i).getPoints();
             int len = array.length;
             for(int j = 0; j < len ; j++){
                distance+= array[j]*array[j];
            }
            if(distance > R){
                R = distance;
            }
        }
        System.out.println("The Raduis of the data is " + Math.sqrt(R));
        return Math.sqrt(R);
    }

    public int find(HashMap<Integer, Point> hashMap, W w,double gamma_guess){

        int index = -1;
        int breakPoint = (w.getIndex()==hashMap.size())?0:w.getIndex();
        for (int j = breakPoint; j < hashMap.size(); j++) {
            Point p = hashMap.get(j);
            if ((Anwser(p, w) <= 0 || Distance(p, w) < gamma_guess / 2)) {
                index = j;
                break;
            }
        }
        if(index == -1){
            for (int j = 0; j < hashMap.size(); j++) {
                Point p = hashMap.get(j);
                if ((Anwser(p, w) <= 0 || Distance(p, w) < gamma_guess / 2)) {
                    index = j;
                    break;
                }
            }
        }
        return index;
    }

    public boolean judege(HashMap<Integer, Point> hashMap, W w,double gamma_guess,Double R){
           int max_epoch = FindMaxIteratoin(R, gamma_guess);
           for(int i = 0; i < max_epoch ; i++){
               int violationIndex = find(hashMap,w,gamma_guess);
               if(violationIndex > -1){
                   Update(hashMap.get(violationIndex),w);
                   w.setIndex(violationIndex+1);
                   //System.out.println(violationIndex);
                   //System.out.println(w.toString());
               }
               else{
                   return false;
              }
           }
           return true;
    }

    public void stop(HashMap<Integer, Point> hashMap, W w,double gamma_guess,Double R) {
        Boolean flag = judege(hashMap, w, gamma_guess, R);
        if (flag) {
            Double gamma_new = UpdateGamma(gamma_guess);
            System.out.println("**********************************");
            System.out.println("The Gamma_guess change to :" + gamma_new);
//            if(gamma_new<0.1){
//                System.out.println("结束");
//                System.out.println(gamma_guess/2);
//                return;
//            }
            int dimension = hashMap.get(0).getPoints().length;
            double[] warray = new double[dimension];
            w.setW(warray);
            stop(hashMap, w, gamma_new, R);

        }else{
            System.out.println("The final w is " + w.toString());
            System.out.println("The final gamma_guess " + gamma_guess/2);
            evaluate(w, hashMap, gamma_guess);

        }
    }

    private int FindMaxIteratoin(double radius, double gamma_guess) {
         return (int) (12*(radius/gamma_guess)*(radius/gamma_guess));
    }

    private double UpdateGamma(double gamma_guess) {
         return gamma_guess/=2;
    }

    /*
    * 经过感知机分离后，错误率计算
     */
    private double evaluate(W w, HashMap<Integer, Point> hashMap,double gamma_guess) {
        int n = hashMap.size();
        //System.out.println(n);
        int count = 0;
        Point p = new Point();
        for(int i = 0; i < n  ; i++){
            p = hashMap.get(i);
            if (Anwser(p, w) > 0 ){
                count++;
            }
        }
        double result = new BigDecimal((float)count/ n).setScale(2, BigDecimal.ROUND_HALF_UP).doubleValue();
        System.out.println("correct rate is:"+ result);
        return result;
    }

    /*
     * 点乘返回sum
     */
    private double Dot(Point p, W w) {
        double sum = 0;
        for (int j = 0; j < p.getPoints().length; j++) {
            sum += w.getW()[j] * p.getPoints()[j];
        }
        return sum;
    }

    /*
     * 返回函数计算的值
     */
    private double Anwser(Point p, W w) {
        //System.out.println(Arrays.toString(w));
        //System.out.println(b);
        return p.getLable() * (Dot(p,w));
    }

    public void Update(Point p, W w) {
        int eta = 1;
        for (int j = 0; j < w.getW().length; j++) {
            w.getW()[j] += eta * p.getLable() * p.getPoints()[j];
        }
        //b += eta * point.y;
    }

    public double Distance(Point p, W w) {
        int eta = 1;
        double sum = 0;
        double result = 0;
        for (int j = 0; j < w.getW().length; j++) {
            result += w.getW()[j] *p.getPoints()[j];
            sum += w.getW()[j] * w.getW()[j];
        }
        //b += eta * point.y;
        return abs(result)/sqrt(sum);
    }

    public List<Integer> Calculate(HashMap<Integer, Point> hashMap, W w,double gamma_guess){
        List<Integer> list = new ArrayList<>();
        int i = 0;
        for (int j = 0; j < hashMap.size(); j++) {
            Point p = hashMap.get(j);
            if ((Anwser(p, w) <= 0 || Distance(p, w) < gamma_guess / 2)) {
                list.add(j);
            }
        }
        return list;

    }






}
