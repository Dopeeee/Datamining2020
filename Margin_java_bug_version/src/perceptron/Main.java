package perceptron;

import java.io.IOException;
import java.util.HashMap;

/**
 * @Auther SUN Pengliang
 * @Date 2020/11/14
 */
public class Main {
    public static void main(String args[]) throws IOException {
        FileReader fileRead = new FileReader();
        System.out.println("请输入文件名");
        String filename = args[0];
        HashMap<Integer, Point> hashMap = fileRead.readFile(filename);

        Perceptron perceptron = new Perceptron();
        double R = perceptron.findR(hashMap);
        double gamma_guess = R;

        W w = new W();
        int dimension = hashMap.get(0).getPoints().length;
        double[] warray = new double[dimension];
        w.setW(warray);

        //perceptron.train(hashMap,w,gamma_guess,R);
        perceptron.stop(hashMap,w,gamma_guess,R);



    }
}
