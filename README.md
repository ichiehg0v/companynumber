# 統編與抬頭核對小工具

## 目的

這個小工具用來確認報名人填寫的統編與抬頭是否正確。

## 實作方法

這個工具是經過與 GPT 討論後，使用 Python 實作的程式碼。

## 操作方式

1. 開啟 VSCode 並安裝 Python 擴充功能。
2. 修改 `input.csv` 文件，將你的統編與抬頭資料填入。請確保文件儲存為 Big-5 編碼的 CSV 格式。
3. 回到 VSCode 並執行程式碼。
4. 程式執行完畢後，會生成一份新的 `output.csv` 文件，告訴你統編是否正確。

## 注意事項

- 使用的統編資料來自 [openfunltd/twcompany](https://github.com/openfunltd/twcompany?tab=readme-ov-file) 的公司統編資料。這些資料有可能不是最新的，若結果有不一致，仍需要到財政部網站查找最新的資料。

## 希望達到但還沒達到
- 可以變成網頁操作
- 不知道為什麼 input 一定要是 big-5，我把程式碼改成 utf-8，希望 input 可以存成 utf-8 就跑不出結果了（但 output 就可以輸出 utf-8）
- 統編 original 比對的資料想要可以隨時更新
