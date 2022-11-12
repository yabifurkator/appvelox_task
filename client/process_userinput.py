from dataclasses import dataclass

from handlers import \
    get_all_tasks, \
    create_new_task, \
    get_task_by_id, \
    complete_task_by_id, \
    delete_task_by_id

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
    CommandHandlerPair(command='delete', handler=delete_task_by_id)
]


def process_userinput(userinput):
    userinput_list = [word.strip() for word in userinput.split()]
    command = userinput_list[0]
    
    for pair in command_handler_pairs:
        if pair.command == command:
            pair.handler(userinput_list)
            return
    
    raise UnknownCommand(command=command)
