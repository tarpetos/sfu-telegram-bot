import time
from telepot.loop import MessageLoop
from .action_processor import ActionProcessor
from .config import BOT


class ZipperBot:
    def start(self) -> None:
        action = ActionProcessor()
        MessageLoop(
            BOT, handle={"chat": action.on_chat_message, "callback_query": action.on_callback_query}
        ).run_as_thread()

        print("Listening ...")
        while True:
            time.sleep(1)