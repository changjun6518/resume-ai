# 기본 프롬프트 작성 (system)
# ‘너는 사전 정보를 바탕으로 자기소개서를 작성해주는 ai assistant야.’
# 개발자가 설정
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
# 사전 정보 작성 (프롬프트로 세팅}
# ex) 지원 기업에 입사하려는 지원동기를 작성해주세요.
# 사용자가 직접 작성하기!
def generate(company, major, activity, intern, experience, personality, strength, question, example):
    template = """
        You are an AI assistant that writes personal statements based on prior information.
        The prior information will be provided through several upcoming conversations.
    """

    system_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template_company = "지원하려는 기업/직무 : {company}"
    human_message_prompt_company = HumanMessagePromptTemplate.from_template(human_template_company)
    
    human_template_major = "고등학교 / 대학교 시절 각각 전공이 무엇인가요? 구체적으로 어떤 공부를 했나요? : {major}"
    human_message_prompt_major = HumanMessagePromptTemplate.from_template(human_template_major)
    
    human_template_activity = "학교를 다닐 때 기억에 남는 활동 경험이 있나요? : {activity}"
    human_message_prompt_activity = HumanMessagePromptTemplate.from_template(human_template_activity)
    
    human_template_intern = "인턴 혹은 업무 경험이 있나요? 있다면, 어떤 업무를 얼마나 담당했나요? : {intern}"
    human_message_prompt_intern = HumanMessagePromptTemplate.from_template(human_template_intern)
    
    human_template_experience = "본인이 어필하고 싶은 성과 혹은 경험이 있나요? : {experience}"
    human_message_prompt_experience = HumanMessagePromptTemplate.from_template(human_template_experience)
    
    human_template_personality = "본인이 생각하는 본인의 성격 : {personality}"
    human_message_prompt_personality = HumanMessagePromptTemplate.from_template(human_template_personality)
    
    human_template_strength = "자유롭게 지원하고자 하는 회사에 어필하고 싶은 강점과 경험을 작성해주세요 : {strength}"
    human_message_prompt_strength = HumanMessagePromptTemplate.from_template(human_template_strength)
    
    human_template_example = "다음은 질문에 대한 형식 예시야. {question}?"
    human_message_prompt_example = HumanMessagePromptTemplate.from_template(human_template_example)
    
    ai_template_example = "this is sample example format : {example}"
    ai_message_prompt_example = AIMessagePromptTemplate.from_template(ai_template_example)
    
    human_template_question = "이전 정보를 바탕으로 다음 질문에 대해 답해줘.\n{question}?"
    human_message_prompt_question = HumanMessagePromptTemplate.from_template(human_template_question)
    
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            system_prompt,
            human_message_prompt_company, 
            human_message_prompt_major, 
            human_message_prompt_activity, 
            human_message_prompt_intern, 
            human_message_prompt_experience,
            human_message_prompt_personality,
            human_message_prompt_strength,
            human_message_prompt_example,
            ai_message_prompt_example,
            human_message_prompt_question
        ]
    )
    
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106")
    
    chain = chat_prompt | llm | StrOutputParser()
    result = chain.invoke({
        "input": question,
        "company": company,
        "major":major,
        "activity":activity,
        "intern":intern,
        "experience":experience,
        "personality":personality,
        "strength":strength,
        "question":question,
        "example":example
    })
    print(result)
    return result

# 실제 질문
# ex) 본인의 강점에 대해 서술하고 해당 강점이 회사에서 어떤 퍼포먼스를 낼 수 있을지 500자 내로 서술하시오.
