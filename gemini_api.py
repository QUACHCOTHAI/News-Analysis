import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")
llm = os.getenv("Model_Name")
if key is None or llm is None:
    raise ValueError("GEMINI_API_KEY and GEMINI_LLM must be set in the environment variables.")

genai.configure(api_key=key)
model = genai.GenerativeModel(llm)

def get_gemini_analysis(article_text):
    prompt = f"""
            Bạn hãy đọc bài báo sau và đưa ra:
            1. Tóm tắt ngắn gọn nội dung chính. Nội dung trình bài theo danh sách gạch đầu dòng.
            2. Nhận xét của bạn về bài báo này theo các từng thành phần sau:
                - Tin tức/Bài báo có đáng tin không?
                - Mức độ thiên vị như thế nào 
                - Bài báo có cảm xúc tiêu cực hay tích cực?
                - Đưa ra một số điểm mạnh và điểm yếu của bài báo.
            3. Đánh giá tổng thể về bài báo này.
        Bài báo:
        {article_text}
        """

    
    response = model.generate_content(prompt)
    return {"analysis": response.text}
