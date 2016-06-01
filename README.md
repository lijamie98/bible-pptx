# bible-pptx


## 中文使用說明

### 如何產生思高聖經 PPTX 檔案
  * 準備 PPTX Template 檔案：
   * 以 template-simple 或 template-dark 作為生成的範本
   * 拷貝到你所要的新的 Template 檔案，假設你所要的theme是kingdom，那麼範本檔名為 template-kingdom.pptx，並將檔案放在bible-pptx/data/templates下面。
  * 產生思高聖經 PPTX 檔案
   * 打開　ｃｍｄ
   * cd 到　bible-pptx 檔案夾
   * connvert.py --theme=kingdom
   * 產生的 PPTX 檔案在 bible-pptx/data/pptx/kingdom 下面


Chinese Sigao Bible PPT Generation Program

The bible-pptx is designed to create PPTX files for Chinese Sigao Bible. It consists of three parts:
  * Downloader
  * HTML to CSV converter
  * CSV to PPTX converter

The HTML files are retrieved from 'http://www.ccreadbible.org/Chinese%20Bible/sigao/'
