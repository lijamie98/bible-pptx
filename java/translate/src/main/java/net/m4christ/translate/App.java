package net.m4christ.translate;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class App {
    public final static String CSV_INPUT_FOLDER = "C:\\bible-pptx\\data\\csv\\traditional";
    public final static String CSV_OUTPUT_FOLDER = "C:\\bible-pptx\\data\\csv\\simplified";
    public final static zhcode zc = new zhcode();

    public void convertAllCsv(File csvInputFolder, File csvOutputFolder) throws IOException {
        for (File csvInputFile : csvInputFolder.listFiles()) {
            File csvOutputFile = new File(csvOutputFolder, csvInputFile.getName());
            convertCsv(csvInputFile, csvOutputFile);
        }
    }

    public void convertCsv(File csvInputFile, File csvOutputFile) throws IOException {
        String traditionalContent = readFileToString(csvInputFile.getAbsolutePath());
        String simplifiedContent = readFileToString(csvOutputFile.getAbsolutePath());
        String str = zc.convertString(traditionalContent, Encoding.UTF8T, Encoding.UTF8S);
        if (!str.equals(simplifiedContent)) {
            System.out.println("Writing to " + csvOutputFile);
            saveStringToFile(csvOutputFile.getAbsolutePath(), str);
        }
    }
    
//    public void convertCsv(File csvInputFile, File csvOutputFile) throws IOException {
//        System.out.println("Writing to " + csvOutputFile);
//        BufferedReader br = new BufferedReader(new FileReader(csvInputFile));
//        PrintWriter pw = new PrintWriter(new FileWriter(csvOutputFile, false));
//        String str;
//        while ((str = br.readLine()) != null) {
//            str = zc.convertString(str, Encoding.UTF8T, Encoding.UTF8S);
//            pw.println(str);
//        }
//
//        pw.flush();
//        pw.close();
//    }


    static String readFileToString(String path) {
        try {
            byte[] encoded = Files.readAllBytes(Paths.get(path));
            return new String(encoded);
        } catch (IOException e) {
            return "";
        }

    }

    static void saveStringToFile(String path, String content) throws IOException {
        Files.write(Paths.get(path), content.getBytes(), StandardOpenOption.CREATE);
    }

    public static void main(String[] args) {
        App app = new App();
        try {
            app.convertAllCsv(new File(CSV_INPUT_FOLDER), new File(CSV_OUTPUT_FOLDER));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
