import os

from allennlp_demo.common import config, http
from allennlp_semparse import predictors, models  # noqa: F401


class NlvrParserModelEndpoint(http.ModelEndpoint):
    def __init__(self):
        c = config.Model.from_file(os.path.join(os.path.dirname(__file__), "model.json"))
        super().__init__(c)


if __name__ == "__main__":
    endpoint = NlvrParserModelEndpoint()
    endpoint.run()
