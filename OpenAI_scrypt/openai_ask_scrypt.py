
import openai
from sys import argv


def main(args):
    openai.api_key ="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"

    print("Question: ", args, '\n')

    response_gpt3 = openai.Completion.create(
        model="text-davinci-003",
        prompt=args,
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Get answer
    answer = response_gpt3['choices'][0]['text'] # type: ignore
    print("Answer: ", answer, '\n')


if __name__ == '__main__':

    main(argv[1])
