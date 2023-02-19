import openai

openai.api_key = ''

def AIchatBot(ins):
    completion = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = ins,
        max_tokens = 1024,
        n=1,
        temperature = 0.5,
        stop = None
    )

    response = completion.choices[0].text
    print(response)

while True:
    ins = input()
    print(AIchatBot(ins))