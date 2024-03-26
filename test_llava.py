import base64
import argparse

from openai import OpenAI

def get_chat(image_file, text_prompt):
    client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="sk-xxx")

    # load test image
    with open(image_file,'rb') as f:
        img_data = f.read()

    encoded_image = base64.b64encode(img_data).decode('ascii')

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        },
                    },
                    {"type": "text", "text": text_prompt},
                ],
            }
        ],
    )

    return response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--image_file', type=str)
    parser.add_argument('-t',
            '--text_prompt',
            type=str,
            default="What's in this image?")

    args = parser.parse_args()

    resp = get_chat(**vars(args))

    print(resp.choices[0].message.content)


if __name__=='__main__':
    main()
