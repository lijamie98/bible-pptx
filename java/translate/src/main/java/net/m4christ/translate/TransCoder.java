package net.m4christ.translate;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;

public class TransCoder {
  // Simplfied/Traditional character equivalence hashes
  static protected HashMap<String, String> s2thash, t2shash;

  static {
    String dataline;

    // Initialize and load in the simplified/traditional character hashses
    s2thash = new HashMap<String, String>();
    t2shash = new HashMap<String, String>();

    try {
      InputStream is = TransCoder.class.getResourceAsStream("src/main/resources/hcutf8.txt");
      BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF8"));
      while ((dataline = br.readLine()) != null) {
        // Skip empty and commented lines
        if (dataline.length() == 0 || dataline.charAt(0) == '#') {
          continue;
        }

        // Simplified to Traditional, (one to many, but pick only one)
        s2thash.put(dataline.substring(0,1), dataline.substring(1,2));

        // Traditional to Simplified, (many to one)
        for (int i = 1; i < dataline.length(); i++) {
          t2shash.put(dataline.substring(i,i+1), dataline.substring(0,1));
        }
      }
    } catch (Exception e) {
      System.err.println(e);
    }
  }

  public static void toSimplified(char[] cbuf, int offset, int length) {
    for (int i = offset; i < (offset + length); i++) {
      char c = cbuf[i];
      String currchar = String.valueOf(c);
      if (t2shash.containsKey(currchar) == true) {
        cbuf[i] = ((String) t2shash.get(currchar)).charAt(0);
      }
    }
  }

  public static String toSimpliefed(String inline) {
    // Call the StringBuffer version
    StringBuffer outline = new StringBuffer(inline);
    toSimplified(outline);

    return outline.toString();
  }

  public static void toSimplified(StringBuffer dataline) {
    int lineindex;
    String currchar;

    for (lineindex = 0; lineindex < dataline.length(); lineindex++) {
      currchar = String.valueOf(dataline.charAt(lineindex));
      if (t2shash.containsKey(currchar) == true) {
        dataline.replace(lineindex, lineindex+1, (String)t2shash.get(currchar));
      }
    }
  }

  public static void toTraditional(StringBuffer dataline) {
    int lineindex;
    String currchar;

    for (lineindex = 0; lineindex < dataline.length(); lineindex++) {
      currchar = String.valueOf(dataline.charAt(lineindex));
      if (s2thash.containsKey(currchar) == true) {
        dataline.replace(lineindex, lineindex+1, (String)s2thash.get(currchar));
      }
    }
  }



  public static String toTraditional(String inline) {
    StringBuffer outline = new StringBuffer(inline);
    toTraditional(outline);

    return outline.toString();
  }
}