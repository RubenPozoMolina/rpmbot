from utils.chat_utils import Chat, ChatCreationError


class TestChatUtils:

    def test_chat_utils(self):
        chat = Chat()
        assert chat is not None

    def test_chat_utils_exception(self):
        try:
            chat = Chat(model="invalid_model")
        except ChatCreationError as e:
            assert str(e) == "Failed to create chat with model invalid_model"
        else:
            assert False, "Expected ChatCreationError to be raised"

    def test_chat_utils_send_message(self):
        chat = Chat()
        message = chat.send_message("user", "Hello")
        assert message is not None


    def test_chat_context(self):
        chat = Chat()
        chat.send_message("assistant", "Return only the number without any comment")
        r1 = chat.send_message("user", "1 + 1")
        assert r1== "2"
        r2 = chat.send_message("user", "Now sum 1 more.")
        assert r2 == "3"
        r3 = chat.send_message("user", "Now multiply by 3")
        assert r3 == "9"
