def process_file(file_content):
    # Простая обработка текста для проверки ошибок в коде (например, с помощью линтера)
    lines = file_content.split('\n')
    suggestions = []

    for line in lines:
        if 'TODO' in line:
            suggestions.append('Found TODO comment')

    return suggestions

