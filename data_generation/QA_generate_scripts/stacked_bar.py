from openai import OpenAI
import os
import json
import re
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def read_csv_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_types_from_template(template):
    matches = re.findall(r'"type_of_question": "(.*?)"', template)
    return ", ".join(matches)


template = '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What is the investment in Technology for the year 2020?"
    },
    {
        "from": "gpt",
        "value": "The investment in Technology for the year 2020 can be retrieved directly from the chart. Look for the bar representing 'Technology' (the yellow bar) and identify its length value at the y-axis label for the year 2020. The investment amount shown is 20000.",
        "label": "20000"
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value":"Which sector had the highest investment in 2022?"
    },
    {
        "from": "gpt",
        "value": "To determine which sector had the highest investment in 2022, observe the segment of each sector's bar for the year 2022. 'Technology' (the yellow bar) is the highest segment in that year. Therefore, the sector with the highest investment is Technology.",
        "label": "Technology"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of protein content across all fruits?"
    },
    {
        "from": "gpt",
        "value": "To find the range of protein content, we identify the minimum and maximum values of protein across all fruits. The minimum protein content is 1.2 units (found in Grapes, Pineapple, and Watermelon) and the maximum is 1.6 units (found in Banana), resulting in a range of 1.2-1.6 units.",
        "label": "1.2-1.6"
    },
    {
        "from": "human",
        "type_of_question": "Find correlations/ trends",
        "value": "How has the distribution of sales among different product categories changed over the past five years?"
    },
    {
        "from": "gpt",
        "value": "By examining the stacked bar chart, we can observe the sales distribution across different product categories from 2019 to 2023. In 2019, Category A dominated the sales, followed by Category B and Category C. Over the years, the proportion of Category A's sales has decreased, while Category B and Category C have seen an increase. In 2023, Category B has overtaken Category A as the leading product category in terms of sales. This trend indicates a shift in consumer preferences or market dynamics over the five-year period.",
        "label": "Shift in market dynamics"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "Which year had the highest total sales, and how do the product categories contribute to it?"
    },
    {
        "from": "gpt",
        "value": "To determine the year with the highest total sales, we look at the height of the stacked bars representing each year. The tallest bar corresponds to 2021. In 2021, the contribution of each product category to the total sales is as follows: Category A contributed the most, followed by Category B and Category C. Thus, 2021 had the highest total sales, with Category A being the major contributor.",
        "label": "2021"
    }
]
```
'''

def get_chart_type(file_name):
    if file_name.startswith('vl_'):
        return 'vega-lite'
    elif file_name.startswith('echart_'):
        return 'echart'
    elif file_name.startswith('matplot_'):
        return 'matplotlib'
    elif file_name.startswith('seaborn_'):
        return 'seaborn'
    else:
        return 'unknown'

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        else:
            return file.read()


def generate_qa_pairs(args, table_data, task_types):
    spec, chart_name, save_dir = args

    chart_type = get_chart_type(chart_name)

    # client = OpenAI(base_url='',
    #     api_key='')
    
    # client = OpenAI(base_url='',
    #     api_key='') 
    client = OpenAI(base_url='',
        api_key='')

    question = f''' Here is a stacked bar chart presented by {chart_type} code and table data {table_data}.{spec}
    Please generate questions about the chart in different task types.
    The task types are {task_types}.

    You should imagine that you are looking at the image presented by the code, not the code itself.
    Remember in your answer, what is given is only an image of chart and you answer based on the image.
    The value and label are ground truth of your question, so make sure the answer is correct.
    Avoid using invalid escape character in string.
    Use approximate colour names rather than hexadecimal colours.
    Additionally, I want to save your output to a json file, so I hope you can organize your answer like
    {template}, and must include the answer with ```json ```.
    '''

    messages = [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {chart_type}."},
        {"role": "user", "content": f"{question}"}
    ]
    try:
        response = client.chat.completions.create(
            # model="gpt-3.5-turbo-16k",
            model="gpt-4o",
            messages=messages
        )
        print(response)
    except:
        return
    try:
        assistant_reply = response.choices[0].message.content
        print(assistant_reply)
        json_spec_blocks = re.findall(
            r'```(.*?)```', assistant_reply, re.DOTALL)
        if json_spec_blocks:
            json_spec = json_spec_blocks[0].strip()
        else:
            json_spec = assistant_reply
        # assert json_spec.startswith('json')
        json_spec = json_spec.lstrip('json')
        qa_pairs = json.loads(json_spec)
        json_path = f'{save_dir}/{os.path.splitext(chart_name)[0]}.json'  # 强制保存为 .json 文件
        with open(json_path, 'w') as file:
            json.dump(qa_pairs, file, indent=4)
        print(f"Save qa_pairs to {json_path}")
    except Exception as e:
        print(f"Error processing {chart_name}: {e}")



def main(chart_dir, save_dir, table_dir, max_workers):
    task_types = extract_types_from_template(template)
    chart_list = [f for f in os.listdir(chart_dir) if f.endswith(('.json', '.py', '.html'))]
    args_list = [
        (read_file_content(os.path.join(chart_dir, chart_name)), chart_name, save_dir, read_csv_content(os.path.join(table_dir, f"{os.path.splitext(chart_name)[0]}.csv")), task_types)
        for chart_name in chart_list if not os.path.exists(os.path.join(save_dir, f"{os.path.splitext(chart_name)[0]}.json"))
    ]

    args_list = args_list[:]  # Limit for demonstration

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(generate_qa_pairs, args) for args in args_list]
        for future in tqdm(as_completed(futures), total=len(args_list), desc='Processing'):
            future.result()  # This will raise any exceptions caught during the execution of the task


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--chart_dir', type=str,
                        default=r'stacked_bar_chart')
    parser.add_argument('--save_dir', type=str,
                        default=r'stacked_bar_chart_QA')
    parser.add_argument('--output_file', type=str,
                        default='output.json')
    parser.add_argument('--max_workers', type=int,
                        default=200, help='Number of worker processes')
    parser.add_argument('--multiprocessing', type=bool, default=True)
    parser.add_argument('--table_dir', type=str, required=True, help='Path to the table data CSV file.')

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(chart_dir=args.chart_dir, save_dir=args.save_dir, table_dir=args.table_dir, max_workers=args.max_workers)
