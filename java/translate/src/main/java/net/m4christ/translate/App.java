package net.m4christ.translate;

import java.io.*;

public class App
{
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
        System.out.println("Writing to " + csvOutputFile);
        BufferedReader br = new BufferedReader(new FileReader(csvInputFile));
        PrintWriter pw = new PrintWriter(new FileWriter(csvOutputFile, false));
        String str;
        while ((str = br.readLine()) != null) {
            str = zc.convertString(str, Encoding.UTF8T, Encoding.UTF8S);
            pw.println(str);
        }

        pw.flush();
        pw.close();
    }

    public static void main( String[] args )    {
        App app = new App();
        try {
            app.convertAllCsv(new File(CSV_INPUT_FOLDER), new File(CSV_OUTPUT_FOLDER));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
