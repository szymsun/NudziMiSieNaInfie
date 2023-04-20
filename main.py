import openai

openai.api_key = "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"


while True:
    request = input("Tell Something $ ")
    if request == "exit":
        break
    else:
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": request}])
        print(completion.choices[0].message.content)

