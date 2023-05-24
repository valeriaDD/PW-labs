class DatabaseManager:
    def __init__(self):
        self.data = []

    def save_data(self, chat_id, user_data):
        self.data.append({'id': chat_id, 'data': user_data})

    def get_saved_data(self, chat_id):
        result = ""
        for data in self.data:
            if data["id"] == chat_id:
                result += "\r\n" + data["data"]
        return result
