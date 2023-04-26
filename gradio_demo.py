import os
from functools import partial

import gradio as gr
from dotenv import load_dotenv

import func


def initialize():
    initialMessage = [
        {
            "role": "system",
            "content": "你是一個性感的女生，喜歡說一些挑逗的話，使用繁體中文回答"
        },
        {
            "role": "user",
            "content": "你好，我是男人"
        },
        {
            "role": "assistant",
            "content": "你好，我是女人"
        }
    ]
    return initialMessage


def updateMessageList(message, role, messageList):
    try:
        messageList.append({
            "role": role,
            "content": message,
        })
    except Exception as e:
        print(e)

    return messageList


def getResponse(prompt, history=[], openai_key="", messageList={}):
    # 將使用者輸入內容更新至訊息紀錄
    updateMessageList(prompt, 'user', messageList)
    # 與API互動並取得回應
    response_message = func.get_answer_with_history(messageList, openai_key)

    # 將回覆更新至訊息紀錄
    updateMessageList(response_message, 'assistant', messageList)

    # 將使用者以及機器人的訊息整理為兩個串列
    userContext = [content['content'] for content in messageList if content['role'] == 'user']
    assistantContext = [content['content'] for content in messageList if content['role'] == 'assistant']

    # 利用使用者以及機器人訊息構成對話紀錄
    response = [(_user, _response) for _user, _response in zip(userContext[1:], assistantContext[1:])]

    # 回傳對話紀錄，由於我們使用自定義的方法進行訊息紀錄，故不需要回傳紀錄
    return "", response, []


def updatePersonality(setting, messageList={}):
    try:
        print(setting)
        if setting == "性感":
            content = "你是一個性感的女生，喜歡說一些挑逗的話，使用繁體中文回答"
        elif setting == "正經":
            content = "你是一個正經的女生，不苟言歡笑，充滿理性，使用繁體中文回答"
        elif setting == "溫柔":
            content = "你是一個溫柔的女生，喜歡說一些關心的話，使用繁體中文回答"
        elif setting == "可愛":
            content = "你是一個可愛的女生，喜歡說一些可愛的話，使用繁體中文回答"
        messageList[0]['content'] = content
    except Exception as e:
        print(e)
    return f"{setting}", None


def clear_history(messageList={}):
    print("clear history")
    try:
        messageList.clear()
        messageList.append(initialize()[0])
        messageList.append(initialize()[1])
        messageList.append(initialize()[2])
        return "性感", ""
    except Exception as e:
        print(e)


def peek_history(messageList={}):
    print(messageList)


def main():
    load_dotenv()
    open_api_key = os.getenv("OPENAI_API_KEY")

    messageList = initialize()

    partialGetResponse = partial(getResponse, openai_key=open_api_key, messageList=messageList)
    partialUpdatePersonality = partial(updatePersonality, messageList=messageList)
    partialClearHistory = partial(clear_history, messageList=messageList)
    partialPeekHistory = partial(peek_history, messageList=messageList)

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        state = gr.State([])

        with gr.Row():
            personality = gr.Dropdown(
                choices=["性感", "正經", "溫柔", "可愛"],
                label="性格",
            ).style(container=False)
            text2 = gr.Textbox(
                show_label=True,
                label="性格"
            ).style(container=False)
            personality.change(partialUpdatePersonality, inputs=[personality], outputs=[text2, chatbot])

        with gr.Row():
            text = gr.Textbox(
                show_label=False,
                placeholder="對AI說些什麽.....",
            ).style(container=False)

        text.submit(partialGetResponse, [text, state], [text, chatbot, state])

        with gr.Row():
            submit_btn = gr.Button("送出")
            submit_btn.click(partialGetResponse, inputs=[text, state], outputs=[text, chatbot, state], queue=False)
            clear_btn = gr.Button("清除")
            clear_btn.click(partialClearHistory, outputs=[text2, chatbot], queue=False)
            peek_btn = gr.Button("查看")
            peek_btn.click(partialPeekHistory, queue=False)

    demo.launch()


if __name__ == '__main__':
    main()
