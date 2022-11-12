from dataclasses import dataclass

from handlers import \
    get_all_tasks, \
    create_new_task, \
    get_task_by_id, \
    complete_task_by_id, \
    delete_task_by_id, \
    help_handler, \
    HandlerReturn

from exceptions import \
    UserInputException, \
    UnknownCommand

@dataclass
class CommandHandlerPair:
    command: str
    handler: callable

command_handler_pairs = [
    CommandHandlerPair(command='list', handler=get_all_tasks),
    CommandHandlerPair(command='new', handler=create_new_task),
    CommandHandlerPair(command='get', handler=get_task_by_id),
    CommandHandlerPair(command='complete', handler=complete_task_by_id),
    CommandHandlerPair(command='delete', handler=delete_task_by_id),
    CommandHandlerPair(command='help', handler=help_handler)
]


def process_userinput(userinput):
    userinput_list = [word.strip() for word in userinput.split()]
    command = userinput_list[0]
    
    for pair in command_handler_pairs:
        if pair.command == command:
            hr: HandlerReturn = pair.handler(userinput_list)
            print('HTTP response: {}'.format(hr.http_response))
            print('output: {}'.format(
                hr.handler_response if not hr.handler_response is None else '-'
            ))
            return
    
    raise UnknownCommand(command=command)
