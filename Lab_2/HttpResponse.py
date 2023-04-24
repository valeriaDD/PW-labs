import json


class HttpResponse:
    def __init__(self, response):
        open_brace_index = response.find('{')
        if open_brace_index != -1:
            self.header = response[0:open_brace_index]
            close_brace_index = response.rfind('}')

            if close_brace_index != -1:
                response_body = response[open_brace_index:close_brace_index + 1]
                self.body = json.loads(response_body)
            else:
                print("No body")
        else:
            print("No response")

