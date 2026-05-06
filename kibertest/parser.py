import re
import random

def parse_gift_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    questions = []
    # Ищем блоки с ::qN:: ... { ... }
    pattern = r'(::q\d+::)\s*([^{]*)\{([^}]+)\}'
    matches = re.findall(pattern, content, re.DOTALL)

    for q_id, text, options_block in matches:
        q_id = q_id.strip(':').strip()
        question_text = text.strip()
        options = []
        correct_index = -1

        # Разбираем строки, начинающиеся с = или ~
        for line in options_block.split('\n'):
            line = line.strip().rstrip(';')
            if line.startswith('='):
                options.append(line[1:].strip())
                correct_index = len(options) - 1
            elif line.startswith('~'):
                options.append(line[1:].strip())

        if question_text and options and correct_index != -1:
            questions.append({
                'id': q_id,
                'question': question_text,
                'options': options,
                'correct': correct_index
            })
    return questions

def get_random_questions(questions, count=20):
    if len(questions) <= count:
        return questions
    return random.sample(questions, count)