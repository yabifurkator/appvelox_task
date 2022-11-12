from requests.exceptions import RequestException

from process_userinput import process_userinput
from exceptions import UserInputException

def main():
    while (userinput := input('> ')) != 'exit':
        userinput = userinput.strip()
        if not userinput:
            continue
        try:
            process_userinput(userinput=userinput)
            continue
        except UserInputException as ex:
            print('ошибка ввода:', str(ex))
        except RequestException as ex:
            print('ошибка подключения:', str(ex))
        except Exception as ex:
            print('неизвестная ошибка:', str(ex))
        print('для просмотра мануала напишите \'help\' без кавычек')


if __name__ == '__main__':
    main()
