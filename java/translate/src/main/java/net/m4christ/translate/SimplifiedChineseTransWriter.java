/*
 * SimplifiedChineseTransWriter.java
 *
 * Created on May 21, 2007, 10:31 PM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package net.m4christ.translate;

import java.io.PrintWriter;

/**
 *
 * @author Jamie Li
 */
public class SimplifiedChineseTransWriter extends PrintWriter{
  private boolean bTranscode = false;
  PrintWriter writer = null;

  /** Creates a new instance of SimplifiedChineseTransWriter */
  public SimplifiedChineseTransWriter(PrintWriter out, boolean bTranscode) {
    super(out);

    writer = out;
    this.bTranscode = bTranscode;
  }

  public void close() {
    writer.close();
  }

  public void flush() {
    writer.flush();
  }

  public void write(char[] cbuf, int off, int len) {
    if (bTranscode) {
      TransCoder.toSimplified(cbuf, off, len);
    }

    writer.write(cbuf, off, len);
  }
}