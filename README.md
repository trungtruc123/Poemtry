
# 1. Sử dụng AI sinh thơ lục bát
# 2. Giới thiệu đề tài
Hiện nay việc sáng tác thơ đang bị hao một dần bởi vì việc sáng tác bài thơ đòi hỏi rất nhiều công phu, thời gian, tâm huyết của tác giả. Liệu có cách nào có thể dùng trí tuệ nhân tạo để sáng tác thơ được hay không ? 
## 2.1. Các bước thực hiện :
* Craw data poemtry from internet and saved
* Preprocessing data, and write DataLoader ( return tokenizer of poemtry)
* Initialize Trainer with TrainingArguments and GPT-2 model
* Train and save the model
* Test the model
## 2.3. Thành viên
Trần Trung Trực -fptSoft
## 2.4. Data train, model:
https://drive.google.com/drive/folders/1TdO5jdbeIZfWgZKVgspXKGEQW4_XN1dd?usp=sharing
* Liên hệ: fb: https://www.facebook.com/profile.php?id=100038801181933
# 3. Giao diện ứng dụng
** Giao diện home **
** Giao diện predict **
<img src ='/display/image.png'>

# 4. Môi trường cài đặt 
- **python3 **
- tensorflow 1.14
- flask
- pip install -r requirements.txt
- Ngoài ra còn 1 số thư viện có thể cài thêm trong quá trình chạy
# 5. Hướng dẫn chạy
- create envs skin : conda create -n poem python=3
- activate skin :   conda activate poem
-
- open directory project and open terminal: git clone https://github.com/trungtruc123/AI_POEMTRY.git
- pip install -r requirements.txt
- python app.py 
# 6. Hướng phát triển
Vì dữ liệu mình craw còn quá ít nên 1 số bài thơ sẽ bị overfit hoặc không có vần điệu. Nên hướng phát triển sẽ craw thêm dữ liệu và fine-tuning.
Dự án tiếp theo mình sẽ sinh rap (oh zê)
# 7. Tài liệu tham khảo
https://www.philschmid.de/fine-tune-a-non-english-gpt-2-model-with-huggingface

https://huggingface.co/
