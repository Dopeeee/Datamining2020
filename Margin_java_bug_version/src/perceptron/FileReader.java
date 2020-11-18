package perceptron;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

/**
 * @Auther SUN Pengliang
 * @Date 2020/11/15
 */
public class FileReader {

    public HashMap<Integer,Point> readFile(String path) throws IOException {


        Perceptron perceptron = new Perceptron();
        //String pathname = "data.txt"; // 绝对路径或相对路径都可以，写入文件时演示相对路径,读取以上路径的input.txt文件
        //防止文件建立或读取失败，用catch捕捉错误并打印，也可以throw;
        //不关闭文件会导致资源的泄露，读写文件都同理
        //Java的try-with-resources可以优雅关闭文件，异常时自动关闭文件；详细解读https://stackoverflow.com/a/12665271

        HashMap<Integer,Point> hashMap = new HashMap<>();

        try (
                java.io.FileReader reader = new java.io.FileReader(path);
                BufferedReader br = new BufferedReader(reader) // 建立一个对象，它把文件内容转成计算机能读懂的语言

        ) {
            String line;
            int number = 0;
            int dimension = 0;
            int lineIndex = 0;


            while ((line = br.readLine()) != null) {
                if(lineIndex == 0){

                    String n = line.split(" ")[0];
                    String d = line.split(" ")[1];
                    number = Integer.valueOf(n);
                    dimension = Integer.valueOf(d);
                    System.out.println("The number of samples are " + number);
                    System.out.println("The dimension of data is " + dimension);
                    lineIndex++;
                    continue;
                }
                //一次读入一行数据
                Point p = new Point();
                double[] array = new double[dimension];
                for(int i = 0; i < dimension ; i++){
                    array[i] = Double.parseDouble(line.split(" ")[i]);
                }

                int label = 2*Integer.valueOf(line.split(" ")[dimension])-1;

                p.setLable(label);
                p.setPoints(array);
                hashMap.put(lineIndex-1,p);
                lineIndex++;

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        //double R = perceptron.findR(hashMap);
        //System.out.println(R);
        return hashMap;
    }


}
