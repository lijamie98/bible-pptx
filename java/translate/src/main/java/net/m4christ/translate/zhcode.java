package net.m4christ.translate;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.Hashtable;

/* Copyright 2002 Erik Peterson 
   Code and program free for non-commercial use.
   Contact erik@mandarintools.com for fees and
   licenses for commercial use.
*/

public class zhcode extends Encoding {
  // Simplfied/Traditional character equivalence hashes
  protected Hashtable<String, String> s2thash, t2shash;
  public boolean autodetect;

  // Constructor
  public zhcode() {
    super();
    String dataline;
    autodetect = false;

    // Initialize and load in the simplified/traditional character hashses
    s2thash = new Hashtable<String, String>();
    t2shash = new Hashtable<String, String>();

    try {
      InputStream pydata = zhcode.class.getResourceAsStream("hcutf8.txt");
      BufferedReader in = new BufferedReader(new InputStreamReader(pydata, "UTF8"));
      while ((dataline = in.readLine()) != null) {
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
    }
    catch (Exception e) {
      System.err.println(e);
    }

  }


  public String convertString(String inline, int source_encoding, int target_encoding) {
    StringBuffer outline = new StringBuffer(inline);
    convertStringBuffer(outline, source_encoding, target_encoding);
    return outline.toString();

	/*
	int lineindex;
	String currchar;
	CharSequence dataline;
	
	if (source_encoding == HZ) {
	    dataline = hz2gb(inline.toString());
	} else {
	    dataline = inline;
	}

	for (lineindex = 0; lineindex < dataline.length(); lineindex++) {
	    currchar = "" + dataline.charAt(lineindex);
	    if ((source_encoding == GB2312 || source_encoding == GBK || source_encoding == ISO2022CN_GB ||
		 source_encoding == HZ || 
		 source_encoding == UNICODE || source_encoding == UNICODES || source_encoding == UTF8 ||
		 source_encoding == UTF8S) 
		&&
		(target_encoding == BIG5 || target_encoding == CNS11643 || target_encoding == UNICODET ||
		 target_encoding == UTF8T ||
		 target_encoding == ISO2022CN_CNS)) {
		if (s2thash.containsKey(currchar) == true) {
		    outline.append(s2thash.get(currchar));
		} else {
		    outline.append(currchar);
		}
	    } else if ((source_encoding == BIG5 || source_encoding == CNS11643 || 
			source_encoding == UNICODET ||
			source_encoding == UTF8 || source_encoding == UTF8T ||
			source_encoding == ISO2022CN_CNS || source_encoding == GBK || 
			source_encoding == UNICODE) 
		       &&
		       (target_encoding == GB2312 || target_encoding == UNICODES || 
			target_encoding == ISO2022CN_GB ||
			target_encoding == UTF8S || target_encoding == HZ)) {
		if (t2shash.containsKey(currchar) == true) {
		    outline.append(t2shash.get(currchar));
		} else {
		    outline.append(currchar);
		}
	    } else {
		outline.append(currchar);
	    }
	}

	if (target_encoding == HZ) {
	    // Convert to look like HZ
	    return gb2hz(outline.toString());
	}

	return outline.toString();
	*/
  }


  public void convertStringBuffer(StringBuffer dataline, int source_encoding, int target_encoding) {
    int lineindex;
    String currchar;

    if (source_encoding == HZ) {
      hz2gbStringBuffer(dataline);
    }

    for (lineindex = 0; lineindex < dataline.length(); lineindex++) {
      currchar = "" + dataline.charAt(lineindex);
      if ((source_encoding == GB2312 || source_encoding == GBK || source_encoding == ISO2022CN_GB ||
              source_encoding == HZ ||
              source_encoding == UNICODE || source_encoding == UNICODES || source_encoding == UTF8 ||
              source_encoding == UTF8S)
              &&
              (target_encoding == BIG5 || target_encoding == CNS11643 || target_encoding == UNICODET ||
                      target_encoding == UTF8T ||
                      target_encoding == ISO2022CN_CNS)) {
        if (s2thash.containsKey(currchar) == true) {
          dataline.replace(lineindex, lineindex+1, (String)s2thash.get(currchar));
        }
      } else if ((source_encoding == BIG5 || source_encoding == CNS11643 ||
              source_encoding == UNICODET ||
              source_encoding == UTF8 || source_encoding == UTF8T ||
              source_encoding == ISO2022CN_CNS || source_encoding == GBK ||
              source_encoding == UNICODE)
              &&
              (target_encoding == GB2312 || target_encoding == UNICODES ||
                      target_encoding == ISO2022CN_GB ||
                      target_encoding == UTF8S || target_encoding == HZ)) {
        if (t2shash.containsKey(currchar) == true) {
          dataline.replace(lineindex, lineindex+1, (String)t2shash.get(currchar));
        }
      }
    }

    if (target_encoding == HZ) {
      // Convert to look like HZ
      gb2hzStringBuffer(dataline);
    }

  }


  public String hz2gb(String hzstring) {
    StringBuffer gbstring = new StringBuffer(hzstring);
    hz2gbStringBuffer(gbstring);
    return gbstring.toString();
  }


  public void hz2gbStringBuffer(StringBuffer hzstring) {
    byte[] gbchar = new byte[2];
    int i = 0;

    // Convert to look like equivalent Unicode of GB
    for (i = 0; i < hzstring.length(); i++) {
      if (hzstring.charAt(i) == '~') {
        if (hzstring.charAt(i+1) == '{') {
          hzstring.delete(i, i+2);
          while (i < hzstring.length()) {
            if (hzstring.charAt(i) == '~' && hzstring.charAt(i+1) == '}') {
              hzstring.delete(i, i+2);
              i--;
              break;
            } else if (hzstring.charAt(i) == '\r' || hzstring.charAt(i) == '\n') {
              break;
            }
            gbchar[0] = (byte)(hzstring.charAt(i) + 0x80);
            gbchar[1] = (byte)(hzstring.charAt(i+1) + 0x80);
            try {
              hzstring.replace(i, i+2, new String(gbchar, "GB2312"));
            }  catch (Exception usee) { System.err.println(usee.toString()); }
            i++;
          }
        } else if (hzstring.charAt(i+1) == '~') { // ~~ becomes ~
          hzstring.replace(i, i+2, "~");
        }
      }
    }

  }



  public String gb2hz(String gbstring) {
    StringBuffer hzbuffer = new StringBuffer(gbstring);
    gb2hzStringBuffer(hzbuffer);
    return hzbuffer.toString();
  }



  public void gb2hzStringBuffer(StringBuffer gbstring) {
    byte[] gbbytes = new byte[2];
    int i;
    boolean terminated = false;

    for (i = 0; i < gbstring.length(); i++) {
      if ((int)gbstring.charAt(i) > 0x7f) {
        gbstring.insert(i, "~{");
        terminated = false;
        while (i < gbstring.length()) {
          if (gbstring.charAt(i) == '\r' || gbstring.charAt(i) == '\n') {
            gbstring.insert(i, "~}");
            i+=2;
            terminated = true;
            break;
          } else if ((int)gbstring.charAt(i) <= 0x7f) {
            gbstring.insert(i, "~}");
            i+=2;
            terminated = true;
            break;
          }
          try {
            gbbytes = gbstring.substring(i, i+1).getBytes("GB2312");
          }
          catch (UnsupportedEncodingException uee) { System.out.println(uee); }
          gbstring.delete(i, i+1);
          gbstring.insert(i, (char)(gbbytes[0] + 256 - 0x80));
          gbstring.insert(i+1, (char)(gbbytes[1] + 256 - 0x80));
          i+=2;
        }
        if (terminated == false) {
          gbstring.insert(i, "~}");
          i+=2;
        }
      } else {
        if (gbstring.charAt(i) == '~') {
          gbstring.replace(i, i+1, "~~");
          i++;
        }
      }
    }

  }


    /*
    public void convertFile(String sourcefile, String outfile, int source_encoding, int target_encoding) {
	BufferedReader srcbuffer;
	BufferedWriter outbuffer;
	String dataline;
	
	try {
	    srcbuffer = new BufferedReader(new InputStreamReader(new FileInputStream(sourcefile), javaname[source_encoding]));
	    outbuffer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(outfile), javaname[target_encoding]));
	    while ((dataline = srcbuffer.readLine()) != null) {
		outbuffer.write(convertString(dataline, source_encoding, target_encoding));
		outbuffer.newLine();
	    }
	    srcbuffer.close();
	    outbuffer.close();
	}
	catch (Exception ex) {
	    System.err.println(ex);
	}
    }
    */

}